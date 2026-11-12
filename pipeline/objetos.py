"""Objetos desenhados em tons de cinza (viram recorte em retícula na colagem). Todos: f(w,h)->Image L (255=fundo)."""
from base import *
def _base(w,h): im=Image.new('L',(w,h),255); return im,ImageDraw.Draw(im)
def grad_ellipse(d,box,c0,c1,n=40):
    x0,y0,x1,y1=box
    for k in range(n):
        t=k/(n-1); c=int(c0+(c1-c0)*t); s=t*0.5
        d.ellipse((x0+(x1-x0)*s*0.6,y0+(y1-y0)*s*0.6,x1-(x1-x0)*s*0.9,y1-(y1-y0)*s*0.9),fill=c)
def globo(w,h):
    im,d=_base(w,h); r=min(w,h)*0.46; cx,cy=w/2,h/2
    grad_ellipse(d,(cx-r,cy-r,cx+r,cy+r),90,215)
    for k in range(-3,4):
        rx=abs(r*math.cos(k*math.pi/8)); d.ellipse((cx-rx,cy-r,cx+rx,cy+r),outline=40,width=3)
    for k in range(-3,4):
        y=cy+r*math.sin(k*math.pi/8); dx=(r*r-(y-cy)**2)**0.5; d.line([(cx-dx,y),(cx+dx,y)],fill=40,width=3)
    d.ellipse((cx-r,cy-r,cx+r,cy+r),outline=20,width=5); return im
def livro(w,h):
    im,d=_base(w,h)
    for s in (-1,1):
        pts=[(w/2,h*0.25),(w/2+s*w*0.46,h*0.15),(w/2+s*w*0.46,h*0.82),(w/2,h*0.92)]
        d.polygon(pts,fill=225,outline=30)
        for k in range(9):
            y=h*(0.3+k*0.06); d.line([(w/2+s*w*0.06,y+5),(w/2+s*w*0.38,y-h*0.03)],fill=120,width=3)
    d.line([(w/2,h*0.25),(w/2,h*0.92)],fill=30,width=5)
    d.polygon([(w*0.02,h*0.85),(w/2,h*0.98),(w*0.98,h*0.85),(w*0.98,h*0.88),(w/2,h*1.0),(w*0.02,h*0.88)],fill=60)
    return im
def lampada(w,h):
    im,d=_base(w,h); cx=w/2; r=w*0.36
    grad_ellipse(d,(cx-r,h*0.05,cx+r,h*0.05+2*r),120,245)
    d.polygon([(cx-r*0.55,h*0.05+1.7*r),(cx+r*0.55,h*0.05+1.7*r),(cx+r*0.4,h*0.78),(cx-r*0.4,h*0.78)],fill=200)
    for k in range(4): y=h*(0.79+k*0.045); d.rounded_rectangle((cx-r*0.42,y,cx+r*0.42,y+h*0.035),radius=6,fill=70+k*15)
    d.ellipse((cx-r*0.18,h*0.96,cx+r*0.18,h*1.0),fill=40)
    d.line([(cx-r*0.2,h*0.62),(cx-r*0.1,h*0.4),(cx,h*0.55),(cx+r*0.1,h*0.4),(cx+r*0.2,h*0.62)],fill=60,width=4)
    return im
def relogio(w,h):
    im,d=_base(w,h); r=min(w,h)*0.42; cx,cy=w/2,h*0.55
    d.rectangle((cx-r*0.18,cy-r*1.28,cx+r*0.18,cy-r*1.05),fill=60); d.ellipse((cx-r*0.25,cy-r*1.4,cx+r*0.25,cy-r*1.2),fill=80)
    grad_ellipse(d,(cx-r,cy-r,cx+r,cy+r),70,150); d.ellipse((cx-r*0.86,cy-r*0.86,cx+r*0.86,cy+r*0.86),fill=238)
    for k in range(12):
        a=k*math.pi/6; d.line([(cx+r*0.7*math.sin(a),cy-r*0.7*math.cos(a)),(cx+r*0.8*math.sin(a),cy-r*0.8*math.cos(a))],fill=30,width=5)
    d.line([(cx,cy),(cx+r*0.45,cy-r*0.3)],fill=20,width=8); d.line([(cx,cy),(cx-r*0.1,cy-r*0.65)],fill=20,width=6); d.ellipse((cx-10,cy-10,cx+10,cy+10),fill=20)
    return im
