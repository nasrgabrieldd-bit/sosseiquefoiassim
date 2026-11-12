"""Narração frase a frase (Kokoro pt-BR) com mapa de tempos por frase. Uso: narra.py roteiro.json saida_dir [voz] [vel]"""
import json, sys, os, re, subprocess
import numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
rot=json.load(open(sys.argv[1])); out=sys.argv[2]
voz=sys.argv[3] if len(sys.argv)>3 else 'pm_alex+pm_santa:0.6'; vel=float(sys.argv[4]) if len(sys.argv)>4 else 0.98
M=os.environ.get('MODELOS',os.path.expanduser('~/tts'))
k=Kokoro(f'{M}/kokoro-v1.0.onnx',f'{M}/voices-v1.0.bin')
def estilo(v):
    if '+' not in v: return v
    a,r=v.split('+'); b,p=(r.split(':')+['0.5'])[:2]; p=float(p)
    return p*k.get_voice_style(a)+(1-p)*k.get_voice_style(b)
V=estilo(voz); SR=24000
def sint(txt):
    # frases internas separadas por ? ! . ganham micro-pausa
    partes=[p for p in re.split(r'(?<=[\?\!\.])\s+',txt) if p]; seg=[]
    for i,p in enumerate(partes):
        a,_=k.create(p,voice=V,speed=vel,lang='pt-br'); seg.append(a.astype(np.float32))
        if i<len(partes)-1: seg.append(np.zeros(int((0.38 if p.endswith('?') else 0.22)*SR),np.float32))
    return np.concatenate(seg)
INICIO=0.1; t=INICIO; trechos=[np.zeros(int(INICIO*SR),np.float32)]; mapa=[]
for c in rot['cenas']:
    cm={'id':c['id'],'inicio':round(t,3),'frases':[]}
    for j,(leg,tts) in enumerate(c['frases']):
        a=sint(tts); d=len(a)/SR
        cm['frases'].append({'leg':leg,'inicio':round(t,3),'dur':round(d,3)})
        trechos.append(a); t+=d
        last=j==len(c['frases'])-1
        p=0.42 if last else (0.34 if tts.rstrip().endswith('?') else 0.2)
        trechos.append(np.zeros(int(p*SR),np.float32)); t+=p
    cm['fim']=round(t,3); mapa.append(cm); print(c['id'],round(t,2))
au=np.concatenate(trechos); au=au/np.max(np.abs(au))*0.89
sf.write(f'{out}/voz_bruta.wav',au,SR)
subprocess.run(['ffmpeg','-loglevel','error','-y','-i',f'{out}/voz_bruta.wav','-af',
 'highpass=f=70,equalizer=f=180:t=q:w=1:g=2,equalizer=f=3500:t=q:w=1.5:g=2,acompressor=threshold=-18dB:ratio=2.5:attack=8:release=120,aecho=0.8:0.5:22:0.05',
 '-ar','48000',f'{out}/voz.wav'],check=True)
json.dump({'voz':voz,'vel':vel,'total':round(t,3),'cenas':mapa},open(f'{out}/tempos.json','w'),ensure_ascii=False,indent=1)
print('total',round(t,2))
