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

## 2. Rotina diária (todo dia, ~16:17)
1. Leia `agenda.json`. Se algum vídeo das próximas 48 h não tiver `.mp4` no repositório, produza (mesmo processo acima) e faça push.
2. **Publicação** conforme `PUBLICACAO.md` (método configurado). Agende o que estiver pendente para as próximas datas, respeitando os limites da ferramenta. Marque `status: "agendado"` só com o ID devolvido pela API.
3. Confira os posts das últimas 48 h (enviados / erro) e anote em `agenda.json`.
4. Aviso curto ao fundador: o que foi agendado, o que deu erro, o que falta.

## Aprendizados (atualize a cada ciclo)
- Frase de gancho com até 16 palavras; cena 2 começa antes de 8 s.
- Roteiro com menos de ~175 palavras faladas fica abaixo de 61 s: alongue antes de narrar.
- Glifos `→` e `≈` não existem nas fontes: use palavras ("viram", "~").
- Zoom de câmera no máximo 1,18 e sempre ancorado no alvo; elementos perto da borda saem da tela.
