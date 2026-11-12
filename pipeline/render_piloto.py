"""Render do piloto NR-P001 (colagem). Uso: render_piloto.py ep_dir [quadros|video] [t1,t2,...]"""
import json,sys,subprocess,math
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from base import *
import colagem as C
EP=sys.argv[1]; MODO=sys.argv[2] if len(sys.argv)>2 else 'video'
rot=json.load(open(f'{EP}/roteiro.json')); tm=json.load(open(f'{EP}/tempos.json'))
FPS=30; DUR=tm['total']+0.6; NF=int(DUR*FPS)
COR=tuple(C.PAPEL_M); C.MATERIA_ATUAL['nome']=rot['materia']
BG=C.papel(W,H,7)
cen={c['id']:c for c in tm['cenas']}
def cue(cid,fi=0,frac=0.0):
    f=cen[cid]['frases'][fi]; return f['inicio']+frac*f['dur']-cen[cid]['inicio']
def cue_palavra(cid,fi,palavra):
    f=cen[cid]['frases'][fi]; i=f['leg'].lower().find(palavra.lower()); return f['inicio']-cen[cid]['inicio']+f['dur']*max(0,i)/len(f['leg'])
# ---------- elementos (pré-renderizados, com sombra)
def S(img,**k): return shadow(img,**k)   # (desloca 40 px)
def rot_(img,a): return img.rotate(a,expand=True,resample=Image.BICUBIC)
EL={}
EL['tv']=S(rot_(C.recorte_retícula(C.tv_cinza(470,423),cell=7),-6),off=(8,12),blur=12,alpha=90)
EL['tv_p']=S(rot_(C.recorte_retícula(C.tv_cinza(380,342),cell=6),5),off=(6,9),blur=10,alpha=90)
EL['radio']=S(rot_(C.recorte_retícula(C.radio_cinza(360,336),cell=6),-4),off=(6,9),blur=10,alpha=90)
jp0=torn(C.jornal(560,720,0.0),8); jp1=torn(C.jornal(560,720,1.0),8)
EL['jp']=S(rot_(jp0,-3),off=(8,10),blur=12,alpha=80)
EL['jp_p']=S(rot_(torn(C.jornal(300,390,0.0),5),4),off=(5,7),blur=8,alpha=80)
JB0=torn(C.jornal(1000,1290,0.0),12); JB1=torn(C.jornal(1000,1290,1.0),12)
EL['jd']=S(rot_(torn(C.jornal(560,720,1.0,seed=9,titulo='DIARIO DO RIO DE JANEIRO',data='RIO DE JANEIRO  ·  1857',rodape='FOLHETIM — O GUARANI'),8),3),off=(8,10),blur=12,alpha=80)
# faixa do rodapé recortada
ft=int(1290*0.70)-20; EL['rodape']=S(rot_(torn(JB1.crop((0,ft,1000,1290)).resize((820,int((1290-ft)*0.82))),7,seed=4),-2),off=(8,10),blur=12,alpha=80)
def T(txt,size=46,**k): return S(rot_(C.tira(txt,size,**k),k.get('a',-3) if False else -3),off=(4,6),blur=6,alpha=70)
def B(txt,size,maxw,ang=0,**k): return S(rot_(C.bloco(txt,size,maxw,**k),ang),off=(6,8),blur=8,alpha=60)
EL['b_pergunta']=B('por que a novela sempre para na melhor parte?',74,720,ang=0)
EL['t_1836']=T('1836',64); EL['t_paris']=T('PARIS, 1836',46)
EL['t_80']=T('80 francos/ano',50); EL['b_40']=B('40 francos/ano',62,600,ang=3)
EL['t_ann']=[T(x,40) for x in ['ANNONCES','ANNONCES','ANNONCES']]
EL['b_folhetim']=B('FOLHETIM',72,600,ang=-4); EL['t_ent']=T('= espaço de entretenimento',40)
EL['caps']=[T(f'capítulo {i}',48) for i in (1,2,3)]
EL['t_balzac']=T('BALZAC, 1836',46)
EL['b_gancho']=B('o gancho',70,600,ang=-3)
EL['t_rio']=T('RIO DE JANEIRO, 1857',44); EL['b_52']={}
EL['t_janabr']=T('de janeiro a abril',40); EL['b_guarani']=B('O Guarani',60,500,ang=-4)
EL['b_meyer']=B('a telenovela é uma "tradução" atualizada do folhetim',52,740,ang=0)
EL['t_meyer']=T('— Marlyse Meyer, Folhetim: uma história',30)
EL['b_cta']=B('qual final de capítulo te deixou mais aflito?',68,740,ang=-1)
EL['t_200']=T('de 1836 até hoje: quase 200 anos',40)
def bloco52(n):
    if n not in EL['b_52']: EL['b_52'][n]=B(f'{n} edições',70,600,ang=2)
    return EL['b_52'][n]
