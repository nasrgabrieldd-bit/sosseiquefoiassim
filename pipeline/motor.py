"""Motor de render da colagem (cenas descritas no roteiro.json).
Uso: motor.py ep_dir video|quadros t1,t2|prancha|capa|eventos"""
import json,sys,subprocess,math
import os
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from base import *
import colagem as C, objetos as O
MARCA=json.load(open(ROOT+'/marca/marca.json'))
EP=sys.argv[1]; MODO=sys.argv[2] if len(sys.argv)>2 else 'video'
rot=json.load(open(f'{EP}/roteiro.json')); tm=json.load(open(f'{EP}/tempos.json'))
FPS=30; DUR=tm['total']+0.6; NF=int(DUR*FPS)
COR=tuple(C.PAPEL_M); C.MATERIA_ATUAL['nome']=rot['materia']
BG=C.papel(W,H,sum(map(ord,rot['id'])))
FOLHA=C.folha_transicao()
CEN={c['id']:c for c in tm['cenas']}; SPEC={c['id']:c for c in rot['cenas']}
TINTA=C.PAL['tinta']; LAR=C.PAL['destaque']; PAPEL=C.PAL['papel']
def S(img,**k): return shadow(img,**k)
def R(img,a): return img.rotate(a,expand=True,resample=Image.BICUBIC) if a else img
# ---------- tempos
def cue(cid,e):
    if e is None: return 0.0
    fi,x=e; f=CEN[cid]['frases'][fi]; base=f['inicio']-CEN[cid]['inicio']
    if isinstance(x,str):
        i=f['leg'].lower().find(x.lower())
        if i<0: raise SystemExit(f'palavra "{x}" não está na frase {fi} de {cid}')
        return base+f['dur']*i/len(f['leg'])
    return base+f['dur']*float(x)
# ---------- construção dos elementos
def mk_nota(txt,size,ang,cor):
    f=F('caveat',700,size); lines=txt.split('\n'); w=int(max(f.getlength(l) for l in lines))+30; h=int(size*1.2*len(lines))+30
    t=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(t)
    for i,l in enumerate(lines): d.text((15,15+i*size*1.2),l,font=f,fill=cor)
    return R(t,ang)
def mk_numero(txt,size,cor):
    f=F('anton',400,size); bb=f.getbbox(txt); im=Image.new('RGBA',(bb[2]+20,bb[3]+20),(0,0,0,0))
    ImageDraw.Draw(im).text((10,0),txt,font=f,fill=cor); return im
def mk_verbete(pal,classe,defi,w=640):
    f1=F('playfair-display',900,64); f2=F('special-elite',400,30); f3=F('special-elite',400,34)
    lines=wrap(defi,f3,w-60); h=60+80+44+len(lines)*44+30
    im=Image.new('RGBA',(w,h),PAPEL+(255,)); d=ImageDraw.Draw(im)
    d.text((30,26),pal,font=f1,fill=TINTA); d.text((32,112),classe,font=f2,fill=(120,110,100))
    for i,l in enumerate(lines): d.text((30,160+i*44),l,font=f3,fill=TINTA)
    return torn(im,4,seed=len(pal))
def mk_cal(ano_mes,dias_riscados,inicio_semana=0,ndias=31,w=620):
    f1=F('playfair-display',900,52); f2=F('inter',800,34); fs=F('special-elite',400,26)
    cw=(w-40)/7; h=150+6*cw+20
    im=Image.new('RGBA',(w,int(h)),PAPEL+(255,)); d=ImageDraw.Draw(im)
    d.rectangle((0,0,w,92),fill=TINTA); d.text(((w-f1.getlength(ano_mes))/2,14),ano_mes,font=f1,fill=PAPEL)
    for i,s in enumerate('DSTQQSS'): d.text((20+i*cw+cw/2-8,102),s,font=fs,fill=(110,100,95))
    for n in range(1,ndias+1):
        p=n-1+inicio_semana; r,c=divmod(p,7); x=20+c*cw; y=140+r*cw
        d.text((x+cw/2-f2.getlength(str(n))/2,y+cw/2-22),str(n),font=f2,fill=TINTA)
    return torn(im,4,seed=7),cw
