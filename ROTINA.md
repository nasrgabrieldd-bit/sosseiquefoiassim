# Rotina automática

Duas tarefas agendadas rodam em sessões novas. Cada uma clona este repositório, roda `bash setup.sh` e segue esta página.

Horários de postagem: **12:00 e 19:00 (America/Sao_Paulo)**, todos os dias, nas 3 redes. Semana editorial = **sexta a quinta** (14 vídeos).

## 1. Produção semanal (quarta-feira, ~14:47)
Objetivo: deixar prontos e no GitHub os 14 vídeos da próxima semana (sexta a quinta).

1. **Calendário da semana.** Pesquise na web (WebSearch) os eventos da sexta à quinta seguintes, e anote em `semanas/AAAA-MM-DD/calendario.md` (data da sexta), com fonte e data de cada um:
   - esportes: finais e decisões (Libertadores, Copa do Brasil, Brasileirão, Champions, Copa do Mundo, F1, Olimpíadas, NBA);
   - cinema, TV e música: Oscar, Globo de Ouro, Grammy, estreias muito esperadas, finais de reality e novela;
   - datas comemorativas e feriados do Brasil (ex.: 20/11 Dia da Consciência Negra), dias mundiais da ONU/UNESCO;
   - efemérides: aniversários "redondos" de fatos históricos (50, 100, 200 anos...);
   - ciência e espaço: eclipses, chuvas de meteoros, lançamentos, prêmios Nobel;
   - educação: ENEM, vestibulares, volta às aulas;
   - cultura pop e memes do momento (só como gancho falado/escrito, sem imagens de terceiros).
2. **Pauta (14 temas).** No mínimo **5 temas ligados a eventos da semana** e os demais atemporais. Para cada evento, encontre uma curiosidade educativa VERDADEIRA que se conecte a ele (ex.: final da Libertadores → por que a taça se chama Libertadores e quem foram os "libertadores"; Oscar → por que a estatueta tem esse apelido). O evento entra no gancho ou na cena "e hoje?". Poste o vídeo do evento 1 a 2 dias antes ou no próprio dia.
   - Gire as matérias: na semana, pelo menos 8 matérias diferentes; nunca a mesma matéria duas vezes seguidas.
   - Não repita tema de `PAUTAS.md`.
   - Evite tragédias recentes, política partidária, apostas e qualquer tema que exija imagem de terceiros para funcionar.
3. **Pesquisa e roteiro.** Para cada tema, 2 a 4 buscas em fontes confiáveis (enciclopédias, museus, universidades, livros didáticos, veículos de referência). Escreva o roteiro no builder da semana `lotes/semana_AAAA-MM-DD.py` (modelo: `lotes/lote1.py`) seguindo `PRODUCAO.md`. Rode o builder.
4. **Produção.** Para cada episódio: `python3 pipeline/narra.py ...` → conferir duração (61 a 175 s) → `python3 pipeline/motor.py EP prancha` → olhar a prancha com Read e corrigir o que estiver cortado/sobreposto → `bash pipeline/produz.sh EP` → `python3 pipeline/posts.py EP`. Rode 2 produções em paralelo (a máquina tem 2 núcleos).
5. **Commit e push depois de cada vídeo** (`episodios/<ID>/<ID>.mp4`, `capa.png`, `posts.md`, `roteiro.json`, `tempos.json`). Confirme HTTP 200 da URL raw: `https://raw.githubusercontent.com/nasrgabrieldd-bit/sosseiquefoiassim/main/episodios/<ID>/<ID>.mp4`.
6. **Agenda.** Acrescente os 14 itens em `agenda.json` (`id`, `data`, `hora`, `status: "pendente"`). Atualize `PAUTAS.md`.
7. **Aviso ao fundador** (push no celular): lista dos 14 temas com data/hora, quais são os 5+ ligados a eventos e qualquer pendência.

Se a sessão acabar no meio, a rotina diária termina o que faltar.

## 2. Rotina diária (todo dia, ~05:15, logo após a cota do YouTube zerar)
1. Leia `agenda.json`. Se algum vídeo das próximas 48 h não tiver `.mp4` no repositório, produza (mesmo processo acima) e faça push.
2. **Publicação** conforme `PUBLICACAO.md`: primeiro o YouTube pelo Composio (cota diária), depois Instagram e TikTok pelo Zernio. Agende o que estiver pendente para as próximas datas, respeitando os limites da ferramenta. Marque `status: "agendado"` só com o ID devolvido pela API.
3. Confira os posts das últimas 48 h (enviados / erro) e anote em `agenda.json`.
4. Aviso curto ao fundador: o que foi agendado, o que deu erro, o que falta.

## Aprendizados (atualize a cada ciclo)
- Frase de gancho com até 16 palavras; cena 2 começa antes de 8 s.
- Roteiro com menos de ~175 palavras faladas fica abaixo de 61 s: alongue antes de narrar.
- Glifos `→` e `≈` não existem nas fontes: use palavras ("viram", "~").
- Zoom de câmera no máximo 1,18 e sempre ancorado no alvo; elementos perto da borda saem da tela.