nota_cache={}
def NOTA(txt,size=58,ang=-4,cor=None):
    k=(txt,size,ang)
    if k not in nota_cache:
        f=F('caveat',700,size); lines=txt.split('\n'); w=int(max(f.getlength(l) for l in lines))+30; h=int(size*1.2*len(lines))+30
        t=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(t)
        for i,l in enumerate(lines): d.text((15,15+i*size*1.2),l,font=f,fill=cor or C.PAL['tinta'])
        nota_cache[k]=rot_(t,ang)
    return nota_cache[k]
# ---------- animação
EV=[]  # eventos de som
def back(p):
    p=max(0,min(1,p)); c1=1.70158; c3=c1+1; return 1+c3*(p-1)**3+c1*(p-1)**2
def put(st,img,c,t=None,t0=0,dur=0.32,scale=1.0,alpha=1.0,slide=None,wob=0):
    """cola img centrada em c; se t dado, anima entrada em t0 (pop, ou slide=(dx,dy))."""
    if t is not None:
        if t<t0: return
        p=(t-t0)/dur
        if slide:
            q=ease(p); c=(c[0]+slide[0]*(1-q),c[1]+slide[1]*(1-q)); alpha*=min(1,p*2.5)
        else:
            scale*=back(p)*0.4+0.6 if p<1 else 1.0; alpha*=min(1,p*3)
    if wob and t is not None: scale*=1+0.012*math.sin(t*2.2)
    im=img
    if abs(scale-1)>0.004: im=img.resize((max(1,int(img.width*scale)),max(1,int(img.height*scale))),Image.BILINEAR)
    if alpha<0.999: im=im.copy(); im.putalpha(im.split()[3].point(lambda v:int(v*alpha)))
    st.alpha_composite(im,(int(c[0]-im.width/2),int(c[1]-im.height/2)))
def reveal(st,img,xy,p):
    """escrita à mão: revela da esquerda p/ direita"""
    if p<=0: return
    w=int(img.width*min(1,p)); st.alpha_composite(img.crop((0,0,w,img.height)),(int(xy[0]),int(xy[1])))
def camera(st,scale,anchor,screen,blur=0):
    a=1/scale; t=st.transform((W,H),Image.AFFINE,(a,0,anchor[0]-screen[0]*a,0,a,anchor[1]-screen[1]*a),resample=Image.BILINEAR,fillcolor=COR+(255,))
    if blur>0.3: t=t.filter(ImageFilter.GaussianBlur(blur))
    return t
# ---------- cenas: f(t local) -> palco RGBA (antes da câmera)
def c1(t):
    st=BG.copy()
    put(st,EL['tv'],(CX+30,660),scale=1.0+0.012*math.sin(t*2.2))
    put(st,EL['b_pergunta'],(CX,1070))
    put(st,EL['t_1836'],(230,470),t=t,t0=cue('c1',1,0.55))
    put(st,NOTA('é um truque!',62,-6,C.PAL['destaque']),(720,440),t=t,t0=cue('c1',1,0.1))
    return camera(st,1.0+0.05*smooth(t/6.5),(CX,800),(CX,800))
def c2(t):
    st=BG.copy()
    put(st,EL['jp'],(CX-60,760),t=t,t0=0,slide=(700,0),dur=0.4)
    put(st,EL['t_paris'],(260,440),t=t,t0=0.25)
    put(st,NOTA('Émile de Girardin',56,-3),(725,485),t=t,t0=cue_palavra('c2',1,'Girardin'))
    put(st,EL['t_80'],(640,980),t=t,t0=cue('c2',2,0.55))
    p=(t-cue('c2',2,0.75))/0.3
    if p>0:
        d=ImageDraw.Draw(st); x0,x1=470,470+(810-470)*min(1,p); d.line([(x0,990),(x1,970)],fill=C.PAL['destaque'],width=10)
    put(st,EL['b_40'],(620,1110),t=t,t0=cue('c2',2,0.05))
    return camera(st,1.0+0.04*smooth(t/11),(CX,800),(CX,800))