def mk_areas(a_lbl,b_lbl,ratio,w=760):
    big=int(w*0.62); small=int(big/math.sqrt(ratio)); h=big+90
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im); f=F('inter',800,34)
    d.rectangle((0,0,big,big),fill=LAR); d.text((16,big+16),a_lbl,font=f,fill=TINTA)
    x=big+40; d.rectangle((x,big-small,x+small,big),fill=TINTA); d.text((x,big+16),b_lbl,font=f,fill=TINTA)
    return im
CACHE={}
def build(el,key):
    if key in CACHE: return CACHE[key]
    t=el['t']; ang=el.get('ang',0); out=None
    if t=='obj':
        w=el.get('w',360); h=el.get('h',w); out=S(R(C.recorte_retícula(O.OBJ[el['nome']](w,h),cell=el.get('cell',6)),ang),off=(7,10),blur=10,alpha=90)
    elif t=='tv': w=el.get('w',420); out=S(R(C.recorte_retícula(C.tv_cinza(w,int(w*0.9)),cell=7),ang),off=(8,12),blur=12,alpha=90)
    elif t=='radio': w=el.get('w',360); out=S(R(C.recorte_retícula(C.radio_cinza(w,int(w*0.93)),cell=6),ang),off=(7,10),blur=10,alpha=90)
    elif t=='jornal':
        kw=dict(seed=el.get('seed',5),titulo=el.get('titulo','LA PRESSE'),data=el.get('data','PARIS  ·  1836'),rodape=el.get('rodape','FEUILLETON'))
        w=el.get('w',560); h=el.get('h',int(w*1.29))
        j0=torn(C.jornal(w,h,0.0,**kw),8); j1=torn(C.jornal(w,h,1.0,**kw),8)
        out=(S(R(j0,ang),off=(8,10),blur=12,alpha=80),S(R(j1,ang),off=(8,10),blur=12,alpha=80))
    elif t=='tira': out=S(R(C.tira(el['txt'],el.get('size',44)),ang if ang else -3),off=(4,6),blur=6,alpha=70)
    elif t=='bloco':
        cor={'laranja':LAR,'tinta':TINTA,'papel':PAPEL}[el.get('cor','laranja')]; fg=PAPEL if el.get('cor')=='tinta' else TINTA
        out=S(R(C.bloco(el['txt'],el.get('size',64),el.get('maxw',700),cor=cor,fg=fg),ang),off=(6,8),blur=8,alpha=60)
    elif t=='nota': out=mk_nota(el['txt'],el.get('size',58),ang if ang else -4,LAR if el.get('cor')=='laranja' else TINTA)
    elif t=='numero': out=R(mk_numero(el['txt'],el.get('size',300),LAR if el.get('cor','laranja')=='laranja' else TINTA),ang)
    elif t=='verbete': out=S(R(mk_verbete(el['palavra'],el.get('classe',''),el['def'],el.get('w',640)),ang),off=(8,10),blur=10,alpha=80)
    elif t=='cal':
        im,cw=mk_cal(el['titulo'],el.get('riscar',[]),el.get('inicio',0),el.get('ndias',31)); out=(im,cw)
    elif t=='areas': out=mk_areas(el['a'],el['b'],el['ratio'],el.get('w',760))
    CACHE[key]=out; return out
def seta_mao(d,p0,p1,k,cor,esp=10):
    (x0,y0),(x1,y1)=p0,p1; L=math.hypot(x1-x0,y1-y0); nx,ny=-(y1-y0)/L,(x1-x0)/L
    cx,cy=(x0+x1)/2+nx*L*0.12,(y0+y1)/2+ny*L*0.12; pts=[]
    n=max(2,int(24*k))
    for i in range(n+1):
        t=i/24
        if t>k: break
        pts.append(((1-t)**2*x0+2*(1-t)*t*cx+t*t*x1,(1-t)**2*y0+2*(1-t)*t*cy+t*t*y1))
    if len(pts)>1: d.line(pts,fill=cor,width=esp,joint='curve')
    if k>=0.95 and len(pts)>2:
        ex,ey=pts[-1]; px,py=pts[-3]; a=math.atan2(ey-py,ex-px); h=34
        for s_ in (-0.55,0.55): d.line([(ex,ey),(ex-h*math.cos(a+s_),ey-h*math.sin(a+s_))],fill=cor,width=esp)
# ---------- animação
def back(p):
    p=max(0,min(1,p)); c1=1.70158; c3=c1+1; return 1+c3*(p-1)**3+c1*(p-1)**2
