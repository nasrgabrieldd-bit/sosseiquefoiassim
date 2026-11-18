"""Gera os roteiros do lote 3 (SSA-035 a SSA-048, 30/11 a 06/12/2026). Não rode depois de produzir: sobrescreve roteiros.
Calendário e fontes dos eventos: semanas/2026-11-30/calendario.md"""
import json,os
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'/episodios'
ASS=["A fonte tá na legenda. Só sei que foi assim!","Só sei que foi assim!"]  # leg mostra a fonte; tts não fala isso
def f(leg,tts=None): return [leg,tts or leg]
def tira(txt,pos,e=None,**k): return dict(t='tira',txt=txt,pos=pos,e=e,**k)
def bloco(txt,pos,e=None,**k): return dict(t='bloco',txt=txt,pos=pos,e=e,**k)
def nota(txt,pos,e=None,**k): return dict(t='nota',txt=txt,pos=pos,e=e,**k)
def obj(nome,pos,e=None,**k): return dict(t='obj',nome=nome,pos=pos,e=e,**k)
def num(txt,pos,e=None,**k): return dict(t='numero',txt=txt,pos=pos,e=e,**k)
def seta(de,ate,e=None,**k): return dict(t='seta',de=de,ate=ate,pos=[0,0],e=e,**k)
def risco(de,ate,e=None,**k): return dict(t='risco',de=de,ate=ate,pos=[0,0],e=e,**k)
def jornal(titulo,data,rodape,pos,e=None,**k): return dict(t='jornal',titulo=titulo,data=data,rodape=rodape,pos=pos,e=e,**k)
def tv(pos,e=None,**k): return dict(t='tv',pos=pos,e=e,**k)
def radio(pos,e=None,**k): return dict(t='radio',pos=pos,e=e,**k)
def verb(palavra,classe,defi,pos,e=None,**k): return dict(t='verbete',palavra=palavra,classe=classe,defi=defi,pos=pos,e=e,**k)
EPS={}

# ------------------------------------------------------------ 035 EDUCAÇÃO FÍSICA (30/11 · 154 anos do 1º jogo entre seleções)
EPS['SSA-035']=dict(materia='EDUCAÇÃO FÍSICA',titulo='O primeiro jogo oficial entre seleções terminou 0 a 0',
 fontes=["Scottish Football Museum, 'Scotland v England: the world's first football international fixture'.","The FA, 'England v Scotland: the oldest international' (2014).","National Football Museum (Reino Unido), 'World's first international'.","Flashscore Brasil (06/11/2026) e Correio da Manhã (08/11/2026): última rodada do Brasileirão e final da Copa do Brasil."],
 capa=dict(elementos=[jornal('GLASGOW HERALD','30 NOV. 1872','SCOTLAND v ENGLAND',[520,740],w=460,ang=-3),num('0 x 0',[560,1110],size=200)]),
 cenas=[
  dict(id='c1',frases=[f("O primeiro jogo oficial entre seleções da história terminou 0 a 0.","O primeiro jogo oficial entre seleções da história terminou zero a zero."),f("E foi há exatos 154 anos.","E foi há exatos cento e cinquenta e quatro anos.")],
   elementos=[jornal('GLASGOW HERALD','30 NOV. 1872','SCOTLAND v ENGLAND',[400,700],w=440,ang=-3,balanca=True),num('0 x 0',[700,1030],None,size=190),tira('há 154 anos',[300,1150],[1,'154'],size=46)]),
  dict(id='c2',fonte='Fonte: The FA (2014); Scottish Football Museum',frases=[f("Glasgow, Escócia, 30 de novembro de 1872.","Glasgow, Escócia, trinta de novembro de mil oitocentos e setenta e dois."),f("A federação inglesa desafiou os escoceses pelos jornais."),f("Um clube de Glasgow, o Queen's Park, topou. E os 11 escoceses eram todos de lá.","Um clube de Glasgow, o Cuíns Parc, topou. E os onze escoceses eram todos de lá.")],
   elementos=[tira('GLASGOW · 30/11/1872',[520,430],None,size=48),jornal('THE SCOTSMAN','OUT. 1872','A CHALLENGE',[330,730],[1,'desafiou'],w=380,ang=-4,marca=[1,'jornais']),
     tira("QUEEN'S PARK F.C.",[680,880],[2,"Queen's"],size=44),num('11',[700,1080],[2,'11'],size=170,cor='tinta')]),
  dict(id='c3',fonte='Fonte: Scottish Football Museum; The FA',frases=[f("O jogo foi num campo de críquete, chamado Hamilton Crescent.","O jogo foi num campo de críquete, chamado Rémilton Crécent."),f("O ingresso custava 1 xelim, e as mulheres entravam de graça.","O ingresso custava um xelim, e as mulheres entravam de graça."),f("E não tinha travessão: o alto do gol era só uma fita.")],
   elementos=[tira('HAMILTON CRESCENT',[520,440],None,size=50),bloco('1 xelim',[330,650],[1,'xelim'],size=84),nota('mulheres:\nde graça',[700,660],[1,'mulheres'],cor='laranja',size=58),
     bloco('sem travessão',[520,930],[2,'travessão'],size=74,cor='tinta',ang=-3),nota('só uma fita!',[640,1100],[2,'fita'],cor='laranja',size=62)]),
  dict(id='c4',fonte='Fonte: Scottish Football Museum',frases=[f("Os ingleses eram mais pesados e jogavam no drible: cada um tentando levar a bola sozinho."),f("Os escoceses fizeram diferente: tocavam a bola entre eles."),f("Era o passe virando estratégia.")],
   camera=dict(push=0.06),elementos=[tira('INGLATERRA: drible',[330,470],None,size=48),obj('corredor',[330,760],[0,'drible'],w=300,ang=-4),
     tira('ESCÓCIA: passe',[700,600],[1,'escoceses'],size=48),seta([560,880],[800,880],[1,'tocavam']),bloco('o passe virou\nestratégia',[540,1090],[2,'passe'],size=60,maxw=720)]),
  dict(id='c5',fonte='Fonte: National Football Museum; The FA',frases=[f("No primeiro tempo, a Escócia teve um gol anulado: a bola teria passado por cima da fita."),f("No fim, outra bola bateu na fita."),f("E mesmo assim, ninguém marcou.")],
   elementos=[bloco('GOL ANULADO',[520,520],None,size=84,cor='tinta',ang=-3),nota('por cima da fita',[560,700],[0,'cima'],cor='laranja',size=60),
     risco([200,860],[840,860],[1,'fita']),num('0 x 0',[520,1060],[2,'ninguém'],size=190)]),
  dict(id='c6',fonte='Fonte: Flashscore (06/11/2026); Correio da Manhã',frases=[f("E hoje? Esta semana tem a última rodada do Brasileirão, na quarta."),f("E a final da Copa do Brasil, no domingo."),f("Se algum desses jogos acabar 0 a 0, lembra: o futebol entre seleções começou exatamente assim.","Se algum desses jogos acabar zero a zero, lembra: o futebol entre seleções começou exatamente assim.")],
   elementos=[obj('celular',[250,700],None,w=240,ang=-4),tira('QUA · 38ª rodada',[660,560],[0,'quarta'],size=44),tira('DOM · final da Copa',[660,700],[1,'domingo'],size=42),
     num('0 x 0',[680,960],[2,'0 a 0'],size=150),nota('começou assim',[560,1140],[2,'começou'],cor='laranja',size=58)]),
  dict(id='c7',frases=[f("Então: 154 anos atrás, o primeiro jogo entre seleções acabou sem gol.","Então: cento e cinquenta e quatro anos atrás, o primeiro jogo entre seleções acabou sem gol."),f("Agora você sabe que até o 0 a 0 tem história.","Agora você sabe que até o zero a zero tem história."),ASS],
   elementos=[jornal('GLASGOW HERALD','30 NOV. 1872','SCOTLAND v ENGLAND',[360,660],None,w=400,ang=3),num('0 x 0',[740,820],None,size=160),bloco('até o 0 x 0 tem história',[520,1100],[1,'história'],size=66,maxw=780)])])

