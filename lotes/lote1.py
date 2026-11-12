"""Gera os roteiros do lote 1 (SSA-002 a SSA-014). Não rode depois de produzir: sobrescreve roteiros."""
import json,os,sys
BASE=__import__('os').path.dirname(__import__('os').path.dirname(__import__('os').path.abspath(__file__)))+'/episodios'
ASS=["A fonte tá na legenda. Só sei que foi assim!","A fonte tá na legenda. Só sei que foi assim!"]
def f(leg,tts=None): return [leg,tts or leg]
def tira(txt,pos,e=None,**k): return dict(t='tira',txt=txt,pos=pos,e=e,**k)
def bloco(txt,pos,e=None,**k): return dict(t='bloco',txt=txt,pos=pos,e=e,**k)
def nota(txt,pos,e=None,**k): return dict(t='nota',txt=txt,pos=pos,e=e,**k)
def obj(nome,pos,e=None,**k): return dict(t='obj',nome=nome,pos=pos,e=e,**k)
def num(txt,pos,e=None,**k): return dict(t='numero',txt=txt,pos=pos,e=e,**k)
def seta(de,ate,e=None,**k): return dict(t='seta',de=de,ate=ate,pos=[0,0],e=e,**k)
def risco(de,ate,e=None,**k): return dict(t='risco',de=de,ate=ate,pos=[0,0],e=e,**k)
EPS={}
# ------------------------------------------------------------ 002 MATEMÁTICA
EPS['SSA-002']=dict(materia='MATEMÁTICA',titulo='Em 1582, 10 dias sumiram do calendário',
 fontes=["Bula Inter gravissimas, papa Gregório XIII, 24/02/1582.","Correio Braziliense, 'A noite de 4 de outubro de 1582 durou 10 dias' (2025).","Il Post, 'Quando entrò in vigore il calendario gregoriano' (2016)."],
 capa=dict(elementos=[dict(t='cal',titulo='OUTUBRO 1582',inicio=1,riscar=list(range(5,15)),pos=[540,700],ang=-3),
   bloco('10 dias que nunca existiram',[520,1150],size=74,maxw=760)]),
 cenas=[
  dict(id='c1',frases=[f("Em 1582, 10 dias simplesmente sumiram do calendário.","Em mil quinhentos e oitenta e dois, dez dias simplesmente sumiram do calendário."),f("E não foi erro de impressão.")],
   elementos=[dict(t='cal',titulo='OUTUBRO 1582',inicio=1,riscar=list(range(5,15)),riscar_em=[0,'sumiram'],pos=[520,700],ang=-3),
     nota('não foi erro\nde impressão!',[740,1120],[1,0.1],cor='laranja',ang=-6)]),
  dict(id='c2',fonte='Fonte: Correio Braziliense (2025)',frases=[f("O problema vinha da Roma antiga."),f("O calendário juliano contava o ano com 365 dias e 6 horas.","O calendário juliano contava o ano com trezentos e sessenta e cinco dias e seis horas."),f("Só que o ano do Sol é um pouquinho mais curto.")],
   elementos=[tira('ROMA ANTIGA',[300,430]),obj('relogio',[520,720],[0,0.3],w=380,ang=-4,balanca=True),
     tira('365 dias + 6 horas',[330,1020],[1,0.3]),tira('ano do Sol: 365 d 5 h 48 min',[560,1120],[2,0.5],size=40)]),
  dict(id='c3',frases=[f("Sobravam uns 11 minutos por ano. Parece nada.","Sobravam uns onze minutos por ano. Parece nada."),f("Mas em séculos, o erro virou 10 dias inteiros.","Mas em séculos, o erro virou dez dias inteiros."),f("E a Páscoa, que depende da primavera, estava saindo do lugar.")],
   elementos=[num('11 min',[520,560],None,size=200,cor='tinta'),nota('por ano...',[760,720],[0,0.5]),
     dict(t='contador',de=1,ate=10,fmt='= {n} dias de erro',pos=[520,900],e=[1,0.3]),obj('globo',[300,1080],[2,0.3],w=230),nota('Páscoa fora\ndo lugar',[680,1100],[2,'Páscoa'],cor='laranja')]),
  dict(id='c4',fonte='Fonte: bula Inter gravissimas (1582)',frases=[f("Aí o papa Gregório 13 assinou uma bula: a Inter gravissimas.","Aí o papa Gregório Treze assinou uma bula: a Ínter graviíssimas."),f("Depois da quinta-feira, 4 de outubro, veio a sexta, 15 de outubro.","Depois da quinta-feira, quatro de outubro, veio a sexta-feira, quinze de outubro.")],
   elementos=[dict(t='verbete',palavra='Inter gravissimas',classe='bula papal · 24 fev. 1582',defi='',w=700,pos=[520,520]) if False else tira('INTER GRAVISSIMAS · 1582',[520,470],size=48),
     obj('coroa',[520,700],[0,0.2],w=260),bloco('QUI 4',[300,1000],[1,'quinta'],size=90,cor='tinta'),seta([440,1000],[600,1000],[1,'veio']),bloco('SEX 15',[760,1000],[1,'sexta'],size=90)]),
  dict(id='c5',frases=[f("Quem dormiu no dia 4 acordou no dia 15.","Quem dormiu no dia quatro acordou no dia quinze."),f("E nem todo mundo topou: a Inglaterra só mudou em 1752.","E nem todo mundo topou: a Inglaterra só mudou em mil setecentos e cinquenta e dois.")],
   camera=dict(push=0.08),elementos=[obj('lampada',[330,650],None,w=260,ang=-5),nota('dormiu dia 4...',[640,560],[0,0.1],size=62),nota('...acordou dia 15!',[620,820],[0,0.55],size=62,cor='laranja'),
     tira('INGLATERRA: só em 1752',[520,1100],[1,'Inglaterra'],size=46)]),
  dict(id='c6',fonte='Regra do calendário gregoriano (1582)',frases=[f("E hoje? A regra que veio junto ainda manda no seu calendário."),f("Ano bissexto a cada 4 anos, mas virada de século só se der pra dividir por 400.","Ano bissexto a cada quatro anos, mas virada de século só se der pra dividir por quatrocentos."),f("Por isso 2000 teve 29 de fevereiro, e 1900 não.","Por isso dois mil teve vinte e nove de fevereiro, e mil e novecentos não.")],
   elementos=[obj('celular',[300,640],None,w=300,ang=-4),bloco('29 FEV',[680,560],[0,0.5],size=80),tira('a cada 4 anos',[680,720],[1,0.1]),tira('século: só se ÷ 400',[640,830],[1,'século'],size=40),
     tira('2000: bissexto',[330,1050],[2,'2000'],size=44),tira('1900: não',[700,1120],[2,'1900'],size=44),risco([600,1120],[800,1120],[2,'não'])]),
  dict(id='c7',frases=[f("Então: 10 dias sumiram por causa de 11 minutos por ano.","Então: dez dias sumiram por causa de onze minutos por ano."),f("Se você dormisse dia 4 e acordasse dia 15, o que ia fazer primeiro? Comenta aí.","Se você dormisse dia quatro e acordasse dia quinze, o que ia fazer primeiro? Comenta aí."),ASS],
   elementos=[dict(t='cal',titulo='OUTUBRO 1582',inicio=1,riscar=list(range(5,15)),pos=[520,640],ang=2,escala=0.8),bloco('o que você faria?',[520,1080],[1,0.2],size=70),nota('comenta aí!',[760,1180],[1,0.7],cor='laranja')])])