def coroa(w,h):
    im,d=_base(w,h)
    pts=[(w*0.05,h*0.85),(w*0.05,h*0.3),(w*0.27,h*0.6),(w*0.5,h*0.15),(w*0.73,h*0.6),(w*0.95,h*0.3),(w*0.95,h*0.85)]
    for k in range(30):
        t=k/29; d.polygon([(x,y+ (h*0.85-y)*t*0.9) for x,y in pts],fill=int(110+100*(1-t)))
    d.polygon(pts,outline=30); d.rectangle((w*0.05,h*0.78,w*0.95,h*0.95),fill=60)
    for x in (0.05,0.5,0.95): d.ellipse((w*x-w*0.05,h*(0.3 if x!=0.5 else 0.15)-w*0.05,w*x+w*0.05,h*(0.3 if x!=0.5 else 0.15)+w*0.05),fill=40)
    for x in (0.25,0.5,0.75): d.ellipse((w*x-w*0.04,h*0.82,w*x+w*0.04,h*0.91),fill=200)
    return im
def maca(w,h):
    im,d=_base(w,h); cx,cy=w/2,h*0.58; r=w*0.42
    for k in range(40):
        t=k/39; c=int(70+150*t)
        d.ellipse((cx-r*(1-t*0.5)-r*0.15,cy-r*0.9*(1-t*0.5),cx+r*(1-t*0.6)-r*0.15,cy+r*0.9*(1-t*0.55)),fill=c)
        d.ellipse((cx-r*(1-t*0.6)+r*0.15,cy-r*0.9*(1-t*0.5),cx+r*(1-t*0.5)+r*0.15,cy+r*0.9*(1-t*0.55)),fill=c)
    d.line([(cx,cy-r*0.75),(cx+w*0.04,h*0.08)],fill=30,width=int(w*0.04))
    d.ellipse((cx+w*0.04,h*0.06,cx+w*0.32,h*0.2),fill=90); d.ellipse((cx-r*0.55,cy-r*0.5,cx-r*0.3,cy-r*0.2),fill=250)
    return im
def coracao(w,h):
    im,d=_base(w,h); r=w*0.27
    for k in range(30):
        t=k/29; c=int(60+170*t); s=1-t*0.55
        d.ellipse((w*0.5-2*r*s,h*0.3-r*s,w*0.5,h*0.3+r*s),fill=c); d.ellipse((w*0.5,h*0.3-r*s,w*0.5+2*r*s,h*0.3+r*s),fill=c)
        d.polygon([(w*0.5-2*r*s+3,h*0.33),(w*0.5+2*r*s-3,h*0.33),(w*0.5,h*0.33+(h*0.62)*s)],fill=c)
    return im
def polvo(w,h):
    im,d=_base(w,h); cx=w/2
    for i in range(8):
        base_x=cx+(i-3.5)*w*0.055; dirx=(i-3.5)/3.5
        pts=[]
        for k in range(36):
            t=k/35; x=base_x+dirx*w*0.42*t+math.sin(t*4+i)*w*0.03; y=h*0.48+h*0.42*t-(h*0.12*t*t if abs(dirx)>0.6 else 0)
            pts.append((x,y))
        # ponta enrolada
        ex,ey=pts[-1]; 
        for k in range(12):
            a=k/11*math.pi*1.4; r=w*0.035*(1-k/14); pts.append((ex+math.copysign(1,dirx or 1)*r*math.sin(a),ey-r*(1-math.cos(a))))
        for k in range(len(pts)-1):
            t=k/len(pts); wd=max(3,int(w*0.075*(1-t)**0.8)); d.line([pts[k],pts[k+1]],fill=int(60+90*t),width=wd)
    grad_ellipse(d,(cx-w*0.26,h*0.04,cx+w*0.26,h*0.56),60,215)
    for s_ in (-1,1): d.ellipse((cx+s_*w*0.1-w*0.06,h*0.36,cx+s_*w*0.1+w*0.06,h*0.45),fill=248); d.ellipse((cx+s_*w*0.1-w*0.025,h*0.39,cx+s_*w*0.1+w*0.025,h*0.44),fill=15)
    return im
def frasco(w,h):
    im,d=_base(w,h); cx=w/2
    d.rectangle((cx-w*0.12,h*0.05,cx+w*0.12,h*0.4),fill=215,outline=40,width=4)
    d.polygon([(cx-w*0.12,h*0.4),(cx+w*0.12,h*0.4),(cx+w*0.45,h*0.95),(cx-w*0.45,h*0.95)],fill=225,outline=40)
    for k in range(25):
        t=k/24; y=h*(0.65+0.3*t); dx=w*0.12+(w*0.33)*((y-h*0.4)/(h*0.55))
        d.line([(cx-dx+4,y),(cx+dx-4,y)],fill=int(150-80*t),width=int(h*0.014)+1)
    for (x,y,r) in [(0.45,0.72,0.03),(0.55,0.6,0.02),(0.5,0.5,0.015)]: d.ellipse((w*x-w*r,h*y-w*r,w*x+w*r,h*y+w*r),fill=245,outline=60)
    d.rectangle((cx-w*0.15,h*0.02,cx+w*0.15,h*0.08),fill=60); return im
