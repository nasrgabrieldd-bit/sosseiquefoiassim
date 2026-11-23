"""Confere a área segura (TikTok/Reels/Shorts) sobre um quadro já renderizado de um episódio.
Pinta em vermelho translúcido a 'zona morta' oficial do Reels/Shorts em 1080x1920 (topo 220px,
base 450px, laterais 35px — fonte: print de referência enviado por Gabriel em 20/11/2026) e em
verde a caixa segura que o pipeline usa de fato (base.py: SX0,SY0,SX1,SY1). Em laranja tracejado,
a coluna de ícones do feed do TikTok (até ~240px a partir da borda direita), que é mais larga que
a margem lateral oficial do Reels e por isso merece atenção extra nesse lado.
Uso: python3 margens.py EP_DIR t
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
EP = sys.argv[1]
t = sys.argv[2] if len(sys.argv) > 2 else '3.0'
sys.argv = [sys.argv[0], EP, 'quadros', t]
import motor as M          # executa o módulo com o EP acima (gera /tmp/q_<t>.png como efeito colateral)
from base import *

im = M.quadro(float(t)).convert('RGBA')
ov = Image.new('RGBA', im.size, (0, 0, 0, 0))
d = ImageDraw.Draw(ov)

# zona morta oficial Reels/Shorts (1080x1920): topo 220, base 450, laterais 35
d.rectangle((0, 0, W, 220), fill=(255, 0, 0, 70))
d.rectangle((0, H - 450, W, H), fill=(255, 0, 0, 70))
d.rectangle((0, 0, 35, H), fill=(255, 0, 0, 70))
d.rectangle((W - 35, 0, W, H), fill=(255, 0, 0, 70))

# aviso: coluna de ícones do feed do TikTok (mais larga que a margem oficial do Reels)
d.rectangle((W - 240, int(H * 0.45), W - 35, int(H * 0.92)), outline=(255, 140, 0, 255), width=4)

# caixa segura usada de fato pelo pipeline
d.rectangle((SX0, SY0, SX1, SY1), outline=(0, 200, 80, 255), width=6)

im = Image.alpha_composite(im, ov)
out = f'/tmp/margens_{os.path.basename(EP.rstrip("/"))}_{t}.png'
im.convert('RGB').save(out)
print(out)
