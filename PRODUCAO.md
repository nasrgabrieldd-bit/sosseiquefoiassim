# Manual de produção de um vídeo

## Formato
Vertical 1080×1920, 30 fps, 61 a 175 s (alvo 65–90 s). Voz Kokoro "A" (60% pm_alex + 40% pm_santa, 0,98×), trilha procedural baixa e efeitos. Visual: colagem do `MARCA.md` (papel envelhecido, rasgados lilás/laranja, cor da matéria só num pedaço de papel e na etiqueta).

## Roteiro (gerado por um builder em `lotes/`)
Campos: `id` (SSA-###, sequencial), `materia` (uma de `pipeline/colagem.py: MATERIAS`), `titulo`, `chamada` (capa, curta, em CAIXA ALTA), `fontes` (lista completa), `capa.elementos`, `cenas`.
Cada cena: `id`, `frases` = lista de `[legenda, fala]` (legenda com algarismos; fala com números por extenso e nomes estrangeiros escritos como se pronunciam), `elementos`, `camera`, `fonte` (linha curta mostrada na tela).

Estrutura obrigatória (6 a 8 cenas):
1. **Gancho** (cena 1): primeira frase com até 16 palavras, com lacuna (contradição, número, mito, pergunta). Quadro 0 já completo. Sem saudação nem nome do canal.
2. Contexto (começa antes de 8 s).
3. a 5. Desenvolvimento, com a resposta só a partir da cena 3–4.
6. **"E hoje?"**: ligação com o presente (evento da semana, celular, novela, futebol, meme), com fonte.
7. CTA: retoma o gancho + convite para interagir + assinatura `A fonte tá na legenda. Só sei que foi assim!`.
Entre 175 e 230 palavras faladas.

**Variedade no CTA (regra fixa, desde 13/11):** nunca termine dois vídeos seguidos com a mesma estrutura. Alterne entre formatos como:
- Pergunta direta: "Qual [x] você faria?"
- Pedido de opinião/voto: "Time A ou time B? Comenta."
- Pedido de marcação: "Marca aquele amigo que [faz x]."
- Afirmação sem pergunta: "Agora você sabe de onde vem [x]." (sem CTA de comentário)
- Convite a salvar/compartilhar: "Salva esse pra lembrar na prova."
- Pergunta sobre experiência própria: "Isso já te aconteceu?"
`pipeline/posts.py` já roda os hashtags de preenchimento em um pequeno rodízio; a parte manual é o texto do CTA em si — escreva pensando na última vez que terminou um vídeo e evite repetir a abertura.

## Elementos (`t`)
`obj` (desenho em retícula: ver `pipeline/objetos.py: OBJ`, além de `tv`, `radio`), `jornal` (titulo, data, rodape, `marca`=[frase, palavra] para o marca-texto), `tira` (etiqueta de máquina de escrever), `bloco` (título rasgado laranja/grafite), `nota` (manuscrito), `numero` (Anton gigante), `verbete` (cartão de dicionário), `cal` (calendário com `riscar`), `areas` (comparação de tamanho), `contador`, `seta` (à mão), `risco`.
Comuns: `pos` [x,y] = centro; `e` = [índice da frase, "palavra" | fração] para a entrada (sem `e` = já na tela); `anim` pop | slide_l/r/b/t | fade | escrita; `sai`; `ang`; `escala`; `balanca`; `foco` (desfoca o resto: rack focus).
Câmera: `push` (aproximação lenta), `zooms` [{e, escala≤1.18, alvo}], `congela` {de, ate} (quadro P&B).

Área segura: todo conteúdo entre x 92–930 e y 380–1200. Legenda em y 1240; linha de fonte em 1372. Nada perto das bordas.

## Comandos
```
python3 lotes/semana_AAAA-MM-DD.py              # gera os roteiro.json
python3 pipeline/narra.py episodios/ID/roteiro.json episodios/ID
python3 pipeline/motor.py episodios/ID prancha   # /tmp/prancha_ID.png: revisar com Read
bash pipeline/produz.sh episodios/ID             # vídeo final episodios/ID/ID.mp4 + capa.png
python3 pipeline/posts.py episodios/ID           # posts.md
```

## Checagem antes de publicar
- Cada número e afirmação bate com a fonte (releia as fontes, não confie na memória).
- Duração entre 61 e 175 s (`tempos.json` → `total`).
- Prancha: nada cortado, sobreposto à legenda ou fora da área segura; palavras-chave (`e`) existem na frase.
- Nomes estrangeiros com grafia fonética na fala.
