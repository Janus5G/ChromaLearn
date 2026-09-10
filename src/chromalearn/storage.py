import json, os, tempfile
from pathlib import Path

SYSTEM_CONFIG = Path(os.environ.get("CHROMALEARN_CONFIG", "/etc/chromalearn/config.json"))
PROFILE_DIR = Path(os.environ.get("CHROMALEARN_PROFILE_DIR", "/var/lib/chromalearn/profiles"))

DEFAULT_CONFIG = {
  "api_url":"http://127.0.0.1:8000/v1/chat/completions",
  "model":"local-model",
  "listen_host":"127.0.0.1",
  "listen_port":8765,
  "auth_mode":"none",
  "api_key_env":"CHROMALEARN_API_KEY",
  "request_timeout_seconds":90,
  "temperature":0.35,
  "max_tokens":700,
  "privacy":{"persist_student_chats":False,"retention_days":0},
  "school_name":"",
  "adaptive_learning":{"enabled":True,"session_only":True},
  "session":{"idle_timeout_minutes":20,"absolute_timeout_minutes":60}
}

DEFAULT_PROFILE = {
  "id":"default", "name":"Standard læringsprofil", "subject":"Generelt",
  "level":"Ikke angivet", "help_level":2, "assessment_mode":"practice",
  "allow_analogous_examples":True, "source_policy":"Brug opgavens materiale og almindeligt etableret viden. Opfind ikke kilder eller citater.",
  "modalities":["text","visual","audio","activity"], "enabled":True
}

def _atomic_json(path, data, mode=0o640):
    path.parent.mkdir(parents=True,exist_ok=True)
    fd,tmp=tempfile.mkstemp(prefix=path.name+'.',dir=path.parent)
    try:
        with os.fdopen(fd,'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=2,sort_keys=True); f.write('\n')
        os.chmod(tmp,mode); os.replace(tmp,path)
    finally:
        if os.path.exists(tmp): os.unlink(tmp)

def load_config():
    c=json.loads(json.dumps(DEFAULT_CONFIG))
    if SYSTEM_CONFIG.exists():
        try:
            loaded=json.loads(SYSTEM_CONFIG.read_text(encoding='utf-8'))
            for k,v in loaded.items(): c[k]=v
        except Exception: pass
    return c

def save_config(config):
    clean=dict(config)
    # Secrets are deliberately not accepted as config values.
    clean.pop('api_key',None)
    _atomic_json(SYSTEM_CONFIG,clean,0o640)

def validate_profile(p):
    out=dict(DEFAULT_PROFILE); out.update(p or {})
    ident=str(out.get('id','')).strip()
    if not ident or not all(ch.isalnum() or ch in '-_' for ch in ident): raise ValueError('Ugyldigt profil-id')
    out['id']=ident[:64]; out['name']=str(out.get('name',''))[:120] or ident
    out['subject']=str(out.get('subject','Generelt'))[:120]; out['level']=str(out.get('level',''))[:120]
    out['help_level']=max(1,min(4,int(out.get('help_level',2))))
    if out.get('assessment_mode') not in {'practice','homework','assignment','exam'}: raise ValueError('Ugyldig opgavetype')
    out['allow_analogous_examples']=bool(out.get('allow_analogous_examples',True)); out['enabled']=bool(out.get('enabled',True))
    out['source_policy']=str(out.get('source_policy',''))[:1000]
    allowed={'text','visual','audio','activity'}
    mods=out.get('modalities',['text'])
    if not isinstance(mods,list): raise ValueError('Modaliteter skal være en liste')
    out['modalities']=[m for m in mods if m in allowed]
    if not out['modalities']: out['modalities']=['text']
    return out

def list_profiles(include_disabled=False):
    PROFILE_DIR.mkdir(parents=True,exist_ok=True)
    result=[]
    for p in sorted(PROFILE_DIR.glob('*.json')):
        try:
            obj=validate_profile(json.loads(p.read_text(encoding='utf-8')))
            if include_disabled or obj.get('enabled'): result.append(obj)
        except Exception: continue
    if not result: result=[dict(DEFAULT_PROFILE)]
    return result

def get_profile(pid):
    for p in list_profiles(include_disabled=True):
        if p['id']==pid: return p
    if pid=='default': return dict(DEFAULT_PROFILE)
    raise KeyError(pid)

def save_profile(profile):
    p=validate_profile(profile)
    _atomic_json(PROFILE_DIR/(p['id']+'.json'),p,0o660)
    return p

def delete_profile(pid):
    if pid=='default': raise ValueError('Standardprofilen kan ikke slettes')
    p=PROFILE_DIR/(pid+'.json')
    if p.exists(): p.unlink()

def adaptive_key(subject, topic='general'):
    return (str(subject).strip().lower()[:120] or 'general')+'::'+(str(topic).strip().lower()[:120] or 'general')