def colar(st,img,c,scale=1.0,alpha=1.0):
    im=img
    if abs(scale-1)>0.004: im=img.resize((max(1,int(img.width*scale)),max(1,int(img.height*scale))),Image.BILINEAR)
    if alpha<0.999: im=im.copy(); im.putalpha(im.split()[3].point(lambda v:int(v*alpha)))
    st.alpha_composite(im,(int(c[0]-im.width/2),int(c[1]-im.height/2)))
def camera(st,scale,anchor,screen,blur=0):
    a=1/scale; t=st.transform((W,H),Image.AFFINE,(a,0,anchor[0]-screen[0]*a,0,a,anchor[1]-screen[1]*a),resample=Image.BILINEAR,fillcolor=COR+(255,))
    if blur>0.3: t=t.filter(ImageFilter.GaussianBlur(blur))
    return t
def desenha(st,el,key,tl,t0,cid,estatico=False):
    anim=el.get('anim','pop'); p=1.0 if estatico else (tl-t0)/el.get('dur',0.3)
    if p<0: return
    alpha=1.0; scale=el.get('escala',1.0); c=list(el['pos'])
    if 'sai' in el:
        ts=cue(cid,el['sai']); 
        if tl>=ts: alpha*=max(0,1-(tl-ts)/0.25)
        if alpha<=0: return
    if el.get('balanca') and not estatico: scale*=1+0.012*math.sin(tl*2.2)
    if p<1:
        if anim=='pop': scale*=back(p)*0.4+0.6; alpha*=min(1,p*3)
        elif anim.startswith('slide'):
            q=ease(p); dx,dy={'slide_l':(-700,0),'slide_r':(700,0),'slide_b':(0,500),'slide_t':(0,-400)}[anim]
            c=[c[0]+dx*(1-q),c[1]+dy*(1-q)]; alpha*=min(1,p*2.5)
        elif anim=='fade': alpha*=p
    t=el['t']
    if t=='jornal':
        j0,j1=build(el,key)
        if 'marca' in el:
            sw=smooth((tl-cue(cid,el['marca']))/0.9)
            if sw<=0: img=j0
            elif sw>=1: img=j1
            else:
                img=j0.copy(); x1=int(j0.width*(0.08+0.84*sw)); img.paste(j1.crop((0,0,x1,j0.height)),(0,0),j1.crop((0,0,x1,j0.height)))
        else: img=j1 if el.get('destacar') else j0
        colar(st,img,c,scale,alpha); return
    if t=='contador':
        k=smooth(max(0,tl-t0)/el.get('conta',1.3)) if not estatico else 1
        n=int(round(el['de']+(el['ate']-el['de'])*k)); txt=el['fmt'].format(n=f"{n:,}".replace(',','.'))
        img=build({'t':'bloco','txt':txt,'size':el.get('size',70),'maxw':800,'cor':el.get('cor','laranja'),'ang':el.get('ang',2)},(key,txt))
        colar(st,img,c,scale,alpha); return
    if t=='seta':
        d=ImageDraw.Draw(st); k=smooth(p) if not estatico else 1; (x0,y0),(x1,y1)=el['de'],el['ate']
        if k>0: seta_mao(d,(x0,y0),(x1,y1),k,TINTA if el.get('cor')!='laranja' else LAR,el.get('esp',10))
        return
    if t=='risco':
        d=ImageDraw.Draw(st); k=smooth((tl-t0)/0.35) if not estatico else 1; (x0,y0),(x1,y1)=el['de'],el['ate']
        if k>0: d.line([(x0,y0),(x0+(x1-x0)*k,y0+(y1-y0)*k)],fill=LAR,width=el.get('esp',12))
        return
    if t=='cal':
        im,cw=build(el,key); im=im.copy(); d=ImageDraw.Draw(im)
        for j,n in enumerate(el.get('riscar',[])):
            tj=cue(cid,el['riscar_em'])+j*0.12 if 'riscar_em' in el else -1
            if estatico or tj<0 or tl>=tj:
                p_=n-1+el.get('inicio',0); r,cc=divmod(p_,7); x=20+cc*cw; y=140+r*cw
                d.line([(x+8,y+8),(x+cw-8,y+cw-8)],fill=LAR,width=8); d.line([(x+cw-8,y+8),(x+8,y+cw-8)],fill=LAR,width=8)
        colar(st,S(R(im,el.get('ang',0)),off=(8,10),blur=10,alpha=80),c,scale,alpha); return
    img=build(el,key)
    if anim=='escrita' and not estatico:
        q=max(0,min(1,(tl-t0)/el.get('dur',1.0)))
        if q<=0: return
        w=int(img.width*q); im2=img.crop((0,0,w,img.height)); st.alpha_composite(im2,(int(c[0]-img.width/2),int(c[1]-img.height/2))); return
    colar(st,img,c,scale,alpha)
