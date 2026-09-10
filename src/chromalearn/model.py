import json, os, urllib.request, urllib.error

def headers_for(config):
    h={"Content-Type":"application/json"}
    mode=config.get('auth_mode','none')
    if mode=='bearer_env':
        env=config.get('api_key_env','CHROMALEARN_API_KEY')
        key=os.environ.get(env,'')
        if key: h['Authorization']='Bearer '+key
    return h

def call_model(config, messages):
    payload=json.dumps({
      'model':config.get('model','local-model'), 'messages':messages,
      'temperature':float(config.get('temperature',0.35)),
      'max_tokens':int(config.get('max_tokens',700))
    }).encode()
    req=urllib.request.Request(config['api_url'],data=payload,headers=headers_for(config),method='POST')
    try:
        with urllib.request.urlopen(req,timeout=int(config.get('request_timeout_seconds',90))) as r:
            out=json.loads(r.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        details=e.read().decode('utf-8','replace')[:800]; raise RuntimeError(f'AI-server HTTP {e.code}: {details}')
    except urllib.error.URLError as e: raise RuntimeError(f'Kan ikke nå AI-serveren: {e.reason}')
    try: return out['choices'][0]['message']['content'].strip()
    except Exception: raise RuntimeError('AI-serverens svar er ikke OpenAI-kompatibelt chat-completions format')

def test_backend(config):
    reply=call_model(config,[{'role':'system','content':'Reply with exactly: CHROMALEARN_OK'},{'role':'user','content':'health check'}])
    return {'ok':'CHROMALEARN_OK' in reply,'reply':reply[:200]}