def caderno(w,h):
    im,d=_base(w,h)
    d.rectangle((w*0.08,h*0.04,w*0.94,h*0.96),fill=70)
    d.rectangle((w*0.13,h*0.04,w*0.92,h*0.94),fill=232)
    for k in range(16): y=h*(0.12+k*0.05); d.line([(w*0.2,y),(w*0.88,y)],fill=170,width=2)
    rng=random.Random(4)
    for k in range(12):
        y=h*(0.11+k*0.05); x=w*0.22
        while x<w*0.84: l=rng.uniform(15,60); d.line([(x,y),(x+l,y-rng.uniform(-2,2))],fill=60,width=3); x+=l+rng.uniform(8,16)
    for k in range(10): y=h*(0.08+k*0.09); d.ellipse((w*0.05,y,w*0.13,y+h*0.035),outline=40,width=4)
    return im
def moldura(w,h):
    im,d=_base(w,h)
    for k in range(18):
        t=k/17; c=int(70+120*abs(0.5-t)*2); m=w*0.012*k
        d.rectangle((m,m*h/w,w-m,h-m*h/w),outline=c,width=int(w*0.014)+1)
    m=w*0.22; d.rectangle((m,m,w-m,h-m),fill=246)
    for (x,y) in [(0.3,0.3),(0.7,0.3),(0.3,0.75),(0.7,0.75)]:
        d.line([(w*x,h*y),(w*x+w*0.03,h*y+w*0.03)],fill=40,width=6); d.ellipse((w*x-6,h*y-6,w*x+6,h*y+6),fill=40)
    return im
def medalha(w,h):
    im,d=_base(w,h); cx=w/2
    d.polygon([(cx-w*0.3,0),(cx-w*0.08,0),(cx+w*0.05,h*0.45),(cx-w*0.1,h*0.45)],fill=110)
    d.polygon([(cx+w*0.3,0),(cx+w*0.08,0),(cx-w*0.05,h*0.45),(cx+w*0.1,h*0.45)],fill=150)
    r=w*0.33; grad_ellipse(d,(cx-r,h*0.38,cx+r,h*0.38+2*r),80,225); d.ellipse((cx-r*0.7,h*0.38+r*0.3,cx+r*0.7,h*0.38+r*1.7),outline=60,width=5)
    return im
def computador(w,h):
    im,d=_base(w,h)
    d.rounded_rectangle((w*0.05,h*0.05,w*0.95,h*0.72),radius=int(w*0.04),fill=60)
    d.rectangle((w*0.1,h*0.1,w*0.9,h*0.66),fill=225)
    f=F('archivo-black',400,int(h*0.12)); rng=random.Random(2)
    for k in range(4):
        s=''.join(rng.choice('01') for _ in range(6)); d.text((w*0.16,h*(0.12+k*0.13)),s,font=f,fill=30)
    d.polygon([(w*0.4,h*0.72),(w*0.6,h*0.72),(w*0.66,h*0.88),(w*0.34,h*0.88)],fill=100)
    d.rounded_rectangle((w*0.22,h*0.88,w*0.78,h*0.95),radius=8,fill=80); return im
def castelo(w,h):
    im,d=_base(w,h); n=5; tw=w/(n*1.5)
    d.rectangle((w*0.04,h*0.45,w*0.96,h*0.98),fill=150)
    for i in range(n):
        x=w*0.04+i*(w*0.92-tw)/(n-1); tt=h*(0.15 if i in (0,n-1) else 0.28)
        for k in range(20): t=k/19; d.rectangle((x,tt+(h-tt)*t*0.9,x+tw,h*0.98),fill=int(170-90*t))
        for k in range(3): d.rectangle((x+k*tw/2.6,tt-h*0.06,x+k*tw/2.6+tw/5,tt),fill=110)
    d.rounded_rectangle((w*0.44,h*0.66,w*0.56,h*0.98),radius=int(w*0.05),fill=40); return im
def celular(w,h):
    im,d=_base(w,h); d.rounded_rectangle((w*0.15,h*0.02,w*0.85,h*0.98),radius=int(w*0.1),fill=50)
    d.rounded_rectangle((w*0.2,h*0.07,w*0.8,h*0.93),radius=int(w*0.07),fill=230)
    for k in range(4):
        y=h*(0.15+k*0.18); s=-1 if k%2 else 1; x0=w*(0.25 if s>0 else 0.38)
        d.rounded_rectangle((x0,y,x0+w*0.37,y+h*0.1),radius=16,fill=170 if s>0 else 110)
    return im