def cena(cid,tl,primeira=False):
    sp=SPEC[cid]; st=BG.copy(); dur=CEN[cid]['fim']-CEN[cid]['inicio']
    focus_k=0; els=sp.get('elementos',[])
    for i,el in enumerate(els):
        t0=cue(cid,el.get('e')); key=(cid,i)
        if el.get('foco'):
            if tl<t0: continue
            k=smooth((tl-t0)/0.4); focus_k=k
            st=st.filter(ImageFilter.GaussianBlur(10*k)); st.alpha_composite(Image.new('RGBA',(W,H),COR+(int(110*k),)))
        estat=primeira and el.get('e') is None
        desenha(st,el,key,tl,t0,cid,estatico=estat)
    cam=sp.get('camera',{}); push=cam.get('push',0.04)
    scale=1.0+push*smooth(tl/max(1,dur)); anchor=list(cam.get('ancora',[CX,800]))
    for z in cam.get('zooms',[]):   # zoom em torno do alvo (o alvo fica parado na tela)
        k=smooth((tl-cue(cid,z['e']))/z.get('dur',1.0))
        if k>0: scale=scale*(1-k)+min(1.18,z['escala'])*k; anchor=[anchor[0]*(1-k)+z['alvo'][0]*k,anchor[1]*(1-k)+z['alvo'][1]*k]
    fz=cam.get('congela')
    if fz:
        a=cue(cid,fz['de']); b=cue(cid,fz['ate'])
        if a<=tl<b: scale*=1.06
    out=camera(st,scale,anchor,anchor)
    if fz and cue(cid,fz['de'])<=tl<cue(cid,fz['ate']):
        g=out.convert('L').convert('RGBA'); out=Image.blend(out,g,0.85)
    return out
# ---------- UI
def marca_topo(img): C.marca_topo(img)
CHUNKS=[]
for c in tm['cenas']:
    for f in c['frases']:
        ws=f['leg'].split(); tot=len(f['leg']); cur=[]; grupos=[]
        for w_ in ws:
            if cur and len(' '.join(cur+[w_]))>24: grupos.append(cur); cur=[]
            cur.append(w_)
        if cur: grupos.append(cur)
        pos=0
        for g in grupos:
            wt=[]
            for w_ in g: wt.append(f['inicio']+f['dur']*pos/tot); pos+=len(w_)+1
            CHUNKS.append((wt[0],f['inicio']+f['dur']*min(1,pos/tot),g,wt))
FL=F('inter',800,54)
def legenda(img,t):
    ch=None
    for i,(a,b,g,wt) in enumerate(CHUNKS):
        nxt=CHUNKS[i+1][0] if i+1<len(CHUNKS) else b+0.6
        if a<=t<min(nxt,b+0.5): ch=(g,wt)
    if not ch: return
    g,wt=ch; d=ImageDraw.Draw(img); txt=' '.join(g); w=FL.getlength(txt); y=1240
    d.rectangle((CX-w/2-18,y-6,CX+w/2+18,y+66),fill=TINTA); x=CX-w/2
    for w_,a in zip(g,wt):
        d.text((x,y),w_,font=FL,fill=LAR if a<=t else (250,246,236)); x+=FL.getlength(w_+' ')
def ui(img,cid,t):
    marca_topo(img); C.chip_materia(img,rot['materia']); legenda(img,t)
    fo=SPEC[cid].get('fonte')
    if fo: C.fonte(img,fo)
    C.barra(img,min(1,t/DUR))
def quadro(t):
    ids=[c['id'] for c in tm['cenas']]; cid=ids[0]
    for c in tm['cenas'][1:]:
        if t>=c['inicio']-0.1: cid=c['id']
    c0=0.0 if cid==ids[0] else CEN[cid]['inicio']
    im=cena(cid,max(0,t-c0),primeira=(cid==ids[0]))
    for c in tm['cenas'][1:]:   # transição: folha de papel rasgada atravessa a tela
        b=c['inicio']-0.1
        if abs(t-b)<0.22:
            k=(t-(b-0.22))/0.44; y=H-(H+FOLHA.height)*k; im.alpha_composite(FOLHA,(-60,int(y)))
    ui(im,cid,t); return im