# ------------------------------------------------------------ 003 FILOSOFIA
EPS['SSA-003']=dict(materia='FILOSOFIA',titulo='O Mito da Caverna (e o seu feed)',
 fontes=["PLATÃO. A República, Livro VII.","PARISER, Eli. The Filter Bubble: What the Internet Is Hiding from You. Penguin Press, 2011."],
 capa=dict(elementos=[obj('caverna',[530,700],w=620,h=520,ang=-2),bloco('e se tudo que você vê for só sombra?',[520,1160],size=70,maxw=760),tira('PLATÃO',[260,440],size=56)]),
 cenas=[
  dict(id='c1',frases=[f("E se tudo que você já viu fosse só sombra?"),f("Há uns 2.400 anos, Platão contou essa história.","Há uns dois mil e quatrocentos anos, Platão contou essa história.")],
   elementos=[obj('caverna',[530,680],None,w=640,h=520,ang=-2,balanca=True),bloco('e se fosse só sombra?',[520,1100],None,size=72),tira('PLATÃO, A REPÚBLICA',[700,440],[1,'Platão'],size=44)]),
  dict(id='c2',fonte='Fonte: Platão, A República, Livro VII',frases=[f("Imagina pessoas presas numa caverna desde crianças, olhando só pra parede do fundo."),f("Atrás delas tem uma fogueira."),f("E entre o fogo e os prisioneiros passam objetos que fazem sombra na parede.")],
   camera=dict(push=0.07),
   elementos=[obj('caverna',[520,680],None,w=740,h=580),nota('presos desde crianças',[520,1090],[0,'presas'],size=56,sai=[1,0.0]),nota('fogueira',[770,1090],[1,'fogueira'],cor='laranja',size=60),nota('sombras!',[290,1090],[2,'sombra'],cor='laranja',size=60)]),
  dict(id='c3',fonte='Fonte: Platão, A República, Livro VII',frases=[f("Os prisioneiros acham que as sombras são a realidade."),f("Afinal, é tudo o que eles conhecem.")],
   elementos=[bloco('sombra = realidade?',[520,560],None,size=80),obj('olho' if False else 'lampada',[300,880],[0,0.5],w=240),nota('é tudo o que\nconhecem',[650,900],[1,0.1],size=62)]),
  dict(id='c4',frases=[f("Um dia, um deles se solta e sai da caverna."),f("A luz do sol machuca os olhos. Mas, aos poucos, ele enxerga o mundo de verdade.")],
   camera=dict(push=0.1),elementos=[obj('caverna',[300,600],None,w=420,h=340,ang=-4),seta([480,640],[700,560],[0,'sai']),obj('lampada',[760,520],[1,0.05],w=240,ang=6),
     bloco('o mundo de verdade',[520,1050],[1,'enxerga'],size=72)]),
  dict(id='c5',frases=[f("Ele volta pra contar pros outros. E sabe o que acontece?"),f("Riem dele, e ninguém quer sair."),f("Pra Platão, sair da caverna é aprender.")],
   elementos=[obj('caverna',[520,620],None,w=640,h=500),nota('rá rá rá',[300,430],[1,0.0],cor='laranja',size=66),bloco('sair da caverna = aprender',[520,1080],[2,'sair'],size=66,maxw=760)]),
  dict(id='c6',fonte='Fonte: Eli Pariser, The Filter Bubble (2011)',frases=[f("E hoje? Pensa no seu feed."),f("Em 2011, o escritor Eli Pariser chamou de bolha de filtros quando o algoritmo te mostra só mais do mesmo.","Em dois mil e onze, o escritor Ilai Párizer chamou de bolha de filtros quando o algoritmo te mostra só mais do mesmo."),f("Às vezes, a caverna cabe no celular.")],
   elementos=[obj('celular',[520,680],None,w=360,balanca=True),tira('ELI PARISER, 2011',[300,430],[1,'Pariser'],size=44),bloco('bolha de filtros',[650,1000],[1,'bolha'],size=70),nota('a caverna cabe\nno celular',[330,1120],[2,0.2],cor='laranja',size=58)]),
  dict(id='c7',frases=[f("Então, a pergunta de Platão continua valendo: o que você vê é a coisa, ou só a sombra?"),f("O que já te fez sair da caverna? Comenta."),ASS],
   elementos=[obj('caverna',[520,650],None,w=600,h=480,ang=2),bloco('a coisa ou a sombra?',[520,1060],[0,'coisa'],size=74),nota('comenta!',[780,1180],[1,0.5],cor='laranja')])])
