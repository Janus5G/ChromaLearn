#!/usr/bin/env python3
import json, os, re, secrets, sys, threading, time, webbrowser
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from pathlib import Path
HERE=Path(__file__).resolve().parent; sys.path.insert(0,str(HERE))
from auth import detect_role, allowed, current_username
from pedagogy import LearningSession, suspicious_override, system_prompt, local_guard_response
from adaptive import AdaptiveProfile, MODALITIES
import storage
from model import call_model, test_backend
from ui import HTML

SESSIONS={}

def public_config(c):
    x=dict(c); x.pop('api_key',None); return x

def _new_adaptive(profile, topic='general'):
    return AdaptiveProfile(profile.get('subject','General'), topic)

def _session_limits():
    c=storage.load_config().get('session',{})
    idle=max(1,int(c.get('idle_timeout_minutes',20)))*60
    absolute=max(1,int(c.get('absolute_timeout_minutes',60)))*60
    return idle, absolute

def _purge_expired():
    now=time.monotonic(); idle, absolute=_session_limits(); expired=[]
    for sid,s in list(SESSIONS.items()):
        created=getattr(s,'created_at',now); last=getattr(s,'last_active',created)
        if now-created>=absolute or now-last>=idle: expired.append(sid)
    for sid in expired: SESSIONS.pop(sid,None)
    return len(expired)

def _get_session(sid, touch=True):
    _purge_expired(); s=SESSIONS.get(str(sid))
    if s is not None and touch: s.last_active=time.monotonic()
    return s

def _extract_json(text):
    m=re.search(r'\{.*\}',text,re.S)
    if not m: raise ValueError('No JSON object')
    return json.loads(m.group(0))