def eventos():
    e=[]
    for c in tm['cenas'][1:]: e.append({'t':c['inicio']-0.1,'tipo':'whoosh'})
    for c in rot['cenas']:
        cid=c['id']; base=CEN[cid]['inicio']
        for el in c.get('elementos',[]):
            if el.get('e') is None: continue
            t=base+cue(cid,el['e']); tp=el['t']
            if tp in ('tira','contador'): e.append({'t':t,'tipo':'tecla','n':4})
            elif tp in ('risco','seta'): e.append({'t':t,'tipo':'marca','d':0.35})
            elif el.get('anim')=='escrita': e.append({'t':t,'tipo':'marca','d':el.get('dur',1.0)})
            elif el.get('foco'): e.append({'t':t,'tipo':'whoosh'})
            else: e.append({'t':t,'tipo':'pop'})
            if tp=='jornal' and 'marca' in el: e.append({'t':base+cue(cid,el['marca']),'tipo':'marca','d':0.9})
            if tp=='cal' and 'riscar_em' in el:
                for j in range(len(el.get('riscar',[]))): e.append({'t':base+cue(cid,el['riscar_em'])+j*0.12,'tipo':'tecla','n':1})
        fz=c.get('camera',{}).get('congela')
        if fz: e.append({'t':base+cue(cid,fz['de']),'tipo':'tecla','n':1})
    return e
if MODO=='quadros':
    for t in [float(x) for x in sys.argv[3].split(',')]: quadro(t).convert('RGB').save(f'/tmp/q_{t:.2f}.png')
elif MODO=='prancha':
    ts=[]
    for c in tm['cenas']:
        for f in c['frases']: ts.append(min(DUR-0.1,f['inicio']+f['dur']*0.92))
    ts=[0.0]+ts; n=len(ts); cols=8; rows=(n+cols-1)//cols
    b=Image.new('RGB',(cols*270,rows*500),'white'); dd=ImageDraw.Draw(b)
    for i,t in enumerate(ts):
        im=quadro(t).convert('RGB').crop((0,180,1080,1440)).resize((270,315)); b.paste(im,((i%cols)*270,(i//cols)*500)); dd.text(((i%cols)*270+5,(i//cols)*500+320),f'{t:.1f}s',fill=(0,0,0))
    b.save(f'/tmp/prancha_{rot["id"]}.png'); print(f'/tmp/prancha_{rot["id"]}.png')
elif MODO=='capa':
    sp={'id':'capa','elementos':rot['capa']['elementos']}; SPEC['capa']=sp
    st=BG.copy()
    for i,el in enumerate(sp['elementos']):
        if el['t']=='bloco': el=dict(el,txt=el['txt'].upper(),size=int(el.get('size',64)*0.8),maxw=780)
        if el['t'] in ('tira','numero') and el['pos'][1]<500: el=dict(el,pos=[el['pos'][0],max(el['pos'][1],520)])
        desenha(st,el,('capa',i),0,0,'capa',estatico=True)
    if rot.get('chamada'):
        f=F('anton',400,64); t=rot['chamada']; w=f.getlength(t)
        ch=C.rasgado(int(w)+60,96,TINTA,seed=3,amp=5,fibra=False); ImageDraw.Draw(ch).text((30,6),t,font=f,fill=(250,247,240))
        ch=S(R(ch,-2),off=(6,8),blur=8,alpha=70); colar(st,ch,(CX,1335))
    marca_topo(st); C.chip_materia(st,rot['materia']); st.convert('RGB').save(f'{EP}/capa.png'); print('capa ok')
elif MODO=='eventos':
    json.dump(eventos(),open(f'{EP}/eventos.json','w')); print(round(DUR,2))
else:
    p=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
       '-c:v','libx264','-preset','veryfast','-crf','20','-pix_fmt','yuv420p',f'{EP}/video_mudo.mp4'],stdin=subprocess.PIPE)
    for i in range(NF):
        p.stdin.write(quadro(i/FPS).convert('RGB').tobytes())
        if i%300==0: print(i,NF,flush=True)
    p.stdin.close(); p.wait(); print('fim')