def corredor(w,h):
    im,d=_base(w,h); c=60; L=lambda p,q,wd: d.line([(w*p[0],h*p[1]),(w*q[0],h*q[1])],fill=c,width=int(w*wd))
    d.ellipse((w*0.48,h*0.02,w*0.64,h*0.16),fill=c)
    L((0.55,0.17),(0.45,0.5),0.12); L((0.52,0.24),(0.72,0.36),0.06); L((0.72,0.36),(0.8,0.24),0.05)
    L((0.5,0.24),(0.32,0.36),0.06); L((0.32,0.36),(0.25,0.46),0.05)
    L((0.45,0.5),(0.66,0.68),0.08); L((0.66,0.68),(0.6,0.95),0.07); L((0.45,0.5),(0.3,0.72),0.08); L((0.3,0.72),(0.1,0.78),0.07)
    return im
OBJ={'globo':globo,'livro':livro,'lampada':lampada,'relogio':relogio,'coroa':coroa,'maca':maca,'coracao':coracao,'polvo':polvo,
     'frasco':frasco,'caderno':caderno,'moldura':moldura,'medalha':medalha,'computador':computador,'castelo':castelo,'celular':celular,'corredor':corredor}
def caverna(w,h):
    im,d=_base(w,h)
    d.rounded_rectangle((0,h*0.02,w,h),radius=int(w*0.1),fill=45)
    for k in range(24):
        t=k/23; c=int(150+80*t); m=t*w*0.12
        d.ellipse((w*0.06+m*1.5,h*0.1+m,w*0.94-m*0.3,h*1.75),fill=c)
    d.rectangle((0,h*0.9,w,h),fill=45)
    for k in range(14):
        t=k/13; r=w*(0.22-0.18*t); d.ellipse((w*0.82-r,h*0.78-r,w*0.82+r,h*0.78+r),fill=int(200+55*t))
    d.polygon([(w*0.77,h*0.9),(w*0.79,h*0.74),(w*0.81,h*0.8),(w*0.83,h*0.62),(w*0.85,h*0.8),(w*0.87,h*0.9)],fill=255,outline=60)
    for x,y in [(0.2,0.42),(0.28,0.38),(0.36,0.44)]:
        d.ellipse((w*x-w*0.035,h*y-w*0.035,w*x+w*0.035,h*y+w*0.035),fill=95); d.rounded_rectangle((w*x-w*0.05,h*y+w*0.035,w*x+w*0.05,h*y+h*0.22),radius=10,fill=95)
    for x in (0.46,0.57,0.68):
        d.ellipse((w*x-w*0.04,h*0.56,w*x+w*0.04,h*0.56+w*0.08),fill=25); d.rounded_rectangle((w*x-w*0.065,h*0.56+w*0.075,w*x+w*0.065,h*0.9),radius=18,fill=25)
    return im
def telha(w,h):
    im,d=_base(w,h)
    for k in range(60):
        t=k/59; x0=w*0.1+w*0.8*t; c=int(80+150*math.sin(t*math.pi))
        d.polygon([(x0,h*0.1),(x0+w*0.8/59+1,h*0.1),(x0+w*0.8/59*1.2+1,h*0.95),(x0-w*0.03*(0.5-t),h*0.95)],fill=c)
    d.polygon([(w*0.1,h*0.1),(w*0.9,h*0.1),(w*0.95,h*0.95),(w*0.05,h*0.95)],outline=40); return im
def arvore(w,h):
    im,d=_base(w,h)
    d.polygon([(w*0.44,h*0.95),(w*0.47,h*0.5),(w*0.53,h*0.5),(w*0.58,h*0.95)],fill=60)
    d.line([(w*0.5,h*0.6),(w*0.3,h*0.45)],fill=60,width=int(w*0.04)); d.line([(w*0.52,h*0.58),(w*0.72,h*0.42)],fill=60,width=int(w*0.04))
    rng=random.Random(3)
    for k in range(26):
        x=w*rng.uniform(0.15,0.85); y=h*rng.uniform(0.08,0.5); r=w*rng.uniform(0.1,0.17); grad_ellipse(d,(x-r,y-r,x+r,y+r),110,200,12)
    for x,y in [(0.3,0.35),(0.6,0.3),(0.72,0.45),(0.42,0.2)]: d.ellipse((w*x-w*0.03,h*y-w*0.03,w*x+w*0.03,h*y+w*0.03),fill=30)
    d.rectangle((0,h*0.95,w,h),fill=90); return im
OBJ.update({'caverna':caverna,'telha':telha,'arvore':arvore})