# ------------------------------------------------------------ 036 FÍSICA
EPS['SSA-036']=dict(materia='FÍSICA',titulo='Por que o céu é azul (e não violeta)',
 fontes=["Encyclopaedia Britannica, 'Rayleigh scattering'.","NASA Space Place, 'Why is the sky blue?'.","Royal Museums Greenwich, 'Why is the sky blue?'.","UC Riverside, Physics FAQ, 'Why is the sky blue?'.","NASA Scientific Visualization Studio, 'Curiosity Captures a Martian Sunset' (2015)."],
 capa=dict(elementos=[obj('lampada',[520,640],w=380,ang=-4),bloco('por que o céu é azul?',[520,1120],size=72,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Pela física, o céu devia ser violeta."),f("Mas ele é azul. E o motivo tá em você.")],
   elementos=[obj('lampada',[520,620],None,w=360,ang=-4,balanca=True),bloco('VIOLETA?',[520,950],None,size=100,cor='tinta',ang=-3),nota('o motivo tá em você',[560,1130],[1,'motivo'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: NASA Space Place',frases=[f("A luz do Sol parece branca, mas é a mistura de todas as cores."),f("Quando ela entra na atmosfera, bate nas moléculas do ar."),f("E cada cor reage de um jeito.")],
   elementos=[obj('lampada',[300,600],None,w=260),tira('luz branca = todas as cores',[560,860],[0,'mistura'],size=42),obj('globo',[700,620],[1,'atmosfera'],w=280,ang=6),nota('cada cor\nde um jeito',[560,1080],[2,'cada'],cor='laranja',size=58)]),
  dict(id='c3',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Em 1871, o físico Lord Rayleigh mostrou que as cores de onda mais curta se espalham muito mais.","Em mil oitocentos e setenta e um, o físico Lord Rêili mostrou que as cores de onda mais curta se espalham muito mais."),f("Azul e violeta se espalham pelo céu inteiro. O vermelho passa quase reto.")],
   elementos=[tira('LORD RAYLEIGH · 1871',[520,440],None,size=48),bloco('onda curta\nespalha mais',[520,680],[0,'curta'],size=70,maxw=700),
     tira('azul e violeta: pra todo lado',[520,940],[1,'Azul'],size=40),tira('vermelho: quase reto',[520,1080],[1,'vermelho'],size=44),seta([300,1150],[760,1150],[1,'reto'])]),
  dict(id='c4',fonte='Fonte: Royal Museums Greenwich; UC Riverside',frases=[f("Então por que não violeta?"),f("O Sol manda menos violeta do que azul, e parte dele fica lá no alto da atmosfera."),f("E o nosso olho é bem menos sensível ao violeta. Resultado: a gente vê azul.")],
   elementos=[bloco('por que não violeta?',[520,480],None,size=70),tira('1. o Sol manda menos violeta',[520,700],[1,'menos'],size=40),
     tira('2. o olho sente menos violeta',[520,850],[2,'olho'],size=40),bloco('= AZUL',[520,1060],[2,'Resultado'],size=110,cor='tinta')]),
  dict(id='c5',fonte='Fonte: NASA Space Place',frases=[f("No fim da tarde, o Sol está baixo, e a luz atravessa muito mais ar."),f("O azul vai se espalhando pelo caminho."),f("E o que sobra pra chegar no seu olho é laranja e vermelho.")],
   camera=dict(push=0.08),elementos=[obj('lampada',[250,860],None,w=220,ang=8),seta([380,820],[780,560],[0,'atravessa']),nota('muito mais ar',[640,840],[0,'mais ar'],size=58),
     bloco('LARANJA',[640,1070],[2,'laranja'],size=84)]),
  dict(id='c6',fonte='Fonte: NASA Scientific Visualization Studio (2015)',frases=[f("E hoje? Em Marte, o pôr do sol é azul."),f("Em 2015, o robô Curiosity filmou isso por lá.","Em dois mil e quinze, o robô Quiurióssiti filmou isso por lá."),f("A poeira marciana deixa o azul passar melhor do que o vermelho.")],
   elementos=[obj('globo',[520,640],None,w=380,ang=-6),tira('MARTE · CURIOSITY · 2015',[520,920],[1,'Curiosity'],size=44),bloco('pôr do sol azul',[520,1100],[0,'azul'],size=74,cor='tinta')]),
  dict(id='c7',frases=[f("Então: o céu só não é violeta por causa do Sol e do seu próprio olho."),f("Qual foi o pôr do sol mais bonito que você já viu? Conta onde foi."),ASS],
   elementos=[obj('lampada',[520,620],None,w=320,ang=3),bloco('não é violeta\npor causa do seu olho',[520,1000],[0,'olho'],size=58,maxw=760),nota('conta onde foi!',[700,1170],[1,'Conta'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 037 LÍNGUA PORTUGUESA
EPS['SSA-037']=dict(materia='LÍNGUA PORTUGUESA',titulo='Por que só o português tem "segunda-feira"',
 fontes=["Catholic Encyclopedia, 'St. Martin of Braga'.","MARTINHO DE DUME (Braga). De correctione rusticorum, séc. VI (trad. inglesa de A. Graham).","Marco Neves (Universidade NOVA de Lisboa), em Xataka Brasil: de onde vem o 'feira' dos dias da semana.","Instituto da Lingua Galega (Univ. de Santiago de Compostela): os nomes dos dias em galego."],
 capa=dict(elementos=[dict(t='cal',titulo='SEGUNDA-FEIRA',inicio=0,ndias=7,pos=[520,660],ang=-3),bloco('um bispo apagou os deuses da semana',[520,1130],size=64,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("As outras grandes línguas latinas dão aos dias nomes de deuses. O português, não."),f("A culpa é de um bispo do século 6.","A culpa é de um bispo do século seis.")],
   elementos=[bloco('SEGUNDA-FEIRA',[520,560],None,size=90,cor='tinta',ang=-3),nota('sem deuses?',[720,760],None,cor='laranja',size=64),tira('SÉCULO VI',[330,1000],[1,'bispo'],size=56)]),
  dict(id='c2',fonte='Fonte: Marco Neves (Univ. NOVA de Lisboa), via Xataka',frases=[f("Em espanhol, segunda é lunes. Em francês, lundi. Em italiano, lunedì.","Em espanhol, segunda é lúnes. Em francês, lã-dí. Em italiano, lunedí."),f("Todos querem dizer: dia da Lua."),f("E em espanhol, terça é de Marte, quarta de Mercúrio, quinta de Júpiter, sexta de Vênus.")],
   elementos=[tira('lunes',[260,470],[0,'lunes'],size=52),tira('lundi',[520,560],[0,'lundi'],size=52),tira('lunedì',[780,470],[0,'lunedì'],size=52),bloco('= dia da Lua',[520,760],[1,'Lua'],size=80),
     tira('martes · miércoles · jueves · viernes',[520,1050],[2,'Marte'],size=36)]),
  dict(id='c3',fonte='Fonte: Catholic Encyclopedia',frases=[f("No século 6, um bispo chamado Martinho de Dume pregava na região de Braga, hoje em Portugal.","No século seis, um bispo chamado Martinho de Dúme pregava na região de Braga, hoje em Portugal."),f("E ele achava um absurdo cristão chamar os dias pelos nomes de deuses pagãos.")],
   elementos=[tira('MARTINHO DE DUME',[520,450],None,size=52),obj('livro',[340,760],[0,'Braga'],w=320,ang=-4),tira('BRAGA',[720,700],[0,'Braga'],size=50),nota('um absurdo!',[640,1060],[1,'absurdo'],cor='laranja',size=70)]),
  dict(id='c4',fonte='Fonte: Martinho de Dume, De correctione rusticorum',frases=[f("Num sermão, ele condenou batizar os dias de Marte, Mercúrio, Júpiter, Vênus e Saturno."),f("E defendeu o jeito da Igreja: contar os dias em ordem.")],
   elementos=[tira('Marte',[260,480],[0,'Marte'],size=48),tira('Mercúrio',[560,520],[0,'Mercúrio'],size=48),tira('Júpiter',[820,600],[0,'Júpiter'],size=44),tira('Vênus',[330,640],[0,'Vênus'],size=48),tira('Saturno',[620,700],[0,'Saturno'],size=48),
     risco([180,590],[880,590],[1,'Igreja']),bloco('contar em ordem',[520,960],[1,'ordem'],size=80,cor='tinta')]),
  dict(id='c5',fonte='Fonte: Marco Neves (Univ. NOVA de Lisboa), via Xataka',frases=[f("A Igreja chamava os dias de feria: segunda feria, terceira feria..."),f("Feria, em latim, era dia de festa, dia livre."),f("Com o tempo, virou segunda-feira, terça-feira, quarta-feira."),f("Domingo é o dia do Senhor. E o sábado veio do shabat, dos hebreus.","Domingo é o dia do Senhor. E o sábado veio do xabát, dos hebreus.")],
   elementos=[verb('feria','latim, subst. fem.','dia de festa; dia livre.',[520,540],[0,'feria'],w=640),tira('segunda feria',[300,820],[0,'segunda'],size=44),seta([470,830],[580,900],[2,'virou']),bloco('segunda-feira',[640,960],[2,'segunda-feira'],size=64),
     tira('domingo = dia do Senhor',[400,1120],[3,'Domingo'],size=38)]),
  dict(id='c6',fonte='Fonte: Instituto da Lingua Galega (USC)',frases=[f("E hoje? Até o galego, o primo mais próximo do português, usa oficialmente luns e martes.","E hoje? Até o galego, o primo mais próximo do português, usa oficialmente lúns e martes."),f("Toda vez que você reclama da segunda-feira, está usando um calendário de igreja de quase 1.500 anos.","Toda vez que você reclama da segunda-feira, está usando um calendário de igreja de quase mil e quinhentos anos.")],
   elementos=[tira('GALEGO: luns, martes...',[520,460],None,size=46),obj('celular',[330,800],[1,'reclama'],w=280,ang=-4),bloco('quase\n1.500 anos',[680,820],[1,'1.500'],size=72,maxw=420)]),
  dict(id='c7',frases=[f("Então: o português trocou a Lua pela segunda por causa de um sermão."),f("Marca aquele amigo que odeia segunda-feira e manda essa história pra ele."),ASS],
   elementos=[dict(t='cal',titulo='SEGUNDA-FEIRA',inicio=0,ndias=7,pos=[520,620],ang=2,escala=0.85),bloco('marca quem odeia segunda',[520,1060],[1,'Marca'],size=64,maxw=780)])])

# ------------------------------------------------------------ 038 HISTÓRIA (01/12 · véspera da última rodada do Brasileirão)
EPS['SSA-038']=dict(materia='HISTÓRIA',titulo='Por que a última rodada começa toda no mesmo minuto',
 fontes=["The Analyst (Opta), 'The Disgrace of Gijón: West Germany v Austria, 1982'.","Mental Floss, 'The Disgrace of Gijón: the most controversial match in World Cup history'.","The National (25/06/2026), sobre Argélia e Gijón 1982.","Reuters, via Malay Mail (22/06/2024): jogos simultâneos desde a Euro de 1984.","WION: FIFA mudou a regra para a Copa de 1986.","Flashscore Brasil (06/11/2026): 38ª rodada do Brasileirão em 02/12, todos às 21h30."],
 capa=dict(elementos=[obj('relogio',[520,640],w=420,ang=-3),bloco('a culpa é de um jogo de 1982',[520,1110],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Nesta quarta, os 10 jogos do Brasileirão começam no mesmo minuto. Culpa de 1982.","Nesta quarta, os dez jogos do Brasileirão começam no mesmo minuto. Culpa de mil novecentos e oitenta e dois."),f("De um jogo que ganhou o apelido de Desgraça de Gijón.","De um jogo que ganhou o apelido de Desgraça de Rirrón.")],
   elementos=[obj('relogio',[520,620],None,w=400,balanca=True),tira('10 jogos · 21h30',[520,900],None,size=56),bloco('DESGRAÇA DE GIJÓN',[520,1100],[1,'Desgraça'],size=66,cor='tinta',ang=-3)]),
  dict(id='c2',fonte='Fonte: The National (2026); Mental Floss',frases=[f("Copa do Mundo da Espanha. A Argélia estreia vencendo a poderosa Alemanha Ocidental por 2 a 1.","Copa do Mundo da Espanha. A Argélia estreia vencendo a poderosa Alemanha Ocidental por dois a um."),f("No último jogo do grupo, bate o Chile. E fica esperando."),f("Porque Alemanha e Áustria só jogariam no dia seguinte.")],
   elementos=[tira('ESPANHA · 1982',[520,440],None,size=52),bloco('ARGÉLIA 2 x 1 ALEMANHA',[520,640],[0,'2 a 1'],size=62,maxw=800),tira('ARGÉLIA x CHILE: vitória',[520,820],[1,'Chile'],size=44),
     dict(t='cal',titulo='JUNHO 1982',inicio=1,ndias=30,riscar=[24],riscar_em=[2,'seguinte'],pos=[520,1050],escala=0.5,ang=2)]),
  dict(id='c3',fonte='Fonte: WION; The Analyst (Opta)',frases=[f("E a conta era simples: uma vitória alemã magra classificava os dois europeus e eliminava a Argélia."),f("Logo aos 10 minutos, a Alemanha fez 1 a 0.","Logo aos dez minutos, a Alemanha fez um a zero.")],
   elementos=[tira('vitória alemã magra =',[520,470],None,size=48),tira('Alemanha e Áustria: passam',[520,620],[0,'europeus'],size=48),tira('Argélia: fora',[520,760],[0,'eliminava'],size=52),num('1 x 0',[520,1020],[1,'1 a 0'],size=200),nota("10'",[820,900],[1,'10'],cor='laranja',size=72)]),
  dict(id='c4',fonte='Fonte: The Analyst (Opta); Mental Floss',frases=[f("E aí, o jogo praticamente parou."),f("No segundo tempo inteiro, foram só 2 chutes.","No segundo tempo inteiro, foram só dois chutes."),f("Narradores na Alemanha e na Áustria chegaram a pedir pro público mudar de canal.")],
   camera=dict(congela=dict(de=[0,'parou'],ate=[1,0.9])),elementos=[bloco('o jogo parou',[520,520],None,size=84,cor='tinta'),num('2',[330,820],[1,'2'],size=260),nota('chutes no 2º\ntempo inteiro',[680,820],[1,'chutes'],size=56),
     tv([520,1060],[2,'canal'],w=260)]),
  dict(id='c5',fonte='Fonte: Mental Floss',frases=[f("A Argélia protestou. Mas a FIFA disse não ter achado prova de combinação."),f("O resultado ficou. Só que a lição também ficou.")],
   elementos=[jornal('EL PAÍS','26 JUN. 1982','GIJÓN',[400,700],None,w=420,ang=-3),bloco('sem prova',[700,620],[0,'prova'],size=70,cor='tinta',ang=4),nota('mas ficou a lição',[600,1080],[1,'lição'],cor='laranja',size=62)]),
  dict(id='c6',fonte='Fonte: Reuters (2024); WION; Flashscore Brasil (06/11/2026)',frases=[f("Desde a Euro de 1984 e a Copa de 1986, as últimas rodadas de grupo são jogadas ao mesmo tempo.","Desde a Euro de mil novecentos e oitenta e quatro e a Copa de mil novecentos e oitenta e seis, as últimas rodadas de grupo são jogadas ao mesmo tempo."),f("E hoje? A ideia pegou. Nesta quarta, 2 de dezembro, os 10 jogos da última rodada do Brasileirão começam às 21h30.","E hoje? A ideia pegou. Nesta quarta, dois de dezembro, os dez jogos da última rodada do Brasileirão começam às vinte e uma e trinta.")],
   elementos=[tira('EURO 1984',[300,460],None,size=50),tira('COPA 1986',[720,520],[0,'Copa'],size=50),bloco('tudo ao mesmo tempo',[520,700],[0,'mesmo tempo'],size=68),
     obj('relogio',[330,1010],[1,'pegou'],w=260),tira('QUA 02/12 · 21h30',[680,960],[1,'21h30'],size=44),tira('10 jogos',[700,1100],[1,'10'],size=48)]),
  dict(id='c7',frases=[f("Então: 10 jogos no mesmo minuto, por causa de um 1 a 0 de 1982.","Então: dez jogos no mesmo minuto, por causa de um um a zero de mil novecentos e oitenta e dois."),f("Na sua opinião: jogo simultâneo é justiça ou exagero? Comenta."),ASS],
   elementos=[obj('relogio',[520,620],None,w=360,ang=3),bloco('justiça ou exagero?',[520,1020],[1,'justiça'],size=74),nota('comenta!',[780,1160],[1,'Comenta'],cor='laranja')])])

# ------------------------------------------------------------ 039 ARTE (02/12 · Dia Nacional do Samba)
EPS['SSA-039']=dict(materia='ARTE',titulo='O primeiro samba de sucesso foi parar no registro com um dono só',
 fontes=["Agência Brasil (27/11/2016), 'Primeiro samba faz hoje 100 anos e ganha exposição na Biblioteca Nacional'.","Jornal da USP, entrevista com o prof. José Geraldo Vinci de Moraes sobre 'Pelo Telefone'.","National Geographic Brasil (2023), 'Dia Nacional do Samba: quais são as origens'."],
 capa=dict(elementos=[radio([520,660],w=420,ang=-3),bloco('o samba era de todo mundo. O registro, de um só',[520,1130],size=60,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("O primeiro samba a fazer sucesso foi registrado como se tivesse um dono só."),f("E muita gente da época não concordou.")],
   elementos=[radio([520,640],None,w=400,ang=-3,balanca=True),bloco('um dono só?',[520,1000],None,size=84,cor='tinta'),nota('não concordaram',[620,1150],[1,'concordou'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: Agência Brasil (2016)',frases=[f("Rio de Janeiro, 1916.","Rio de Janeiro, mil novecentos e dezesseis."),f("Na casa da Tia Ciata, perto da Praça Onze, rolavam rodas de música que varavam a noite."),f("Numa dessas rodas, nasceu uma música chamada Pelo Telefone.")],
   elementos=[tira('RIO · 1916',[520,440],None,size=56),tira('casa da TIA CIATA',[520,620],[1,'Ciata'],size=50),nota('Praça Onze',[720,760],[1,'Praça'],cor='laranja',size=58),bloco('"Pelo Telefone"',[520,1020],[2,'Pelo'],size=80)]),
  dict(id='c3',fonte='Fonte: Agência Brasil (2016)',frases=[f("Em 27 de novembro de 1916, o músico Donga registrou a música na Biblioteca Nacional, como samba.","Em vinte e sete de novembro de mil novecentos e dezesseis, o músico Dônga registrou a música na Biblioteca Nacional, como samba."),f("Junto, foi uma partitura pra piano escrita à mão e assinada por Pixinguinha.")],
   elementos=[verb('samba','registro nº 3.295 · Biblioteca Nacional','"Pelo Telefone", de Donga. 27 de novembro de 1916.',[520,560],[0,'registrou'],w=700),tira('DONGA',[300,820],[0,'Donga'],size=56),
     obj('caderno',[600,1000],[1,'partitura'],w=300,ang=4),nota('Pixinguinha',[760,1160],[1,'Pixinguinha'],cor='laranja',size=56)]),
  dict(id='c4',fonte='Fonte: Jornal da USP',frases=[f("Em janeiro de 1917, a Casa Edison gravou a música.","Em janeiro de mil novecentos e dezessete, a Casa Édison gravou a música."),f("A versão cantada por Baiano estourou no Carnaval."),f("No disco, vinha escrito: samba carnavalesco.")],
   camera=dict(push=0.06),elementos=[tira('CASA EDISON · 1917',[520,450],None,size=50),radio([520,720],[0,'gravou'],w=360),tira('voz: BAIANO',[300,960],[1,'Baiano'],size=48),bloco('SAMBA CARNAVALESCO',[540,1110],[2,'samba carnavalesco'],size=60,cor='tinta')]),
  dict(id='c5',fonte='Fonte: Jornal da USP',frases=[f("Só que muita gente que frequentava a roda disse que a música era de todos, e não só do Donga.","Só que muita gente que frequentava a roda disse que a música era de todos, e não só do Dônga."),f("O sambista Sinhô resumiu assim: samba é como passarinho, é de quem pegar.")],
   elementos=[bloco('de todos?',[520,540],None,size=90),nota('ou só do Donga?',[620,740],[0,'Donga'],cor='laranja',size=60),tira('SINHÔ:',[300,920],[1,'Sinhô'],size=50),
     bloco('"samba é como passarinho, é de quem pegar"',[540,1090],[1,'passarinho'],size=52,maxw=780,cor='tinta')]),
  dict(id='c6',fonte='Fonte: Agência Brasil (2016), citando Carlos Sandroni',frases=[f("E tem mais: outros sambas já tinham sido gravados antes."),f("Só que nenhum tinha feito sucesso."),f("Por isso Pelo Telefone é chamado de o primeiro samba gravado e registrado que fez sucesso.")],
   elementos=[tira('gravados antes: sim',[520,480],None,size=48),tira('sucesso: não',[520,620],[1,'sucesso'],size=48),risco([380,620],[660,620],[1,'nenhum']),bloco('o 1º samba\nde sucesso',[520,950],[2,'primeiro'],size=80,maxw=700)]),
  dict(id='c7',fonte='Fonte: National Geographic Brasil (2023)',frases=[f("E hoje, 2 de dezembro, é Dia Nacional do Samba.","E hoje, dois de dezembro, é Dia Nacional do Samba."),f("Mais de um século depois, a briga pela autoria do Pelo Telefone ainda aparece nos livros de música.")],
   elementos=[dict(t='cal',titulo='DEZEMBRO',inicio=2,ndias=31,riscar=[2],riscar_em=[0,'2 de'],pos=[520,640],escala=0.7,ang=-2),bloco('DIA NACIONAL DO SAMBA',[520,1050],[0,'Dia'],size=62,maxw=800)]),
  dict(id='c8',frases=[f("Então: o primeiro samba de sucesso nasceu de muita gente, e foi registrado por um."),f("Salva esse pra contar na próxima roda de samba."),ASS],
   elementos=[radio([520,620],None,w=340,ang=3),bloco('nasceu de muitos,\nregistrado por um',[520,1000],[0,'registrado'],size=62,maxw=760),nota('salva esse!',[740,1170],[1,'Salva'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 040 MATEMÁTICA (02/12 · noite da última rodada)
EPS['SSA-040']=dict(materia='MATEMÁTICA',titulo='Bastam 23 pessoas pra ter 50% de chance de aniversário repetido',
 fontes=["Scientific American, 'Probability and the Birthday Paradox'.","Live Science, 'What is the birthday paradox?'.","Cálculo exato com 365 dias igualmente prováveis: 23 pessoas = 50,7%; 30 = 70,6%; 57 = 99,0%.","Flashscore Brasil (06/11/2026): 38ª rodada do Brasileirão em 02/12, todos às 21h30."],
 capa=dict(elementos=[num('23',[520,640],size=360),bloco('pessoas = 50% de chance',[520,1080],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Bastam 23 pessoas pra ter 50% de chance de dois aniversários iguais.","Bastam vinte e três pessoas pra ter cinquenta por cento de chance de dois aniversários iguais."),f("Parece pouco? A matemática diz que não.")],
   elementos=[num('23',[520,620],None,size=340),bloco('= 50% de chance',[520,960],None,size=80),nota('parece pouco?',[700,1130],[1,'pouco'],cor='laranja',size=60)]),
  dict(id='c2',frases=[f("O ano tem 365 dias. Então a intuição diz: precisa de muita gente.","O ano tem trezentos e sessenta e cinco dias. Então a intuição diz: precisa de muita gente."),f("Tipo, umas 180 pessoas.","Tipo, umas cento e oitenta pessoas."),f("Mas a intuição está olhando pro lugar errado.")],
   elementos=[dict(t='cal',titulo='365 DIAS',inicio=3,ndias=31,pos=[520,620],escala=0.7,ang=-3),tira('intuição: ~180 pessoas',[520,960],[1,'180'],size=46),risco([300,960],[740,960],[2,'errado'])]),
  dict(id='c3',fonte='Fonte: Scientific American',frases=[f("Você não está comparando só você com os outros."),f("Está comparando todo mundo com todo mundo."),f("Com 23 pessoas, isso dá 253 pares.","Com vinte e três pessoas, isso dá duzentos e cinquenta e três pares.")],
   elementos=[tira('você x os outros',[520,460],None,size=48),risco([330,460],[710,460],[1,'todo mundo']),bloco('todo mundo x todo mundo',[520,660],[1,'todo'],size=60,maxw=780),
     dict(t='contador',de=0,ate=253,fmt='{n} pares',pos=[520,980],e=[2,'253'],size=96)]),
  dict(id='c4',fonte='Fonte: Live Science',frases=[f("E cada par é uma nova chance de coincidência."),f("A conta exata dá 50,7%.","A conta exata dá cinquenta vírgula sete por cento.")],
   camera=dict(push=0.05,zooms=[dict(e=[1,'50,7'],escala=1.15,alvo=[520,900],dur=0.7)]),elementos=[nota('cada par =\numa chance',[520,560],None,size=66),num('50,7%',[520,900],[1,'50,7'],size=220)]),
  dict(id='c5',fonte='Fonte: Live Science; cálculo com 365 dias',frases=[f("Com 30 pessoas, a chance passa de 70%.","Com trinta pessoas, a chance passa de setenta por cento."),f("Com 57, chega a 99%. Quase certeza.","Com cinquenta e sete, chega a noventa e nove por cento. Quase certeza.")],
   elementos=[tira('23 pessoas · 50%',[520,480],None,size=50),tira('30 pessoas · 70%',[520,640],[0,'30'],size=50),tira('57 pessoas · 99%',[520,800],[1,'57'],size=50),bloco('quase certeza',[520,1040],[1,'certeza'],size=80,cor='tinta')]),
  dict(id='c6',frases=[f("E hoje? Olha a última rodada do Brasileirão, hoje à noite."),f("Em cada jogo, 22 jogadores mais o árbitro são 23 pessoas.","Em cada jogo, vinte e dois jogadores mais o árbitro são vinte e três pessoas."),f("Pela matemática, em mais ou menos metade dos 10 jogos, duas pessoas em campo fazem aniversário no mesmo dia.","Pela matemática, em mais ou menos metade dos dez jogos, duas pessoas em campo fazem aniversário no mesmo dia.")],
   elementos=[tv([520,600],None,w=380),tira('22 jogadores + 1 árbitro',[520,880],[1,'árbitro'],size=44),num('23',[300,1060],[1,'23'],size=150),nota('em ~metade\ndos jogos!',[680,1070],[2,'metade'],cor='laranja',size=58)]),
  dict(id='c7',frases=[f("Então: 23 pessoas, 50% de chance.","Então: vinte e três pessoas, cinquenta por cento de chance."),f("Faz o teste no grupo da sua turma e conta aqui se deu coincidência."),ASS],
   elementos=[num('23',[520,620],None,size=320),bloco('faz o teste\nna sua turma',[520,1020],[1,'teste'],size=64,maxw=700),nota('conta aqui!',[760,1170],[1,'conta'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 041 LITERATURA (03/12 · 100 anos do sumiço de Agatha Christie)
EPS['SSA-041']=dict(materia='LITERATURA',titulo='Há 100 anos, Agatha Christie sumiu por 11 dias',
 fontes=["The National Archives (Reino Unido), '20s People: investigating the strange disappearance of Mrs Agatha Christie'.","National Geographic, 'The mystery of Agatha Christie's disappearance'.","BBC Countryfile, 'Agatha Christie's disappearance'.","Leeds Mercury (21/12/1926): Arthur Conan Doyle e a luva levada a um médium.","Guinness World Records, 'Best-selling author for fiction'."],
 capa=dict(elementos=[jornal('DAILY MAIL','DEZ. 1926','MRS. CHRISTIE MISSING',[520,740],w=460,ang=-3),num('11',[790,470],size=220),tira('dias',[790,640],size=50)]),
 cenas=[
  dict(id='c1',frases=[f("Há exatos 100 anos, a escritora mais vendida do mundo sumiu sem deixar explicação.","Há exatos cem anos, a escritora mais vendida do mundo sumiu sem deixar explicação."),f("Foram 11 dias.","Foram onze dias.")],
   elementos=[jornal('DAILY MAIL','DEZ. 1926','MRS. CHRISTIE MISSING',[430,700],None,w=440,ang=-3,balanca=True),num('11',[760,1020],[1,'11'],size=240),tira('dias',[760,1180],[1,'dias'],size=46)]),
  dict(id='c2',fonte='Fonte: National Archives (UK); National Geographic',frases=[f("Inglaterra, noite de 3 de dezembro de 1926.","Inglaterra, noite de três de dezembro de mil novecentos e vinte e seis."),f("Agatha Christie, então com 36 anos, sai de casa de carro, sem dizer pra onde.","Ágata Crísti, então com trinta e seis anos, sai de casa de carro, sem dizer pra onde.")],
   elementos=[tira('03/12/1926 · NOITE',[520,450],None,size=50),bloco('AGATHA CHRISTIE, 36',[520,660],[1,'Agatha'],size=66,cor='tinta'),nota('pra onde?',[700,880],[1,'onde'],cor='laranja',size=70)]),
  dict(id='c3',fonte='Fonte: National Archives (UK); National Geographic',frases=[f("Na manhã seguinte, o carro é achado abandonado numa colina chamada Newlands Corner.","Na manhã seguinte, o carro é achado abandonado numa colina chamada Niúlands Córner."),f("Com os faróis acesos, uma mala e um casaco de pele lá dentro.")],
   elementos=[tira('NEWLANDS CORNER',[520,450],None,size=50),bloco('carro abandonado',[520,650],[0,'abandonado'],size=74),tira('faróis acesos',[330,880],[1,'faróis'],size=46),tira('mala',[700,960],[1,'mala'],size=46),tira('casaco de pele',[440,1080],[1,'casaco'],size=46)]),
  dict(id='c4',fonte='Fonte: BBC Countryfile; Leeds Mercury (21/12/1926)',frases=[f("Começa uma das maiores buscas da história da Inglaterra."),f("Segundo relatos da época, mais de mil policiais, milhares de voluntários e até aviões."),f("Arthur Conan Doyle, o criador do Sherlock Holmes, levou uma luva dela a um médium.","Ártur Cônan Dóil, o criador do Xérloque Rômes, levou uma luva dela a um médium.")],
   camera=dict(push=0.05),elementos=[bloco('A GRANDE BUSCA',[520,470],None,size=76,cor='tinta'),dict(t='contador',de=0,ate=1000,fmt='+{n} policiais',pos=[520,660],e=[1,'mil'],size=64),
     tira('milhares de voluntários',[520,800],[1,'voluntários'],size=44),tira('CONAN DOYLE',[330,980],[2,'Conan'],size=50),nota('uma luva\nao médium',[700,1060],[2,'luva'],cor='laranja',size=58)]),
  dict(id='c5',fonte='Fonte: National Geographic; National Archives (UK)',frases=[f("11 dias depois, ela é encontrada num hotel em Harrogate, a uns 350 quilômetros dali.","Onze dias depois, ela é encontrada num hotel em Rárrogueit, a uns trezentos e cinquenta quilômetros dali."),f("Hospedada com outro nome, como se tivesse vindo da África do Sul.")],
   elementos=[tira('HARROGATE · HOTEL',[520,450],None,size=50),num('350 km',[520,680],[0,'350'],size=170),bloco('outro nome',[400,960],[1,'nome'],size=78,cor='tinta',ang=-4),nota('"da África do Sul"',[640,1120],[1,'África'],cor='laranja',size=56)]),
  dict(id='c6',fonte='Fonte: National Archives (UK); National Geographic',frases=[f("Ela nunca contou o que fez nesses 11 dias.","Ela nunca contou o que fez nesses onze dias."),f("Na autobiografia, só escreveu que, pela primeira vez na vida, estava realmente doente.")],
   elementos=[obj('livro',[520,640],None,w=380,ang=-3),bloco('nunca contou',[520,960],[0,'nunca'],size=86),nota('"realmente doente"',[600,1130],[1,'doente'],cor='laranja',size=58)]),
  dict(id='c7',fonte='Fonte: Guinness World Records',frases=[f("E hoje? O Guinness estima que os livros dela venderam uns 2 bilhões de cópias.","E hoje? O Guinness estima que os livros dela venderam uns dois bilhões de cópias."),f("Mas o mistério mais famoso dela não está em nenhum livro.")],
   elementos=[dict(t='contador',de=0,ate=2,fmt='{n} bilhões de livros',pos=[520,560],e=[0,'bilhões'],size=74),obj('livro',[520,860],None,w=300,ang=4),nota('em nenhum livro',[600,1120],[1,'nenhum'],cor='laranja',size=60)]),
  dict(id='c8',frases=[f("Então: 100 anos depois, ninguém sabe o que aconteceu naqueles 11 dias.","Então: cem anos depois, ninguém sabe o que aconteceu naqueles onze dias."),f("Se fosse um livro dela, qual seria o final? Comenta sua teoria."),ASS],
   elementos=[num('11',[520,620],None,size=320),bloco('qual seria o final?',[520,1000],[1,'final'],size=70),nota('comenta sua teoria',[640,1160],[1,'teoria'],cor='laranja',size=54)])])

# ------------------------------------------------------------ 042 HISTÓRIA (03/12 · Dia Internacional das Pessoas com Deficiência)
EPS['SSA-042']=dict(materia='HISTÓRIA',titulo='O braille foi criado por um garoto de 15 anos',
 fontes=["Encyclopaedia Britannica, 'Louis Braille' e 'Braille (writing system)'.","Musée Louis Braille (Coupvray), 'Barbier, l'intuitif'.","National Geographic, 'Louis Braille, creator of the writing system'.","PBS NewsHour, 'Inventor Louis Braille touched lives with literacy'.","ONU/DESA, 'International Day of Persons with Disabilities, 3 December' (res. 47/3, 1992).","Anvisa, RDC nº 71/2009 (nome do medicamento em braille na embalagem)."],
 capa=dict(elementos=[num('15',[330,560],size=280),obj('livro',[650,720],w=380,ang=4),bloco('anos: a idade do inventor do braille',[520,1130],size=64,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("O sistema que permite cegos lerem foi criado por um garoto de 15 anos.","O sistema que permite cegos lerem foi criado por um garoto de quinze anos."),f("E a ideia começou com um código pra ler no escuro.")],
   elementos=[num('15',[330,620],None,size=300),tira('anos',[330,850],None,size=50),obj('livro',[690,700],None,w=340,ang=4,balanca=True),nota('ler no escuro',[560,1100],[1,'escuro'],cor='laranja',size=64)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica',frases=[f("França, 1812. Louis Braille, de 3 anos, brincava na oficina do pai, que fazia selas.","França, mil oitocentos e doze. Luí Brái, de três anos, brincava na oficina do pai, que fazia selas."),f("Uma ferramenta escorregou e feriu um olho dele."),f("Veio uma infecção, e ele perdeu a visão dos dois olhos.")],
   elementos=[tira('FRANÇA · 1812',[520,440],None,size=52),bloco('LOUIS BRAILLE, 3 ANOS',[520,640],[0,'Louis'],size=62,cor='tinta'),nota('a oficina do pai',[560,820],[0,'oficina'],size=58),
     tira('uma ferramenta escorregou',[520,980],[1,'ferramenta'],size=44),nota('perdeu a visão',[620,1140],[2,'perdeu'],cor='laranja',size=60)]),
  dict(id='c3',fonte='Fonte: Musée Louis Braille; National Geographic',frases=[f("Aos 10 anos, foi estudar num instituto pra jovens cegos, em Paris.","Aos dez anos, foi estudar num instituto pra jovens cegos, em Paris."),f("Em 1821, um ex-oficial de artilharia, Charles Barbier, levou à escola um código de pontos em relevo.","Em mil oitocentos e vinte e um, um ex-oficial de artilharia, Charl Barbiê, levou à escola um código de pontos em relevo."),f("Era pensado pra ler mensagens sem luz, e o Exército não quis.")],
   elementos=[tira('PARIS · 1819',[300,450],None,size=48),tira('CHARLES BARBIER · 1821',[560,600],[1,'Barbier'],size=46),bloco('pontos em relevo',[520,800],[1,'relevo'],size=74),
     nota('pra ler sem luz',[400,1000],[2,'luz'],size=58),bloco('EXÉRCITO: NÃO',[640,1130],[2,'Exército'],size=56,cor='tinta',ang=3)]),
  dict(id='c4',fonte='Fonte: National Geographic; Musée Louis Braille',frases=[f("Só que o código tinha um problema: cada sinal tinha até 12 pontos, e representava sons, não letras.","Só que o código tinha um problema: cada sinal tinha até doze pontos, e representava sons, não letras."),f("Não dava pra soletrar direito, nem pontuar.")],
   elementos=[num('12',[330,640],None,size=260),tira('pontos por sinal',[330,860],[0,'pontos'],size=44),tira('sons, não letras',[700,620],[0,'sons'],size=46),bloco('sem soletrar,\nsem pontuar',[620,1040],[1,'soletrar'],size=60,maxw=640,cor='tinta')]),
  dict(id='c5',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Braille simplificou: 6 pontos, em duas colunas de 3.","Brái simplificou: seis pontos, em duas colunas de três."),f("Cabia na ponta de um dedo, e dava 63 combinações: letras, números, pontuação e até música.","Cabia na ponta de um dedo, e dava sessenta e três combinações: letras, números, pontuação e até música."),f("Ele apresentou o sistema aos 15 anos, em 1824.","Ele apresentou o sistema aos quinze anos, em mil oitocentos e vinte e quatro.")],
   camera=dict(push=0.06),elementos=[num('6',[300,640],None,size=300),tira('pontos · 2 colunas de 3',[640,560],[0,'colunas'],size=40),dict(t='contador',de=0,ate=63,fmt='{n} combinações',pos=[620,780],e=[1,'63'],size=64),
     tira('letras · números · música',[520,960],[1,'música'],size=42),bloco('1824 · 15 ANOS',[520,1110],[2,'1824'],size=66,cor='tinta')]),
  dict(id='c6',fonte='Fonte: National Geographic; PBS NewsHour',frases=[f("Mas a invenção demorou a pegar. Um diretor da escola chegou a proibir o sistema e queimar livros em braille."),f("A escola só adotou oficialmente o braille em 1854, 2 anos depois da morte dele.","A escola só adotou oficialmente o braille em mil oitocentos e cinquenta e quatro, dois anos depois da morte dele.")],
   elementos=[bloco('PROIBIDO',[520,520],[0,'proibir'],size=96,cor='tinta',ang=-4),nota('livros queimados',[560,720],[0,'queimar'],cor='laranja',size=60),tira('adotado em 1854',[520,940],[1,'1854'],size=52),nota('2 anos depois\nda morte dele',[600,1110],[1,'morte'],size=54)]),
  dict(id='c7',fonte='Fonte: ONU/DESA; Anvisa, RDC 71/2009',frases=[f("E hoje, 3 de dezembro, é o Dia Internacional das Pessoas com Deficiência, criado pela ONU em 1992.","E hoje, três de dezembro, é o Dia Internacional das Pessoas com Deficiência, criado pela ONU em mil novecentos e noventa e dois."),f("Repara na caixa de remédio: no Brasil, o nome do medicamento tem que vir em braille.")],
   elementos=[tira('ONU · 3 DE DEZEMBRO',[520,450],None,size=50),bloco('Dia Internacional das Pessoas com Deficiência',[520,660],[0,'Dia'],size=54,maxw=800),obj('frasco',[330,980],[1,'remédio'],w=240),nota('nome em braille',[680,1000],[1,'braille'],cor='laranja',size=58)]),
  dict(id='c8',frases=[f("Então: um código rejeitado pelo Exército virou, nas mãos de um garoto de 15 anos, leitura pra milhões de pessoas.","Então: um código rejeitado pelo Exército virou, nas mãos de um garoto de quinze anos, leitura pra milhões de pessoas."),f("Agora você sabe de onde vêm aqueles pontinhos."),ASS],
   elementos=[num('15',[330,620],None,size=280),obj('livro',[690,700],None,w=320,ang=-3),bloco('agora você sabe\nde onde vêm os pontinhos',[520,1060],[1,'pontinhos'],size=56,maxw=780)])])

# ------------------------------------------------------------ 043 SOCIOLOGIA (04/12 · Dia Internacional dos Bancos)
EPS['SSA-043']=dict(materia='SOCIOLOGIA',titulo='O dinheiro de papel nasceu na China (e só vale porque a gente acredita)',
 fontes=["Springer, Encyclopedia (verbete 'Jiaozi [Paper Money]').","Deutsche Bundesbank, 'The secret of the alchemists' (coleção de cédulas).","Fitzwilliam Museum / Univ. de Cambridge: Marco Polo e o papel-moeda de Kublai Khan.","Banco Central do Brasil, 'Origem e evolução do dinheiro'.","Banco de España, '¿Cuál es el origen del dinero?'.","ONU, resolução 74/245 (2019): Dia Internacional dos Bancos, 4 de dezembro."],
 capa=dict(elementos=[jornal('JIAOZI','SICHUAN · SÉC. XI','PAPEL QUE VIROU DINHEIRO',[520,740],w=460,ang=-3),bloco('por que um papel vale alguma coisa?',[520,1150],size=62,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Uma nota de dinheiro é só papel. Então por que ela vale alguma coisa?"),f("A resposta começou na China, há uns mil anos.")],
   elementos=[jornal('JIAOZI','SICHUAN · SÉC. XI','PAPEL QUE VIROU DINHEIRO',[520,700],None,w=440,ang=-3,balanca=True),bloco('só papel?',[700,1060],None,size=84,cor='tinta',ang=4),tira('CHINA · ~1000 ANOS',[330,1160],[1,'China'],size=42)]),
  dict(id='c2',fonte='Fonte: Springer, verbete "Jiaozi"',frases=[f("Século 11, região de Sichuan, na China.","Século onze, região de Sê-tchuán, na China."),f("Lá, as moedas eram de ferro. E mil moedas pesavam uns 12 quilos e meio.","Lá, as moedas eram de ferro. E mil moedas pesavam uns doze quilos e meio."),f("Pra comprar uma peça de seda, você precisava carregar de 45 a 50 quilos de moeda.","Pra comprar uma peça de seda, você precisava carregar de quarenta e cinco a cinquenta quilos de moeda.")],
   elementos=[tira('SICHUAN · SÉCULO XI',[520,450],None,size=50),bloco('moedas de ferro',[520,620],[1,'ferro'],size=72,cor='tinta'),num('12,5 kg',[520,830],[1,'12'],size=150),tira('= 1.000 moedas',[520,980],[1,'mil'],size=44),nota('seda = 45 a 50 kg!',[580,1120],[2,'seda'],cor='laranja',size=58)]),
  dict(id='c3',fonte='Fonte: Springer, verbete "Jiaozi"',frases=[f("Então, comerciantes começaram a guardar o ferro e a entregar recibos de papel."),f("Quem tinha o recibo podia trocar pelo ferro depois."),f("Esses papéis se chamavam jiaozi.","Esses papéis se chamavam tchiáu-dzi.")],
   elementos=[tira('ferro guardado',[330,480],None,size=48),seta([480,500],[620,600],[0,'recibos']),bloco('recibo de papel',[660,660],[0,'recibos'],size=60),nota('troca depois',[400,880],[1,'trocar'],size=58),verb('jiaozi','chinês, séc. XI','recibo de papel que circulava no lugar das moedas de ferro.',[560,1060],[2,'jiaozi'],w=620)]),
  dict(id='c4',fonte='Fonte: Deutsche Bundesbank; Springer',frases=[f("Em 1024, o governo da dinastia Song assumiu o negócio e lançou as primeiras notas oficiais.","Em mil e vinte e quatro, o governo da dinastia Sung assumiu o negócio e lançou as primeiras notas oficiais."),f("Era o primeiro papel-moeda emitido por um governo."),f("E também veio o primeiro problema: imprimiram demais, e as notas perderam valor.")],
   elementos=[tira('DINASTIA SONG · 1024',[520,450],None,size=50),bloco('1º papel-moeda\nde um governo',[520,690],[1,'governo'],size=70,maxw=720),bloco('imprimiram demais',[520,960],[2,'demais'],size=66,cor='tinta',ang=-3),nota('perdeu valor',[660,1120],[2,'valor'],cor='laranja',size=60)]),
  dict(id='c5',fonte='Fonte: Bundesbank; Fitzwilliam Museum',frases=[f("Séculos depois, Marco Polo viu o papel-moeda na China e ficou espantado."),f("Escreveu que o imperador tinha o segredo dos alquimistas: a arte de produzir dinheiro.")],
   elementos=[tira('MARCO POLO',[520,460],None,size=56),obj('livro',[330,760],[0,'espantado'],w=300,ang=-5),nota('espantado!',[700,640],[0,'espantado'],cor='laranja',size=64),bloco('"o segredo dos alquimistas"',[540,1040],[1,'alquimistas'],size=60,maxw=760)]),
  dict(id='c6',fonte='Fonte: Banco Central do Brasil; Banco de España',frases=[f("Pro Banco Central do Brasil, o dinheiro não vale por si mesmo, e sim pelo que ele pode comprar."),f("O Banco da Espanha fala em dinheiro baseado na confiança."),f("Ou seja: uma nota vale porque todo mundo combina que ela vale.")],
   elementos=[bloco('não vale por si',[520,500],[0,'si'],size=74,cor='tinta'),tira('vale pelo que compra',[520,670],[0,'comprar'],size=46),bloco('CONFIANÇA',[520,880],[1,'confiança'],size=100),nota('todo mundo combina',[600,1100],[2,'combina'],cor='laranja',size=60)]),
  dict(id='c7',fonte='Fonte: ONU, resolução 74/245 (2019)',frases=[f("E hoje, 4 de dezembro, é o Dia Internacional dos Bancos, criado pela ONU em 2019.","E hoje, quatro de dezembro, é o Dia Internacional dos Bancos, criado pela ONU em dois mil e dezenove."),f("E pra muita gente, o dinheiro já nem é papel: virou um número na tela do celular.")],
   elementos=[tira('ONU · 4 DE DEZEMBRO',[520,450],None,size=50),bloco('Dia Internacional dos Bancos',[520,640],[0,'Bancos'],size=62,maxw=780),obj('celular',[520,950],[1,'celular'],w=280,ang=-4)]),
  dict(id='c8',frases=[f("Então: uma nota vale porque a gente acredita nela."),f("Se amanhã ninguém aceitasse mais dinheiro, o que você usaria pra pagar as coisas?"),ASS],
   elementos=[jornal('JIAOZI','SICHUAN · SÉC. XI','PAPEL QUE VIROU DINHEIRO',[520,680],None,w=420,ang=2),bloco('o que você usaria?',[520,1080],[1,'usaria'],size=72)])])

# ------------------------------------------------------------ 044 QUÍMICA
EPS['SSA-044']=dict(materia='QUÍMICA',titulo='Por que a cebola faz você chorar',
 fontes=["IMAI, S. et al. 'An onion enzyme that makes the eyes water'. Nature 419, 685 (2002).","Library of Congress, 'Why does chopping an onion make you cry?' (Everyday Mysteries).","The Conversation, 'Monday's medical myth: chewing gum stops onion tears'.","FoodNavigator (14/01/2022): cebolas Sunions, obtidas por cruzamento, chegam ao Reino Unido."],
 capa=dict(elementos=[obj('frasco',[520,640],w=360,ang=-4),bloco('a cebola solta um gás no seu olho',[520,1110],size=68,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Cortar cebola faz você chorar porque ela solta um gás no ar."),f("E existe uma enzima só pra fabricar ele.")],
   elementos=[obj('frasco',[520,620],None,w=340,ang=-4,balanca=True),bloco('um gás no ar',[520,960],None,size=86,cor='tinta'),nota('uma enzima só pra isso',[560,1130],[1,'enzima'],cor='laranja',size=56)]),
  dict(id='c2',fonte='Fonte: Library of Congress',frases=[f("Dentro das células da cebola, algumas substâncias ficam guardadas separadas."),f("Quando a faca rompe as células, elas se misturam."),f("E começa uma reação química em cadeia.")],
   elementos=[tira('dentro da célula: separado',[520,460],None,size=44),bloco('a faca rompe',[520,680],[1,'faca'],size=80),seta([300,860],[740,860],[1,'misturam']),bloco('REAÇÃO EM CADEIA',[520,1060],[2,'reação'],size=64,cor='tinta')]),
  dict(id='c3',fonte='Fonte: Library of Congress; Nature (2002)',frases=[f("Primeiro, uma enzima transforma compostos de enxofre em ácidos."),f("Aí entra uma segunda enzima, descoberta em 2002 por cientistas japoneses.","Aí entra uma segunda enzima, descoberta em dois mil e dois por cientistas japoneses."),f("O nome dela é fator lacrimogêneo sintase. É ela que fabrica o gás.")],
   elementos=[tira('1ª enzima: enxofre vira ácido',[520,450],None,size=42),tira('NATURE · 2002',[520,620],[1,'2002'],size=50),verb('fator lacrimogêneo sintase','enzima · Nature, 2002','fabrica o gás que faz os olhos lacrimejarem.',[520,900],[2,'fator'],w=700)]),
  dict(id='c4',fonte='Fonte: Library of Congress',frases=[f("O gás tem um nome complicado: syn-propanotial-S-óxido.","O gás tem um nome complicado: sin propanotiál ésse óxido."),f("Ele voa até o seu olho, e os nervos sentem a irritação."),f("Aí as glândulas soltam lágrima pra lavar o olho.")],
   camera=dict(push=0.06),elementos=[bloco('syn-propanotial-S-óxido',[520,500],None,size=56,maxw=800,cor='tinta'),seta([300,700],[700,780],[1,'voa']),nota('irritação!',[700,880],[1,'irritação'],cor='laranja',size=66),bloco('LÁGRIMA',[480,1070],[2,'lágrima'],size=96)]),
  dict(id='c5',fonte='Fonte: The Conversation',frases=[f("E mascar chiclete não adianta: o gatilho está no olho, não na boca."),f("O que ajuda é cebola gelada, faca bem afiada, e uma janela aberta ou exaustor ligado.")],
   elementos=[bloco('chiclete: mito',[520,500],None,size=76,cor='tinta',ang=-3),risco([290,500],[750,500],[0,'adianta']),tira('cebola gelada',[330,750],[1,'gelada'],size=48),tira('faca afiada',[700,850],[1,'afiada'],size=48),tira('janela ou exaustor',[430,980],[1,'janela'],size=48)]),
  dict(id='c6',fonte='Fonte: FoodNavigator (2022)',frases=[f("E hoje? Já existe cebola que quase não faz chorar."),f("Ela se chama Sunions, foi criada por cruzamento, sem mexer no gene, e já é vendida nos Estados Unidos e no Reino Unido.","Ela se chama Sân-iôns, foi criada por cruzamento, sem mexer no gene, e já é vendida nos Estados Unidos e no Reino Unido.")],
   elementos=[bloco('cebola sem lágrima',[520,520],None,size=72),tira('SUNIONS',[520,720],[1,'Sunions'],size=60),tira('cruzamento natural',[330,900],[1,'cruzamento'],size=44),tira('EUA · Reino Unido',[680,1040],[1,'Reino'],size=46)]),
  dict(id='c7',frases=[f("Então: a lágrima da cebola é química pura, com gás e enzima própria."),f("Já chorou cortando cebola na frente de alguém, e a pessoa achou que era de verdade?"),ASS],
   elementos=[obj('frasco',[520,620],None,w=320,ang=3),bloco('química pura',[520,960],[0,'química'],size=80,cor='tinta'),nota('já te aconteceu?',[640,1140],[1,'chorou'],cor='laranja',size=58)])])

# ------------------------------------------------------------ 045 ARTE (05/12 · 100 anos da morte de Monet)
EPS['SSA-045']=dict(materia='ARTE',titulo='Monet pintou os últimos quadros quase sem ver as cores',
 fontes=["Encyclopaedia Britannica, 'Claude Monet'.","GRUENER, A. 'The effect of cataracts and cataract surgery on Claude Monet'. British Journal of General Practice, 2015;65(634):254.","Hektoen International, 'Monet and his cataracts' (2017).","Musée Marmottan Monet, 'Le pont japonais' (1918–1924).","Musée de l'Orangerie, 'Les Nymphéas'."],
 capa=dict(elementos=[dict(t='obj',nome='moldura',pos=[520,680],w=520,h=600,ang=-3),bloco('pintando sem ver as cores',[520,1150],size=68,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Nos últimos anos, Monet pintava cores que ele mesmo não enxergava direito.","Nos últimos anos, Monê pintava cores que ele mesmo não enxergava direito."),f("E há exatos 100 anos, ele morreu.","E há exatos cem anos, ele morreu.")],
   elementos=[obj('moldura',[520,690],None,w=480,h=560,ang=-3,balanca=True),nota('cores que\nnão via',[760,460],None,cor='laranja',size=60),tira('05/12/1926',[520,1110],[1,'100'],size=56)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Claude Monet foi um dos criadores do impressionismo.","Clôd Monê foi um dos criadores do impressionismo."),f("No jardim da casa dele, em Giverny, pintou o lago, as ninfeias e a ponte japonesa dezenas de vezes.","No jardim da casa dele, em Jivêrní, pintou o lago, as ninfeias e a ponte japonesa dezenas de vezes.")],
   elementos=[tira('CLAUDE MONET · 1840–1926',[520,450],None,size=46),bloco('IMPRESSIONISMO',[520,620],[0,'impressionismo'],size=74,cor='tinta'),tira('GIVERNY',[300,820],[1,'Giverny'],size=52),obj('arvore',[700,950],[1,'jardim'],w=280),nota('dezenas de vezes',[400,1110],[1,'dezenas'],cor='laranja',size=58)]),
  dict(id='c3',fonte='Fonte: Hektoen International (2017)',frases=[f("Por volta de 1912, com 72 anos, veio o diagnóstico: catarata nos dois olhos.","Por volta de mil novecentos e doze, com setenta e dois anos, veio o diagnóstico: catarata nos dois olhos."),f("A catarata deixa a lente do olho turva e amarelada.")],
   elementos=[tira('~1912 · 72 ANOS',[520,450],None,size=52),bloco('CATARATA',[520,660],[0,'catarata'],size=110,cor='tinta'),nota('nos dois olhos',[640,840],[0,'dois'],cor='laranja',size=60),tira('lente turva e amarelada',[520,1040],[1,'amarelada'],size=46)]),
  dict(id='c4',fonte='Fonte: British Journal of General Practice (2015)',frases=[f("Ele mesmo escreveu que as cores já não tinham a mesma intensidade."),f("O vermelho parecia lamacento. E a pintura ficava cada vez mais escura.")],
   camera=dict(push=0.06),elementos=[obj('moldura',[520,680],None,w=460,h=530),nota('"as cores já não tinham\na mesma intensidade"',[520,1080],[0,'intensidade'],size=50),bloco('vermelho lamacento',[520,420+40],[1,'lamacento'],size=60,cor='tinta',ang=-3)]),
  dict(id='c5',fonte='Fonte: Musée Marmottan Monet',frases=[f("Compara as pontes japonesas claras e verdes da virada do século com as de 1918 a 1924: quase abstratas, cheias de vermelho e marrom.","Compara as pontes japonesas claras e verdes da virada do século com as de mil novecentos e dezoito a mil novecentos e vinte e quatro: quase abstratas, cheias de vermelho e marrom."),f("O Museu Marmottan diz que essas telas refletem a visão afetada pela catarata.","O Museu Marmotã diz que essas telas refletem a visão afetada pela catarata.")],
   elementos=[tira('~1899: claro e verde',[300,470],None,size=44),tira('1918–1924: vermelho e marrom',[600,600],[0,'1918'],size=40),obj('moldura',[520,850],[0,'abstratas'],w=380,h=380,ang=3),bloco('a visão na tela',[520,1120],[1,'visão'],size=66,cor='tinta')]),
  dict(id='c6',fonte='Fonte: British Journal of General Practice (2015)',frases=[f("Em 1923, aos 82 anos, ele operou um dos olhos.","Em mil novecentos e vinte e três, aos oitenta e dois anos, ele operou um dos olhos."),f("E depois da cirurgia, ao ver as cores de verdade, chegou a destruir telas que tinha pintado antes.")],
   elementos=[tira('1923 · 82 ANOS',[520,460],None,size=52),bloco('cirurgia',[520,640],[0,'operou'],size=84),bloco('telas destruídas',[520,950],[1,'destruir'],size=72,cor='tinta',ang=-4),nota('ao ver as cores reais',[600,1130],[1,'verdade'],cor='laranja',size=54)]),
  dict(id='c7',fonte="Fonte: Musée de l'Orangerie",frases=[f("E hoje? As Ninfeias gigantes que ele doou à França estão no Museu da Orangerie, em Paris.","E hoje? As Ninfeias gigantes que ele doou à França estão no Museu da Oranjerrí, em Paris."),f("Foram inauguradas em 1927, meses depois da morte dele.","Foram inauguradas em mil novecentos e vinte e sete, meses depois da morte dele.")],
   elementos=[tira("MUSÉE DE L'ORANGERIE",[520,450],None,size=46),obj('moldura',[520,720],[0,'Ninfeias'],w=600,h=300),tira('inauguradas em 1927',[520,980],[1,'1927'],size=48),nota('meses depois',[640,1120],[1,'meses'],cor='laranja',size=58)]),
  dict(id='c8',frases=[f("Então: as últimas telas do Monet mostram também como o olho dele via o mundo.","Então: as últimas telas do Monê mostram também como o olho dele via o mundo."),f("Salva esse pra lembrar da catarata na próxima vez que vir um Monet escuro.","Salva esse pra lembrar da catarata na próxima vez que vir um Monê escuro."),ASS],
   elementos=[obj('moldura',[520,640],None,w=440,h=500,ang=2),bloco('a tela mostra\no olho do pintor',[520,1030],[0,'olho'],size=60,maxw=740),nota('salva esse!',[760,1170],[1,'Salva'],cor='laranja',size=54)])])

# ------------------------------------------------------------ 046 BIOLOGIA (05/12 · Dia Mundial do Solo)
EPS['SSA-046']=dict(materia='BIOLOGIA',titulo='Uma colher de terra tem mais seres vivos que gente no planeta',
 fontes=["FAO, 'World Soil Day' (página oficial).","FAO Stories: 'There are more living organisms in a tablespoon of soil than there are people on Earth'.","ANTHONY, M. et al. PNAS (2023), via Yale Environment 360: solo abriga ~59% das espécies.","InforMEA/ONU: história do Dia Mundial do Solo (IUSS 2002, ONU 2013).","ONU: população mundial passou de 8 bilhões em novembro de 2022."],
 capa=dict(elementos=[obj('arvore',[520,640],w=420),bloco('mais vida que gente no planeta',[520,1120],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Numa colher de sopa de terra, tem mais seres vivos do que gente no planeta."),f("E o planeta tem mais de 8 bilhões de pessoas.","E o planeta tem mais de oito bilhões de pessoas.")],
   elementos=[obj('arvore',[520,620],None,w=400,balanca=True),bloco('1 colher de terra',[520,940],None,size=74),dict(t='contador',de=0,ate=8,fmt='> {n} bilhões de pessoas',pos=[520,1110],e=[1,'8'],size=56)]),
  dict(id='c2',fonte='Fonte: FAO',frases=[f("Quem diz isso é a FAO, a agência da ONU pra alimentação e agricultura."),f("São bactérias, fungos, vermes minúsculos e um monte de bichos que a gente nem consegue enxergar.")],
   elementos=[tira('FAO · ONU',[520,450],None,size=56),tira('bactérias',[300,680],[1,'bactérias'],size=48),tira('fungos',[720,760],[1,'fungos'],size=48),tira('vermes minúsculos',[400,880],[1,'vermes'],size=46),nota('invisíveis!',[680,1040],[1,'enxergar'],cor='laranja',size=66)]),
  dict(id='c3',fonte='Fonte: Anthony et al., PNAS (2023), via Yale e360',frases=[f("Um estudo de 2023 estimou que quase 59% das espécies da Terra vivem no solo.","Um estudo de dois mil e vinte e três estimou que quase cinquenta e nove por cento das espécies da Terra vivem no solo."),f("Mais da metade da vida do planeta mora debaixo dos seus pés.")],
   camera=dict(push=0.05,zooms=[dict(e=[0,'59'],escala=1.15,alvo=[520,700],dur=0.7)]),elementos=[tira('PNAS · 2023',[520,450],None,size=52),num('59%',[520,700],[0,'59'],size=260),nota('debaixo dos\nseus pés',[560,1060],[1,'pés'],cor='laranja',size=62)]),
  dict(id='c4',fonte='Fonte: FAO',frases=[f("E solo demora muito pra se formar: pode levar até mil anos pra criar só 2 ou 3 centímetros.","E solo demora muito pra se formar: pode levar até mil anos pra criar só dois ou três centímetros."),f("Ou seja: solo perdido não volta no tempo de uma vida.")],
   elementos=[num('1.000',[520,580],None,size=200),tira('anos',[800,700],None,size=48),seta([520,760],[520,900],[0,'centímetros']),bloco('2 a 3 cm',[520,980],[0,'centímetros'],size=90,cor='tinta'),nota('não volta',[700,1140],[1,'volta'],cor='laranja',size=60)]),
  dict(id='c5',fonte='Fonte: FAO',frases=[f("E é dele que vem quase tudo o que a gente come: a FAO calcula que 95% dos alimentos são produzidos no solo.","E é dele que vem quase tudo o que a gente come: a FAO calcula que noventa e cinco por cento dos alimentos são produzidos no solo."),f("Mas cerca de um terço dos solos do mundo já está degradado.")],
   elementos=[num('95%',[520,600],[0,'95'],size=240),tira('dos alimentos vêm do solo',[520,820],[0,'alimentos'],size=44),bloco('1/3 degradado',[520,1040],[1,'terço'],size=84,cor='tinta',ang=-3)]),
  dict(id='c6',fonte='Fonte: FAO; InforMEA/ONU',frases=[f("E hoje, 5 de dezembro, é o Dia Mundial do Solo.","E hoje, cinco de dezembro, é o Dia Mundial do Solo."),f("A ONU oficializou a data em 2013, no aniversário de um rei da Tailândia que defendeu a ideia.","A ONU oficializou a data em dois mil e treze, no aniversário de um rei da Tailândia que defendeu a ideia.")],
   elementos=[dict(t='cal',titulo='DEZEMBRO',inicio=2,ndias=31,riscar=[5],riscar_em=[0,'5 de'],pos=[520,640],escala=0.7,ang=-2),bloco('DIA MUNDIAL DO SOLO',[520,1020],[0,'Dia'],size=66),obj('coroa',[760,1150],[1,'rei'],w=160)]),
  dict(id='c7',frases=[f("Então: uma colher de terra tem mais vida do que gente no mundo inteiro."),f("Marca aquele amigo que tem horta, jardim ou vasinho de planta em casa."),ASS],
   elementos=[obj('arvore',[520,620],None,w=360,ang=2),bloco('marca quem tem\nhorta ou vasinho',[520,1030],[1,'Marca'],size=62,maxw=740)])])

# ------------------------------------------------------------ 047 LÍNGUA PORTUGUESA (06/12 · final da Copa do Brasil no Mané Garrincha)
EPS['SSA-047']=dict(materia='LÍNGUA PORTUGUESA',titulo='O estádio da final da Copa do Brasil tem nome de passarinho',
 fontes=["Encyclopaedia Britannica, 'Garrincha'.","Sesc SP, 'Anjo extraordinário' (sobre a biografia 'Estrela Solitária', de Ruy Castro).","Portal Latino-Americano da USP, 'Garrincha, Mané'.","Correio da Manhã (08/11/2026): Grêmio e Palmeiras decidem a Copa do Brasil em 06/12, em jogo único, no Mané Garrincha.","O Hoje (23/04/2026): estádio volta ao nome original, Mané Garrincha."],
 capa=dict(elementos=[obj('medalha',[520,640],w=360,ang=-4),bloco('Garrincha é nome de passarinho',[520,1110],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("A final da Copa do Brasil é hoje, num estádio com nome de passarinho."),f("Garrincha. E não é sobrenome.")],
   elementos=[obj('medalha',[520,620],None,w=340,ang=-4,balanca=True),bloco('GARRINCHA',[520,940],None,size=110,cor='tinta',ang=-3),nota('não é sobrenome',[600,1120],[1,'sobrenome'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica; USP',frases=[f("O nome dele era Manuel Francisco dos Santos."),f("Nasceu em 1933, em Pau Grande, um distrito de Magé, no Rio de Janeiro.","Nasceu em mil novecentos e trinta e três, em Pau Grande, um distrito de Magé, no Rio de Janeiro.")],
   elementos=[verb('Manuel Francisco dos Santos','nome de registro','o Mané Garrincha.',[520,560],[0,'Manuel'],w=720),tira('1933',[300,860],[1,'1933'],size=60),tira('PAU GRANDE · MAGÉ (RJ)',[600,980],[1,'Pau'],size=44)]),
  dict(id='c3',fonte='Fonte: Sesc SP, sobre a biografia de Ruy Castro',frases=[f("Ainda criança, ele ganhou o apelido em casa. Segundo o biógrafo Ruy Castro, foi a irmã mais velha, Rosa."),f("Garrincha é o nome de um passarinho pequeno e marrom, também chamado de cambaxirra.")],
   elementos=[tira('RUY CASTRO',[330,450],[0,'Ruy'],size=52),nota('a irmã Rosa',[700,560],[0,'Rosa'],cor='laranja',size=62),verb('garrincha','subst. fem.','passarinho pequeno e marrom; também chamado de cambaxirra.',[520,900],[1,'passarinho'],w=700)]),
  dict(id='c4',fonte='Fonte: Sesc SP, sobre a biografia de Ruy Castro',frases=[f("Na descrição do Ruy Castro, é um passarinho que canta bonito e não se adapta à gaiola."),f("Pequeno, rápido e difícil de segurar. Que nem o Mané com a bola no pé.")],
   camera=dict(push=0.06),elementos=[bloco('canta bonito',[330,520],[0,'canta'],size=66),bloco('não se adapta\nà gaiola',[640,720],[0,'gaiola'],size=60,cor='tinta',maxw=560),nota('difícil de segurar',[520,1000],[1,'segurar'],cor='laranja',size=62)]),
  dict(id='c5',fonte='Fonte: USP; Encyclopaedia Britannica',frases=[f("E ele tinha as pernas tortas, com uns 6 centímetros de diferença entre elas.","E ele tinha as pernas tortas, com uns seis centímetros de diferença entre elas."),f("Mesmo assim, foi campeão do mundo em 1958 e 1962, e o melhor jogador da Copa de 62.","Mesmo assim, foi campeão do mundo em mil novecentos e cinquenta e oito e mil novecentos e sessenta e dois, e o melhor jogador da Copa de sessenta e dois.")],
   elementos=[num('6 cm',[520,560],[0,'6'],size=180),tira('de diferença nas pernas',[520,720],[0,'diferença'],size=44),obj('medalha',[300,960],[1,'campeão'],w=220),tira('1958 · 1962',[660,920],[1,'1958'],size=56),nota('craque da Copa de 62',[640,1090],[1,'melhor'],cor='laranja',size=52)]),
  dict(id='c6',fonte='Fonte: Correio da Manhã (08/11/2026)',frases=[f("E hoje, Grêmio e Palmeiras decidem a Copa do Brasil no Estádio Nacional Mané Garrincha, em Brasília."),f("E pela primeira vez, a final da competição é em jogo único.")],
   elementos=[tira('DOMINGO · 06/12',[520,450],None,size=52),bloco('GRÊMIO x PALMEIRAS',[520,640],[0,'Grêmio'],size=70,cor='tinta'),tira('MANÉ GARRINCHA · BRASÍLIA',[520,820],[0,'Brasília'],size=40),bloco('jogo único',[520,1030],[1,'único'],size=86)]),
  dict(id='c7',frases=[f("Então: o estádio da final tem nome de passarinho, e de um dos maiores dribladores da história."),f("E aí: Grêmio ou Palmeiras? Comenta quem leva."),ASS],
   elementos=[obj('medalha',[520,620],None,w=320,ang=3),bloco('Grêmio ou Palmeiras?',[520,1000],[1,'Grêmio'],size=70),nota('comenta quem leva',[640,1160],[1,'Comenta'],cor='laranja',size=54)])])

# ------------------------------------------------------------ 048 FILOSOFIA
EPS['SSA-048']=dict(materia='FILOSOFIA',titulo='Aquiles nunca alcança a tartaruga (será?)',
 fontes=["Stanford Encyclopedia of Philosophy, 'Zeno's Paradoxes'.","Internet Encyclopedia of Philosophy, 'Zeno's Paradoxes'.","ARISTÓTELES. Física, livro VI, 239b.","Encyclopaedia Britannica, 'Paradoxes of Zeno'."],
 capa=dict(elementos=[obj('corredor',[520,640],w=420),bloco('o mais rápido nunca alcança o mais lento?',[520,1120],size=62,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Segundo um filósofo grego, o corredor mais rápido nunca alcança o mais lento."),f("E a lógica dele é bem difícil de derrubar.")],
   elementos=[obj('corredor',[520,620],None,w=400,balanca=True),bloco('NUNCA ALCANÇA',[520,960],None,size=90,cor='tinta',ang=-3),nota('difícil de derrubar',[600,1140],[1,'derrubar'],cor='laranja',size=56)]),
  dict(id='c2',fonte='Fonte: Stanford Encyclopedia of Philosophy',frases=[f("Zenão de Eleia viveu no século 5 antes de Cristo.","Zenão de Eléia viveu no século cinco antes de Cristo."),f("Ele criava argumentos pra defender o mestre, Parmênides, pra quem o movimento não existia de verdade.")],
   elementos=[tira('ZENÃO DE ELEIA · SÉC. V a.C.',[520,460],None,size=44),obj('livro',[330,760],[1,'Parmênides'],w=300,ang=-4),tira('PARMÊNIDES',[700,700],[1,'Parmênides'],size=50),nota('o movimento\nnão existe?',[640,1000],[1,'movimento'],cor='laranja',size=60)]),
  dict(id='c3',fonte='Fonte: Internet Encyclopedia of Philosophy',frases=[f("A versão mais famosa é Aquiles contra a tartaruga."),f("A tartaruga sai na frente."),f("Quando Aquiles chega onde ela estava, ela já andou mais um pouco.")],
   elementos=[bloco('AQUILES x TARTARUGA',[520,500],None,size=66),tira('largada da tartaruga',[620,700],[1,'frente'],size=44),seta([200,880],[560,880],[2,'chega']),seta([600,940],[760,940],[2,'andou'],cor='laranja'),nota('mais um pouco',[620,1080],[2,'pouco'],cor='laranja',size=58)]),
  dict(id='c4',frases=[f("Quando ele chega nesse novo ponto, ela andou mais um pouquinho."),f("E assim pra sempre: infinitos trechos pra percorrer."),f("Então Aquiles nunca alcança?")],
   camera=dict(push=0.08),elementos=[seta([200,500],[500,500],[0,'chega']),seta([520,560],[660,560],[0,'pouquinho'],cor='laranja'),seta([680,620],[760,620],[1,'infinitos'],cor='laranja'),bloco('INFINITOS TRECHOS',[520,860],[1,'infinitos'],size=74,cor='tinta'),bloco('nunca alcança?',[520,1080],[2,'nunca'],size=76)]),
  dict(id='c5',fonte='Fonte: Stanford Encyclopedia; Internet Encyclopedia of Philosophy',frases=[f("O livro do Zenão se perdeu. A gente conhece o argumento pelo Aristóteles, que tentou responder."),f("E um detalhe: no texto do Aristóteles nem tem tartaruga. Ela entrou na história depois.")],
   elementos=[tira('ARISTÓTELES · FÍSICA, LIVRO VI',[520,460],None,size=42),obj('livro',[520,720],[0,'Aristóteles'],w=320,ang=3),bloco('nem tinha tartaruga',[520,1040],[1,'tartaruga'],size=70,cor='tinta',ang=-3)]),
  dict(id='c6',fonte='Fonte: Internet Encyclopedia of Philosophy',frases=[f("A matemática ajuda a explicar: metade, mais um quarto, mais um oitavo, e assim por diante, somam exatamente 1.","A matemática ajuda a explicar: metade, mais um quarto, mais um oitavo, e assim por diante, somam exatamente um."),f("Infinitos pedaços podem ter um total finito."),f("Essa ideia de limite só foi formalizada no século 19.","Essa ideia de limite só foi formalizada no século dezenove.")],
   elementos=[bloco('1/2 + 1/4 + 1/8 + ... = 1',[520,520],[0,'metade'],size=66,maxw=800),tira('infinitos pedaços',[330,760],[1,'Infinitos'],size=46),tira('total finito',[700,860],[1,'finito'],size=50),tira('LIMITE · SÉCULO XIX',[520,1060],[2,'limite'],size=48)]),
  dict(id='c7',fonte='Fonte: Stanford Encyclopedia of Philosophy',frases=[f("E hoje? Tem filósofo que ainda discute se a matemática resolveu tudo, ou só deu nome ao problema."),f("Já são uns 2.500 anos de debate.","Já são uns dois mil e quinhentos anos de debate.")],
   elementos=[bloco('resolveu tudo?',[520,520],[0,'resolveu'],size=80),nota('ou só deu nome\nao problema?',[580,760],[0,'nome'],cor='laranja',size=58),num('2.500',[520,1020],[1,'2.500'],size=170),tira('anos de debate',[700,1170],[1,'debate'],size=40)]),
  dict(id='c8',frases=[f("Então: o corredor mais rápido alcança, sim. Mas explicar por que levou mais de 2 mil anos.","Então: o corredor mais rápido alcança, sim. Mas explicar por que levou mais de dois mil anos."),f("Qual outro paradoxo já deu nó na sua cabeça?"),ASS],
   elementos=[obj('corredor',[520,620],None,w=360,ang=3),bloco('qual paradoxo te deu nó?',[520,1020],[1,'paradoxo'],size=64,maxw=780)])])

# ------------------------------------------------------------ grava os roteiro.json
DATAS={'SSA-035':('2026-11-30','12:00'),'SSA-036':('2026-11-30','19:00'),
 'SSA-037':('2026-12-01','12:00'),'SSA-038':('2026-12-01','19:00'),
 'SSA-039':('2026-12-02','12:00'),'SSA-040':('2026-12-02','19:00'),
 'SSA-041':('2026-12-03','12:00'),'SSA-042':('2026-12-03','19:00'),
 'SSA-043':('2026-12-04','12:00'),'SSA-044':('2026-12-04','19:00'),
 'SSA-045':('2026-12-05','12:00'),'SSA-046':('2026-12-05','19:00'),
 'SSA-047':('2026-12-06','12:00'),'SSA-048':('2026-12-06','19:00')}
CHAMADAS={
 'SSA-035':'O 1º JOGO ACABOU 0 A 0','SSA-036':'O CÉU DEVIA SER VIOLETA',
 'SSA-037':'UM BISPO APAGOU OS DEUSES','SSA-038':'A CULPA É DE 1982',
 'SSA-039':'O SAMBA ERA DE QUEM?','SSA-040':'BASTAM 23 PESSOAS',
 'SSA-041':'O MISTÉRIO QUE ELA NÃO CONTOU','SSA-042':'INVENTADO AOS 15 ANOS',
 'SSA-043':'POR QUE ESSE PAPEL VALE?','SSA-044':'POR QUE ISSO ACONTECE?',
 'SSA-045':'PINTANDO SEM VER','SSA-046':'MAIS VIDA QUE GENTE',
 'SSA-047':'NOME DE PASSARINHO','SSA-048':'VOCÊ CONSEGUE REFUTAR?'}

if __name__=='__main__':
    for k,ep in EPS.items():
        for c in ep['cenas']:
            for el in c['elementos']:
                if el.get('t')=='verbete' and 'defi' in el: el['def']=el.pop('defi')
                if el.get('e') is None: el.pop('e',None)
            if c.get('fonte') is None: c.pop('fonte',None)
        for c in ep['cenas']+[ep['capa']]:
            for el in c['elementos']:
                if 'pos' in el and el['pos'][1]>1140: el['pos']=[el['pos'][0],1140]
        d=f'{BASE}/{k}'; os.makedirs(d,exist_ok=True)
        rot=dict(id=k,chamada=CHAMADAS[k],**ep)
        json.dump(rot,open(f'{d}/roteiro.json','w'),ensure_ascii=False,indent=1)
        w=sum(len(fr[1].split()) for c in ep['cenas'] for fr in c['frases'] if fr is not ASS)
        first=ep['cenas'][0]['frases'][0][0]
        print(k,ep['materia'],DATAS[k],w,'palavras | gancho:',len(first.split()),'palavras')