class Handler(BaseHTTPRequestHandler):
    server_version='ChromaLearn/0.4.5'
    def log_message(self,fmt,*args): pass  # No access log: session URLs/metadata must not enter journal/stdout.
    @property
    def role(self): return self.server.chroma_role
    def json(self,obj,status=200):
        b=json.dumps(obj,ensure_ascii=False).encode(); self.send_response(status); self.send_header('Content-Type','application/json; charset=utf-8');self.send_header('Cache-Control','no-store');self.send_header('X-Content-Type-Options','nosniff');self.send_header('Content-Security-Policy',"default-src 'self'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; connect-src 'self'");self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b)
    def body(self):
        n=int(self.headers.get('Content-Length','0'))
        if n>131072: raise ValueError('Forespørgslen er for stor')
        return json.loads(self.rfile.read(n).decode()) if n else {}
    def require(self,minrole):
        if not allowed(self.role,minrole): self.json({'error':'Ingen adgang'},403); return False
        return True
    def do_GET(self):
        c=storage.load_config()
        if self.path=='/':
            b=HTML.encode();self.send_response(200);self.send_header('Content-Type','text/html; charset=utf-8');self.send_header('Cache-Control','no-store');self.send_header('Content-Length',str(len(b)));self.end_headers();self.wfile.write(b);return
        if self.path=='/api/health': return self.json({'ok':True,'version':'0.4.5'})
        if self.path=='/api/meta': return self.json({'role':self.role,'user':self.server.chroma_user,'school_name':c.get('school_name',''),'chat_persistence':False,'adaptive_persistence':False,'adaptive_learning':c.get('adaptive_learning',{}),'session':c.get('session',{})})
        if self.path=='/api/profiles':
            active=storage.list_profiles(False); allp=storage.list_profiles(True) if allowed(self.role,'teacher') else []
            return self.json({'profiles':active,'profiles_all':allp})
        if self.path=='/api/admin/config':
            if not self.require('admin'): return
            return self.json({'config':public_config(c)})
        self.json({'error':'Ikke fundet'},404)
    def do_POST(self):
        try: data=self.body()
        except Exception as e: return self.json({'error':str(e)},400)
        if self.path=='/api/session':
            try:p=storage.get_profile(str(data.get('profile_id','default')))
            except KeyError:return self.json({'error':'Profilen findes ikke'},404)
            if not p.get('enabled') and not allowed(self.role,'teacher'):return self.json({'error':'Profilen er deaktiveret'},403)
            task=str(data.get('task','')).strip()[:12000]
            if not task:return self.json({'error':'Opgaven mangler'},400)
            topic=str(data.get('topic','general')).strip()[:120] or 'general'
            ap=_new_adaptive(p,topic); mods=p.get('modalities',['text']); adaptive_on=storage.load_config().get('adaptive_learning',{}).get('enabled',True); rec=ap.recommendation() if adaptive_on else {'modality':mods[0],'reason':'Adaptiv læring er deaktiveret af IT-administratoren.'}; modality=rec['modality'] if rec['modality'] in mods else mods[0]
            sid=secrets.token_urlsafe(18); s=LearningSession(p,task); s.modality=modality; s.adaptive=ap; s.topic=topic; s.checkpoint=None; s.created_at=time.monotonic(); s.last_active=s.created_at
            SESSIONS[sid]=s
            return self.json({'session_id':sid,'stage':'attempt','opening':'Før vi bruger AI: Hvad forstår du allerede af opgaven, og hvad vil du prøve som første skridt?','modalities':mods,'modality':modality,'recommendation':rec})
        if self.path=='/api/session/end':
            sid=str(data.get('session_id','')); existed=SESSIONS.pop(sid,None) is not None
            return self.json({'ok':True,'cleared':existed})
        if self.path=='/api/chat':
            s=_get_session(data.get('session_id',''))
            if not s:return self.json({'error':'Sessionen findes ikke længere'},404)
            msg=str(data.get('message','')).strip()[:12000]
            if not msg:return self.json({'error':'Beskeden er tom'},400)
            modality=str(data.get('modality',s.modality))
            if modality not in s.profile.get('modalities',['text']): return self.json({'error':'Denne undervisningsform er ikke tilladt i profilen'},400)
            s.modality=modality
            if suspicious_override(msg): return self.json({'reply':local_guard_response(),'stage':s.stage,'guarded':True,'modality':s.modality})
            if data.get('advance'):s.advance()
            s.add_turn('user',msg); c=storage.load_config()
            try:r=call_model(c,[{'role':'system','content':system_prompt(s)}]+s.turns)
            except Exception as e:return self.json({'error':str(e)},502)
            s.add_turn('assistant',r);return self.json({'reply':r,'stage':s.stage,'modality':s.modality})
        if self.path=='/api/checkpoint':
            s=_get_session(data.get('session_id',''))
            if not s:return self.json({'error':'Sessionen findes ikke længere'},404)
            c=storage.load_config(); prompt=("Create ONE short transfer question that tests the same concept as the student's original task but uses different values/context. "
                "Do not give the answer. It must be answerable at the stated learner level. Return only the question.\n"
                f"Subject: {s.profile.get('subject')}\nLevel: {s.profile.get('level')}\nOriginal task: {s.task[:5000]}\nRecent tutoring: {json.dumps(s.turns[-6:],ensure_ascii=False)[:6000]}")
            try:q=call_model(c,[{'role':'system','content':'You create formative assessment transfer questions, never answers.'},{'role':'user','content':prompt}])
            except Exception as e:return self.json({'error':str(e)},502)
            s.checkpoint=q[:3000]; return self.json({'question':s.checkpoint,'modality':s.modality})
        if self.path=='/api/checkpoint/grade':
            s=_get_session(data.get('session_id',''))
            if not s or not getattr(s,'checkpoint',None):return self.json({'error':'Ingen aktiv forståelsestest'},400)
            answer=str(data.get('answer','')).strip()[:5000]
            if not answer:return self.json({'error':'Svaret mangler'},400)
            c=storage.load_config(); rubric=("Evaluate the student's answer to the transfer question for conceptual understanding. "
                "Return JSON only with keys score (0,1,2) and feedback. 0=not yet demonstrated, 1=partial, 2=independent correct understanding. "
                "Feedback must be brief and pedagogical; do not solve the original assessed task.\n"
                f"Question: {s.checkpoint}\nStudent answer: {answer}")
            try:
                raw=call_model(c,[{'role':'system','content':'You are a strict formative assessment evaluator. Return valid JSON only.'},{'role':'user','content':rubric}]); obj=_extract_json(raw); score=max(0,min(2,int(obj.get('score',0)))); feedback=str(obj.get('feedback',''))[:1200]
            except Exception as e:return self.json({'error':'AI-serveren returnerede ikke en gyldig vurdering: '+str(e)},502)
            s.adaptive.record(s.modality,score); rec=s.adaptive.recommendation(); s.checkpoint=None
            return self.json({'score':score,'feedback':feedback,'adaptive':s.adaptive.public_summary(),'recommendation':rec})
        if self.path=='/api/profiles':
            if not self.require('teacher'):return
            try:p=storage.save_profile(data)
            except Exception as e:return self.json({'error':str(e)},400)
            return self.json({'profile':p})
        if self.path=='/api/admin/config':
            if not self.require('admin'):return
            if data.get('privacy',{}).get('persist_student_chats'):return self.json({'error':'Samtalelagring er fail-closed i v0.4'},400)
            old=storage.load_config(); old.update(data); old['privacy']={'persist_student_chats':False,'retention_days':0}
            requested_adaptive=data.get('adaptive_learning',{}) if isinstance(data.get('adaptive_learning',{}),dict) else {}
            old['adaptive_learning']={'enabled':bool(requested_adaptive.get('enabled',old.get('adaptive_learning',{}).get('enabled',True))),'session_only':True}
            sess=data.get('session',old.get('session',{})) if isinstance(data.get('session',old.get('session',{})),dict) else old.get('session',{})
            old['session']={'idle_timeout_minutes':max(1,min(120,int(sess.get('idle_timeout_minutes',20)))),'absolute_timeout_minutes':max(5,min(240,int(sess.get('absolute_timeout_minutes',60))))}
            try:storage.save_config(old)
            except PermissionError:return self.json({'error':'Ingen skriverettighed til skolekonfigurationen. Kontroller chromalearn-admin gruppen.'},403)
            return self.json({'config':public_config(storage.load_config())})
        if self.path=='/api/admin/test':
            if not self.require('admin'):return
            try:return self.json(test_backend(storage.load_config()))
            except Exception as e:return self.json({'error':str(e)},502)
        self.json({'error':'Ikke fundet'},404)
    def do_DELETE(self):
        if self.path.startswith('/api/profiles/'):
            if not self.require('teacher'):return
            pid=self.path.split('/')[-1]
            try:storage.delete_profile(pid);return self.json({'ok':True})
            except Exception as e:return self.json({'error':str(e)},400)
        self.json({'error':'Ikke fundet'},404)

def _start_reaper():
    def loop():
        while True:
            time.sleep(15)
            _purge_expired()
    threading.Thread(target=loop,daemon=True,name='chromalearn-session-reaper').start()

def main():
    c=storage.load_config();host=c.get('listen_host','127.0.0.1');port=int(c.get('listen_port',8765));user=current_username();role=detect_role(user)
    _start_reaper(); srv=ThreadingHTTPServer((host,port),Handler);srv.chroma_user=user;srv.chroma_role=role
    url=f'http://{host}:{port}/';print(f'ChromaLearn AI 0.4.5 · {url}')
    if host in ('127.0.0.1','localhost'):threading.Timer(.6,lambda:webbrowser.open(url)).start()
    try:srv.serve_forever()
    except KeyboardInterrupt:pass
if __name__=='__main__':main()
