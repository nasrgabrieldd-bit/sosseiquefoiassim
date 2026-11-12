"""Gera posts.md (YouTube, Instagram, TikTok) a partir do roteiro.json. Uso: posts.py ep_dir"""
import json,sys
EP=sys.argv[1]; r=json.load(open(f'{EP}/roteiro.json')); import os
M=json.load(open(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/marca/marca.json'))
TAG={'HISTÓRIA':'#historia','LITERATURA':'#literatura','LÍNGUA PORTUGUESA':'#portugues #lingua','GEOGRAFIA':'#geografia','MATEMÁTICA':'#matematica',
 'FÍSICA':'#fisica #ciencia','QUÍMICA':'#quimica #ciencia','BIOLOGIA':'#biologia #ciencia','FILOSOFIA':'#filosofia','ARTE':'#arte #historiadaarte','EDUCAÇÃO FÍSICA':'#educacaofisica #esporte'}
mat=r['materia'].capitalize() if r['materia']!='LÍNGUA PORTUGUESA' else 'Língua Portuguesa'
mat={'EDUCAÇÃO FÍSICA':'Educação Física','HISTÓRIA':'História','MATEMÁTICA':'Matemática','FÍSICA':'Física','QUÍMICA':'Química','GEOGRAFIA':'Geografia'}.get(r['materia'],mat)
gancho=' '.join(f[0] for f in r['cenas'][0]['frases'])
cta=[f[0] for f in r['cenas'][-1]['frases'] if '?' in f[0]]
cta=cta[0] if cta else 'Comenta aí!'
fontes='\n'.join('• '+x for x in r['fontes'])
import re
fontes_curtas='; '.join(re.split(r'[,(]',x)[0].strip().rstrip('.') for x in r['fontes'])
tags=f"{TAG.get(r['materia'],'')} #curiosidades #educacao #aprendendo #sosseiquefoiassim"
yt=f"""## YouTube (Shorts)
**Título:** {r['titulo']} #shorts
**Descrição:**
{gancho}

Matéria: {mat}

Fontes:
{fontes}

Narração gerada por IA. Roteiro checado em fontes confiáveis.
{tags}
"""
ig=f"""## Instagram (Reels)
{gancho}

{cta} 👇

📚 Fontes: {fontes_curtas}.
🎙️ Narração gerada por IA.
{tags} #aprendanoinsta
"""
tk=f"""## TikTok
{r['titulo'].lower()} 🤓
Fontes: {fontes_curtas}. Narração IA.
{tags} #fyp #aprendernotiktok
"""
open(f'{EP}/posts.md','w').write(f"# {r['id']} — {r['titulo']}\n\n{yt}\n{ig}\n{tk}")
print('ok')
