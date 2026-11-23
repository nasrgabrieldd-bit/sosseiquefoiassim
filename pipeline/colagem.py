from base import *
# Opção 1 — COLAGEM (inspirada nas referências: fundo chapado, recorte P&B em retícula, blocos laranja, máquina de escrever, anotação à mão)
PAL=dict(fundo=(198,182,246),tinta=(20,18,22),destaque=(255,92,38),papel=(240,235,222),marca=(255,214,64),sec=(70,60,96))
CORES_MATERIA={'história':(198,182,246),'ciências':(170,226,204),'arte':(250,214,120),'filosofia':(232,232,226),'geografia':(160,206,240)}
def papel(w,h,seed=3,cor=None):
    cor=cor or PAL['fundo']; base=np.ones((h,w,3),np.float32)*np.array(cor,np.float32)
    n=noise(w,h,0.6,1,seed)*16+noise(w,h,30,8,seed+1)*18
    return Image.fromarray((base+n[...,None]).clip(0,255).astype(np.uint8)).convert('RGBA')
def jornal(w,h,destacar=0.0,seed=5,titulo='LA PRESSE',data='PARIS  ·  1836',rodape='FEUILLETON DE LA PRESSE'):
    rng=random.Random(seed)
    im=Image.new('RGBA',(w,h),(236,229,211,255))
    a=np.asarray(im).astype(np.float32); a[...,:3]+=noise(w,h,0.8,1,seed)[...,None]*30+noise(w,h,25,6,seed+2)[...,None]*25
    im=Image.fromarray(a.clip(0,255).astype(np.uint8)); d=ImageDraw.Draw(im)
    m=int(w*0.06); ink=(30,28,26)
    t=titulo; sz=int(w*0.13)
    while F('playfair-display',900,sz).getlength(t)>w-2*m: sz-=2
    f=F('playfair-display',900,sz); d.text(((w-f.getlength(t))/2,m+(int(w*0.13)-sz)*0.6),t,font=f,fill=ink)
    y=m+int(w*0.17); d.line([(m,y),(w-m,y)],fill=ink,width=max(2,w//300))
    fs=F('special-elite',400,int(w*0.032)); s=data; d.text(((w-fs.getlength(s))/2,y+8),s,font=fs,fill=ink); y+=int(w*0.06)
    d.line([(m,y),(w-m,y)],fill=ink,width=2)
    cols=4; cw=(w-2*m-(cols-1)*14)/cols; foot=int(h*0.70); lh=max(8,w//130)
    for c in range(cols):
        x=m+c*(cw+14); yy=y+16
        while yy<foot-14:
            if rng.random()<0.07: yy+=lh; d.rectangle((x,yy,x+cw*0.7,yy+lh),fill=ink); yy+=lh*2; continue
            d.rectangle((x,yy,x+cw*rng.uniform(0.75,1),yy+lh*0.45),fill=(90,86,80)); yy+=lh
    d.line([(m,foot),(w-m,foot)],fill=ink,width=max(3,w//250))
    ff=F('special-elite',400,int(w*0.038)); t=rodape; d.text(((w-ff.getlength(t))/2,foot+12),t,font=ff,fill=ink)
    yy=foot+int(w*0.075); cw=(w-2*m-28)/3
    for c in range(3):
        x=m+c*(cw+14); y2=yy
        while y2<h-m: d.rectangle((x,y2,x+cw*rng.uniform(0.8,1),y2+lh*0.45),fill=(70,66,60)); y2+=lh
    if destacar>0:
        hl=Image.new('RGBA',(w,h),(0,0,0,0)); x1=m-10+(w-2*m+20)*destacar
        ImageDraw.Draw(hl).rectangle((m-10,foot-8,x1,h-m+10),fill=PAL['marca']+(140,))
        im=Image.fromarray(np.minimum(np.asarray(im),np.asarray(Image.alpha_composite(im,hl))).astype(np.uint8))
    return im
def tv_cinza(w,h):
    """TV antiga desenhada em tons de cinza (vira retícula)."""
    im=Image.new('L',(w,h),255); d=ImageDraw.Draw(im)
    bx0,by0,bx1,by1=w*0.06,h*0.22,w*0.94,h*0.86
    for k in range(60):  # corpo com gradiente
        t=k/59; c=int(205-95*t); d.rounded_rectangle((bx0,by0+(by1-by0)*t*0.98,bx1,by1),radius=int(w*0.06),fill=c)
    d.rounded_rectangle((bx0,by0,bx1,by1),radius=int(w*0.06),outline=30,width=int(w*0.012))
    sx0,sy0,sx1,sy1=w*0.13,h*0.29,w*0.70,h*0.78
    for k in range(40):
        t=k/39; c=int(70+140*(1-abs(t-0.35)*1.6)); c=max(30,min(230,c))
        d.rounded_rectangle((sx0+t*30,sy0+t*20,sx1-t*30,sy1-t*20),radius=int(w*0.08),fill=c)
    d.rounded_rectangle((sx0,sy0,sx1,sy1),radius=int(w*0.08),outline=20,width=int(w*0.015))
    d.ellipse((sx0+w*0.08,sy0+h*0.06,sx0+w*0.22,sy0+h*0.14),fill=245)
    for j in range(2):
        cy=h*(0.40+j*0.18); cx=w*0.82; r=w*0.055
        d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=60); d.ellipse((cx-r*0.5,cy-r*0.8,cx+r*0.3,cy-r*0.1),fill=200)
    for k in range(6): d.line([(w*0.76,h*(0.68+k*0.025)),(w*0.88,h*(0.68+k*0.025))],fill=40,width=3)
    d.line([(w*0.5,h*0.22),(w*0.28,h*0.02)],fill=25,width=int(w*0.014)); d.line([(w*0.5,h*0.22),(w*0.70,h*0.0)],fill=25,width=int(w*0.014))
    d.ellipse((w*0.44,h*0.17,w*0.56,h*0.25),fill=40)
    d.polygon([(w*0.18,h*0.86),(w*0.24,h*0.86),(w*0.16,h*0.99),(w*0.12,h*0.99)],fill=40)
    d.polygon([(w*0.76,h*0.86),(w*0.82,h*0.86),(w*0.88,h*0.99),(w*0.84,h*0.99)],fill=40)
    return im
def halftone_cor(img,cell=8):
    """retícula colorida: mesmo grid clássico do halftone() em P&B (tamanho do ponto pela
    luminância local, linhas alternadas), mas cada ponto é pintado com a cor local da
    ilustração — dá o efeito 'foto a cores' tipo impressão antiga, preservando as cores
    (azul do oceano, verde dos continentes etc.) em vez de misturar tinta por canal CMYK
    (que em grade única sem ângulos de tela só produz ruído). Sempre a partir de uma
    ilustração desenhada por código, nunca de uma foto real."""
    w,h=img.size
    lum=np.asarray(img.convert('L')).astype(np.float32)/255
    cor=np.asarray(img.convert('RGB'))
    small_l=Image.fromarray((lum*255).astype(np.uint8)).resize((w//cell+2,h//cell+2),Image.BILINEAR)
    small_c=Image.fromarray(cor).resize((w//cell+2,h//cell+2),Image.BILINEAR)
    al=np.asarray(small_l); ac=np.asarray(small_c)
    out=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(out)
    for j in range(al.shape[0]):
        for i in range(al.shape[1]):
            v=al[j,i]/255; r=(1-v)**0.8*cell*0.8
            if r>0.55:
                x=i*cell+(cell/2 if j%2 else 0); y=j*cell
                col=tuple(int(c) for c in ac[j,i])
                d.ellipse((x-r,y-r,x+r,y+r),fill=col+(255,))
    return out
def recorte_retícula_cor(img_rgba,cell=8,borda=14):
    """variante colorida do recorte_retícula: retícula colorida + borda branca de adesivo.
    É o 'recorte de foto colorida' da colagem."""
    w,h=img_rgba.size
    mask=img_rgba.split()[3].point(lambda v:255 if v>10 else 0).filter(ImageFilter.MaxFilter(5))
    dots=halftone_cor(img_rgba,cell)
    base=Image.new('RGBA',(w,h),(238,236,230,255)); base.putalpha(mask); base.alpha_composite(dots)
    a=base.split()[3]; a=ImageChops.multiply(a,mask); base.putalpha(a)
    pad=borda*2; out=Image.new('RGBA',(w+pad*2,h+pad*2),(0,0,0,0))
    big=Image.new('L',out.size,0); big.paste(mask,(pad,pad)); white=big.filter(ImageFilter.MaxFilter(borda*2+1))
    wl=Image.new('RGBA',out.size,(252,250,246,255)); wl.putalpha(white); out.alpha_composite(wl); out.alpha_composite(base,(pad,pad))
    return out
def phong_esfera(ts,luz=(-0.5,-0.55,0.65),ambient=0.3,difusa=0.85,especular=0.55,brilho=26):
    """Sombreamento 3D (Lambert + especular Blinn-Phong) de uma esfera inscrita num quadrado ts×ts,
    calculado por pixel com numpy — dá volume e brilho de verdade, bem mais 'redondo' que um
    degradê de elipses. Retorna (sombra 0-1 float, brilho especular 0-1 float, dentro bool) todos
    arrays (ts,ts). 100% matemática/código, sem IA e sem foto."""
    yy,xx=np.mgrid[0:ts,0:ts].astype(np.float64)
    cx=cy=ts/2; r=ts/2
    dx=(xx-cx)/r; dy=(yy-cy)/r
    dist2=dx*dx+dy*dy; dentro=dist2<=1.0
    dz=np.sqrt(np.clip(1-dist2,0,1))
    L=np.array(luz,dtype=np.float64); L=L/np.linalg.norm(L)
    difus=np.clip(dx*L[0]+dy*L[1]+dz*L[2],0,1)
    Hx,Hy,Hz=L[0],L[1],L[2]+1.0; hl=math.sqrt(Hx*Hx+Hy*Hy+Hz*Hz); Hx,Hy,Hz=Hx/hl,Hy/hl,Hz/hl
    ndoth=np.clip(dx*Hx+dy*Hy+dz*Hz,0,1)
    spec=np.where(dentro,ndoth**brilho*especular,0.0)
    sombra=np.clip(ambient+difusa*difus,0,1)
    return sombra,spec,dentro
def aplica_phong(base_rgba,**kw):
    """Aplica phong_esfera() sobre uma textura RGBA já pintada (plana) do tamanho do quadrado que a
    contém — multiplica a cor pela sombra e soma um brilho branco especular, recorta no círculo."""
    ts=base_rgba.width; sombra,spec,dentro=phong_esfera(ts,**kw)
    a=np.asarray(base_rgba).astype(np.float64)
    rgb=a[...,:3]*sombra[...,None]+255.0*spec[...,None]
    alpha=a[...,3]*dentro
    out=np.dstack([rgb.clip(0,255),alpha.clip(0,255)]).astype(np.uint8)
    return Image.fromarray(out,'RGBA')
def bola_natal(w,h,seed=0,cor=(196,30,40)):
    """bola de Natal (enfeite de árvore) com sombreamento 3D de verdade (phong_esfera) — vidro
    brilhante, capinho dourado e gancho — 100% desenhado, sem foto nem IA."""
    ts=int(min(w,h*0.92)); im=Image.new('RGBA',(w,h),(0,0,0,0))
    base=Image.new('RGBA',(ts,ts),cor+(255,))
    esfera=aplica_phong(base,luz=(-0.5,-0.6,0.62),ambient=0.22,difusa=0.95,especular=0.85,brilho=38)
    im.alpha_composite(esfera,(int((w-ts)/2),int(h-ts)))
    cx=w/2; topo=h-ts
    cw,ch=ts*0.22,ts*0.14
    d=ImageDraw.Draw(im)
    d.rectangle((cx-cw/2,topo-ch*0.4,cx+cw/2,topo+ch*0.6),fill=(214,178,70,255),outline=(120,90,30,255))
    d.ellipse((cx-cw*0.45,topo-ch*0.75,cx+cw*0.45,topo-ch*0.05),fill=(230,196,96,255),outline=(120,90,30,255))
    d.arc((cx-cw*0.3,topo-ch*2.1,cx+cw*0.3,topo-ch*0.6),30,150,fill=(120,90,30,255),width=4)
    return im
def papai_noel(w,h,seed=0):
    """Papai Noel — personagem genérico do folclore de Natal (barba branca, casaco vermelho,
    gorro, bota preta), sem referência a qualquer marca, ator ou obra protegida. Barriga com
    sombreamento 3D de verdade (aplica_phong, igual à bola_natal) — 100% desenhado, sem foto/IA."""
    im=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(im); cx=w*0.5
    for s in (-1,1):
        x0=cx+s*w*0.13
        d.rounded_rectangle((x0-w*0.1,h*0.86,x0+w*0.12,h*0.99),radius=int(w*0.05),fill=(28,22,20,255))
        d.rounded_rectangle((x0-w*0.11,h*0.64,x0+w*0.11,h*0.9),radius=int(w*0.07),fill=(176,26,30,255))
    ts=int(w*0.64)
    base=Image.new('RGBA',(ts,ts),(190,28,32,255))
    belly=aplica_phong(base,luz=(-0.5,-0.6,0.6),ambient=0.42,difusa=0.72,especular=0.16,brilho=9)
    topo=h*0.3; im.alpha_composite(belly,(int(cx-ts/2),int(topo)))
    beltY=topo+ts*0.62
    d.rectangle((cx-ts*0.5,beltY,cx+ts*0.5,beltY+h*0.065),fill=(24,20,18,255))
    bw=h*0.09
    d.rectangle((cx-bw/2,beltY-h*0.008,cx+bw/2,beltY+h*0.073),fill=(214,178,70,255),outline=(120,90,30,255))
    for s in (-1,1):
        x0=cx+s*ts*0.44
        d.rounded_rectangle((x0-w*0.08,h*0.4,x0+w*0.08,h*0.66),radius=int(w*0.06),fill=(176,26,30,255))
        d.ellipse((x0-w*0.09,h*0.58,x0+w*0.09,h*0.7),fill=(248,248,248,255))
        d.ellipse((x0-w*0.08,h*0.66,x0+w*0.08,h*0.78),fill=(250,230,214,255))
    fcy=h*0.3
    d.ellipse((cx-w*0.22,fcy-w*0.14,cx+w*0.22,fcy+w*0.24),fill=(252,250,248,255))
    d.ellipse((cx-w*0.12,fcy-w*0.1,cx+w*0.12,fcy+w*0.08),fill=(240,192,160,255))
    for s in (-1,1):
        d.ellipse((cx+s*w*0.1-10,fcy+6,cx+s*w*0.1+14,fcy+26),fill=(236,140,130,180))
    for s in (-1,1):
        d.ellipse((cx+s*w*0.05-5,fcy-10,cx+s*w*0.05+5,fcy),fill=(30,26,24,255))
    d.ellipse((cx-7,fcy+2,cx+7,fcy+16),fill=(224,150,120,255))
    d.polygon([(cx-w*0.2,fcy-w*0.12),(cx+w*0.14,fcy-w*0.12),(cx+w*0.28,fcy-w*0.52)],fill=(190,28,32,255))
    d.ellipse((cx+w*0.22,fcy-w*0.6,cx+w*0.34,fcy-w*0.48),fill=(250,250,250,255))
    d.rectangle((cx-w*0.22,fcy-w*0.16,cx+w*0.16,fcy-w*0.08),fill=(250,250,250,255))
    return im
def earthrise(w,h,seed=4):
    """ilustração 100% desenhada (inventada, não é a foto real da Apollo 8): Terra colorida vista
    do espaço sobre o horizonte lunar — céu estrelado, oceano com gradiente, continentes, nuvens,
    sombra/terminador e crateras na base. Serve de 'foto' central colorida da colagem."""
    rng=random.Random(seed)
    im=Image.new('RGBA',(w,h),(8,8,18,255)); d=ImageDraw.Draw(im)
    for _ in range(150):
        x,y=rng.uniform(0,w),rng.uniform(0,h*0.62); r=rng.uniform(0.6,1.8)
        d.ellipse((x-r,y-r,x+r,y+r),fill=(230,230,240,rng.randint(120,255)))
    cx,cy,r=w*0.6,h*0.34,w*0.3
    rr=r*1.05; ts=int(rr*2.3)
    terra=Image.new('RGBA',(ts,ts),(24,92,150,255)); dt=ImageDraw.Draw(terra)
    for cxr,cyr,s,col in [(0.35,0.42,0.42,(74,124,62)),(0.62,0.3,0.3,(96,140,70)),
                          (0.5,0.68,0.33,(120,150,80)),(0.78,0.6,0.22,(90,130,66))]:
        pts=[]
        for i in range(10):
            a=i/10*2*math.pi; rad=s*rr*(0.6+0.4*rng.random())
            pts.append((rr+cxr*rr*0.9+rad*math.cos(a)-rr*0.45, rr+cyr*rr*0.9+rad*math.sin(a)-rr*0.45))
        dt.polygon(pts,fill=col+(255,))
    for _ in range(16):
        x,y=rng.uniform(rr*0.3,rr*1.7),rng.uniform(rr*0.3,rr*1.7); s=rng.uniform(rr*0.12,rr*0.3)
        dt.ellipse((x-s,y-s*0.5,x+s,y+s*0.5),fill=(246,248,250,255))
    # sombreamento 3D de verdade (Lambert + especular), luz vindo de cima-esquerda,
    # fazendo as vezes do terminador dia/noite sem precisar de elipse de sombra "falsa"
    terra=aplica_phong(terra,luz=(-0.55,-0.62,0.56),ambient=0.16,difusa=0.95,especular=0.3,brilho=18)
    im.alpha_composite(terra,(int(cx-terra.width/2),int(cy-terra.height/2)))
    luay=h*0.74
    d.polygon([(0,luay),(w,luay-h*0.02),(w,h),(0,h)],fill=(74,70,64,255))
    for _ in range(11):
        x=rng.uniform(0,w); y=luay+rng.uniform(10,h*0.2); rc=rng.uniform(14,40)
        d.ellipse((x-rc,y-rc*0.4,x+rc,y+rc*0.4),fill=(54,50,48,255))
    return im
def recorte_retícula(gray,cell=7,borda=14):
    """retícula P&B + borda branca de adesivo (o 'recorte' da colagem)."""
    w,h=gray.size; mask=gray.point(lambda v:255 if v<250 else 0).filter(ImageFilter.MaxFilter(5))
    dots=halftone(gray,cell,(18,16,20,255))
    base=Image.new('RGBA',(w,h),(238,236,230,255)); base.putalpha(mask); base.alpha_composite(dots)
    a=base.split()[3]; a=ImageChops.multiply(a,mask); base.putalpha(a)
    pad=borda*2; out=Image.new('RGBA',(w+pad*2,h+pad*2),(0,0,0,0))
    big=Image.new('L',out.size,0); big.paste(mask,(pad,pad)); white=big.filter(ImageFilter.MaxFilter(borda*2+1))
    wl=Image.new('RGBA',out.size,(252,250,246,255)); wl.putalpha(white); out.alpha_composite(wl); out.alpha_composite(base,(pad,pad))
    return out
def tira(txt,size=34,cor=None,fg=None,font=('special-elite',400)):
    f=F(font[0],font[1],size); w=int(f.getlength(txt))+size; h=int(size*1.6)
    im=Image.new('RGBA',(w,h),(cor or PAL['papel'])+(255,)); ImageDraw.Draw(im).text((size//2,int(size*0.25)),txt,font=f,fill=fg or PAL['tinta'])
    return torn(im,3,seed=len(txt))
def bloco(txt,size,maxw,cor=None,fg=None):
    f=F('inter',900,size); lines=wrap(txt,f,maxw); lh=int(size*1.02)
    w=int(max(f.getlength(l) for l in lines))+int(size*0.9); h=lh*len(lines)+int(size*0.55)
    im=Image.new('RGBA',(w,h),(cor or PAL['destaque'])+(255,)); d=ImageDraw.Draw(im)
    for i,l in enumerate(lines): d.text((int(size*0.45),int(size*0.12)+i*lh),l,font=f,fill=fg or PAL['tinta'])
    return im
def nota(img,xy,txt,size=54,cor=None,ang=0):
    f=F('caveat',700,size); lines=txt.split('\n'); w=int(max(f.getlength(l) for l in lines))+20; h=int(size*1.15*len(lines))+20
    t=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(t)
    for i,l in enumerate(lines): d.text((10,10+i*size*1.15),l,font=f,fill=cor or PAL['tinta'])
    if ang: t=t.rotate(ang,expand=True,resample=Image.BICUBIC)
    img.alpha_composite(t,(int(xy[0]),int(xy[1])))
import json as _j
_MARCA=_j.load(open(ROOT+'/marca/marca.json'))
def marca_topo(img):
    d=ImageDraw.Draw(img); f=F('inter',900,40); t=_MARCA['nome_topo']; w=f.getlength(t)
    d.rounded_rectangle((CX-w/2-16,256,CX+w/2+30,312),radius=10,fill=PAL['fundo'])
    d.text((CX-w/2,262),t,font=f,fill=PAL['tinta']); d.rectangle((CX+w/2+8,292,CX+w/2+20,304),fill=PAL['destaque'])
def legenda(img,txt):
    d=ImageDraw.Draw(img); f=F('inter',800,50); y=1236
    for l in wrap(txt,f,770):
        w=f.getlength(l); d.rectangle((CX-w/2-16,y-4,CX+w/2+16,y+62),fill=PAL['tinta']); d.text((CX-w/2,y),l,font=f,fill=(250,246,236)); y+=70
def fonte(img,txt):
    d=ImageDraw.Draw(img); f=F('special-elite',400,26); w=f.getlength(txt); d.text((CX-w/2,1372),txt,font=f,fill=PAL['sec'])
def barra(img,p):
    d=ImageDraw.Draw(img); d.rectangle((0,1904,int(W*p),1920),fill=PAL['destaque'])
_tv=None
def tv(w=430):
    global _tv
    if _tv is None or _tv.width!=w+56: _tv=recorte_retícula(tv_cinza(w,int(w*0.9)),cell=7)
    return _tv
def capa():
    im=papel(W,H)
    j=torn(jornal(560,720,destacar=1.0),8).rotate(6,expand=True,resample=Image.BICUBIC); paste_sh(im,j,(100,430),off=(8,10),blur=12,alpha=80)
    t=tv(430).rotate(-7,expand=True,resample=Image.BICUBIC); paste_sh(im,t,(500,620),off=(8,12),blur=12,alpha=90)
    paste_sh(im,tira('1836',46).rotate(-4,expand=True,resample=Image.BICUBIC),(120,360),off=(4,6),blur=6,alpha=70)
    nota(im,(530,318),'continua no\npróximo capítulo...',56,ang=-6)
    b=bloco('a novela nasceu no rodapé do jornal',84,700); paste_sh(im,b,(CX-b.width//2+20,1100),off=(6,8),blur=8,alpha=60)
    marca_topo(im); return im
def cena():
    im=papel(W,H,7)
    j=torn(jornal(560,720,destacar=1.0),8).rotate(-3,expand=True,resample=Image.BICUBIC); paste_sh(im,j,(CX-310,385),off=(8,10),blur=12,alpha=80)
    tg=bloco('RODAPÉ',52,600).rotate(-8,expand=True,resample=Image.BICUBIC); paste_sh(im,tg,(640,840),off=(5,7),blur=6,alpha=70)
    nota(im,(120,1138),'"rés-do-chão": o térreo da página',50,cor=PAL['sec'])
    marca_topo(im); legenda(im,'O romance foi morar no rodapé do jornal'); fonte(im,'Fonte: MEYER, M. Folhetim: uma história (Cia. das Letras, 1996)'); barra(im,0.35)
    return im
def thumb():
    w,h=1280,720; im=papel(w,h,9)
    j=torn(jornal(400,520,destacar=1.0),6).rotate(5,expand=True,resample=Image.BICUBIC); paste_sh(im,j,(680,60),alpha=80)
    t=recorte_retícula(tv_cinza(360,324),cell=6).rotate(-6,expand=True,resample=Image.BICUBIC); paste_sh(im,t,(870,300),alpha=90)
    b=bloco('a novela nasceu no rodapé',92,560); paste_sh(im,b,(60,170),alpha=60)
    paste_sh(im,tira('PARIS, 1836',40).rotate(-3,expand=True),(80,90),alpha=60)
    nota(im,(80,560),'continua amanhã...',64)
    return im

MATERIAS={'HISTÓRIA':(198,182,246),'LITERATURA':(178,226,198),'LÍNGUA PORTUGUESA':(248,224,140),'GEOGRAFIA':(166,208,240),
 'MATEMÁTICA':(214,236,150),'FÍSICA':(186,204,232),'QUÍMICA':(246,186,214),'BIOLOGIA':(200,220,166),'FILOSOFIA':(228,226,218),
 'ARTE':(252,198,182),'EDUCAÇÃO FÍSICA':(150,222,212),'SOCIOLOGIA':(234,214,178)}
def chip_materia(img,materia):
    f=F('special-elite',400,30); t=materia; w=f.getlength(t)
    im=Image.new('RGBA',(int(w)+44,52),PAL['tinta']+(255,)); ImageDraw.Draw(im).text((22,9),t,font=f,fill=(250,246,236))
    im=im.rotate(-2,expand=True,resample=Image.BICUBIC); img.alpha_composite(im,(int(CX-im.width/2),318))
def radio_cinza(w,h):
    im=Image.new('L',(w,h),255); d=ImageDraw.Draw(im)
    d.arc((w*0.25,h*0.0,w*0.75,h*0.35),180,360,fill=30,width=int(w*0.03))
    bx0,by0,bx1,by1=w*0.04,h*0.16,w*0.96,h*0.96
    for k in range(50):
        t=k/49; c=int(200-100*t); d.rounded_rectangle((bx0,by0+(by1-by0)*t*0.97,bx1,by1),radius=int(w*0.08),fill=c)
    d.rounded_rectangle((bx0,by0,bx1,by1),radius=int(w*0.08),outline=25,width=int(w*0.012))
    cx,cy,r=w*0.34,h*0.58,w*0.22
    d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=70)
    for y in range(int(cy-r+8),int(cy+r),10):
        dx=(r*r-(y-cy)**2)**0.5*0.9; d.line([(cx-dx,y),(cx+dx,y)],fill=150,width=3)
    d.rounded_rectangle((w*0.62,h*0.32,w*0.9,h*0.5),radius=8,fill=220,outline=40,width=3)
    for i in range(7): x=w*0.64+i*w*0.035; d.line([(x,h*0.36),(x,h*0.46)],fill=60,width=2)
    for j in range(2):
        kx=w*(0.68+j*0.15); ky=h*0.72; kr=w*0.055; d.ellipse((kx-kr,ky-kr,kx+kr,ky+kr),fill=50); d.ellipse((kx-kr*0.4,ky-kr*0.8,kx+kr*0.2,ky-kr*0.2),fill=190)
    return im

# =====================================================================
# IDENTIDADE "SÓ SEI QUE FOI ASSIM" (manual de marca, 12/11/2026)
# Paleta oficial: laranja #F15A24, grafite #242424, papel #F3EFE7, lilás #BBA4E8, branco.
# A cor da matéria aparece só como pedaço de papel rasgado/fita (o fundo é sempre papel).
# =====================================================================
LARANJA=(241,90,36); GRAFITE=(36,36,36); PAPEL_M=(243,239,231); LILAS=(187,164,232); BRANCO=(255,255,255)
PAL.update(destaque=LARANJA,tinta=GRAFITE,papel=PAPEL_M,sec=(95,88,80))
MATERIA_ATUAL={'nome':'HISTÓRIA'}
def rasgado(w,h,cor,seed=0,amp=None,fibra=True):
    """pedaço de papel rasgado: borda irregular + fibra clara na borda"""
    rng=random.Random(seed); amp=amp or max(6,min(w,h)*0.04)
    def borda(n,f): return [f(i/n,rng.uniform(-amp,amp)) for i in range(n+1)]
    pts=borda(18,lambda t,j:(t*w,amp+j))+borda(18,lambda t,j:(w-amp+j,t*h))+borda(18,lambda t,j:((1-t)*w,h-amp+j))+borda(18,lambda t,j:(amp+j,(1-t)*h))
    m=Image.new('L',(w,h),0); ImageDraw.Draw(m).polygon(pts,fill=255)
    out=Image.new('RGBA',(w,h),(0,0,0,0))
    if fibra:
        fb=Image.new('RGBA',(w,h),(250,247,240,255)); fb.putalpha(m); out.alpha_composite(fb)
        m2=m.filter(ImageFilter.MinFilter(int(max(3,amp*0.5))//2*2+1))
    else: m2=m
    a=np.asarray(Image.new('RGB',(w,h),cor)).astype(np.float32)+noise(w,h,0.8,1,seed)[...,None]*18
    body=Image.fromarray(a.clip(0,255).astype(np.uint8)).convert('RGBA'); body.putalpha(m2); out.alpha_composite(body)
    return out
def _rabiscos(d,w,h,rng,x0,y0,x1,y1,alpha=26):
    y=y0
    while y<y1:
        x=x0+rng.uniform(0,40); 
        while x<x1-40:
            L=rng.uniform(30,110); pts=[]
            for k in range(14):
                t=k/13; pts.append((x+L*t,y+math.sin(t*rng.uniform(8,14))*rng.uniform(3,7)))
            d.line(pts,fill=(40,34,28,alpha),width=2); x+=L+rng.uniform(10,26)
        y+=rng.uniform(34,46)
def papel(w,h,seed=3,cor=None):
    """fundo oficial: papel envelhecido + manuscrito apagado + rasgados lilás/laranja/matéria nas bordas"""
    rng=random.Random(seed); base=np.ones((h,w,3),np.float32)*np.array(PAPEL_M,np.float32)
    n=noise(w,h,0.7,1,seed)*14+noise(w,h,40,10,seed+1)*22
    yy,xx=np.mgrid[0:h,0:w]; vg=((xx/w-0.5)**2+(yy/h-0.5)**2)**0.5
    warm=np.stack([vg*30,vg*40,vg*60],-1)
    im=Image.fromarray((base+n[...,None]-warm).clip(0,255).astype(np.uint8)).convert('RGBA')
    lay=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(lay)
    _rabiscos(d,w,h,rng,int(w*0.04),int(h*0.04),int(w*0.55),int(h*0.16),alpha=40)
    _rabiscos(d,w,h,rng,int(w*0.45),int(h*0.8),int(w*0.96),int(h*0.95),alpha=40)
    im.alpha_composite(lay.filter(ImageFilter.GaussianBlur(0.6)))
    st_=Image.new('RGBA',(w,h),(0,0,0,0)); d2=ImageDraw.Draw(st_)
    for _ in range(4):  # manchas de papel velho
        x,y,r=rng.uniform(0,w),rng.uniform(0,h),rng.uniform(60,180); d2.ellipse((x-r,y-r,x+r,y+r),fill=(150,120,80,14))
    im.alpha_composite(st_.filter(ImageFilter.GaussianBlur(40)))
    cm=MATERIAS.get(MATERIA_ATUAL['nome'],LILAS)
    def cola(img,x,y,ang): im.alpha_composite(img.rotate(ang,expand=True,resample=Image.BICUBIC),(int(x),int(y)))
    s=min(w,h)
    if h>=w:  # vertical
        cola(rasgado(int(s*0.62),int(s*0.42),LILAS,seed+11),w-int(s*0.42),-int(s*0.12),-14)
        cola(rasgado(int(s*0.5),int(s*0.34),LARANJA,seed+12),-int(s*0.22),h-int(s*0.5),10)
        cola(rasgado(int(s*0.7),int(s*0.12),cm,seed+13,amp=8),-int(s*0.15),int(h*0.71),-8)
        cola(rasgado(int(s*0.36),int(s*0.3),LILAS,seed+14),w-int(s*0.24),h-int(s*0.62),18)
    else:
        cola(rasgado(int(s*0.6),int(s*0.4),LILAS,seed+11),w-int(s*0.45),-int(s*0.15),-10)
        cola(rasgado(int(s*0.5),int(s*0.35),LARANJA,seed+12),-int(s*0.2),h-int(s*0.3),8)
        cola(rasgado(int(s*0.8),int(s*0.12),cm,seed+13,amp=8),int(w*0.55),h-int(s*0.16),-4)
    return im
def bloco(txt,size,maxw,cor=None,fg=None):
    f=F('archivo-black',400,size); lines=wrap(txt,f,maxw); lh=int(size*1.22)
    w=int(max(f.getlength(l) for l in lines))+int(size*1.0); h=lh*len(lines)+int(size*0.6)
    im=rasgado(w,h,cor or LARANJA,seed=len(txt)+size,amp=max(5,size*0.08)); d=ImageDraw.Draw(im)
    for i,l in enumerate(lines): d.text((int(size*0.5),int(size*0.22)+i*lh),l,font=f,fill=fg or GRAFITE)
    return im
def tira(txt,size=34,cor=None,fg=None,font=('special-elite',400)):
    f=F(font[0],font[1],size); w=int(f.getlength(txt))+size+10; h=int(size*1.7)
    im=rasgado(w,h,cor or (252,250,245),seed=len(txt),amp=4); ImageDraw.Draw(im).text((size//2+5,int(size*0.3)),txt,font=f,fill=fg or GRAFITE)
    return im
def marca_topo(img):
    """assinatura no topo: SÓ SEI QUE FOI ASSIM (Anton) num rasgado de papel, 'ASSIM' sublinhado em laranja"""
    f=F('anton',400,44); t1='SÓ SEI QUE FOI '; t2='ASSIM'; w1=f.getlength(t1); w2=f.getlength(t2); W_=int(w1+w2)+44
    strip=rasgado(W_,64,(252,250,245),seed=5,amp=4); d=ImageDraw.Draw(strip)
    d.text((22,2),t1,font=f,fill=GRAFITE); d.text((22+w1,2),t2,font=f,fill=GRAFITE)
    d.line([(22+w1,56),(22+w1+w2*0.5,53),(22+w1+w2,55)],fill=LARANJA,width=5)
    strip=strip.rotate(-1.5,expand=True,resample=Image.BICUBIC); img.alpha_composite(strip,(int(CX-strip.width/2),252))
def chip_materia(img,materia):
    f=F('special-elite',400,28); t=materia; w=f.getlength(t)
    cm=MATERIAS.get(materia,LILAS)
    im=rasgado(int(w)+78,50,GRAFITE,seed=9,amp=3,fibra=False); d=ImageDraw.Draw(im)
    d.rectangle((16,15,36,35),fill=cm); d.text((48,9),t,font=f,fill=(250,247,240))
    im=im.rotate(1.5,expand=True,resample=Image.BICUBIC); img.alpha_composite(im,(int(CX-im.width/2),326))
def legenda(img,txt):
    d=ImageDraw.Draw(img); f=F('inter',800,50); y=1236
    for l in wrap(txt,f,770):
        w=f.getlength(l); d.rectangle((CX-w/2-16,y-4,CX+w/2+16,y+62),fill=GRAFITE); d.text((CX-w/2,y),l,font=f,fill=(250,246,236)); y+=70
def barra(img,p):
    d=ImageDraw.Draw(img); d.rectangle((0,1904,int(W*p),1920),fill=LARANJA)
def fita(w=260,h=62,cor=None,seed=0):
    """fita adesiva semitransparente colando um recorte: pontas em corte diagonal irregular,
    friso de brilho e sombra de dobra ao centro (efeito 'colagem' das referências)."""
    cor=cor or (247,222,138)
    rng=random.Random(seed or int(w*7+h))
    j=lambda: rng.uniform(-5,5)
    pts=[(6+j(),0),(w-6+j(),0),(w+j(),h*0.32+j()),(w-6+j(),h),(6+j(),h),(j(),h*0.68+j())]
    m=Image.new('L',(w,h),0); ImageDraw.Draw(m).polygon(pts,fill=255)
    a=np.asarray(Image.new('RGB',(w,h),cor)).astype(np.float32)+noise(w,h,0.6,1,seed or 1)[...,None]*12
    body=Image.fromarray(a.clip(0,255).astype(np.uint8)).convert('RGBA')
    al=Image.new('L',(w,h),222); body.putalpha(ImageChops.multiply(al,m))
    d=ImageDraw.Draw(body)
    d.line([(8,h*0.3),(w-8,h*0.3)],fill=(255,255,255,80),width=2)
    d.line([(8,h*0.72),(w-8,h*0.72)],fill=(0,0,0,26),width=2)
    return body
def carimbo(texto='',data='',r=92,cor=None,seed=0,ang=None):
    """carimbo de borracha desgastado: anel duplo + texto + data, tinta avermelhada/desbotada."""
    cor=cor or (196,40,34)
    rng=random.Random(seed or len(texto)+len(data)+1)
    d2=int(r*2+20)
    im=Image.new('RGBA',(d2,d2),(0,0,0,0)); d=ImageDraw.Draw(im)
    cx=cy=d2/2
    d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=cor+(255,),width=7)
    d.ellipse((cx-r+16,cy-r+16,cx+r-16,cy+r-16),outline=cor+(255,),width=4)
    f1=F('special-elite',400,max(14,int(r*0.3))); f2=F('special-elite',400,max(18,int(r*0.5)))
    if texto:
        t=texto.upper(); w=f1.getlength(t); d.text((cx-w/2,cy-r*0.54),t,font=f1,fill=cor+(255,))
    if data:
        w=f2.getlength(data); d.text((cx-w/2,cy-r*0.1),data,font=f2,fill=cor+(255,))
    n=noise(d2,d2,1.2,2,seed or 3)+0.5; n=np.clip(n,0,1)
    wear=Image.fromarray((n*255).astype(np.uint8))
    a=im.split()[3]; a=ImageChops.multiply(a,wear.point(lambda v:150+int(v*0.4)))
    im.putalpha(a)
    ang=ang if ang is not None else rng.uniform(-14,14)
    return im.rotate(ang,expand=True,resample=Image.BICUBIC)
def folha_transicao(w=1080,h=1920,seed=21):
    """folha de papel rasgada que atravessa a tela na troca de cena"""
    H2=h+360; f=rasgado(w+80,H2,PAPEL_M,seed=seed,amp=40)
    band=rasgado(w+60,150,LARANJA,seed=seed+1,amp=18); f.alpha_composite(band,(10,40))
    band2=rasgado(w+60,110,LILAS,seed=seed+2,amp=16); f.alpha_composite(band2,(10,H2-190))
    d=ImageDraw.Draw(f,'RGBA'); _rabiscos(d,w,H2,random.Random(seed),80,300,w-80,H2-300,alpha=30)
    return shadow(f,off=(0,-12),blur=18,alpha=90)