def c3(t):
    st=Image.new('RGBA',(W,H),COR+(255,)); st.alpha_composite(BG)
    sweep=smooth((t-cue('c3',2,0.62))/0.9)
    jb=JB0 if sweep<=0 else JB1 if sweep>=1 else None
    if jb is None:
        jb=JB0.copy(); m=60; x1=int(m-10+(1000-2*m+20)*sweep); jb.paste(JB1.crop((0,0,x1,1290)),(0,0),JB1.crop((0,0,x1,1290)))
    st.alpha_composite(jb,(CX-500,330))
    pos=[(230,620),(690,760),(330,900)]
    for i,tg in enumerate(EL['t_ann']):
        t0=cue('c3',0,0.6)+i*0.18
        if t>=t0: put(st,tg,pos[i],t=t,t0=t0)
    # câmera: plano geral -> mergulha no rodapé
    z=smooth((t-cue('c3',2,0.35))/1.1)
    foot_y=330+int(1290*0.70)+150
    out=camera(st,0.78*(1-z)+1.35*z,(CX,(330+645)*(1-z)+foot_y*z),(CX,800))
    return out
def c4(t):
    st=BG.copy()
    put(st,EL['rodape'],(CX,640),t=t,t0=0,dur=0.25)
    put(st,EL['b_folhetim'],(690,500),t=t,t0=cue_palavra('c4',0,'folhetim'))
    put(st,EL['t_ent'],(CX,830),t=t,t0=cue_palavra('c4',0,'espaço'))
    for i,cp in enumerate(EL['caps']):
        put(st,cp,(300+i*210,960+i*55),t=t,t0=cue('c4',1,0.62)+i*0.22,slide=(0,120),dur=0.3)
    put(st,EL['t_balzac'],(330,1130),t=t,t0=cue_palavra('c4',1,'Balzac'))
    return camera(st,1.0+0.05*smooth(t/10),(CX,800),(CX,800))
NT_CONT=NOTA('continua\namanhã...',150,-4)
def c5(t):
    st=BG.copy()
    put(st,EL['caps'][0],(250,520),t=t,t0=0); put(st,EL['caps'][1],(470,580)); 
    p=(t-cue_palavra('c5',0,'suspense'))/1.0
    put(st,EL['b_gancho'],(700,500),t=t,t0=cue_palavra('c5',0,'truque'))
    reveal(st,NT_CONT,(CX-NT_CONT.width/2,640),p)
    put(st,NOTA('(pra saber o resto, só comprando o jornal)',46,-2,C.PAL['sec']),(CX,1110),t=t,t0=cue('c5',1,0.1))
    # dolly: aproxima devagar do 'continua'
    return camera(st,1.0+0.10*smooth(t/7.6),(CX,820),(CX,820))
def c6(t):
    st=BG.copy()
    put(st,EL['t_rio'],(300,415),t=t,t0=0.05)
    put(st,EL['jd'],(CX-90,850),t=t,t0=cue('c6',1,0.0),slide=(-700,0),dur=0.4)
    put(st,NOTA('José de Alencar',60,4),(760,440),t=t,t0=cue_palavra('c6',1,'Alencar'))
    put(st,EL['b_guarani'],(720,950),t=t,t0=cue_palavra('c6',1,'Guarani'))
    t0=cue('c6',2,0.05)
    if t>=t0:
        n=max(2,min(52,int(2+50*smooth((t-t0)/1.3)))); put(st,bloco52(n),(620,1110),t=t,t0=t0)
    put(st,EL['t_janabr'],(260,1175),t=t,t0=cue_palavra('c6',2,'janeiro'))
    return camera(st,1.0+0.04*smooth(t/12.8),(CX,800),(CX,800))
def c7(t):
    st=BG.copy(); d=ImageDraw.Draw(st)
    put(st,EL['jp_p'],(260,600),t=t,t0=0)
    tr=cue_palavra('c7',0,'rádio'); tv=cue_palavra('c7',0,'televisão')
    if t>tr-0.15: k=smooth((t-tr+0.15)/0.3); arrow(d,(420,560),(420+120*k,560+40*k),12,C.PAL['tinta'],40)
    put(st,EL['radio'],(700,700),t=t,t0=tr)
    if t>tv-0.15: k=smooth((t-tv+0.15)/0.3); arrow(d,(620,900),(620-130*k,900+70*k),12,C.PAL['tinta'],40)
    put(st,EL['tv_p'],(330,1040),t=t,t0=tv)
    q=cue('c7',1,0.25)
    if t>=q:
        k=smooth((t-q)/0.4); bl=st.filter(ImageFilter.GaussianBlur(10*k))   # rack focus: fundo desfoca, citação entra
        bl.alpha_composite(Image.new('RGBA',(W,H),COR+(int(110*k),)))
        put(bl,EL['b_meyer'],(CX,760),t=t,t0=q); put(bl,EL['t_meyer'],(CX,960),t=t,t0=q+0.5); st=bl
    return camera(st,1.0+0.04*smooth(t/10.5),(CX,800),(CX,800))
