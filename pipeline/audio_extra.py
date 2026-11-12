"""Trilha procedural (arpejo 'curioso') e efeitos (whoosh, pop, máquina de escrever, marca-texto). Uso: audio_extra.py eventos.json dur saida_dir"""
import json,sys,numpy as np,soundfile as sf
SR=48000; ev=json.load(open(sys.argv[1])); dur=float(sys.argv[2]); out=sys.argv[3]
rng=np.random.default_rng(1); N=int(dur*SR)+SR
def nota(f,d=0.5,amp=0.3):
    t=np.arange(int(d*SR))/SR; env=np.exp(-t*7)*(1-np.exp(-t*400))
    return amp*env*(np.sin(2*np.pi*f*t)+0.35*np.sin(4*np.pi*f*t)+0.12*np.sin(6*np.pi*f*t))
mus=np.zeros(N,np.float32); bpm=100; e=60/bpm/2
A=lambda n:440*2**((n-69)/12)
prog=[[57,60,64,69],[53,57,60,65],[48,55,60,64],[55,59,62,67]]  # Am F C G
pat=[0,2,1,3,2,1,3,2]; i=0; t=0.0
while t<dur:
    ch=prog[(i//8)%4]; f=A(ch[pat[i%8]]+12); s=int(t*SR); x=nota(f,0.45,0.22); mus[s:s+len(x)]+=x[:max(0,N-s)]
    if i%8==0:
        b=nota(A(ch[0]-12),1.4,0.35); mus[s:s+len(b)]+=b[:max(0,N-s)]
    if i%4==2:  # 'tick' leve de percussão
        k=rng.normal(0,1,int(0.03*SR))*np.exp(-np.arange(int(0.03*SR))/SR*150)*0.05; mus[s:s+len(k)]+=k[:max(0,N-s)]
    i+=1; t+=e
fade=np.ones(N); fl=int(1.5*SR); fade[int(dur*SR)-fl:int(dur*SR)]=np.linspace(1,0,fl); fade[int(dur*SR):]=0; mus*=fade
sf.write(f'{out}/trilha.wav',np.stack([mus,mus],1)*0.6,SR)
fx=np.zeros(N,np.float32)
def add(s,x):
    s=int(s*SR); fx[s:s+len(x)]+=x[:max(0,N-s)]
for e_ in ev:
    t,tp=e_['t'],e_['tipo']
    if tp=='whoosh':
        n=int(0.35*SR); x=rng.normal(0,1,n); 
        # passa-banda varrendo: filtro simples de média móvel variável
        env=np.sin(np.linspace(0,np.pi,n))**2; y=np.convolve(x,np.ones(6)/6,'same')-np.convolve(x,np.ones(40)/40,'same'); add(t-0.12,0.35*y*env)
    elif tp=='pop':
        n=int(0.09*SR); tt=np.arange(n)/SR; f=np.linspace(900,380,n); add(t,0.35*np.sin(2*np.pi*np.cumsum(f)/SR)*np.exp(-tt*45))
    elif tp=='tecla':
        for j in range(e_.get('n',4)):
            n=int(0.025*SR); add(t+j*0.07+rng.uniform(0,0.02),rng.normal(0,1,n)*np.exp(-np.arange(n)/SR*260)*0.25)
    elif tp=='marca':
        n=int(e_.get('d',0.6)*SR); x=rng.normal(0,1,n); y=np.convolve(x,np.ones(3)/3,'same'); env=0.5+0.5*np.sin(np.arange(n)/SR*2*np.pi*9); add(t,0.08*y*env)
sf.write(f'{out}/efeitos.wav',np.stack([fx,fx],1),SR)
print('ok')