# ------------------------------------------------------------ 004 ARTE
EPS['SSA-004']=dict(materia='ARTE',titulo='A Mona Lisa ficou famosa porque foi roubada',
 fontes=["Smithsonian Magazine, 'The Theft That Made the Mona Lisa a Masterpiece' (James Zug, 2011).","History.com, 'The Heist that Made the Mona Lisa Famous' (Evan Andrews).","TheCollector, 'The Man Who Stole the Mona Lisa: What Happened to Vincenzo Peruggia?'"],
 capa=dict(elementos=[obj('moldura',[520,680],w=560,h=640),bloco('a parede vazia que lotou o museu',[520,1160],size=70,maxw=760),tira('LOUVRE, 1911',[300,410],size=52)]),
 cenas=[
  dict(id='c1',frases=[f("A Mona Lisa ficou famosa de verdade depois de ser roubada."),f("E muita gente foi ao museu só pra ver a parede vazia.")],
   elementos=[obj('moldura',[520,680],None,w=560,h=640,balanca=True),bloco('ROUBADA',[730,470],None,size=70,cor='tinta',ang=8),nota('a parede vazia',[520,1120],[1,'parede'],cor='laranja',size=64)]),
  dict(id='c2',fonte='Fonte: Smithsonian Magazine; History.com',frases=[f("Paris, 21 de agosto de 1911.","Paris, vinte e um de agosto de mil novecentos e onze."),f("Era segunda-feira, e o Louvre estava fechado."),f("Vincenzo Peruggia, que já tinha trabalhado no museu, tira o quadro da parede e sai com ele escondido debaixo da roupa.","Vinchênzo Perúdja, que já tinha trabalhado no museu, tira o quadro da parede e sai com ele escondido debaixo da roupa.")],
   elementos=[tira('PARIS · 21/08/1911',[520,430],None,size=50),bloco('FECHADO',[330,640],[1,'fechado'],size=76,cor='tinta',ang=-5),nota('segunda-feira',[700,620],[1,'segunda'],size=60),
     tira('VINCENZO PERUGGIA',[520,880],[2,'Peruggia'],size=50),nota('debaixo da roupa!',[560,1080],[2,'debaixo'],cor='laranja',size=64)]),
  dict(id='c3',fonte='Fonte: History.com; TheCollector',frases=[f("Por mais de um dia, ninguém percebe."),f("O museu achou que o quadro tinha ido ser fotografado.")],
   elementos=[obj('moldura',[520,660],None,w=500,h=570),dict(t='contador',de=1,ate=28,fmt='{n} horas sem ninguém notar',pos=[520,1080],e=[0,0.3],size=58) if False else nota('...cadê?',[760,1000],[0,0.4],cor='laranja',size=70),
     tira('"foi pra foto"',[400,1120],[1,'fotografado'],size=52)]),
  dict(id='c4',fonte='Fonte: Smithsonian Magazine',frases=[f("Quando o Louvre reabriu, uma semana depois, milhares de pessoas foram olhar o espaço vazio."),f("Na parede, só quatro ganchos de ferro."),f("Até o escritor Franz Kafka foi ver.","Até o escritor Franz Cáfka foi ver.")],
   camera=dict(push=0.04,zooms=[dict(e=[1,0.1],escala=1.3,alvo=[520,680],dur=1.0)]),
   elementos=[obj('moldura',[520,680],None,w=560,h=640),bloco('fila pra ver o nada',[520,1100],[0,'milhares'],size=70),nota('4 ganchos',[800,440],[1,'ganchos'],cor='laranja',size=62),tira('FRANZ KAFKA esteve lá',[330,440],[2,'Kafka'],size=40)]),
  dict(id='c5',fonte='Fonte: TheCollector; History.com',frases=[f("O quadro ficou sumido por mais de dois anos."),f("Em 1913, Peruggia tentou vender a obra pra um negociante de arte em Florença, e acabou preso.","Em mil novecentos e treze, Perúdja tentou vender a obra pra um negociante de arte em Florença, e acabou preso."),f("Na volta ao Louvre, pelo menos 120 mil pessoas foram ver a Mona Lisa em dois dias.","Na volta ao Louvre, pelo menos cento e vinte mil pessoas foram ver a Mona Lisa em dois dias.")],
   elementos=[bloco('PROCURA-SE',[520,470],None,size=84,cor='tinta',ang=-3),tira('FLORENÇA, 1913',[330,700],[1,'Florença'],size=50),nota('preso!',[740,720],[1,'preso'],cor='laranja',size=72),
     dict(t='contador',de=0,ate=120000,fmt='{n} visitantes',pos=[520,980],e=[2,'120'],size=72),tira('em 2 dias',[520,1140],[2,'dois dias'],size=46)]),
  dict(id='c6',fonte='Fonte: Smithsonian Magazine',frases=[f("E hoje? A revista Smithsonian estima uns 8 milhões de visitas à Mona Lisa por ano.","E hoje? A revista Smithsonian estima uns oito milhões de visitas à Mona Lisa por ano."),f("Um sumiço transformou um quadro em celebridade.")],
   elementos=[obj('celular',[300,700],None,w=300,ang=-5),dict(t='contador',de=0,ate=8,fmt='{n} milhões/ano',pos=[680,620],e=[0,'milhões'],size=70),bloco('celebridade',[640,960],[1,'celebridade'],size=80,cor='tinta',ang=3)]),
  dict(id='c7',frases=[f("Então: às vezes, o que deixa algo famoso é justamente a falta dele."),f("Você iria a um museu só pra ver uma parede vazia? Comenta."),ASS],
   elementos=[obj('moldura',[520,650],None,w=480,h=550,ang=-2),bloco('você iria?',[520,1060],[1,0.2],size=80),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 005 LÍNGUA PORTUGUESA
EPS['SSA-005']=dict(materia='LÍNGUA PORTUGUESA',titulo='"Você" veio de "Vossa Mercê"',
 fontes=["LOPES, Célia R. S. A gramaticalização de Vossa Mercê. Soletras (UERJ).","Revista Diadorim (UFRJ): implementação de você no Brasil e em Portugal.","Working Papers em Linguística (UFSC), 2019: Vossa Mercê > Você.","Cadernos de Estudos Linguísticos (UNICAMP): Vossa Mercê > vossemecê > vosmecê > vancê > você."],
 capa=dict(elementos=[obj('coroa',[520,600],w=420),bloco('"você" já foi "Vossa Mercê"',[520,1100],size=78,maxw=760)]),
 cenas=[
  dict(id='c1',frases=[f("Toda vez que você fala você, está chamando alguém de Vossa Mercê."),f("Exagero? A palavra foi encolhendo durante séculos.")],
   elementos=[obj('coroa',[520,600],None,w=420,balanca=True),bloco('você = Vossa Mercê',[520,1060],None,size=80),nota('encolheu!',[780,430],[1,'encolhendo'],cor='laranja',size=66)]),
  dict(id='c2',fonte='Fonte: Lopes (UERJ); Lopes e Brocardo (2016)',frases=[f("Lá no século 14, Vossa Mercê era um tratamento usado com o rei.","Lá no século quatorze, Vossa Mercê era um tratamento usado com o rei."),f("Mercê quer dizer favor, graça."),f("Era tipo dizer: Vossa Graça."),f("O jeito educado de falar com quem estava acima de você.")],
   elementos=[tira('SÉCULO XIV',[300,430],None,size=50),obj('coroa',[700,600],[0,'rei'],w=300,ang=6),dict(t='verbete',palavra='mercê',classe='subst. fem.',defi='graça, favor, benefício concedido por alguém poderoso.',w=660,pos=[500,960],e=[1,0.1])]),
  dict(id='c3',fonte='Fonte: Revista Linguística (UFRJ)',frases=[f("Com o tempo, a expressão passou a ser usada com muito mais gente."),f("E palavra muito usada vai se gastando na boca do povo.")],
   elementos=[bloco('Vossa Mercê',[520,560],None,size=92),nota('usada com todo mundo',[520,800],[0,'muito'],size=60),nota('...gastando...',[520,1050],[1,'gastando'],cor='laranja',size=70)]),
  dict(id='c4',fonte='Fonte: UNICAMP; UFSC (2019)',frases=[f("Vossa Mercê virou vossemecê. Depois vosmecê. Depois vancê."),f("E, no século 17, já aparece escrito: você.","E, no século dezessete, já aparece escrito: você.")],
   elementos=[tira('Vossa Mercê',[300,420],None,size=46),tira('vossemecê',[640,540],[0,'vossemecê'],size=50),tira('vosmecê',[340,680],[0,'vosmecê.'],size=54),tira('vancê',[680,820],[0,'vancê'],size=58),
     bloco('você',[520,1040],[1,'você'],size=110),tira('SÉCULO XVII',[800,1170],[1,'17'],size=36)]),
  dict(id='c5',frases=[f("E não parou: veio ocê. E depois, cê."),f("Cê tá entendendo?")],
   camera=dict(push=0.1),elementos=[bloco('você',[300,520],None,size=80,cor='tinta'),seta([420,600],[560,700],[0,'ocê']),bloco('ocê',[640,760],[0,'ocê'],size=90),seta([600,860],[460,960],[0,'cê.']),bloco('cê',[380,1060],[0,'depois'],size=110),nota('cê tá entendendo?',[720,1170],[1,0.0],cor='laranja',size=56)]),
  dict(id='c6',fonte='Fonte: Diadorim (UFRJ)',frases=[f("E hoje? No celular, virou duas letras: vc."),f("De Vossa Mercê pra vc: de dez letras pra duas."),f("E tem mais: no Brasil, o você se espalhou bem mais rápido. Em Portugal, o tu continua mais comum no dia a dia.")],
   elementos=[obj('celular',[330,720],None,w=340,ang=-4),bloco('vc',[720,600],[0,'vc'],size=130),tira('10 letras viram 2',[700,900],[1,'dez'],size=50),tira('Brasil: você · Portugal: tu',[520,1110],[2,'Portugal'],size=44)]),
  dict(id='c7',frases=[f("Então, quando alguém disser cê, lembra: tem um rei escondido aí."),f("Que outra palavra você acha que encolheu assim? Comenta."),ASS],
   elementos=[obj('coroa',[520,620],None,w=360,ang=-3),bloco('tem um rei escondido no "cê"',[520,1040],[0,'rei'],size=66,maxw=760),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 006 HISTÓRIA
EPS['SSA-006']=dict(materia='HISTÓRIA',titulo='A Bastilha tinha só 7 presos',
 fontes=["Encyclopaedia Britannica, 'Storming of the Bastille'.","Vie-publique.fr (governo francês), 'Que célèbre-t-on le 14 juillet ?'.","Ministère des Armées, '14 Juillet. Jour de la fête nationale'."],
 capa=dict(elementos=[obj('castelo',[520,720],w=640,h=460),num('7',[300,470],size=300),bloco('presos. Só isso.',[600,1120],size=80)]),
 cenas=[
  dict(id='c1',frases=[f("Invadiram a prisão mais temida de Paris e acharam só 7 presos.","Invadiram a prisão mais temida de Paris e acharam só sete presos."),f("Então por que esse dia virou feriado nacional?")],
   elementos=[obj('castelo',[520,700],None,w=640,h=460,balanca=True),num('7',[790,460],None,size=280),bloco('feriado nacional?',[520,1100],[1,'feriado'],size=74)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Paris, 14 de julho de 1789.","Paris, catorze de julho de mil setecentos e oitenta e nove."),f("A Bastilha era uma fortaleza-prisão do rei."),f("E guardava uma coisa que a multidão queria muito: pólvora.")],
   elementos=[tira('PARIS · 14/07/1789',[520,430],None,size=50),obj('castelo',[520,700],[1,'Bastilha'],w=600,h=430),bloco('PÓLVORA',[600,1080],[2,'pólvora'],size=90,cor='tinta',ang=-4)]),
  dict(id='c3',fonte='Fonte: Encyclopaedia Britannica',frases=[f("A multidão invadiu a fortaleza, pegou a pólvora e libertou todos os presos."),f("E aí veio a surpresa: eram só 7.","E aí veio a surpresa: eram só sete.")],
   camera=dict(push=0.04,zooms=[dict(e=[1,'surpresa'],escala=1.25,alvo=[520,700],dur=0.6)]),elementos=[obj('castelo',[520,700],None,w=600,h=430,ang=-2),num('7',[520,700],[1,'só 7'],size=420)]),
  dict(id='c4',fonte='Fonte: Encyclopaedia Britannica',frases=[f("4 falsificadores, 2 homens considerados loucos e 1 nobre preso a pedido da família.","Quatro falsificadores, dois homens considerados loucos e um nobre preso a pedido da família."),f("Nada de multidão de presos políticos.")],
   elementos=[tira('4 falsificadores',[380,500],None,size=56),tira('2 considerados "loucos"',[560,680],[0,'loucos'],size=52),tira('1 nobre',[380,860],[0,'nobre'],size=56),bloco('presos políticos? não.',[560,1080],[1,'políticos'],size=64,cor='tinta')]),
  dict(id='c5',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Mas a Bastilha era um símbolo do poder do rei."),f("E tomar o símbolo virou o grande marco da Revolução Francesa.")],
   elementos=[obj('coroa',[520,620],None,w=380),bloco('SÍMBOLO',[520,920],[0,'símbolo'],size=100),tira('REVOLUÇÃO FRANCESA',[520,1120],[1,'Revolução'],size=46)]),
  dict(id='c6',fonte='Fonte: vie-publique.fr; Ministère des Armées',frases=[f("E hoje? O 14 de julho é a festa nacional da França desde 1880.","E hoje? O catorze de julho é a festa nacional da França desde mil oitocentos e oitenta."),f("E a lei nem diz qual 14 de julho comemora: a tomada da Bastilha, de 1789, ou a festa da Federação, de 1790.","E a lei nem diz qual catorze de julho comemora: a tomada da Bastilha, de mil setecentos e oitenta e nove, ou a festa da Federação, de mil setecentos e noventa.")],
   elementos=[tira('LOI DU 6 JUILLET 1880',[520,440],None,size=46),bloco('14 de julho',[520,640],[0,'festa'],size=96),nota('qual deles?',[760,830],[1,'nem diz'],cor='laranja',size=64),tira('1789',[330,1000],[1,'Bastilha,'],size=60),tira('1790',[700,1060],[1,'Federação'],size=60)]),
  dict(id='c7',frases=[f("Então: 7 presos, e um feriado que já dura quase 150 anos.","Então: sete presos, e um feriado que já dura quase cento e cinquenta anos."),f("Que outro símbolo você acha maior do que o fato? Comenta."),ASS],
   elementos=[num('7',[330,620],None,size=300),obj('castelo',[700,700],None,w=380,h=280),bloco('símbolo > fato?',[520,1060],[1,'símbolo'],size=76),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 007 EDUCAÇÃO FÍSICA
EPS['SSA-007']=dict(materia='EDUCAÇÃO FÍSICA',titulo='Por que a maratona tem 42,195 km?',
 fontes=["Olympedia, 'Marathon, Men — 1908 Summer Olympics'.","German Road Races, '100 Years of the Marathon: 42.195 km' (2008).","Boston.com, 'Why is a marathon 26.2 miles?' (2023)."],
 capa=dict(elementos=[obj('corredor',[520,640],w=440),num('42,195',[520,980],size=190),tira('km',[860,1090],size=50)]),
 cenas=[
  dict(id='c1',frases=[f("A maratona tem 42,195 quilômetros. Por que esses 195 metros?","A maratona tem quarenta e dois quilômetros e cento e noventa e cinco metros. Por que esses cento e noventa e cinco metros?"),f("A resposta tem castelo e camarote real.")],
   elementos=[obj('corredor',[520,600],None,w=420,balanca=True),num('42,195',[520,960],None,size=190),obj('castelo',[300,1120],[1,'castelo'],w=220,h=160),obj('coroa',[760,1120],[1,'camarote'],w=170)]),
  dict(id='c2',fonte='Fonte: Boston.com (2023)',frases=[f("Nas primeiras Olimpíadas modernas, a maratona não tinha distância fixa."),f("Era mais ou menos 40 quilômetros, e mudava de prova pra prova.","Era mais ou menos quarenta quilômetros, e mudava de prova pra prova.")],
   elementos=[obj('medalha',[520,600],None,w=300),tira('~ 40 km',[340,960],[1,'40'],size=70),nota('cada prova\nde um jeito',[700,1000],[1,'mudava'],cor='laranja',size=58)]),
  dict(id='c3',fonte='Fonte: Olympedia; German Road Races',frases=[f("Em Londres, 1908, a largada foi no Castelo de Windsor.","Em Londres, mil novecentos e oito, a largada foi no Castelo de Uíndsor."),f("E a chegada, no estádio, bem na frente do camarote real."),f("Medido assim, deu 26 milhas e 385 jardas: 42,195 quilômetros.","Medido assim, deu vinte e seis milhas e trezentas e oitenta e cinco jardas: quarenta e dois quilômetros e cento e noventa e cinco metros.")],
   elementos=[tira('LONDRES, 1908',[520,430],None,size=50),obj('castelo',[300,640],[0,'Windsor'],w=320,h=240),seta([470,640],[640,760],[1,0.0]),obj('coroa',[740,800],[1,'camarote'],w=220),
     tira('26 milhas + 385 jardas',[520,1000],[2,'milhas'],size=46),bloco('= 42,195 km',[520,1130],[2,'42'],size=72)]),
  dict(id='c4',fonte='Fonte: Olympedia',frases=[f("Muita gente conta que foi capricho da família real."),f("Mas, segundo o Olympedia, a ideia de largar em Windsor partiu dos organizadores.","Mas, segundo o Olimpédia, a ideia de largar em Uíndsor partiu dos organizadores.")],
   elementos=[bloco('capricho da realeza?',[520,520],None,size=70,cor='tinta'),risco([180,520],[860,520],[1,'organizadores']),tira('OLYMPEDIA',[330,800],[1,'Olympedia'],size=50),nota('ideia dos\norganizadores',[640,980],[1,'organizadores'],cor='laranja',size=62)]),
  dict(id='c5',frases=[f("Essa prova ficou famosa: o italiano Dorando Pietri chegou primeiro, mas foi ajudado a cruzar a linha e acabou desclassificado.","Essa prova ficou famosa: o italiano Dorando Piêtri chegou primeiro, mas foi ajudado a cruzar a linha e acabou desclassificado."),f("O ouro ficou com o americano Johnny Hayes.","O ouro ficou com o americano Djóni Reis.")],
   elementos=[obj('corredor',[330,640],None,w=340,ang=-4),tira('DORANDO PIETRI',[660,480],[0,'Pietri'],size=46),bloco('DESCLASSIFICADO',[600,860],[0,'desclassificado'],size=60,cor='tinta',ang=-3),obj('medalha',[740,1080],[1,'ouro'],w=200),tira('JOHNNY HAYES',[380,1120],[1,'Hayes'],size=44)]),
  dict(id='c6',fonte='Fonte: German Road Races (2008)',frases=[f("Em 1921, a federação internacional de atletismo adotou a distância de Londres como oficial.","Em mil novecentos e vinte e um, a federação internacional de atletismo adotou a distância de Londres como oficial."),f("E hoje? Toda maratona oficial tem exatamente 42,195 quilômetros, por causa de um trajeto de 1908.","E hoje? Toda maratona oficial tem exatamente quarenta e dois quilômetros e cento e noventa e cinco metros, por causa de um trajeto de mil novecentos e oito.")],
   elementos=[tira('1921: distância oficial',[520,470],None,size=50),obj('relogio',[330,760],[1,'hoje'],w=280),num('42,195',[640,1040],[1,'exatamente'],size=150)]),
  dict(id='c7',frases=[f("Então, aqueles 195 metros finais têm mais de cem anos de história.","Então, aqueles cento e noventa e cinco metros finais têm mais de cem anos de história."),f("Quantos quilômetros você aguenta correr? Comenta."),ASS],
   elementos=[obj('corredor',[520,620],None,w=380),bloco('quantos km você aguenta?',[520,1060],[1,'Quantos'],size=66,maxw=760),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 008 QUÍMICA
EPS['SSA-008']=dict(materia='QUÍMICA',titulo='Os cadernos de Marie Curie ainda são radioativos',
 fontes=["The Christian Science Monitor, 'Marie Curie: Why her papers are still radioactive' (2011).","Business Insider, 'These personal effects... will be radioactive for another 1,500 years'.","My Modern Met, 'Marie Curie’s Papers Are Still Radioactive'."],
 capa=dict(elementos=[obj('caderno',[520,660],w=460,h=560,ang=-4),bloco('ainda radioativo',[520,1120],size=86),tira('MARIE CURIE',[300,420],size=56)]),
 cenas=[
  dict(id='c1',frases=[f("Os cadernos de Marie Curie ainda são radioativos, mais de cem anos depois."),f("E pra ler, tem regra.")],
   elementos=[obj('caderno',[520,660],None,w=460,h=560,ang=-4,balanca=True),bloco('ainda radioativo',[520,1110],None,size=80),nota('tem regra!',[780,440],[1,'regra'],cor='laranja',size=66)]),
  dict(id='c2',fonte='Fonte: Business Insider; Abakcus',frases=[f("Marie Curie é a única mulher a ganhar o Nobel em duas áreas: física e química."),f("Com o marido, Pierre, ela descobriu o polônio, em 1898. O nome homenageia a Polônia, terra dela.","Com o marido, Pierre, ela descobriu o polônio, em mil oitocentos e noventa e oito. O nome homenageia a Polônia, terra dela.")],
   elementos=[obj('medalha',[300,620],None,w=280),bloco('Nobel: física + química',[620,560],[0,'física'],size=56,maxw=520),tira('POLÔNIO, 1898',[600,880],[1,'polônio'],size=56),obj('frasco',[330,1020],[1,'Polônia'],w=250),nota('homenagem à Polônia',[680,1050],[1,'homenageia'],cor='laranja',size=52)]),
  dict(id='c3',fonte='Fonte: IFLScience',frases=[f("Na época, ninguém sabia o quanto a radiação era perigosa."),f("Poeira de rádio caía nas roupas, nos móveis, nos papéis.")],
   elementos=[obj('frasco',[520,640],None,w=360,balanca=True),bloco('perigo desconhecido',[520,980],[0,'perigosa'],size=70,cor='tinta'),nota('roupas, móveis, papéis...',[520,1150],[1,'roupas'],cor='laranja',size=56)]),
  dict(id='c4',fonte='Fonte: Christian Science Monitor (2011)',frases=[f("Hoje, os cadernos dela ficam em caixas forradas de chumbo, na Biblioteca Nacional da França."),f("Quem quer consultar assina um termo de responsabilidade e usa roupa de proteção.")],
   elementos=[obj('caderno',[330,680],None,w=340,h=420,ang=-6),bloco('CAIXA DE CHUMBO',[680,560],[0,'chumbo'],size=56,cor='tinta',ang=4),tira('BIBLIOTECA NACIONAL DA FRANÇA',[520,940],[0,'Biblioteca'],size=36),nota('assina o termo\ne se protege',[540,1110],[1,'assina'],cor='laranja',size=56)]),
  dict(id='c5',fonte='Fonte: My Modern Met',frases=[f("E vai longe: o rádio-226 leva uns 1.600 anos pra perder metade da radiação.","E vai longe: o rádio duzentos e vinte e seis leva uns mil e seiscentos anos pra perder metade da radiação.")],
   elementos=[tira('RÁDIO-226',[330,470],None,size=60),dict(t='contador',de=0,ate=1600,fmt='{n} anos',pos=[520,740],e=[0,'1.600'],size=110),nota('...só pra cair pela metade',[520,1000],[0,'metade'],cor='laranja',size=58)]),
  dict(id='c6',fonte='Fonte: My Modern Met',frases=[f("E hoje? Sabe aquele avental pesado do raio-x?"),f("É de chumbo, pelo mesmo motivo das caixas dos cadernos: o chumbo segura a radiação.")],
   elementos=[bloco('avental do raio-x',[520,560],None,size=74),tira('= chumbo',[520,760],[1,'chumbo'],size=70),obj('caderno',[700,1020],[1,'caixas'],w=240,h=300,ang=5),nota('segura a radiação',[330,1040],[1,'segura'],cor='laranja',size=56)]),
  dict(id='c7',fonte=None,frases=[f("Então: mais de cem anos depois, a pesquisa de Marie Curie ainda brilha no contador Geiger.","Então: mais de cem anos depois, a pesquisa de Marie Curie ainda apita no contador Gáiguer."),f("Você teria coragem de folhear esse caderno? Comenta."),ASS],
   elementos=[obj('caderno',[520,640],None,w=400,h=490,ang=3),bloco('você folhearia?',[520,1070],[1,'coragem'],size=78),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
EPS['SSA-008']['cenas'][6]['frases'][0]=f("Então: mais de cem anos depois, os papéis de Marie Curie ainda fazem o contador Geiger apitar.","Então: mais de cem anos depois, os papéis de Marie Curie ainda fazem o contador Gáiguer apitar.")
# ------------------------------------------------------------ 009 GEOGRAFIA
EPS['SSA-009']=dict(materia='GEOGRAFIA',titulo='O mapa que encolhe a África',
 fontes=["Mental Floss, 'Why Greenland Appears So Large on Maps'.","Mercator projection (Wikipedia, com referências): exemplos de distorção.","Inquirer Technology, 'Why Africa looks smaller than it really is on Google Maps' (2026)."],
 capa=dict(elementos=[dict(t='areas',a='ÁFRICA',b='GROENLÂNDIA',ratio=14,pos=[520,700]),bloco('14 vezes maior',[520,1140],size=86)]),
 cenas=[
  dict(id='c1',frases=[f("No mapa, a Groenlândia parece do tamanho da África."),f("Mas a África é 14 vezes maior.","Mas a África é catorze vezes maior.")],
   elementos=[obj('globo',[520,640],None,w=420,balanca=True,sai=[1,'África']),dict(t='areas',a='ÁFRICA',b='GROENLÂNDIA',ratio=14,pos=[520,760],e=[1,'África']),bloco('14×',[790,1110],[1,'14'],size=110)]),
  dict(id='c2',fonte='Fonte: Mental Floss',frases=[f("A culpa é de um mapa de 1569, do cartógrafo Gerardus Mercator.","A culpa é de um mapa de mil quinhentos e sessenta e nove, do cartógrafo Gerárdus Mercátor."),f("Ele queria ajudar os navegadores.")],
   elementos=[tira('MERCATOR, 1569',[520,450],None,size=56),obj('globo',[340,760],None,w=340),obj('relogio' if False else 'livro',[720,760],[0,'mapa'],w=300),nota('pra navegar',[520,1080],[1,'navegadores'],cor='laranja',size=66)]),
  dict(id='c3',fonte='Fonte: Science ABC',frases=[f("No mapa dele, seguir uma linha reta é seguir um rumo da bússola. Perfeito pra navegar."),f("Mas, pra isso funcionar, ele esticou tudo que fica perto dos polos.")],
   camera=dict(push=0.04,zooms=[dict(e=[1,'esticou'],escala=1.2,alvo=[520,500],dur=0.8)]),
   elementos=[seta([200,600],[860,600],None),nota('linha reta = rumo',[520,500],None,size=58),bloco('esticado nos polos',[520,860],[1,'esticou'],size=74,cor='tinta'),obj('globo',[520,1080],[1,'polos'],w=200)]),
  dict(id='c4',fonte='Fonte: Mercator projection (Wikipedia)',frases=[f("Por isso a Groenlândia, lá no norte, ficou gigante."),f("Na real, ela tem mais ou menos o tamanho da República Democrática do Congo."),f("E o Alasca parece do tamanho do Brasil, que é quase 5 vezes maior.","E o Alasca parece do tamanho do Brasil, que é quase cinco vezes maior."),f("E a Antártida? Se o mapa mostrasse tudo, ela ficaria infinita, esticada de ponta a ponta.")],
   elementos=[bloco('GROENLÂNDIA',[520,460],None,size=80,cor='tinta'),tira('~ tamanho do Congo',[520,640],[1,'Congo'],size=52),bloco('BRASIL',[330,880],[2,'Brasil'],size=96),tira('5 vezes o Alasca',[700,1000],[2,'5'],size=56),nota('Antártida: infinita!',[520,1150],[3,'infinita'],cor='laranja',size=60)]),
  dict(id='c5',fonte='Fonte: Inquirer Technology (2026)',frases=[f("E hoje? O Google Maps usa uma versão do Mercator."),f("No zoom da sua rua, funciona muito bem. No mapa-múndi, engana.")],
   elementos=[obj('celular',[330,700],None,w=340,ang=-4),bloco('Web Mercator',[690,560],[0,'Mercator'],size=64),nota('rua: ok',[700,800],[1,'rua'],size=64),nota('mundo: engana',[690,980],[1,'engana'],cor='laranja',size=64)]),
  dict(id='c6',frases=[f("Quer ver o tamanho real? Gira um globo: ele não estica nada.")],
   camera=dict(push=0.1),elementos=[obj('globo',[520,700],None,w=520,balanca=True),nota('não estica nada',[520,1100],[0,'estica'],cor='laranja',size=66)]),
  dict(id='c7',frases=[f("Então: a Groenlândia não é gigante, o mapa é que é exagerado."),f("Que país você achava maior do que é? Comenta."),ASS],
   elementos=[dict(t='areas',a='ÁFRICA',b='GROENLÂNDIA',ratio=14,pos=[520,700]),bloco('qual país te enganou?',[520,1110],[1,'país'],size=66),nota('comenta!',[790,450],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 010 LÍNGUA PORTUGUESA
EPS['SSA-010']=dict(materia='LÍNGUA PORTUGUESA',titulo='O mito do "feito nas coxas"',
 fontes=["LA PASTINA FILHO, José. 'Eram as telhas feitas nas coxas das escravas?' Arqueologia, Curitiba, v. 10, p. 17-21, 2006.","ABILIO, G. C.; SILVA, E. M. 'A falsa origem do forró: pseudoetimologia...'. Revista Espacialidades (UFRN), 2024.","Agência Brasil, 'Forró may be declared Brazil's intangible heritage' (2019)."],
 capa=dict(elementos=[obj('telha',[520,640],w=420,h=420,ang=-5),bloco('MITO',[740,460],size=110,cor='tinta',ang=8),bloco('a história das telhas é falsa',[520,1110],size=68,maxw=760)]),
 cenas=[
  dict(id='c1',frases=[f("Você já ouviu que feito nas coxas vem de telhas moldadas nas pernas de pessoas escravizadas?"),f("Essa história é falsa.")],
   elementos=[obj('telha',[520,640],None,w=420,h=420,ang=-5,balanca=True),dict(t='verbete',palavra='nas coxas',classe='loc. adv. (informal)',defi='de qualquer jeito, malfeito.',w=600,pos=[520,1040]),bloco('FALSO',[760,450],[1,'falsa'],size=110,cor='tinta',ang=8)]),
  dict(id='c2',fonte='Fonte: Revista Espacialidades (UFRN), 2024',frases=[f("Ela é repetida há décadas, até em passeio por cidade histórica."),f("E soa convincente: telha torta, feita de qualquer jeito.")],
   elementos=[obj('telha',[340,700],None,w=340,h=340,ang=-8),nota('todo mundo\nconta...',[720,560],[0,'repetida'],size=62),bloco('soa convincente',[640,1000],[1,'convincente'],size=66)]),
  dict(id='c3',fonte='Fonte: La Pastina Filho, Arqueologia (2006)',frases=[f("Em 2006, o arquiteto José La Pastina Filho publicou um estudo pra checar essa história.","Em dois mil e seis, o arquiteto José La Pastína Filho publicou um estudo pra checar essa história."),f("Ele mediu a coxa de um homem de 1,80 metro e fez as contas.","Ele mediu a coxa de um homem de um metro e oitenta e fez as contas.")],
   elementos=[tira('LA PASTINA FILHO, 2006',[520,450],None,size=46),obj('livro',[340,740],[0,'estudo'],w=320),nota('mediu de\nverdade',[720,700],[1,'mediu'],cor='laranja',size=62),tira('homem de 1,80 m',[560,1060],[1,'1,80'],size=54)]),
  dict(id='c4',fonte='Fonte: La Pastina Filho, Arqueologia (2006)',frases=[f("Não fecha. Uma pessoa teria que ficar parada com barro nas pernas, e outras carregando cada telha."),f("Pra uma obra inteira? Não se sustenta.")],
   elementos=[bloco('não fecha',[520,500],None,size=96,cor='tinta'),obj('telha',[330,800],[0,'barro'],w=260,h=260,ang=6),nota('1 parado +\nvários carregando',[700,820],[0,'carregando'],size=56),bloco('não se sustenta',[520,1100],[1,'sustenta'],size=70)]),
  dict(id='c5',frases=[f("Então de onde vem a expressão? A verdade é que ninguém sabe ao certo.")],
   elementos=[bloco('origem?',[520,600],None,size=120),nota('ninguém sabe ao certo',[520,900],[0,'ninguém'],cor='laranja',size=70)]),
  dict(id='c6',fonte='Fonte: Agência Brasil (2019); Espacialidades (UFRN)',frases=[f("E hoje? Origem inventada viraliza fácil."),f("O forró, por exemplo: dizem que vem do inglês for all. Mas a explicação mais aceita é outra: forrobodó.","O forró, por exemplo: dizem que vem do inglês for ól. Mas a explicação mais aceita é outra: forrobodó."),f("Um dicionário de 1912 já trazia forrobodó. Na edição seguinte, apareceu forró.","Um dicionário de mil novecentos e doze já trazia forrobodó. Na edição seguinte, apareceu forró.")],
   elementos=[obj('celular',[320,560],None,w=260,ang=-5),nota('viraliza!',[700,500],[0,'viraliza'],cor='laranja',size=66),tira('for all',[380,800],[1,'for all'],size=60),risco([270,800],[490,800],[1,'Mas']),
     bloco('forrobodó',[680,860],[1,'forrobodó'],size=74),tira('dicionário, 1912',[520,1100],[2,'1912'],size=50)]),
  dict(id='c7',frases=[f("Então: antes de compartilhar a origem de uma expressão, desconfia de história boa demais."),f("Que expressão você quer que a gente investigue? Comenta."),ASS],
   elementos=[bloco('desconfia de história boa demais',[520,620],None,size=72,maxw=760),obj('livro',[520,920],[1,0.0],w=280),nota('comenta!',[780,1170],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 011 FÍSICA
EPS['SSA-011']=dict(materia='FÍSICA',titulo='A maçã nunca caiu na cabeça do Newton',
 fontes=["STUKELEY, William. Memoirs of Sir Isaac Newton's Life (1752) — Royal Society.","History.com, 'Did an apple really fall on Isaac Newton’s head?'.","National Trust, Woolsthorpe Manor."],
 capa=dict(elementos=[obj('maca',[520,640],w=420),bloco('nunca caiu na cabeça',[520,1100],size=76),tira('NEWTON',[300,430],size=60)]),
 cenas=[
  dict(id='c1',frases=[f("A maçã nunca caiu na cabeça do Newton."),f("Mas a história da maçã é real. E é até melhor.")],
   elementos=[obj('maca',[520,640],None,w=420,balanca=True),bloco('na cabeça? não.',[520,1080],None,size=80,cor='tinta'),nota('mas é real!',[780,440],[1,'real'],cor='laranja',size=66)]),
  dict(id='c2',fonte='Fonte: Stukeley (1752); History.com',frases=[f("Quem contou foi o próprio Newton, em 1726, ao amigo William Stukeley.","Quem contou foi o próprio Newton, em mil setecentos e vinte e seis, ao amigo Uíliam Stiúkli."),f("Os dois tomavam chá no jardim, debaixo de umas macieiras.")],
   elementos=[tira('LONDRES, 1726',[300,440],None,size=50),tira('WILLIAM STUKELEY',[620,560],[0,'Stukeley'],size=46),obj('arvore',[520,860],[1,'macieiras'],w=420),nota('chá no jardim',[760,1150],[1,'chá'],cor='laranja',size=56)]),
  dict(id='c3',fonte='Fonte: Stukeley (1752)',frases=[f("E Newton lembrou: foi vendo uma maçã cair que a ideia da gravidade veio à cabeça dele."),f("A pergunta era: por que a maçã cai sempre reta pro chão, e não pro lado ou pra cima?")],
   camera=dict(push=0.05),elementos=[obj('maca',[520,520],None,w=260),seta([520,660],[520,960],[0,'cair']),bloco('por que reta pro chão?',[520,1080],[1,'reta'],size=68),nota('e não pro lado?',[760,700],[1,'lado'],cor='laranja',size=56)]),
  dict(id='c4',frases=[f("A resposta: a Terra puxa a maçã."),f("E a mesma força que puxa a maçã segura a Lua no céu.")],
   elementos=[obj('globo',[400,820],None,w=420),obj('maca',[760,480],None,w=180),seta([700,560],[540,680],[0,'puxa']),obj('globo',[800,1100],[1,'Lua'],w=150),nota('a Lua também!',[640,1180] if False else [700,950],[1,'Lua'],cor='laranja',size=56)]),
  dict(id='c5',fonte='Fonte: Stukeley (1752); History.com',frases=[f("Stukeley publicou essa conversa em 1752, nas memórias sobre Newton.","Stukeley publicou essa conversa em mil setecentos e cinquenta e dois, nas memórias sobre Newton."),f("E em momento nenhum a maçã bate na cabeça. Esse pedaço veio depois.")],
   elementos=[obj('livro',[520,620],None,w=380),tira('MEMÓRIAS, 1752',[520,880],[0,'1752'],size=56),bloco('maçã na cabeça',[520,1080],[1,'cabeça'],size=70,cor='tinta'),risco([230,1080],[810,1080],[1,'depois'])]),
  dict(id='c6',fonte='Fonte: National Trust; Big Think',frases=[f("E hoje? A macieira ainda está lá, na casa onde Newton cresceu, na Inglaterra."),f("Ela tombou numa tempestade, mas rebrotou da raiz."),f("E tem mudas dela em universidades pelo mundo.")],
   elementos=[obj('arvore',[520,700],None,w=460,balanca=True),tira('WOOLSTHORPE, INGLATERRA',[520,430],None,size=42),nota('tombou e rebrotou',[520,1000],[1,'rebrotou'],cor='laranja',size=60),tira('mudas pelo mundo',[520,1140],[2,'mudas'],size=50)]),
  dict(id='c7',frases=[f("Então: a maçã não bateu na cabeça, mas bateu na ideia."),f("Que outra história de cientista você acha exagerada? Comenta."),ASS],
   elementos=[obj('maca',[520,620],None,w=360,ang=4),bloco('bateu na ideia',[520,1060],[0,'ideia'],size=84),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 012 BIOLOGIA
EPS['SSA-012']=dict(materia='BIOLOGIA',titulo='O polvo tem 3 corações e sangue azul',
 fontes=["National Aquarium, 'An Ode to the Octopus' (2020).","Live Science, 'How many hearts does an octopus have?'.","Smithsonian Magazine, 'Ten Wild Facts About Octopuses'."],
 capa=dict(elementos=[obj('polvo',[520,640],w=480),num('3',[260,460],size=260),bloco('corações e sangue azul',[520,1110],size=72)]),
 cenas=[
  dict(id='c1',frases=[f("O polvo tem três corações. E o sangue dele é azul."),f("E quando ele nada, um dos corações para.")],
   elementos=[obj('polvo',[520,640],None,w=480,balanca=True),num('3',[250,460],None,size=240),bloco('sangue azul',[520,1080],[0,'azul'],size=80,cor='tinta'),nota('um coração para!',[760,1180],[1,'para'],cor='laranja',size=52)]),
  dict(id='c2',fonte='Fonte: National Aquarium (2020)',frases=[f("Vamos por partes. Dois corações trabalham só nas brânquias, que fazem o papel do nosso pulmão."),f("Eles empurram o sangue pra pegar oxigênio da água."),f("O terceiro manda esse sangue pro resto do corpo.")],
   elementos=[obj('coracao',[300,560],[0,'Dois'],w=220),obj('coracao',[560,560],[0,'Dois'],w=220),tira('brânquias',[430,760],[0,'brânquias'],size=52),obj('coracao',[700,960],[2,'terceiro'],w=260),tira('corpo todo',[330,1060],[2,'corpo'],size=52)]),
  dict(id='c3',fonte='Fonte: Smithsonian Magazine',frases=[f("E por que azul? Nosso sangue usa ferro pra levar oxigênio. O do polvo usa cobre."),f("A molécula se chama hemocianina. Com oxigênio, ela fica azulada.","A molécula se chama hemocianína. Com oxigênio, ela fica azulada.")],
   elementos=[tira('nós: FERRO',[330,500],[0,'ferro'],size=56),tira('polvo: COBRE',[680,640],[0,'cobre'],size=56),bloco('hemocianina',[520,920],[1,'hemocianina'],size=84,cor='tinta'),nota('= azul',[760,1100],[1,'azulada'],cor='laranja',size=72)]),
  dict(id='c4',fonte='Fonte: National Aquarium (2020)',frases=[f("A hemocianina funciona bem no frio e onde tem pouco oxigênio, como no fundo do mar."),f("É uma adaptação perfeita pra quem mora lá embaixo.")],
   elementos=[obj('polvo',[520,700],None,w=420),nota('frio',[260,480],[0,'frio'],size=70),nota('pouco oxigênio',[700,480],[0,'pouco'],size=60),bloco('fundo do mar',[520,1080],[0,'fundo'],size=80)]),
  dict(id='c5',fonte='Fonte: Live Science',frases=[f("Agora, o coração que para: quando o polvo nada, o coração principal para de bater por um tempo."),f("Por isso ele prefere andar pelo fundo do que nadar.")],
   camera=dict(push=0.04,congela=dict(de=[0,'para de bater'],ate=[1,0.0])),elementos=[obj('coracao',[520,620],None,w=320),bloco('PAUSA',[520,940],[0,'para de bater'],size=100,cor='tinta'),nota('prefere andar',[520,1130],[1,'andar'],cor='laranja',size=62)]),
  dict(id='c6',frases=[f("E hoje? O polvo virou estrela: o documentário Professor Polvo ganhou o Oscar de 2021.","E hoje? O polvo virou estrela: o documentário Professor Polvo ganhou o Oscar de dois mil e vinte e um.")],
   elementos=[obj('polvo',[340,720],None,w=360,ang=-5),obj('medalha',[740,620],[0,'Oscar'],w=240),tira('OSCAR 2021',[700,900],[0,'Oscar'],size=56),nota('estrela!',[520,1110],[0,'estrela'],cor='laranja',size=72)]),
  dict(id='c7',frases=[f("Então: três corações, e um deles tira folga quando o polvo nada."),f("Que bicho você quer ver aqui? Comenta."),ASS],
   elementos=[obj('polvo',[520,640],None,w=440,ang=3),bloco('que bicho é o próximo?',[520,1080],[1,'bicho'],size=68),nota('comenta!',[780,450],[1,0.6],cor='laranja')])])
# ------------------------------------------------------------ 013 HISTÓRIA
EPS['SSA-013']=dict(materia='HISTÓRIA',titulo='O quadro do Grito foi pintado 66 anos depois',
 fontes=["ONO, Rosaria; LIMA, Solange F. de. 'O novo Museu do Ipiranga no bicentenário da Independência do Brasil' (2022).","CartaCapital, reportagem sobre a restauração do Museu do Ipiranga (2022).","Revista de Estudios Brasileños (USP/Salamanca), entrevista com o vice-diretor do Museu Paulista (2022).","SBT News, 'Museu do Ipiranga recebeu 1 milhão de visitantes' (2024)."],
 capa=dict(elementos=[obj('moldura',[520,660],w=600,h=420),num('66',[280,450],size=220),bloco('anos depois do grito',[540,1110],size=72)]),
 cenas=[
  dict(id='c1',frases=[f("O quadro mais famoso da Independência foi pintado 66 anos depois do grito.","O quadro mais famoso da Independência foi pintado sessenta e seis anos depois do grito."),f("E o pintor nem tinha nascido em 1822.","E o pintor nem tinha nascido em mil oitocentos e vinte e dois.")],
   elementos=[obj('moldura',[520,660],None,w=600,h=420,balanca=True),num('66',[260,450],None,size=200),bloco('anos depois',[620,1000],None,size=80),tira('1822',[330,1150],[1,'1822'],size=56)]),
  dict(id='c2',fonte='Fonte: Ono e Lima (2022)',frases=[f("É Independência ou Morte, de Pedro Américo."),f("Foi encomendado em 1886 e entregue em 1888.","Foi encomendado em mil oitocentos e oitenta e seis e entregue em mil oitocentos e oitenta e oito."),f("Pedro Américo nasceu em 1843. Ele pintou uma cena que nunca viu.","Pedro Américo nasceu em mil oitocentos e quarenta e três. Ele pintou uma cena que nunca viu.")],
   elementos=[tira('"INDEPENDÊNCIA OU MORTE!"',[520,430],None,size=46),obj('moldura',[520,680],None,w=460,h=320),tira('encomenda: 1886',[300,920],[1,'1886'],size=46),tira('entrega: 1888',[700,980],[1,'1888'],size=46),
     nota('nunca viu a cena',[520,1150],[2,'nunca'],cor='laranja',size=60)]),
  dict(id='c3',fonte='Fonte: CartaCapital (2022)',frases=[f("E é enorme: tem 7 metros e 60 de largura por 4 metros e 15 de altura.","E é enorme: tem sete metros e sessenta de largura por quatro metros e quinze de altura."),f("Tão grande que, na reforma do museu, não passava pela porta.")],
   camera=dict(push=0.04,zooms=[dict(e=[1,'porta'],escala=1.25,alvo=[520,700],dur=0.8)]),
   elementos=[obj('moldura',[520,660],None,w=640,h=360),bloco('7,60 m × 4,15 m',[520,960],[0,'7'],size=74),nota('não passava pela porta!',[520,1140],[1,'porta'],cor='laranja',size=58)]),
  dict(id='c4',fonte='Fonte: CartaCapital (2022)',frases=[f("Então ele ficou lá dentro, protegido, no meio das obras.")],
   elementos=[obj('castelo',[520,700],None,w=520,h=380),bloco('ficou lá dentro',[520,1060],[0,'dentro'],size=80)]),
  dict(id='c5',fonte='Fonte: Museu do Ipiranga (curadoria) via ABCdoABC',frases=[f("E o próprio museu lembra: essa imagem é uma construção. O pintor imaginou a cena."),f("Quadro histórico não é fotografia.")],
   elementos=[bloco('imagem = construção',[520,560],None,size=76),obj('moldura',[520,860],[0,'imaginou'],w=420,h=300,ang=-3),bloco('não é foto',[640,1130],[1,'fotografia'],size=70,cor='tinta',ang=-3)]),
  dict(id='c6',fonte='Fonte: USP (REB, 2022); SBT News (2024)',frases=[f("E hoje? Depois de quase dez anos fechado, o Museu do Ipiranga reabriu em setembro de 2022, no bicentenário da Independência.","E hoje? Depois de quase dez anos fechado, o Museu do Ipiranga reabriu em setembro de dois mil e vinte e dois, no bicentenário da Independência."),f("Em menos de dois anos, recebeu 1 milhão de visitantes.","Em menos de dois anos, recebeu um milhão de visitantes.")],
   elementos=[obj('castelo',[520,640],None,w=500,h=360),tira('REABERTURA: SET/2022',[520,900],[0,'reabriu'],size=50),dict(t='contador',de=0,ate=1000000,fmt='{n} visitantes',pos=[520,1080],e=[1,'milhão'],size=64)]),
  dict(id='c7',frases=[f("Então: a cena do grito que todo mundo conhece foi imaginada décadas depois."),f("Você já foi ao Museu do Ipiranga? Comenta."),ASS],
   elementos=[obj('moldura',[520,640],None,w=520,h=360,ang=2),bloco('você já foi?',[520,1060],[1,'Museu'],size=80),nota('comenta!',[780,1180],[1,0.7],cor='laranja')])])
# ------------------------------------------------------------ 014 MATEMÁTICA
EPS['SSA-014']=dict(materia='MATEMÁTICA',titulo='Quem transformou o zero em número',
 fontes=["Discover Magazine, 'How We Discovered the Number Zero'.","BRAHMAGUPTA. Brahmasphutasiddhanta (628 d.C.).","FIBONACCI, Leonardo. Liber Abaci (1202).","SEN, S. K.; AGARWAL, R. P. 'Much ado about zero' (arXiv:1601.05983)."],
 capa=dict(elementos=[num('0',[520,700],size=620),tira('ÍNDIA, 628',[300,440],size=56),bloco('o nada que virou número',[520,1130],size=70)]),
 cenas=[
  dict(id='c1',frases=[f("Por muito tempo, o zero nem era considerado um número."),f("Quem mudou isso foi um matemático da Índia, no ano 628.","Quem mudou isso foi um matemático da Índia, no ano seiscentos e vinte e oito.")],
   elementos=[num('0',[520,700],None,size=620),tira('ÍNDIA, 628',[300,440],[1,'Índia'],size=56),bloco('nem era número',[640,1120],None,size=72,cor='tinta')]),
  dict(id='c2',fonte='Fonte: Discover Magazine',frases=[f("Antes, povos como os sumérios e os maias já tinham a ideia de nada."),f("Mas o zero era só um marcador de lugar, um espaço vazio na conta.")],
   elementos=[tira('sumérios',[320,480],[0,'sumérios'],size=56),tira('maias',[700,560],[0,'maias'],size=56),bloco('2 _ 5',[520,820],[1,'marcador'],size=130,cor='tinta'),nota('marcador de lugar',[520,1060],[1,'marcador'],cor='laranja',size=60)]),
  dict(id='c3',fonte='Fonte: Discover Magazine',frases=[f("Em 628, Brahmagupta escreveu regras pra fazer conta com o zero.","Em seiscentos e vinte e oito, Bramagupta escreveu regras pra fazer conta com o zero."),f("Um número mais zero dá ele mesmo. Um número vezes zero dá zero.")],
   elementos=[tira('BRAHMAGUPTA, 628',[520,440],None,size=52),bloco('5 + 0 = 5',[520,700],[1,'mais'],size=110),bloco('5 × 0 = 0',[520,950],[1,'vezes'],size=110,cor='tinta')]),
  dict(id='c4',fonte='Fonte: Kronecker Wallis',frases=[f("Ele até tentou dividir por zero, e não acertou."),f("Essa conta deu dor de cabeça por séculos.")],
   elementos=[bloco('5 ÷ 0 = ?',[520,640],None,size=120),nota('não acertou',[700,880],[0,'acertou'],cor='laranja',size=66),obj('lampada',[320,1000],[1,'séculos'],w=220)]),
  dict(id='c5',fonte='Fonte: Discover Magazine; arXiv (2016)',frases=[f("O zero viajou da Índia pros árabes e chegou à Europa com Fibonacci, num livro de 1202.","O zero viajou da Índia pros árabes e chegou à Europa com Fibonátchi, num livro de mil duzentos e dois."),f("O nome veio junto: sunya, vazio, virou sifr, depois zephirum, e enfim zero.","O nome veio junto: xúnia, vazio, virou sífr, depois zefírum, e enfim zero.")],
   elementos=[tira('ÍNDIA',[260,440],None,size=50),seta([380,460],[520,520],[0,'árabes']),tira('ÁRABES',[600,540],[0,'árabes'],size=50),seta([620,600],[520,680],[0,'Europa']),tira('FIBONACCI, 1202',[420,720],[0,'Fibonacci'],size=46),
     tira('sunya',[300,900],[1,'sunya'],size=46),tira('sifr',[560,960],[1,'sifr'],size=46),tira('zephirum',[330,1060],[1,'zephirum'],size=46),bloco('zero',[700,1120],[1,'enfim'],size=80)]),
  dict(id='c6',fonte='Fonte: eCycle',frases=[f("E hoje? Seu celular funciona com zeros e uns."),f("Sem o zero, não tinha computador. Nem este vídeo.")],
   elementos=[obj('computador',[520,640],None,w=460),tira('0 1 1 0 1 0',[520,950],[0,'zeros'],size=60),nota('nem este vídeo!',[520,1120],[1,'vídeo'],cor='laranja',size=64)]),
  dict(id='c7',frases=[f("Então: o nada virou a base de tudo."),f("Qual número você acha mais importante depois do zero? Comenta."),ASS],
   elementos=[num('0',[520,640],None,size=520),bloco('o nada virou tudo',[520,1080],[0,'nada'],size=76),nota('comenta!',[780,1180],[1,0.6],cor='laranja')])])
for k_,v_ in {'SSA-008': ["IFLScience, 'Marie Curie died from her radioactivity research...'.", "Abakcus, 'Marie Curie’s Radioactive Notebooks'."], 'SSA-014': ['Kronecker Wallis, artigo sobre a história do zero.', "eCycle, 'Zero: conheça a história do número'."], 'SSA-009': ["Science ABC, 'What is wrong with all our maps?'."], 'SSA-013': ["ABCdoABC, 'Museu do Ipiranga inaugura três exposições em estações do Metrô' (curadoria de Paulo César Garcez Marins)."], 'SSA-012': ["Academia de Artes e Ciências Cinematográficas: 'Professor Polvo' (My Octopus Teacher), Oscar de Melhor Documentário em 2021."], 'SSA-011': ["Big Think, 'Newton’s apple tree has descendants and clones all over the world'."]}.items(): EPS[k_]['fontes']+=v_
for k_,v_ in {'SSA-002': 'QUEM APAGOU ESSES DIAS?', 'SSA-003': 'VOCÊ ESTÁ NA CAVERNA?', 'SSA-004': 'O ROUBO QUE MUDOU TUDO', 'SSA-005': 'VOCÊ FALA ISSO TODO DIA', 'SSA-006': 'A REVOLUÇÃO QUE MUDOU TUDO', 'SSA-007': 'POR QUE ESSE NÚMERO?', 'SSA-008': 'PERIGO NA BIBLIOTECA', 'SSA-009': 'VOCÊ APRENDEU ISSO ERRADO?', 'SSA-010': 'MITO OU VERDADE?', 'SSA-011': 'VOCÊ APRENDEU ISSO ERRADO?', 'SSA-012': 'POR QUE ISSO ACONTECE?', 'SSA-013': 'O SEGREDO POR TRÁS DO QUADRO', 'SSA-014': 'QUEM INVENTOU ISSO?'}.items(): EPS[k_]['chamada']=v_
# fix: verbete key name
for k,ep in EPS.items():
    for c in ep['cenas']:
        for el in c['elementos']:
            if el.get('t')=='verbete' and 'defi' in el: el['def']=el.pop('defi')
            if el.get('e') is None: el.pop('e',None)
        if c.get('fonte') is None: c.pop('fonte',None)
    os.makedirs(f'{BASE}/{k}',exist_ok=True)
    ep['id']=k
    json.dump(ep,open(f'{BASE}/{k}/roteiro.json','w'),ensure_ascii=False,indent=1)
    w=sum(len(fr[1].split()) for c in ep['cenas'] for fr in c['frases'])
    first=ep['cenas'][0]['frases'][0][0]
    print(k,ep['materia'],w,'palavras | gancho:',len(first.split()),'palavras')