def pausa_ico():
    im=Image.new('RGBA',(150,150),(0,0,0,0)); d=ImageDraw.Draw(im); d.rounded_rectangle((0,0,150,150),radius=24,fill=(252,250,246,240))
    d.rectangle((42,35,66,115),fill=C.PAL['tinta']); d.rectangle((84,35,108,115),fill=C.PAL['tinta']); return S(rot_(im,-6),off=(5,7),blur=7,alpha=70)
EL['pausa']=pausa_ico(); EL['t_avb']=T('AVENIDA BRASIL, 2012',46); EL['t_52']=T('52 pontos de Ibope em SP',40)
EL['b_500']=B('+500 anunciantes',66,640,ang=-3); EL['t_ann1']=T('ANNONCES, 1836',36)
def c7b(t):
    st=BG.copy()
    put(st,EL['t_avb'],(330,420),t=t,t0=0.05)
    put(st,EL['tv'],(CX+30,720),t=t,t0=0.0,wob=1)
    fz=cue_palavra('c7b',0,'congelada'); fz_fim=cue('c7b',1,0.0)
    if t>=fz: put(st,EL['pausa'],(CX+10,700),t=t,t0=fz,dur=0.18)
    put(st,NOTA('bar lotado!',66,-6,C.PAL['destaque']),(770,990),t=t,t0=cue_palavra('c7b',1,'bar'))
    put(st,EL['t_52'],(320,1000),t=t,t0=cue_palavra('c7b',1,'final'))
    put(st,EL['b_500'],(620,1120),t=t,t0=cue_palavra('c7b',2,'500'))
    put(st,EL['t_ann1'],(770,455),t=t,t0=cue_palavra('c7b',2,'Igualzinho'))
    punch=1.0
    if fz<=t<fz_fim: punch=1.07
    out=camera(st,(1.0+0.03*smooth(t/12))*punch,(CX,760),(CX,780))
    if fz<=t<fz_fim:   # homenagem ao 'congelamento': quadro em P&B enquanto a imagem 'congela'
        g=out.convert('L').point(lambda v:int(v*0.95)).convert('RGBA'); out=Image.blend(out,g,0.85)
    return out
def c8(t):
    st=BG.copy()
    put(st,EL['tv'],(CX+40,600),t=t,t0=0,wob=1)
    put(st,EL['t_200'],(CX,880),t=t,t0=cue('c8',1,0.1))
    put(st,EL['b_cta'],(CX,1050),t=t,t0=cue('c8',2,0.0))
    put(st,NOTA('comenta aí!',62,-8,C.PAL['destaque']),(790,790),t=t,t0=cue('c8',2,0.6))
    return camera(st,1.0+0.05*smooth(t/11),(CX,800),(CX,800))
FUN={'c1':c1,'c2':c2,'c3':c3,'c4':c4,'c5':c5,'c6':c6,'c7':c7,'c7b':c7b,'c8':c8}
# ---------- legendas (blocos curtos, palavra atual em laranja)
CHUNKS=[]
for c in tm['cenas']:
    for f in c['frases']:
        ws=f['leg'].split(); tot=len(f['leg']); acc=0; cur=[]
        grupos=[]; 
        for w_ in ws:
            if cur and len(' '.join(cur+[w_]))>24: grupos.append(cur); cur=[]
            cur.append(w_)
        if cur: grupos.append(cur)
        pos=0
        for g in grupos:
            txt=' '.join(g); wt=[]
            for w_ in g:
                a=f['inicio']+f['dur']*pos/tot; pos+=len(w_)+1; wt.append(a)
            fim=f['inicio']+f['dur']*min(1,pos/tot)
            CHUNKS.append((wt[0],fim,g,wt))
FL=F('inter',800,54)
def legenda(img,t):
    ch=None
    for i,(a,b,g,wt) in enumerate(CHUNKS):
        nxt=CHUNKS[i+1][0] if i+1<len(CHUNKS) else b+0.6
        if a<=t<min(nxt,b+0.5): ch=(g,wt)
    if not ch: return
    g,wt=ch; d=ImageDraw.Draw(img); txt=' '.join(g); w=FL.getlength(txt); y=1240
    d.rectangle((CX-w/2-18,y-6,CX+w/2+18,y+66),fill=C.PAL['tinta']); x=CX-w/2
    for w_,a in zip(g,wt):
        d.text((x,y),w_,font=FL,fill=C.PAL['destaque'] if a<=t else (250,246,236)); x+=FL.getlength(w_+' ')