## Aprendizados (2) — instabilidade do raw.githubusercontent.com no Instagram
- 13/11: o SSA-001 falhou no Instagram ("couldn't fetch your media"), mas o TikTok saiu normal com a mesma URL. O erro era na capa (instagramThumbnail), não no vídeo. Recriar o post só para o Instagram, com a mesma URL, funcionou de primeira — foi falha passageira do GitHub ao servir para o buscador do Meta, não um problema permanente de content-type.
- Se um post ficar "partial" com falha no Instagram citando a URL da mídia: espere 1–2 min e crie um post novo só com a plataforma Instagram, mesmo conteúdo e mesma URL (publish_now). Não precisa trocar de CDN.

## Aprendizados (3) — variedade de CTA e hashtags
- Lote 1 (SSA-001 a 014) terminou 12 dos 14 vídeos com "X? Comenta." e hashtags quase idênticos — risco de parecer template repetido. Corrigido: ver PRODUCAO.md (CTA) e pipeline/posts.py (rodízio de hashtags). Builders novos devem variar a estrutura do CTA, nunca repetindo a mesma abertura duas vezes seguidas.
- Nenhum vídeo do lote 1 estava ligado a evento da semana (meta é ≥5) porque foi produzido antes da rotina semanal existir. A partir do lote de 21–27/11 (produzido na quarta 18/11), aplicar a meta normalmente.


## Aprendizados (4) — lote 3 (SSA-035 a 048, produzido em 18/11)
- A agenda já ia até 29/11 quando a produção semanal de 18/11 rodou (o lote 2 cobriu 10 dias). Em vez de duplicar a semana 20–26/11, o lote 3 cobriu os 14 horários livres seguintes (30/11 a 06/12). Regra prática: a produção semanal sempre começa no primeiro horário sem vídeo em `agenda.json`.
- Prancha: o chip da matéria ocupa y ~318–370. `jornal` com w>460 ou centro acima de y 700 e `bloco` de 2 linhas acima de y 520 encostam nele. Calendário (`cal`) de 31 dias: escala ≤0,55 e centro em y ≥680.
- `risco` por cima de uma `tira` deixa o texto ilegível; só use para "riscar" algo que deve sumir mesmo.
- `verbete` corta a palavra se ela passar de ~20 caracteres em w=700; nomes longos vão em `bloco`.
- Capa: o `bloco` da capa não pode repetir a `chamada` (as duas aparecem juntas).
- Checagem: a Lei 14.567/2023 (escolas de samba) NÃO fixa o 2 de dezembro; o Dia Nacional do Samba é data tradicional (há PL 6.171/2025 para oficializar). Conferir sempre o texto da lei, não a notícia.

## Aprendizados (5) — lote 4 (SSA-052 a SSA-065, produzido em 25/11)
- A agenda ia até 08/12 12h (SSA-051, vídeo-teste aprovado). Pela regra do lote 3, o lote 4 cobriu os 14 horários livres seguintes: 08/12 19h a 15/12 12h. A próxima produção semanal começa em 15/12 19h.
- `carimbo`: com r=110, `txt` de até ~7 caracteres e `data` de até ~5 ("14 DEZ" / "1911"). Texto maior vaza do anel ("ERRADICADA", "FRACASSO?" vazaram).
- A fonte de máquina de escrever (tira/carimbo) não tem "Ł": escreva "Bialystok" (e confira outros diacríticos do Leste Europeu).
- No `numero` (Anton), o ponto médio "·" sai minúsculo; para pontos de código Morse use "•".
- Elementos são desenhados na ordem da lista: um `risco` listado ANTES da `tira` fica escondido por baixo dela. Para riscar, ponha o `risco` depois.
- Linha de `fonte` com mais de ~50 caracteres encosta nas bordas: abrevie (ex.: "Brookhaven Lab", "Museu de Oxford").
- `bloco` de 2 linhas centrado em y 480 encosta no chip da matéria: use y ≥ 560 para títulos longos.
- O builder `lotes/semana_2026-12-08.py` agora tem `valida()`: confere se toda palavra de entrada (`e`, `marca`, `riscar_em`, zoom, congela) está na legenda e se o gancho tem até 16 palavras, antes de gravar. Copie essa função nos próximos builders.
- Se mudar a legenda depois de narrar, o `tempos.json` guarda a legenda antiga (`leg`) e a palavra-chave nova não é encontrada: corrija o `tempos.json` também (ou narre de novo).
- Objetos novos em `objetos.py`: bola (vôlei), montanha, pipa, lupa, saleiro, bandeira (Noruega), meteoro.
- Zoom/push de câmera aproxima tudo em volta do `alvo`: o elemento mais alto da cena sobe e pode cobrir o chip da matéria (aconteceu no SSA-059). Em cena com `zooms`, deixe o elemento mais alto em y ≥ 560 e confira um quadro do vídeo final (`motor.py EP quadros t1,t2`), não só a prancha.
