from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageChops
import numpy as np, math, random
import os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FS=ROOT+'/fontes/'
W,H=1080,1920
SX0,SY0,SX1,SY1=92,260,930,1400   # caixa segura (TikTok/Reels/Shorts)
CX=(SX0+SX1)//2
_fc={}
def F(name,w,size,style='normal'):
    k=(name,w,size,style)
    if k not in _fc: _fc[k]=ImageFont.truetype(f'{FS}{name}/files/{name}-latin-{w}-{style}.woff',size)
    return _fc[k]
def wrap(text,font,maxw):
    out=[]
    for par in text.split('\n'):
        line=''
        for w in par.split(' '):
            t=(line+' '+w).strip()
            if font.getlength(t)<=maxw: line=t
            else:
                if line: out.append(line)
                line=w
        out.append(line)
    return out
def text_block(d,text,font,fill,cx,y,maxw,align='center',lh=1.08,stroke=0,stroke_fill=None,x0=None):
    lines=wrap(text,font,maxw); asc,desc=font.getmetrics(); step=int((asc+desc)*lh)
    for i,l in enumerate(lines):
        w=font.getlength(l)
        x = cx-w/2 if align=='center' else x0
        d.text((x,y+i*step),l,font=font,fill=fill,stroke_width=stroke,stroke_fill=stroke_fill)
    return y+len(lines)*step
def noise(w,h,sigma=1.0,scale=1,seed=0):
    rng=np.random.default_rng(seed)
    a=rng.normal(0,1,(max(1,h//scale),max(1,w//scale))).astype(np.float32)
    im=Image.fromarray(((a*40+128).clip(0,255)).astype(np.uint8))
    if scale>1: im=im.resize((w,h),Image.BICUBIC)
    if sigma>0: im=im.filter(ImageFilter.GaussianBlur(sigma))
    return np.asarray(im).astype(np.float32)/255-0.5
def shadow(img,off=(10,14),blur=14,alpha=110):
    a=img.split()[3].point(lambda v: v*alpha//255)
    sh=Image.new('RGBA',(img.width+80,img.height+80),(0,0,0,0))
    s=Image.new('RGBA',img.size,(0,0,0,255)); s.putalpha(a)
    sh.alpha_composite(s,(40+off[0],40+off[1])); sh=sh.filter(ImageFilter.GaussianBlur(blur))
    sh.alpha_composite(img,(40,40)); return sh  # desloca -40,-40 ao colar
def paste_sh(base,img,xy,**k):
    s=shadow(img,**k); base.alpha_composite(s,(int(xy[0])-40,int(xy[1])-40))
def torn(img,amp=6,seed=1):
    rng=random.Random(seed); w,h=img.size; m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m)
    pts=[]
    for x in range(0,w+1,12): pts.append((x,rng.uniform(0,amp)))
    for y in range(0,h+1,12): pts.append((w-rng.uniform(0,amp),y))
    for x in range(w,-1,-12): pts.append((x,h-rng.uniform(0,amp)))
    for y in range(h,-1,-12): pts.append((rng.uniform(0,amp),y))
    d.polygon(pts,fill=255); out=img.copy(); out.putalpha(ImageChops.multiply(img.split()[3],m)); return out
def halftone(gray,cell,color,ang=0):
    """gray: L image (0 escuro). Retorna RGBA de pontos."""
    w,h=gray.size; small=gray.resize((w//cell+1,h//cell+1),Image.BILINEAR); a=np.asarray(small)
    out=Image.new('RGBA',(w,h),(0,0,0,0)); d=ImageDraw.Draw(out)
    for j in range(a.shape[0]):
        for i in range(a.shape[1]):
            r=(1-a[j,i]/255)**0.8*cell*0.72
            if r>0.6:
                x=i*cell+(cell/2 if j%2 else 0); y=j*cell
                d.ellipse((x-r,y-r,x+r,y+r),fill=color)
    return out
def arrow(d,p0,p1,width,fill,head=40):
    d.line([p0,p1],fill=fill,width=width)
    ang=math.atan2(p1[1]-p0[1],p1[0]-p0[0])
    a1=(p1[0]-head*math.cos(ang-0.5),p1[1]-head*math.sin(ang-0.5))
    a2=(p1[0]-head*math.cos(ang+0.5),p1[1]-head*math.sin(ang+0.5))
    tip=(p1[0]+width*0.6*math.cos(ang),p1[1]+width*0.6*math.sin(ang))
    d.polygon([tip,a1,a2],fill=fill)
def smooth(t): t=max(0,min(1,t)); return t*t*(3-2*t)
def ease(t): t=max(0,min(1,t)); return 1-(1-t)**3