FONTE_TXT={'c2':'Fonte: BnF; Univ. Paris 1','c3':'Fonte: BnF; Univ. Paris 1','c4':'Fonte: MEYER, M. Folhetim: uma história (1996)',
 'c5':'Fonte: MEYER, M. Folhetim: uma história (1996)','c6':'Fonte: Revista Organon (UFRGS)','c7':'Fonte: MEYER, M. Folhetim: uma história (1996)','c7b':'Fontes: Meio & Mensagem (2012); Mais Goiás; Guia da Semana'}
def ui(img,cid,t):
    C.marca_topo(img); C.chip_materia(img,rot['materia']); legenda(img,t)
    if cid in FONTE_TXT: C.fonte(img,FONTE_TXT[cid])
    C.barra(img,min(1,t/DUR))
def quadro(t):
    cid=tm['cenas'][0]['id']
    for c in tm['cenas']:
        if t>=c['inicio']-(0.1 if c['id']!='c1' else 99): cid=c['id']
    c0=cen[cid]['inicio'] if cid!='c1' else 0.0
    im=FUN[cid](max(0,t-c0)); ui(im,cid,t); return im
# eventos de som (whoosh nas trocas; pop nos elementos principais; tecla nas tiras)
def eventos():
    e=[]
    for c in tm['cenas'][1:]: e.append({'t':c['inicio']-0.1,'tipo':'whoosh'})
    a=lambda cid,fi,fr=0: cen[cid]['inicio']+cue(cid,fi,fr)
    w=lambda cid,fi,p: cen[cid]['inicio']+cue_palavra(cid,fi,p)
    e+= [{'t':a('c1',1,0.55),'tipo':'tecla','n':4},{'t':a('c2',2,0.55),'tipo':'tecla','n':5},{'t':a('c2',2,0.05),'tipo':'pop'},
         {'t':a('c2',2,0.75),'tipo':'marca','d':0.3},{'t':a('c3',0,0.6),'tipo':'pop'},{'t':a('c3',0,0.6)+0.18,'tipo':'pop'},{'t':a('c3',0,0.6)+0.36,'tipo':'pop'},
         {'t':a('c3',2,0.62),'tipo':'marca','d':0.9},{'t':w('c4',0,'folhetim'),'tipo':'pop'},{'t':a('c4',1,0.62),'tipo':'tecla','n':3},
         {'t':w('c4',1,'Balzac'),'tipo':'tecla','n':4},{'t':w('c5',0,'truque'),'tipo':'pop'},{'t':w('c5',0,'suspense'),'tipo':'marca','d':1.0},
         {'t':cen['c6']['inicio']+0.05,'tipo':'tecla','n':5},{'t':a('c6',2,0.05),'tipo':'pop'},{'t':w('c7',0,'rádio'),'tipo':'pop'},
         {'t':w('c7',0,'televisão'),'tipo':'pop'},{'t':a('c7',1,0.25),'tipo':'whoosh'},{'t':a('c8',2,0.0),'tipo':'pop'},{'t':w('c7b',0,'congelada'),'tipo':'tecla','n':1},{'t':w('c7b',2,'500'),'tipo':'pop'},{'t':w('c7b',1,'bar'),'tipo':'pop'}]
    return e
if MODO=='quadros':
    ts=[float(x) for x in sys.argv[3].split(',')]
    for t in ts: quadro(t).convert('RGB').save(f'/tmp/q_{t:.2f}.png')
elif MODO=='capa':
    st=BG.copy(); put(st,EL['tv'],(CX+30,640)); put(st,EL['b_pergunta'],(CX,1080))
    big=S(rot_(C.tira('1836',120),-5),off=(5,8),blur=8,alpha=70); put(st,big,(290,540))
    put(st,NOTA('é um truque!',70,-6,C.PAL['destaque']),(730,440))
    C.marca_topo(st); C.chip_materia(st,rot['materia']); st.convert('RGB').save(f'{EP}/capa.png'); print('capa ok')
elif MODO=='eventos':
    json.dump(eventos(),open(f'{EP}/eventos.json','w')); print(DUR)
else:
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
       '-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',f'{EP}/video_mudo.mp4'],stdin=subprocess.PIPE)
    for i in range(NF):
        p.stdin.write(quadro(i/FPS).convert('RGB').tobytes())
        if i%150==0: print(i,NF,flush=True)
    p.stdin.close(); p.wait(); print('fim')
