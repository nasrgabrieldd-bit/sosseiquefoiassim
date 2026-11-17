"""Gera os roteiros do lote 2 (SSA-015 a SSA-034, 20/11 a 29/11/2026). Não rode depois de produzir: sobrescreve roteiros."""
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
EPS={}

# ------------------------------------------------------------ 015 LÍNGUA PORTUGUESA (20/11 · Consciência Negra)
EPS['SSA-015']=dict(materia='LÍNGUA PORTUGUESA',titulo='A palavra "quilombo" nem é portuguesa',
 fontes=["Houaiss, Dicionário da Língua Portuguesa, verbete 'quilombo'.","Museu Afro Brasil, 'Palavras de origem africana no português' (2023).","Instituto Federal de Alagoas, 'Serra da Barriga e o legado de Palmares' (2021)."],
 capa=dict(elementos=[obj('livro',[520,650],w=420,ang=-3),bloco('a palavra "quilombo" nem é portuguesa',[520,1150],size=66,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f('"Quilombo" não é uma palavra portuguesa. Nunca foi.'),f("E isso conta uma história inteira.")],
   elementos=[obj('livro',[520,640],None,w=420,ang=-3,balanca=True),bloco('não é palavra\nportuguesa!',[520,1080],None,size=68,maxw=700)]),
  dict(id='c2',fonte='Fonte: Houaiss, verbete "quilombo"',frases=[f("Ela vem do kimbundu, língua falada em Angola."),f("'Kilombo' queria dizer acampamento de guerreiros.")],
   elementos=[tira('KIMBUNDU · ANGOLA',[300,430]),obj('globo',[520,750],[0,0.1],w=340,ang=-4),tira('kilombo = acampamento de guerreiros',[560,1120],[1,0.1],size=42)]),
  dict(id='c3',frases=[f("No Brasil colonial, virou o nome dado às comunidades de pessoas escravizadas que fugiam e se organizavam livres."),f("Existiram centenas desses quilombos espalhados pelo país, de tamanhos bem diferentes."),f("O mais famoso de todos foi o Quilombo dos Palmares.")],
   elementos=[bloco('comunidades livres',[520,560],None,size=70),nota('o mais famoso:\nPalmares',[600,900],[2,'Palmares'],size=56,cor='laranja')]),
  dict(id='c4',fonte='Fonte: Museu Afro Brasil (2023)',frases=[f("E não é a única: moleque, cafuné, caçula e curinga também vieram de línguas africanas."),f("Muita gente fala essas palavras todo dia sem saber a origem.")],
   elementos=[tira('moleque',[260,460],[0,'moleque'],size=48),tira('cafuné',[760,560],[0,'cafuné'],size=48),tira('caçula',[300,700],[0,'caçula'],size=48),tira('curinga',[720,800],[0,'curinga'],size=48),nota('todo dia, sem saber!',[520,1080],[1,0.3],cor='laranja')]),
  dict(id='c5',frases=[f("Dá pra pensar assim: parte do português do Brasil é africano antes de ser europeu."),f("Estima-se que mais de 200 línguas africanas diferentes chegaram ao Brasil durante o período da escravidão.","Estima-se que mais de duzentas línguas africanas diferentes chegaram ao Brasil durante o período da escravidão.")],
   camera=dict(push=0.08),elementos=[obj('livro',[520,650],None,w=460),bloco('português do Brasil\ntambém é africano',[520,1120],None,size=58,maxw=780)]),
  dict(id='c6',fonte='Fonte: Lei 14.759/2023',frases=[f("E hoje? Hoje, 20 de novembro, é Dia da Consciência Negra, feriado nacional desde 2023.","E hoje? Hoje, vinte de novembro, é Dia da Consciência Negra, feriado nacional desde dois mil e vinte e três."),f("A data lembra Zumbi dos Palmares, morto nesse dia em 1695.","A data lembra Zumbi dos Palmares, morto nesse dia em mil seiscentos e noventa e cinco.")],
   elementos=[dict(t='cal',titulo='NOVEMBRO',inicio=1,riscar=[20],pos=[520,680],ang=-2),tira('ZUMBI DOS PALMARES · 1695',[520,1100],[1,'Zumbi'],size=44)]),
  dict(id='c7',frases=[f("Então: uma palavra de guerra virou símbolo de resistência, e ainda mora no seu vocabulário."),f("Que outra palavra brasileira você acha que pode ter vindo da África? Comenta."),ASS],
   elementos=[obj('livro',[520,640],None,w=420,ang=2),bloco('qual outra palavra?',[520,1080],[1,0.1],size=68),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 016 HISTÓRIA (20/11 · Consciência Negra)
EPS['SSA-016']=dict(materia='HISTÓRIA',titulo='Palmares resistiu quase 100 anos. Alagoas inteira tremeu',
 fontes=["EBSCO Research Starters, 'Slaves Resist Europeans at Palmares'.","Cultural Survival Quarterly, 'Quilombo: Brazilian Maroons during slavery'.","Wikipedia/estudiosos citados, estimativa de população de Palmares (1690s)."],
 capa=dict(elementos=[obj('castelo',[520,660],w=560,ang=-2),num('100',[520,1150],None,size=200,cor='tinta'),bloco('anos resistindo',[520,1330],size=56)]),
 cenas=[
  dict(id='c1',frases=[f("Teve um lugar no Brasil que resistiu a exércitos por quase 100 anos. Sem presidente, sem exército oficial.","Teve um lugar no Brasil que resistiu a exércitos por quase cem anos. Sem presidente, sem exército oficial.")],
   elementos=[obj('castelo',[520,660],None,w=580,ang=-2,balanca=True),num('100',[520,1120],None,size=220,cor='laranja')]),
  dict(id='c2',fonte='Fonte: Cultural Survival Quarterly',frases=[f("Era o Quilombo dos Palmares, fundado por volta de 1605, na Serra da Barriga, em Alagoas.","Era o Quilombo dos Palmares, fundado por volta de mil seiscentos e cinco, na Serra da Barriga, em Alagoas.")],
   elementos=[tira('SERRA DA BARRIGA · ALAGOAS',[520,460]),obj('globo',[520,780],[0,0.3],w=320,ang=3)]),
  dict(id='c3',fonte='Fonte: EBSCO Research Starters',frases=[f("Em seu auge, chegou a ter mais de 20 mil pessoas vivendo lá.","Em seu auge, chegou a ter mais de vinte mil pessoas vivendo lá."),f("Isso era mais gente do que várias cidades europeias da época."),f("Palmares tinha até divisão entre vilas, cada uma com seu próprio chefe local.")],
   elementos=[num('20 mil',[520,600],None,size=160,cor='tinta'),nota('pessoas vivendo\nlivres',[300,1000],[0,0.1],size=58),dict(t='contador',de=1,ate=20,fmt='+ {n} mil pessoas',pos=[700,1120],e=[0,0.5])]),
  dict(id='c4',frases=[f("Os moradores plantavam, criavam animais e treinavam seus próprios guerreiros."),f("Pelo menos seis expedições portuguesas tentaram destruir Palmares e fracassaram.","Pelo menos seis expedições portuguesas tentaram destruir Palmares e fracassaram."),f("Alguns relatos da época chegaram a chamar os moradores de Palmares de 'invencíveis'.")],
   elementos=[seta([260,700],[780,700],None),bloco('6 expedições\nfalharam',[520,1080],[1,'seis'],size=64,maxw=700)]),
  dict(id='c5',fonte='Fonte: almapreta.com.br, "Há exatos 327 anos" (2021)',frases=[f("Só caiu em 1694, numa madrugada de ataque surpresa com tropas e canhões.","Só caiu em mil seiscentos e noventa e quatro, numa madrugada de ataque surpresa com tropas e canhões."),f("Zumbi, o último líder, foi morto no ano seguinte, em 20 de novembro de 1695.","Zumbi, o último líder, foi morto no ano seguinte, em vinte de novembro de mil seiscentos e noventa e cinco.")],
   camera=dict(push=0.08),elementos=[obj('castelo',[520,660],None,w=560,ang=4),risco([320,900],[760,900],[1,'morto']),nota('20/11/1695',[520,1150],[1,'1695'],cor='laranja',size=60)]),
  dict(id='c6',fonte='Fonte: Lei 14.759/2023',frases=[f("E hoje? Esse dia virou o Dia da Consciência Negra, feriado nacional em todo o país desde 2023.","E hoje? Esse dia virou o Dia da Consciência Negra, feriado nacional em todo o país desde dois mil e vinte e três.")],
   elementos=[dict(t='cal',titulo='NOVEMBRO',inicio=1,riscar=[20],pos=[520,700],ang=2),bloco('feriado nacional',[520,1150],None,size=66)]),
  dict(id='c7',frases=[f("Então: quase 100 anos de resistência por uma comunidade inteira, livre, no meio do Brasil colonial.","Então: quase cem anos de resistência por uma comunidade inteira, livre, no meio do Brasil colonial."),f("Marca aquele amigo que precisa conhecer essa história."),ASS],
   elementos=[obj('castelo',[520,640],None,w=520,ang=-3),bloco('marca um amigo',[520,1080],[1,'amigo'],size=66),nota('essa história\nprecisa rodar',[760,1180],[0,0.6],cor='laranja',size=46)])])

# ------------------------------------------------------------ 017 GEOGRAFIA (21/11 · final da Sul-Americana)
EPS['SSA-017']=dict(materia='GEOGRAFIA',titulo='A América do Sul tem 13 países. Só 10 jogam a Libertadores',
 fontes=["CONMEBOL, '104 anos de uma grande história' (relatório institucional).","Wikipedia/CONMEBOL, lista de associações-membro.","Conmebol.com, calendário oficial de 2026 (final da Sul-Americana, 21/11)."],
 capa=dict(elementos=[obj('globo',[520,650],w=440,ang=-3),num('10',[520,1150],None,size=220,cor='laranja'),bloco('países na Conmebol',[520,1330],size=54)]),
 cenas=[
  dict(id='c1',frases=[f("A América do Sul tem 13 países. A Conmebol só tem 10.","A América do Sul tem treze países. A Conmebol só tem dez.")],
   elementos=[obj('globo',[520,660],None,w=460,ang=-3,balanca=True),num('13 → 10',[520,1130],None,size=130,cor='tinta')]),
  dict(id='c2',fonte='Fonte: CONMEBOL, relatório institucional',frases=[f("A Conmebol é a confederação de futebol do continente, fundada em Buenos Aires em 1916.","A Conmebol é a confederação de futebol do continente, fundada em Buenos Aires em mil novecentos e dezesseis.")],
   elementos=[tira('BUENOS AIRES · 1916',[520,460]),obj('medalha',[520,780],[0,'1916'],w=280,ang=4)]),
  dict(id='c3',frases=[f("Ela é mais velha que a própria Copa do Mundo, que só nasceu em 1930.","Ela é mais velha que a própria Copa do Mundo, que só nasceu em mil novecentos e trinta."),f("É a confederação continental de futebol mais antiga do planeta.")],
   elementos=[num('1916',[300,600],None,size=140,cor='tinta'),num('1930',[760,780],None,size=140,cor='laranja'),seta([400,680],[680,720],[0,0.3]),bloco('a mais antiga\ndo mundo',[520,1120],[1,0.3],size=60)]),
  dict(id='c4',frases=[f("Mas Guiana, Suriname e Guiana Francesa ficam de fora."),f("Historicamente, jogam mais perto das confederações do Caribe e da América Central do que da Conmebol."),f("A Guiana Francesa, inclusive, nem é um país independente: é um território da França.")],
   elementos=[tira('GUIANA',[280,460],[0,'Guiana']),tira('SURINAME',[760,540],[0,'Suriname']),tira('GUIANA FRANCESA',[520,660],[0,'Francesa'],size=40),nota('ficam de fora',[520,1080],[0,0.6],cor='laranja',size=60)]),
  dict(id='c5',frases=[f("Por isso só 10 seleções disputam a Libertadores, a Sul-Americana e a Copa América.","Por isso só dez seleções disputam a Libertadores, a Sul-Americana e a Copa América."),f("A Copa América, inclusive, é a competição de seleções mais antiga do mundo ainda em disputa.")],
   camera=dict(push=0.07),elementos=[obj('medalha',[520,680],None,w=320),bloco('10 associações-membro',[520,1100],None,size=62)]),
  dict(id='c6',fonte='Fonte: calendário oficial Conmebol 2026',frases=[f("E hoje? Hoje, 21 de novembro, é a final da Copa Sul-Americana de 2026, em Barranquilla, na Colômbia.","E hoje? Hoje, vinte e um de novembro, é a final da Copa Sul-Americana de dois mil e vinte e seis, em Barranquilla, na Colômbia.")],
   elementos=[tira('BARRANQUILLA · COLÔMBIA',[520,460]),obj('globo',[520,780],[0,'Barranquilla'],w=320,ang=-2)]),
  dict(id='c7',frases=[f("Então: o mapa da América do Sul e o mapa do futebol sul-americano não são exatamente o mesmo mapa."),f("Você sabia que tinha só 10 países na Conmebol? Comenta."),ASS],
   elementos=[obj('globo',[520,640],None,w=420,ang=2),bloco('você sabia?',[520,1080],[1,'sabia'],size=70),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 018 QUÍMICA
EPS['SSA-018']=dict(materia='QUÍMICA',titulo='Chocolate branco não é chocolate, segundo a lei',
 fontes=["Codex Alimentarius (FAO/OMS), norma para produtos de cacau e chocolate.","Anvisa, RDC 264/2005, padrão de identidade e qualidade de produtos de cacau.","Enciclopédia Britannica, verbete 'white chocolate'."],
 capa=dict(elementos=[obj('frasco',[520,660],w=380,ang=-3),bloco('chocolate branco não é chocolate',[520,1150],size=62,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Chocolate branco, pela lei, não é chocolate."),f("E não é força de expressão.")],
   elementos=[obj('frasco',[520,660],None,w=400,ang=-3,balanca=True),bloco('não é chocolate\nde verdade!',[520,1100],None,size=66,maxw=700)]),
  dict(id='c2',fonte='Fonte: Anvisa, RDC 264/2005',frases=[f("Pra se chamar chocolate, um produto precisa ter sólidos de cacau: a parte sólida e marrom da amêndoa, cheia de cacau em pó.")],
   elementos=[tira('CHOCOLATE = SÓLIDOS DE CACAU',[520,480],size=42),obj('frasco',[520,800],[0,'sólidos'],w=320,ang=4)]),
  dict(id='c3',frases=[f("O chocolate branco não leva nada disso."),f("Ele é feito só de manteiga de cacau, açúcar e leite em pó."),f("Essa mistura, inclusive, foi criada originalmente como um jeito de aproveitar sobras da produção de chocolate normal.")],
   elementos=[risco([300,500],[740,500],None),tira('manteiga de cacau + açúcar + leite',[520,900],[1,0.2],size=40)]),
  dict(id='c4',frases=[f("A manteiga de cacau é a gordura da amêndoa, sem cor, sem sabor de chocolate e sem cafeína.")],
   camera=dict(push=0.07),elementos=[bloco('é só gordura\naromatizada',[520,700],None,size=64,maxw=720),nota('zero cafeína',[520,1080],[0,0.7],cor='laranja',size=56)]),
  dict(id='c5',frases=[f("Por isso órgãos como a Anvisa e o Codex Alimentarius, que regula alimentos no mundo todo, exigem a palavra 'branco' no rótulo."),f("Sem sólidos de cacau, legalmente, o produto não pode nem se chamar 'chocolate' sozinho no nome.")],
   elementos=[tira('CODEX ALIMENTARIUS',[520,460]),bloco('"branco" é\nobrigatório no rótulo',[520,880],[0,'rótulo'],size=56,maxw=740)]),
  dict(id='c6',frases=[f("E hoje? Supermercados brasileiros vendem o chocolate branco do lado do chocolate de verdade, com o mesmo cheiro de doce.")],
   elementos=[obj('frasco',[300,650],None,w=300,ang=-3),obj('frasco',[760,650],[0,0.6],w=300,ang=3,cor='laranja'),bloco('lado a lado\nna prateleira',[520,1120],None,size=58)]),
  dict(id='c7',frases=[f("Então: o chocolate branco nunca viu a parte do cacau que dá o gosto de chocolate."),f("Agora você sabe por que o chocolate branco é tão diferente dos outros."),ASS],
   elementos=[obj('frasco',[520,650],None,w=380,ang=2),bloco('agora você sabe',[520,1100],[1,'sabe'],size=66)])])

# ------------------------------------------------------------ 019 BIOLOGIA
EPS['SSA-019']=dict(materia='BIOLOGIA',titulo='Por que bocejo é contagioso (até ler isso pode te dar um)',
 fontes=["Baylor College of Medicine, 'Yawning: an exercise in empathy' (2016).","University of Nottingham, pesquisa de Catriona Morrison sobre bocejo contagioso (2010).","Scientific American, 'Why Is Yawning Contagious?' (2007)."],
 capa=dict(elementos=[bloco('bocejo é contagioso.\naté ler isso pode dar um',[520,700],size=58,maxw=820),nota('...',[520,1100],size=120,cor='laranja')]),
 cenas=[
  dict(id='c1',frases=[f("Só de ler a palavra bocejo, seu cérebro já pode estar se preparando pra bocejar.")],
   elementos=[bloco('seu cérebro já\ntá se preparando',[520,660],None,size=66,maxw=760),nota('bocejo',[520,1080],None,cor='laranja',size=90)]),
  dict(id='c2',fonte='Fonte: Scientific American (2007)',frases=[f("Bocejo contagioso existe de verdade, e cientistas estudam isso há décadas."),f("Cerca de 60% das pessoas bocejam ao ver outra pessoa bocejando.","Cerca de sessenta por cento das pessoas bocejam ao ver outra pessoa bocejando.")],
   elementos=[num('60%',[520,600],None,size=200,cor='tinta'),tira('bocejam ao ver\noutra pessoa',[520,1050],[1,0.3],size=44)]),
  dict(id='c3',fonte='Fonte: Baylor College of Medicine (2016)',frases=[f("A explicação mais aceita é a empatia: quanto mais ligado você é à pessoa, mais fácil pegar o bocejo dela.")],
   elementos=[obj('coracao',[300,650],None,w=260,ang=-4),seta([420,650],[680,650],None),obj('coracao',[760,650],[0,0.6],w=260,ang=4),bloco('empatia',[520,1080],[0,'empatia'],size=70)]),
  dict(id='c4',fonte='Fonte: Universidade de Nottingham (2010)',frases=[f("Numa pesquisa de 2010, pessoas com mais empatia bocejavam mais ao ver vídeos de outras pessoas bocejando.","Numa pesquisa de dois mil e dez, pessoas com mais empatia bocejavam mais ao ver vídeos de outras pessoas bocejando.")],
   elementos=[tira('NOTTINGHAM · 2010',[520,460]),nota('mais empatia =\nmais bocejo',[520,860],[0,0.4],size=58)]),
  dict(id='c5',frases=[f("Até cachorros bocejam quando veem o dono bocejando."),f("E bebês recém-nascidos ainda não pegam o contágio: isso só aparece depois dos 4 ou 5 anos.","E bebês recém-nascidos ainda não pegam o contágio: isso só aparece depois dos quatro ou cinco anos."),f("Pessoas com certas condições que afetam a empatia também bocejam menos ao ver outras bocejando.")],
   camera=dict(push=0.06),elementos=[bloco('cachorros\ntambém pegam',[300,700],None,size=56,maxw=560),num('4-5 anos',[760,900],[1,0.5],size=80,cor='laranja')]),
  dict(id='c6',frases=[f("E hoje? Em reunião, aula ou live, repara: um bocejo costuma puxar outro pela sala inteira."),f("Até ver alguém bocejando numa tela de vídeo já é o suficiente pra ativar o contágio.")],
   elementos=[obj('celular',[520,660],None,w=320),bloco('repara na\npróxima reunião',[520,1100],None,size=58,maxw=740)]),
  dict(id='c7',frases=[f("Então: bocejo pode ser, no fundo, um sinal de quanto você se conecta com quem tá do seu lado."),f("Salva esse vídeo pra lembrar na próxima vez que bocejar."),ASS],
   elementos=[obj('coracao',[520,640],None,w=300,ang=-2),bloco('salva pra lembrar',[520,1080],[1,'salva'],size=64)])])

# ------------------------------------------------------------ 020 ARTE
EPS['SSA-020']=dict(materia='ARTE',titulo='A Vênus de Milo perdeu os braços, e ninguém sabe onde foram parar',
 fontes=["Museu do Louvre, ficha da obra 'Vênus de Milo'.","History.com, 'What happened to the Venus de Milo's arms?' (2015).","Todamatéria, 'Vênus de Milo' (biografia e contexto)."],
 capa=dict(elementos=[obj('moldura',[520,660],w=480,ang=-2),bloco('ninguém sabe onde foram parar os braços',[520,1150],size=56,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Uma das estátuas mais famosas do mundo não tem braços. E ninguém nunca os encontrou.")],
   elementos=[obj('moldura',[520,660],None,w=500,ang=-2,balanca=True),bloco('sem braços.\nnunca encontrados',[520,1100],None,size=62,maxw=740)]),
  dict(id='c2',fonte='Fonte: Museu do Louvre',frases=[f("É a Vênus de Milo, descoberta em 1820 por um fazendeiro grego na ilha de Milos.","É a Vênus de Milo, descoberta em mil oitocentos e vinte por um fazendeiro grego na ilha de Milos.")],
   elementos=[tira('ILHA DE MILOS · 1820',[520,460]),obj('globo',[520,780],[0,'1820'],w=300,ang=3)]),
  dict(id='c3',frases=[f("Ela já estava partida em pedaços quando foi achada, enterrada havia uns 2 mil anos.","Ela já estava partida em pedaços quando foi achada, enterrada havia uns dois mil anos."),f("A estátua tem quase 2 metros de altura e pesa cerca de 900 quilos de mármore.","A estátua tem quase dois metros de altura e pesa cerca de novecentos quilos de mármore.")],
   elementos=[num('2.000 anos',[520,600],None,size=110,cor='tinta'),nota('enterrada,\npartida',[520,1000],[0,0.4],size=58)]),
  dict(id='c4',fonte='Fonte: History.com (2015)',frases=[f("Os braços sumiram antes mesmo de ela chegar à França."),f("Há marcas nos ombros, mas nenhum pedaço de braço jamais apareceu."),f("Furos no corpo da estátua sugerem que ela usava joias, como brincos e um bracelete, que também nunca foram achados.")],
   elementos=[risco([300,500],[740,500],None),bloco('nenhum pedaço\njamais apareceu',[520,900],[1,0.2],size=58,maxw=740)]),
  dict(id='c5',frases=[f("Mesmo assim, em 1821, ela foi parar no Museu do Louvre, em Paris, onde está até hoje.","Mesmo assim, em mil oitocentos e vinte e um, ela foi parar no Museu do Louvre, em Paris, onde está até hoje.")],
   camera=dict(push=0.08),elementos=[obj('moldura',[520,680],None,w=460),tira('MUSEU DO LOUVRE',[520,1120],[0,'Louvre'],size=46)]),
  dict(id='c6',frases=[f("E hoje? Milhões de turistas tiram foto dela todo ano, braços ausentes e tudo."),f("Ela é, hoje, uma das obras mais reproduzidas em pôsteres e livros de arte do mundo.")],
   elementos=[obj('celular',[520,660],None,w=300,ang=-3),bloco('milhões de fotos\npor ano',[520,1100],None,size=58,maxw=720)]),
  dict(id='c7',frases=[f("Então: a estátua mais fotografada do Louvre guarda, até hoje, um mistério sem solução."),f("Time A: braços colados. Time B: deixa assim mesmo. Comenta."),ASS],
   elementos=[obj('moldura',[520,640],None,w=440,ang=2),bloco('time A ou time B?',[520,1080],[1,'time'],size=64)])])

# ------------------------------------------------------------ 021 GEOGRAFIA
EPS['SSA-021']=dict(materia='GEOGRAFIA',titulo='Na Rússia, o réveillon dura 10 horas',
 fontes=["dadosmundiais.com, 'Fusos horários da Rússia'.","dateandtime.info, 'Hora local atual em Rússia'.","Diario de Pernambuco, 'O país que tem 11 fusos horários e atravessa dois continentes' (2026)."],
 capa=dict(elementos=[obj('globo',[520,650],w=440,ang=-3),num('11',[520,1150],None,size=220,cor='laranja'),bloco('fusos horários num país só',[520,1330],size=50)]),
 cenas=[
  dict(id='c1',frases=[f("Tem país em que o réveillon demora 10 horas pra acabar.","Tem país em que o réveillon demora dez horas pra acabar.")],
   elementos=[obj('globo',[520,660],None,w=460,ang=-3,balanca=True),num('10h',[520,1130],None,size=180,cor='tinta')]),
  dict(id='c2',fonte='Fonte: dadosmundiais.com',frases=[f("É a Rússia: o maior país do mundo tem 11 fusos horários diferentes.","É a Rússia: o maior país do mundo tem onze fusos horários diferentes.")],
   elementos=[tira('RÚSSIA · 17 MILHÕES DE KM²',[520,460],size=40),num('11 fusos',[520,800],[0,'11'],size=150,cor='laranja')]),
  dict(id='c3',frases=[f("Ela atravessa a Europa e a Ásia inteiras, de Kaliningrado até a Kamtchatka."),f("São quase 9 mil quilômetros de ponta a ponta.","São quase nove mil quilômetros de ponta a ponta."),f("Pra comparar: isso é mais do que o dobro da distância entre Oiapoque e Chuí, no Brasil.")],
   elementos=[seta([260,700],[780,700],None),num('9.000 km',[520,1080],[1,0.3],size=120,cor='tinta')]),
  dict(id='c4',fonte='Fonte: dateandtime.info',frases=[f("Enquanto um lado do país já tá dormindo, o outro ainda tá almoçando."),f("A diferença entre o leste e o oeste chega a 10 horas.","A diferença entre o leste e o oeste chega a dez horas."),f("Mesmo assim, o país inteiro usa o mesmo horário de verão: nenhum.")],
   elementos=[bloco('dormindo de\num lado...',[280,650],None,size=52,maxw=520),bloco('...almoçando\ndo outro',[760,900],[0,0.5],size=52,maxw=520,cor='laranja')]),
  dict(id='c5',frases=[f("Em 2010, o governo tentou reduzir o número de fusos pra facilitar os negócios do país. Não pegou, e voltaram os 11.","Em dois mil e dez, o governo tentou reduzir o número de fusos pra facilitar os negócios do país. Não pegou, e voltaram os onze.")],
   camera=dict(push=0.07),elementos=[dict(t='contador',de=9,ate=11,fmt='{n} fusos',pos=[520,700],e=[0,0.5]),nota('não pegou!',[520,1100],[0,0.8],cor='laranja',size=56)]),
  dict(id='c6',frases=[f("E hoje? O discurso de fim de ano do presidente russo é gravado uma vez e exibido 11 vezes, uma pra cada fuso.","E hoje? O discurso de fim de ano do presidente russo é gravado uma vez e exibido onze vezes, uma pra cada fuso.")],
   elementos=[obj('celular',[520,660],None,w=320),bloco('11 transmissões\nna mesma noite',[520,1100],None,size=56,maxw=740)]),
  dict(id='c7',frases=[f("Então: um país só, 11 fusos, e uma meia-noite que não acaba nunca de uma vez.","Então: um país só, onze fusos, e uma meia-noite que não acaba nunca de uma vez."),f("Você toparia morar num país com tantos fusos? Comenta."),ASS],
   elementos=[obj('globo',[520,640],None,w=420,ang=2),bloco('você toparia?',[520,1080],[1,'toparia'],size=68)])])

# ------------------------------------------------------------ 022 SOCIOLOGIA
EPS['SSA-022']=dict(materia='SOCIOLOGIA',titulo='O aperto de mão nasceu pra provar que você não tinha arma',
 fontes=["Encyclopaedia Britannica, 'handshake' (história do gesto).","Smithsonian Magazine, 'A Brief History of the Handshake' (2014).","BBC Future, 'The ancient history of the handshake' (2020)."],
 capa=dict(elementos=[nota('aperto de mão\n= "olha, sem arma"',[520,700],size=60,maxw=760,cor='laranja'),bloco('o aperto de mão nasceu pra provar isso',[520,1150],size=58,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("O aperto de mão começou como uma prova: 'olha, não tô armado'.")],
   elementos=[bloco('"olha, não tô\narmado"',[520,700],None,size=70,maxw=720),nota('aperto de mão',[520,1100],None,cor='laranja',size=60)]),
  dict(id='c2',fonte='Fonte: Smithsonian Magazine (2014)',frases=[f("Historiadores encontraram representações do gesto em esculturas da Grécia antiga, com quase 2.400 anos.","Historiadores encontraram representações do gesto em esculturas da Grécia antiga, com quase dois mil e quatrocentos anos.")],
   elementos=[tira('GRÉCIA ANTIGA',[520,460]),num('2.400 anos',[520,800],[0,'2.400'],size=140,cor='tinta')]),
  dict(id='c3',frases=[f("A ideia era simples: estender a mão direita, a mão da espada, mostrava que você vinha em paz."),f("Guerreiros de exércitos diferentes usavam o gesto pra negociar tréguas sem arriscar um ataque surpresa.")],
   elementos=[seta([300,650],[740,650],None),bloco('mão direita\n= mão da espada',[520,1020],None,size=58,maxw=760)]),
  dict(id='c4',fonte='Fonte: Encyclopaedia Britannica',frases=[f("O movimento de sacudir a mão teria vindo de testar se a outra pessoa escondia uma faca na manga.")],
   elementos=[nota('sacudir =\ntestar a manga',[520,700],[0,'manga'],size=58,maxw=700,cor='laranja')]),
  dict(id='c5',frases=[f("Em algumas culturas, o gesto virou até parte de rituais e cerimônias de amizade entre povos diferentes."),f("Já em outras culturas, como partes do Japão e da Tailândia, a reverência sempre foi mais comum do que o toque de mãos.")],
   camera=dict(push=0.06),elementos=[bloco('virou ritual\nde amizade',[520,700],None,size=62,maxw=720)]),
  dict(id='c6',fonte='Fonte: BBC Future (2020)',frases=[f("E hoje? Durante a pandemia, muita gente trocou o aperto de mão pelo toque de cotovelo, por medo de contágio."),f("Alguns ambientes de trabalho mantiveram esse hábito até depois da pandemia passar.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('cotovelo no\nlugar da mão',[520,1100],None,size=58,maxw=720)]),
  dict(id='c7',frases=[f("Então: um gesto que virou educação começou como uma forma de dizer 'pode confiar em mim'."),f("Qual outro cumprimento você acha estranho? Comenta."),ASS],
   elementos=[bloco('qual cumprimento\nvocê acha estranho?',[520,700],[1,'estranho'],size=58,maxw=760),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 023 FILOSOFIA
EPS['SSA-023']=dict(materia='FILOSOFIA',titulo='Se você trocar toda peça de um navio, ele ainda é o mesmo navio?',
 fontes=["Plutarco, Vidas Paralelas, 'Vida de Teseu'.","Stanford Encyclopedia of Philosophy, 'Material Constitution'.","Encyclopaedia Britannica, 'Ship of Theseus'."],
 capa=dict(elementos=[bloco('se você trocar toda peça de um navio, ele ainda é o mesmo navio?',[520,750],size=58,maxw=820),nota('o paradoxo de Teseu',[520,1180],cor='laranja',size=48)]),
 cenas=[
  dict(id='c1',frases=[f("Se você trocar toda peça de um navio, ele ainda é o mesmo navio?")],
   elementos=[bloco('ainda é o\nmesmo navio?',[520,700],None,size=72,maxw=760)]),
  dict(id='c2',fonte='Fonte: Plutarco, Vida de Teseu',frases=[f("Essa pergunta vem de Plutarco, biógrafo grego, falando do navio do herói Teseu.","Essa pergunta vem de Plutarco, biógrafo grego, falando do navio do herói Teseu.")],
   elementos=[tira('PLUTARCO · GRÉCIA ANTIGA',[520,460]),nota('o navio\nde Teseu',[520,850],[0,'Teseu'],size=62,cor='laranja')]),
  dict(id='c3',frases=[f("Os atenienses guardavam o navio como relíquia e iam trocando as tábuas podres, uma por uma, com o tempo."),f("Esse barco, segundo a lenda, era o mesmo usado por Teseu para derrotar o Minotauro em Creta.")],
   elementos=[bloco('trocando tábua\npor tábua',[520,700],None,size=60,maxw=740)]),
  dict(id='c4',frases=[f("Depois de anos, nenhuma peça original restava."),f("Era ainda o navio de Teseu, ou um navio totalmente novo?")],
   camera=dict(push=0.07),elementos=[risco([300,500],[740,500],None),bloco('zero peças\noriginais',[520,900],[0,0.4],size=60,maxw=720,cor='laranja')]),
  dict(id='c5',frases=[f("Alguns filósofos dizem que sim, continua o mesmo, porque a forma e a função não mudaram."),f("Outros dizem que não: identidade depende da matéria, não só da forma."),f("Filósofos modernos ainda usam esse exemplo pra discutir o que realmente faz algo continuar sendo a mesma coisa com o tempo.")],
   elementos=[tira('FORMA CONTINUA = MESMO',[300,650],[0,'forma'],size=38),tira('MATÉRIA MUDOU = OUTRO',[760,850],[1,'matéria'],size=38)]),
  dict(id='c6',fonte='Fonte: Stanford Encyclopedia of Philosophy',frases=[f("E hoje? Seu corpo troca a maior parte das células em poucos anos, e seu celular já trocou de tela, bateria e capa.")],
   elementos=[obj('celular',[520,660],None,w=320,ang=-3),bloco('seu corpo e seu\ncelular também trocam',[520,1120],None,size=52,maxw=760)]),
  dict(id='c7',frases=[f("Então: a pergunta de Plutarco ainda não tem resposta certa, só respostas possíveis."),f("Pra você, ainda seria o mesmo navio? Comenta."),ASS],
   elementos=[bloco('ainda seria\no mesmo?',[520,700],[1,'mesmo'],size=68),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 024 MATEMÁTICA
EPS['SSA-024']=dict(materia='MATEMÁTICA',titulo='Por que todo relógio gira pro mesmo lado',
 fontes=["Scientific American, 'Why Do Clocks Go Clockwise?' (2013).","Encyclopaedia Britannica, verbete 'sundial'.","Smithsonian Magazine, 'Why Do Clocks Run Clockwise?' (2015)."],
 capa=dict(elementos=[obj('relogio',[520,650],w=400,ang=-3),bloco('por que todo relógio gira pro mesmo lado?',[520,1150],size=58,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Todo relógio do mundo gira pro mesmo lado. Isso não é acaso.")],
   elementos=[obj('relogio',[520,660],None,w=420,ang=-3,balanca=True),bloco('não é\nacaso!',[520,1100],None,size=74)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Antes do relógio mecânico, as pessoas usavam relógios de sol pra marcar a hora.")],
   elementos=[tira('RELÓGIO DE SOL',[520,460]),obj('relogio',[520,800],[0,'sol'],w=320,ang=4)]),
  dict(id='c3',fonte='Fonte: Scientific American (2013)',frases=[f("No hemisfério norte, onde os relógios mecânicos foram inventados, a sombra do relógio de sol se move nesse mesmo sentido.")],
   elementos=[seta([300,600],[760,750],None),bloco('sombra se move\nnesse sentido',[520,1050],[0,'sombra'],size=56,maxw=740)]),
  dict(id='c4',frases=[f("Os primeiros relógios mecânicos, feitos na Europa, copiaram esse movimento da sombra pra fazer sentido pra quem já usava relógio de sol."),f("Se tivessem sido inventados mais ao sul, talvez chamássemos de 'sentido horário' justamente o lado contrário.")],
   camera=dict(push=0.07),elementos=[obj('relogio',[520,680],None,w=380)]),
  dict(id='c5',frases=[f("No hemisfério sul, onde o Brasil fica, a sombra do relógio de sol gira pro lado contrário."),f("Mas os relógios continuaram no padrão europeu mesmo assim."),f("Quem inventa um relógio novo hoje em dia nem pensa duas vezes nisso: o padrão já virou universal.")],
   elementos=[risco([300,500],[740,500],None),nota('no hemisfério sul,\nseria ao contrário',[520,900],[0,0.5],size=54,maxw=760,cor='laranja')]),
  dict(id='c6',fonte='Fonte: Smithsonian Magazine (2015)',frases=[f("E hoje? É por isso que a expressão 'sentido horário' é a mesma em qualquer lugar do planeta, mesmo no hemisfério sul.")],
   elementos=[obj('globo',[520,660],None,w=340,ang=-2),bloco('o mesmo em\nqualquer lugar',[520,1100],None,size=58,maxw=720)]),
  dict(id='c7',frases=[f("Então: o jeito que o relógio gira é, na verdade, um registro de onde ele foi inventado."),f("Agora você sabe por que todo relógio copia a sombra do sol."),ASS],
   elementos=[obj('relogio',[520,640],None,w=400,ang=2),bloco('agora você sabe',[520,1080],[1,'sabe'],size=66)])])

# ------------------------------------------------------------ 025 FÍSICA
EPS['SSA-025']=dict(materia='FÍSICA',titulo='Por que o gato quase sempre cai em pé',
 fontes=["NASA, 'The Physics of a Falling Cat' (artigo de divulgação).","Scientific American, 'Why Do Cats Always Land on Their Feet?' (2006).","Encyclopaedia Britannica, 'cat righting reflex'."],
 capa=dict(elementos=[bloco('por que o gato quase sempre cai em pé?',[520,700],size=64,maxw=800),nota('sem bater a cabeça',[520,1120],cor='laranja',size=50)]),
 cenas=[
  dict(id='c1',frases=[f("Solta um gato de cabeça pra baixo, de uma altura segura, e ele quase sempre cai em pé.")],
   elementos=[bloco('cai de\ncabeça pra baixo...',[300,650],None,size=52,maxw=540),bloco('...e aterrissa\nem pé',[760,950],[0,0.6],size=52,maxw=540,cor='laranja')]),
  dict(id='c2',fonte='Fonte: Scientific American (2006)',frases=[f("Isso se chama reflexo de endireitamento, e começa a funcionar quando o gato ainda é filhote, com poucas semanas de vida.")],
   elementos=[tira('REFLEXO DE ENDIREITAMENTO',[520,460],size=38),nota('já funciona\nfilhote',[520,850],[0,'filhote'],size=56)]),
  dict(id='c3',fonte='Fonte: NASA, "The Physics of a Falling Cat"',frases=[f("A coluna do gato é extremamente flexível, então ele gira a parte da frente do corpo pra um lado e a de trás pro outro.")],
   elementos=[seta([300,650],[740,650],None),bloco('gira a frente\ne a traseira\nseparadas',[520,1020],None,size=50,maxw=760)]),
  dict(id='c4',frases=[f("Ele faz tudo isso sem nenhum ponto de apoio no ar, usando só a física do próprio corpo."),f("É o mesmo princípio que ginastas e mergulhadores usam pra girar o corpo no ar sem nenhum apoio.")],
   camera=dict(push=0.07),elementos=[bloco('sem nenhum\nponto de apoio',[520,700],None,size=62,maxw=720)]),
  dict(id='c5',frases=[f("As patas e o rabo ajudam a ajustar a rotação, como um equilibrista corrigindo o giro no ar."),f("Quanto maior a altura da queda, dentro de um limite seguro, mais tempo o gato tem pra se ajustar.")],
   elementos=[nota('equilibrista\nno ar',[520,700],[0,'equilibrista'],size=60,cor='laranja')]),
  dict(id='c6',fonte='Fonte: Encyclopaedia Britannica',frases=[f("E hoje? Vídeos de gatos caindo em pé fazem sucesso desde os primeiros filmes, no fim do século 19.","E hoje? Vídeos de gatos caindo em pé fazem sucesso desde os primeiros filmes, no fim do século dezenove.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('sucesso desde\no século 19',[520,1100],None,size=56,maxw=720)]),
  dict(id='c7',frases=[f("Então: o gato não tem sorte, ele tem uma coluna que funciona como física aplicada."),f("Seu gato (ou o de algum amigo) já fez isso? Comenta."),ASS],
   elementos=[bloco('seu gato já\nfez isso?',[520,700],[1,'gato'],size=66),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 026 HISTÓRIA
EPS['SSA-026']=dict(materia='HISTÓRIA',titulo='A Grande Muralha da China não dá pra ver do espaço',
 fontes=["NASA, 'Is the Great Wall of China really visible from space?' (perguntas frequentes).","Scientific American, 'Fact or Fiction: The Great Wall of China is visible from space'.","China Daily, declarações do astronauta chinês Yang Liwei (2003)."],
 capa=dict(elementos=[obj('globo',[520,650],w=420,ang=-3),bloco('a Muralha da China não dá pra ver do espaço',[520,1150],size=58,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Todo mundo repete que a Muralha da China é a única obra humana visível do espaço."),f("É mito.")],
   elementos=[obj('globo',[520,660],None,w=440,ang=-3,balanca=True),bloco('É MITO',[520,1100],None,size=100,cor='laranja')]),
  dict(id='c2',fonte='Fonte: NASA',frases=[f("Segundo a própria NASA, a muralha é estreita demais, com uns 6 a 9 metros de largura, pra ser vista a olho nu de órbita.","Segundo a própria NASA, a muralha é estreita demais, com uns seis a nove metros de largura, pra ser vista a olho nu de órbita.")],
   elementos=[tira('NASA',[520,440]),num('6-9 m',[520,820],[0,'9'],size=150,cor='tinta')]),
  dict(id='c3',fonte='Fonte: China Daily (2003)',frases=[f("Em 2003, o primeiro astronauta chinês no espaço, Yang Liwei, disse publicamente que não conseguiu ver a muralha.","Em dois mil e três, o primeiro astronauta chinês no espaço, Iang Livei, disse publicamente que não conseguiu ver a muralha.")],
   elementos=[nota('"não consegui\nver a muralha"',[520,700],[0,'muralha'],size=56,cor='laranja'),tira('YANG LIWEI · 2003',[520,1080],[0,'2003'],size=42)]),
  dict(id='c4',frases=[f("Da órbita baixa, coisas como rodovias largas, represas e cidades iluminadas à noite aparecem bem mais fácil."),f("A muralha some porque a cor dela se mistura com o solo ao redor, mesmo sendo enorme em comprimento.")],
   camera=dict(push=0.07),elementos=[bloco('rodovias e represas\naparecem mais fácil',[520,700],None,size=56,maxw=760)]),
  dict(id='c5',frases=[f("O mito provavelmente nasceu décadas antes de qualquer humano ir ao espaço, em livros e colunas de jornal do início do século 20.","O mito provavelmente nasceu décadas antes de qualquer humano ir ao espaço, em livros e colunas de jornal do início do século vinte."),f("Mesmo assim, a muralha continua visível em fotos tiradas de altitudes bem mais baixas, como de avião.")],
   elementos=[nota('nasceu antes\ndo espaço existir\npra gente',[520,750],[0,'espaço'],size=52,maxw=720,cor='laranja')]),
  dict(id='c6',fonte='Fonte: Scientific American',frases=[f("E hoje? O mito continua em livros didáticos e memes, décadas depois de ser desmentido.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('ainda repetido\nem memes',[520,1100],None,size=58,maxw=720)]),
  dict(id='c7',frases=[f("Então: a Muralha é gigante, mas 'gigante' e 'visível do espaço' são coisas bem diferentes."),f("Agora você sabe outro mito pra desmentir na próxima conversa."),ASS],
   elementos=[obj('globo',[520,640],None,w=420,ang=2),bloco('agora você sabe',[520,1080],[1,'sabe'],size=64)])])

# ------------------------------------------------------------ 027 SOCIOLOGIA (26/11 · Thanksgiving)
EPS['SSA-027']=dict(materia='SOCIOLOGIA',titulo='A primeira Ação de Graças pode não ter tido peru nenhum',
 fontes=["Smithsonian Magazine, 'What Was on the Menu at the First Thanksgiving?' (2011).","History.com, 'What Was on the Menu at the First Thanksgiving?'.","Plimoth Patuxet Museums, registros históricos da colheita de 1621."],
 capa=dict(elementos=[bloco('a primeira Ação de Graças pode não ter tido peru nenhum',[520,750],size=58,maxw=820),nota('é mito',[520,1180],cor='laranja',size=60)]),
 cenas=[
  dict(id='c1',frases=[f("A primeira Ação de Graças, em 1621, talvez nem tenha tido peru na mesa.","A primeira Ação de Graças, em mil seiscentos e vinte e um, talvez nem tenha tido peru na mesa.")],
   elementos=[bloco('talvez não teve\nperu nenhum',[520,700],None,size=62,maxw=740)]),
  dict(id='c2',fonte='Fonte: Plimoth Patuxet Museums',frases=[f("O único relato direto da época, escrito pelo colono Edward Winslow, fala em caça de aves e veados.")],
   elementos=[tira('EDWARD WINSLOW · 1621',[520,460]),nota('aves e veados,\nsegundo o relato',[520,850],[0,'veados'],size=52,maxw=700)]),
  dict(id='c3',fonte='Fonte: Smithsonian Magazine (2011)',frases=[f("Os colonos ingleses de Plymouth e os indígenas wampanoag dividiram a mesa por três dias inteiros."),f("Historiadores dizem que o prato principal pode ter sido veado, levado pelos próprios wampanoag.")],
   elementos=[seta([300,650],[740,650],None),bloco('3 dias de\nrefeições juntos',[520,1020],[0,'três'],size=58,maxw=740)]),
  dict(id='c4',frases=[f("Peru selvagem existia na região e pode ter entrado no cardápio, mas não tem prova de que foi o prato central."),f("Também é provável que tenham comido milho, abóbora e frutos do mar, comuns na região na época.")],
   camera=dict(push=0.06),elementos=[nota('talvez entrasse...\nmas não era\no prato central',[520,700],[0,'prato'],size=52,maxw=720,cor='laranja')]),
  dict(id='c5',frases=[f("O peru só virou símbolo obrigatório da data séculos depois, puxado por revistas e depois pela publicidade do século 20.","O peru só virou símbolo obrigatório da data séculos depois, puxado por revistas e depois pela publicidade do século vinte.")],
   elementos=[bloco('virou símbolo\nséculos depois',[520,700],None,size=60,maxw=740)]),
  dict(id='c6',fonte='Fonte: History.com',frases=[f("E hoje? Hoje, 26 de novembro, é dia de Ação de Graças nos Estados Unidos, com peru garantido na mesa de quase todo mundo.","E hoje? Hoje, vinte e seis de novembro, é dia de Ação de Graças nos Estados Unidos, com peru garantido na mesa de quase todo mundo.")],
   elementos=[dict(t='cal',titulo='NOVEMBRO',inicio=1,riscar=[26],pos=[520,680],ang=-2),tira('AÇÃO DE GRAÇAS · EUA',[520,1110],[0,'Graças'],size=42)]),
  dict(id='c7',frases=[f("Então: a tradição que achamos antiga, às vezes, é bem mais recente do que parece."),f("Você comeria veado no lugar do peru? Comenta."),ASS],
   elementos=[bloco('veado ou peru?',[520,700],[1,'veado'],size=68),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 028 EDUCAÇÃO FÍSICA
EPS['SSA-028']=dict(materia='EDUCAÇÃO FÍSICA',titulo='A medalha de ouro olímpica tem só 6 gramas de ouro de verdade',
 fontes=["Comitê Olímpico Internacional, regras de fabricação das medalhas (Carta Olímpica).","Forbes Brasil, 'Medalha de ouro: confira o valor do prêmio máximo da Olimpíada de Paris' (2024).","Bloomberg Línea, 'Quanto vale uma medalha de ouro?' (2024)."],
 capa=dict(elementos=[obj('medalha',[520,650],w=380,ang=-3),num('6g',[520,1150],None,size=220,cor='laranja'),bloco('de ouro de verdade',[520,1330],size=54)]),
 cenas=[
  dict(id='c1',frases=[f("A medalha de ouro olímpica quase não tem ouro."),f("De verdade.")],
   elementos=[obj('medalha',[520,660],None,w=400,ang=-3,balanca=True),bloco('quase não\ntem ouro!',[520,1100],None,size=68,maxw=700)]),
  dict(id='c2',fonte='Fonte: Forbes Brasil (2024)',frases=[f("Na Olimpíada de Paris, a medalha pesava 529 gramas no total.","Na Olimpíada de Paris, a medalha pesava quinhentos e vinte e nove gramas no total.")],
   elementos=[num('529g',[520,600],None,size=170,cor='tinta'),tira('PESO TOTAL',[520,1000],[0,'total'],size=42)]),
  dict(id='c3',fonte='Fonte: Comitê Olímpico Internacional',frases=[f("Só que, dessas 529 gramas, apenas 6 gramas são de ouro puro.","Só que, dessas quinhentos e vinte e nove gramas, apenas seis gramas são de ouro puro.")],
   elementos=[risco([300,500],[740,500],None),num('6g',[520,900],[0,'6'],size=200,cor='laranja')]),
  dict(id='c4',frases=[f("O resto, mais de 500 gramas, é prata. A medalha de ouro é, na prática, uma medalha de prata banhada a ouro.","O resto, mais de quinhentas gramas, é prata. A medalha de ouro é, na prática, uma medalha de prata banhada a ouro."),f("A medalha de prata, por sua vez, é feita quase inteiramente de prata pura de verdade.")],
   camera=dict(push=0.07),elementos=[bloco('prata banhada\na ouro',[520,700],None,size=64,maxw=720)]),
  dict(id='c5',frases=[f("A regra existe desde 1912: o ouro puro saiu de circulação nas medalhas há mais de um século.","A regra existe desde mil novecentos e doze: o ouro puro saiu de circulação nas medalhas há mais de um século."),f("Antes disso, algumas poucas edições chegaram a usar medalhas de ouro maciço, sem nenhuma prata por dentro.")],
   elementos=[tira('REGRA DESDE 1912',[520,460]),nota('mais de um\nséculo assim',[520,850],[0,'século'],size=56)]),
  dict(id='c6',fonte='Fonte: Bloomberg Línea (2024)',frases=[f("E hoje? Com o ouro mais caro, uma medalha de Paris 2024 já vale mais de 950 dólares só em metal.","E hoje? Com o ouro mais caro, uma medalha de Paris dois mil e vinte e quatro já vale mais de novecentos e cinquenta dólares só em metal.")],
   elementos=[obj('celular',[520,660],None,w=300),num('US$ 950',[520,1080],[0,'950'],size=100,cor='laranja')]),
  dict(id='c7',frases=[f("Então: o valor de verdade de uma medalha de ouro nunca esteve no metal, e sim no que ela representa."),f("Você já sabia que o ouro era só 6 gramas? Comenta."),ASS],
   elementos=[obj('medalha',[520,640],None,w=380,ang=2),bloco('você já sabia?',[520,1080],[1,'sabia'],size=66)])])

# ------------------------------------------------------------ 029 HISTÓRIA (27/11 · Black Friday)
EPS['SSA-029']=dict(materia='HISTÓRIA',titulo='"Black Friday" nasceu como xingamento de policial, não de loja',
 fontes=["CNN Brasil, 'Black Friday: entenda a origem do nome e da data' .","tmc.com.br, 'Do desastre ao desconto: a origem caótica da Black Friday'.","bpmoney.com.br, 'De onde vem o nome Black Friday' (2026)."],
 capa=dict(elementos=[jornal('SEXTA-FEIRA NEGRA','FILADÉLFIA · ANOS 1960','CAOS NO TRÂNSITO DO CENTRO',[520,700],w=600),bloco('nasceu como xingamento, não desconto',[520,1300],size=52,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("'Black Friday' não nasceu como festa de desconto. Nasceu como reclamação de policial.")],
   elementos=[bloco('nasceu como\nreclamação!',[520,700],None,size=66,maxw=740)]),
  dict(id='c2',fonte='Fonte: tmc.com.br',frases=[f("Nos anos 1960, na Filadélfia, o dia depois do feriado de Ação de Graças virava um caos de trânsito.","Nos anos mil novecentos e sessenta, na Filadélfia, o dia depois do feriado de Ação de Graças virava um caos de trânsito.")],
   elementos=[jornal('CAOS NO CENTRO','FILADÉLFIA · 1960s','RUAS TOMADAS DE COMPRADORES',[520,700],[0,'Filadélfia'],w=560)]),
  dict(id='c3',fonte='Fonte: CNN Brasil',frases=[f("A polícia usava 'sexta-feira negra' pra descrever aquele caos de gente nas ruas, não como elogio."),f("Os lojistas, inclusive, tentaram outro nome: 'big Friday'. Não emplacou.")],
   elementos=[nota('"sexta-feira\nnegra" = caos',[300,650],[0,'caos'],size=50,maxw=560),risco([600,900],[900,900],[1,'emplacou'])]),
  dict(id='c4',frases=[f("Existe outra versão ainda mais velha: em 1869, especuladores tentaram manipular o preço do ouro em Nova York, e isso também ficou conhecido como uma sexta-feira negra.","Existe outra versão ainda mais velha: em mil oitocentos e sessenta e nove, especuladores tentaram manipular o preço do ouro em Nova York, e isso também ficou conhecido como uma sexta-feira negra.")],
   camera=dict(push=0.06),elementos=[tira('NOVA YORK · 1869',[520,460]),bloco('crise do ouro',[520,850],[0,'ouro'],size=62)]),
  dict(id='c5',frases=[f("Com o tempo, o varejo abraçou o nome e inventou outro sentido: o dia em que as contas saíam do vermelho e iam pro azul... ou pro preto.")],
   elementos=[bloco('do vermelho\npro preto',[520,700],None,size=60,maxw=720,cor='laranja')]),
  dict(id='c6',fonte='Fonte: bpmoney.com.br (2026)',frases=[f("E hoje? No Brasil, a Black Friday chegou só em 2010 e hoje, 27 de novembro, é a data oficial de 2026.","E hoje? No Brasil, a Black Friday chegou só em dois mil e dez e hoje, vinte e sete de novembro, é a data oficial de dois mil e vinte e seis.")],
   elementos=[dict(t='cal',titulo='NOVEMBRO',inicio=1,riscar=[27],pos=[520,680],ang=2),tira('BRASIL · DESDE 2010',[520,1110],[0,'2010'],size=42)]),
  dict(id='c7',frases=[f("Então: antes de ser sinônimo de desconto, 'Black Friday' foi sinônimo de dor de cabeça."),f("Marca aquele amigo que vive esperando a Black Friday."),ASS],
   elementos=[bloco('marca um amigo',[520,700],[1,'amigo'],size=66),nota('comenta/marca!',[780,1180],[0,0.6],cor='laranja')])])

# ------------------------------------------------------------ 030 QUÍMICA
EPS['SSA-030']=dict(materia='QUÍMICA',titulo='A pimenta não queima sua boca de verdade (seu cérebro é enganado)',
 fontes=["Scientific American, 'Why Does Spicy Food Cause Pain?'.","National Institutes of Health (NIH), estudos sobre capsaicina e receptores TRPV1.","Harvard Health Publishing, 'The science of spicy food' (2021)."],
 capa=dict(elementos=[obj('frasco',[520,660],w=360,ang=-3),bloco('a pimenta não queima sua boca de verdade',[520,1150],size=58,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Pimenta não queima sua boca de verdade. Seu cérebro é que é enganado.")],
   elementos=[obj('frasco',[520,660],None,w=380,ang=-3,balanca=True),bloco('seu cérebro\né enganado',[520,1100],None,size=64,maxw=720)]),
  dict(id='c2',fonte='Fonte: NIH, estudos sobre receptores TRPV1',frases=[f("A culpa é da capsaicina, substância da pimenta que gruda num receptor da boca chamado TRPV1.")],
   elementos=[tira('CAPSAICINA → RECEPTOR TRPV1',[520,460],size=40),nota('o mesmo receptor\ndo calor de verdade',[520,850],[0,'receptor'],size=50,maxw=700)]),
  dict(id='c3',fonte='Fonte: Harvard Health Publishing (2021)',frases=[f("Esse receptor é o mesmo que avisa o cérebro quando você encosta em algo quente de verdade, acima de uns 43 graus.","Esse receptor é o mesmo que avisa o cérebro quando você encosta em algo quente de verdade, acima de uns quarenta e três graus.")],
   elementos=[num('43°C',[520,600],None,size=160,cor='laranja'),bloco('mesmo alarme\ndo calor real',[520,1000],[0,0.4],size=54,maxw=720)]),
  dict(id='c4',frases=[f("A capsaicina ativa esse alarme sem esquentar nada de verdade. Seu cérebro recebe o sinal de queimadura, mas não existe dano real."),f("É esse mesmo mecanismo que faz algumas pessoas sentirem até uma sensação de prazer depois da ardência passar.")],
   camera=dict(push=0.07),elementos=[bloco('alarme falso,\nsem dano real',[520,700],None,size=58,maxw=760)]),
  dict(id='c5',frases=[f("É por isso que leite ajuda a aliviar mais que água: ele tem gordura, que dissolve a capsaicina melhor que a água sozinha."),f("Beber água, na verdade, só espalha a capsaicina pela boca inteira e pode até piorar a sensação por um instante.")],
   elementos=[tira('LEITE > ÁGUA PRA ALIVIAR',[520,460],size=38),nota('a gordura\ndissolve melhor',[520,850],[0,'gordura'],size=54)]),
  dict(id='c6',frases=[f("E hoje? Competições de comer pimenta, muito populares em vídeos, usam variedades bem mais fortes que a pimenta de cozinha comum.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('vídeos de\ncomer pimenta',[520,1100],None,size=56,maxw=720)]),
  dict(id='c7',frases=[f("Então: a ardência da pimenta é real como sensação, mas é um alarme disparado à toa."),f("Qual é seu limite de pimenta? Comenta."),ASS],
   elementos=[obj('frasco',[520,640],None,w=360,ang=2),bloco('qual seu limite?',[520,1080],[1,'limite'],size=66)])])

# ------------------------------------------------------------ 031 HISTÓRIA (28/11 · final da Libertadores)
EPS['SSA-031']=dict(materia='HISTÓRIA',titulo='A primeira final da Libertadores também foi no Uruguai, 66 anos antes',
 fontes=["ESPN Deportes, 'Las Copas CONMEBOL Libertadores que ganó Peñarol'.","La Nación, 'Sesenta años, Copa Libertadores, primer partido' (2020).","Conmebol.com, calendário oficial 2026 (final da Libertadores, 28/11, Estádio Centenário)."],
 capa=dict(elementos=[obj('medalha',[520,650],w=380,ang=-3),num('66',[520,1150],None,size=220,cor='laranja'),bloco('anos depois, no mesmo estádio',[520,1330],size=50)]),
 cenas=[
  dict(id='c1',frases=[f("A primeira final da Libertadores da história foi no mesmo estádio da final de 2026: o Centenário, em Montevidéu.","A primeira final da Libertadores da história foi no mesmo estádio da final de dois mil e vinte e seis: o Centenário, em Montevidéu.")],
   elementos=[obj('medalha',[520,660],None,w=400,ang=-3,balanca=True),tira('ESTÁDIO CENTENÁRIO',[520,1080],None,size=46)]),
  dict(id='c2',fonte='Fonte: La Nación (2020)',frases=[f("Foi em 1960, quando a competição ainda se chamava Copa dos Clubes Campeões da América.","Foi em mil novecentos e sessenta, quando a competição ainda se chamava Copa dos Clubes Campeões da América.")],
   elementos=[num('1960',[520,600],None,size=180,cor='tinta'),tira('COPA DOS CLUBES CAMPEÕES',[520,980],[0,'1960'],size=38)]),
  dict(id='c3',fonte='Fonte: ESPN Deportes',frases=[f("O campeão foi o Peñarol, do Uruguai, que venceu o Olimpia, do Paraguai, em duas partidas.")],
   elementos=[tira('PEÑAROL (URU) x OLIMPIA (PAR)',[520,480],size=38),nota('campeão:\nPeñarol',[520,850],[0,'Peñarol'],size=60,cor='laranja')]),
  dict(id='c4',frases=[f("O Peñarol disputou a primeira partida da história da competição toda no próprio Centenário, contra um time boliviano."),f("O placar foi uma goleada: 7 a 1.","O placar foi uma goleada: sete a um.")],
   camera=dict(push=0.07),elementos=[bloco('primeiro jogo\nda história,\nno Centenário',[520,700],None,size=56,maxw=740)]),
  dict(id='c5',frases=[f("Na época, só 7 clubes disputaram o torneio inteiro, porque nem todo país mandou representante.","Na época, só sete clubes disputaram o torneio inteiro, porque nem todo país mandou representante."),f("O Peñarol ainda ganharia o título seguinte, em 1961, virando o primeiro bicampeão da história da taça.","O Peñarol ainda ganharia o título seguinte, em mil novecentos e sessenta e um, virando o primeiro bicampeão da história da taça.")],
   elementos=[num('7 clubes',[520,600],None,size=140,cor='tinta'),nota('hoje são\nbem mais',[520,980],[0,0.6],size=56)]),
  dict(id='c6',fonte='Fonte: calendário oficial Conmebol 2026',frases=[f("E hoje? Hoje, 28 de novembro, é a final da Libertadores de 2026, Palmeiras contra Estudiantes, de novo no Centenário, em Montevidéu.","E hoje? Hoje, vinte e oito de novembro, é a final da Libertadores de dois mil e vinte e seis, Palmeiras contra Estudiantes, de novo no Centenário, em Montevidéu.")],
   elementos=[dict(t='cal',titulo='NOVEMBRO',inicio=1,riscar=[28],pos=[520,680],ang=-2),tira('PALMEIRAS x ESTUDIANTES',[520,1110],[0,'Estudiantes'],size=40)]),
  dict(id='c7',frases=[f("Então: 66 anos depois, a decisão do futebol sul-americano volta pro mesmo palco onde tudo começou.","Então: sessenta e seis anos depois, a decisão do futebol sul-americano volta pro mesmo palco onde tudo começou."),f("Qual time você acha que leva essa final? Comenta."),ASS],
   elementos=[obj('medalha',[520,640],None,w=380,ang=2),bloco('qual time leva?',[520,1080],[1,'leva'],size=66)])])

# ------------------------------------------------------------ 032 FÍSICA
EPS['SSA-032']=dict(materia='FÍSICA',titulo='Por que a bola de futebol curva no ar',
 fontes=["Scientific American, 'The Physics of Soccer'.","Deutsches Museum / Newton, descrição original do efeito Magnus (1671).","Smithsonian Magazine, 'The Science of the Banana Kick' (2014)."],
 capa=dict(elementos=[bloco('por que a bola de futebol curva no ar?',[520,700],size=64,maxw=800),nota('efeito Magnus',[520,1120],cor='laranja',size=56)]),
 cenas=[
  dict(id='c1',frases=[f("Quando um jogador chuta uma bola com efeito, ela curva no ar como se desviasse de alguma coisa.")],
   elementos=[seta([300,650],[740,500],None),bloco('a bola\ndesvia sozinha',[520,950],None,size=62,maxw=720)]),
  dict(id='c2',fonte='Fonte: Scientific American',frases=[f("O nome disso é efeito Magnus, batizado em homenagem ao físico alemão Gustav Magnus, no século 19.","O nome disso é efeito Magnus, batizado em homenagem ao físico alemão Gustav Mágnus, no século dezenove.")],
   elementos=[tira('EFEITO MAGNUS',[520,460]),nota('Gustav Magnus,\nséc. 19',[520,850],[0,'Magnus'],size=54)]),
  dict(id='c3',frases=[f("Quando a bola gira, o ar passa mais rápido de um lado e mais devagar do outro."),f("Isso cria uma diferença de pressão: mais pressão de um lado empurra a bola pro outro.")],
   elementos=[bloco('ar rápido\nde um lado...',[280,650],None,size=50,maxw=520),bloco('...ar lento\ndo outro',[760,950],[0,0.6],size=50,maxw=520,cor='laranja')]),
  dict(id='c4',fonte='Fonte: descrição original de Isaac Newton (1671)',frases=[f("O próprio Isaac Newton já tinha anotado esse efeito observando bolas de tênis, em 1671.","O próprio Isaac Newton já tinha anotado esse efeito observando bolas de tênis, em mil seiscentos e setenta e um.")],
   camera=dict(push=0.06),elementos=[tira('ISAAC NEWTON · 1671',[520,460]),bloco('viu isso\nno tênis',[520,850],[0,'tênis'],size=58)]),
  dict(id='c5',frases=[f("Quanto mais giro o jogador dá na bola, maior a curva, e é por isso que craques treinam esse chute à exaustão."),f("O mesmo efeito explica por que uma bola de tênis com efeito ou uma bola de beisebol curva também fazem curvas parecidas.")],
   elementos=[nota('mais giro =\nmais curva',[520,700],[0,'giro'],size=60,cor='laranja')]),
  dict(id='c6',fonte='Fonte: Smithsonian Magazine (2014)',frases=[f("E hoje? O chute conhecido como 'folha seca', famoso no futebol brasileiro, usa exatamente essa física.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('"folha seca" =\nefeito Magnus',[520,1100],None,size=56,maxw=740)]),
  dict(id='c7',frases=[f("Então: aquele chute impossível de defender é, na verdade, física básica bem treinada."),f("Qual é o chute mais bonito que você já viu? Comenta."),ASS],
   elementos=[bloco('qual o chute\nmais bonito?',[520,700],[1,'chute'],size=62,maxw=740),nota('comenta aí!',[780,1180],[1,0.6],cor='laranja')])])

# ------------------------------------------------------------ 033 LITERATURA
EPS['SSA-033']=dict(materia='LITERATURA',titulo='Frankenstein nunca foi o nome do monstro',
 fontes=["SHELLEY, Mary. Frankenstein; or, The Modern Prometheus (1818).","Encyclopaedia Britannica, verbete 'Frankenstein'.","British Library, 'Mary Shelley and Frankenstein'."],
 capa=dict(elementos=[obj('livro',[520,650],w=400,ang=-3),bloco('Frankenstein nunca foi o nome do monstro',[520,1150],size=60,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Frankenstein nunca foi o nome do monstro. É o nome do cientista que o criou.")],
   elementos=[obj('livro',[520,660],None,w=420,ang=-3,balanca=True),bloco('é o cientista,\nnão o monstro!',[520,1100],None,size=62,maxw=720)]),
  dict(id='c2',fonte='Fonte: Mary Shelley, Frankenstein (1818)',frases=[f("O livro é de 1818, escrito pela britânica Mary Shelley, quando ela tinha só 18 anos.","O livro é de mil oitocentos e dezoito, escrito pela britânica Mary Shelley, quando ela tinha só dezoito anos.")],
   elementos=[tira('MARY SHELLEY · 1818',[520,460]),nota('ela tinha\nsó 18 anos',[520,850],[0,'18'],size=58,cor='laranja')]),
  dict(id='c3',frases=[f("Victor Frankenstein é o estudante que monta uma criatura com partes de corpos e dá vida a ela."),f("A criatura, no livro inteiro, nunca ganha um nome próprio."),f("No romance original, ela aprende sozinha a falar e a ler, observando uma família escondida.")],
   elementos=[bloco('Victor Frankenstein\n= o cientista',[520,700],[0,'Victor'],size=56,maxw=740)]),
  dict(id='c4',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Ela é chamada de 'a criatura', 'o monstro' ou 'o demônio', dependendo do trecho."),f("No livro original, ela também é descrita como extremamente inteligente, bem diferente da imagem de monstro bruto do cinema.")],
   camera=dict(push=0.06),elementos=[tira('"a criatura" · "o monstro" · "o demônio"',[520,700],size=36,maxw=760)]),
  dict(id='c5',frases=[f("A confusão começou ainda no século 19, em peças de teatro que adaptavam o livro.","A confusão começou ainda no século dezenove, em peças de teatro que adaptavam o livro."),f("O público passou a chamar a criatura pelo sobrenome do criador.")],
   elementos=[nota('o público trocou\no nome sozinho',[520,700],[1,'público'],size=54,maxw=720,cor='laranja')]),
  dict(id='c6',fonte='Fonte: British Library',frases=[f("E hoje? Em fantasias, desenhos e memes, 'Frankenstein' virou sinônimo da criatura, mesmo sendo o nome errado.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('o nome errado\nvirou padrão',[520,1100],None,size=56,maxw=740)]),
  dict(id='c7',frases=[f("Então: há mais de 200 anos, o criador e a criatura dividem um nome que, no livro, era só de um deles.","Então: há mais de duzentos anos, o criador e a criatura dividem um nome que, no livro, era só de um deles."),f("Você já sabia dessa? Comenta."),ASS],
   elementos=[obj('livro',[520,640],None,w=400,ang=2),bloco('você já sabia?',[520,1080],[1,'sabia'],size=66)])])

# ------------------------------------------------------------ 034 BIOLOGIA
EPS['SSA-034']=dict(materia='BIOLOGIA',titulo='O "frio na barriga" tem explicação, e não é no estômago',
 fontes=["Harvard Medical School, 'Understanding the stress response'.","Cleveland Clinic, 'Why Do We Get Butterflies in Our Stomach?' (2022).","Scientific American, 'The Gut's Little Brain'."],
 capa=dict(elementos=[obj('coracao',[520,650],w=380,ang=-3),bloco('o "frio na barriga" tem explicação',[520,1150],size=62,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Aquele frio na barriga antes de uma notícia importante tem explicação científica. E não começa no estômago.")],
   elementos=[obj('coracao',[520,660],None,w=400,ang=-3,balanca=True),bloco('não começa\nno estômago!',[520,1100],None,size=62,maxw=720)]),
  dict(id='c2',fonte='Fonte: Harvard Medical School',frases=[f("Quando você se assusta ou se emociona, o corpo libera adrenalina de uma vez.")],
   elementos=[tira('ADRENALINA',[520,460]),nota('liberada\nde uma vez',[520,850],[0,'adrenalina'],size=58,cor='laranja')]),
  dict(id='c3',fonte='Fonte: Cleveland Clinic (2022)',frases=[f("Pra preparar o corpo pra reagir rápido, o sangue é desviado do sistema digestivo pros músculos e pro coração.")],
   elementos=[seta([300,650],[740,650],None),bloco('sangue sai do\nestômago e vai\npros músculos',[520,1020],None,size=54,maxw=740)]),
  dict(id='c4',frases=[f("Com menos sangue circulando ali, o estômago e o intestino ficam temporariamente mais lentos."),f("É esse 'desligar parcial' que a gente sente como frio ou aperto na barriga."),f("O coração também acelera nesse momento, o que reforça ainda mais a sensação no peito e na barriga.")],
   camera=dict(push=0.07),elementos=[bloco('estômago fica\nmais lento',[520,700],None,size=60,maxw=740)]),
  dict(id='c5',fonte='Fonte: Scientific American',frases=[f("O intestino tem tanto neurônio que alguns cientistas chamam ele de 'segundo cérebro' do corpo."),f("É por isso que emoções fortes também mexem tanto com o apetite de muita gente.")],
   elementos=[nota('o "segundo\ncérebro"',[520,700],[0,'cérebro'],size=62,cor='laranja')]),
  dict(id='c6',frases=[f("E hoje? Paixão, prova, entrevista de emprego ou aquele vídeo que viraliza: qualquer emoção forte dispara o mesmo mecanismo.")],
   elementos=[obj('celular',[520,660],None,w=300),bloco('qualquer emoção\nforte dispara isso',[520,1100],None,size=56,maxw=740)]),
  dict(id='c7',frases=[f("Então: o frio na barriga é o seu corpo se preparando pra agir, não um aviso de que algo vai dar errado."),f("Quando foi a última vez que você sentiu isso? Comenta."),ASS],
   elementos=[obj('coracao',[520,640],None,w=380,ang=2),bloco('quando foi\na última vez?',[520,1080],[1,'última'],size=58,maxw=740)])])

# ------------------------------------------------------------ grava os roteiro.json
DATAS={'SSA-015':('2026-11-20','12:00'),'SSA-016':('2026-11-20','19:00'),
 'SSA-017':('2026-11-21','12:00'),'SSA-018':('2026-11-21','19:00'),
 'SSA-019':('2026-11-22','12:00'),'SSA-020':('2026-11-22','19:00'),
 'SSA-021':('2026-11-23','12:00'),'SSA-022':('2026-11-23','19:00'),
 'SSA-023':('2026-11-24','12:00'),'SSA-024':('2026-11-24','19:00'),
 'SSA-025':('2026-11-25','12:00'),'SSA-026':('2026-11-25','19:00'),
 'SSA-027':('2026-11-26','12:00'),'SSA-028':('2026-11-26','19:00'),
 'SSA-029':('2026-11-27','12:00'),'SSA-030':('2026-11-27','19:00'),
 'SSA-031':('2026-11-28','12:00'),'SSA-032':('2026-11-28','19:00'),
 'SSA-033':('2026-11-29','12:00'),'SSA-034':('2026-11-29','19:00')}

CHAMADAS={
 'SSA-015':'NEM É PALAVRA PORTUGUESA','SSA-016':'QUASE 100 ANOS LIVRES',
 'SSA-017':'SÓ 10 PAÍSES JOGAM','SSA-018':'NÃO É CHOCOLATE DE VERDADE',
 'SSA-019':'VOCÊ JÁ TÁ BOCEJANDO','SSA-020':'OS BRAÇOS NUNCA VOLTARAM',
 'SSA-021':'UM PAÍS, 11 FUSOS','SSA-022':'PRA PROVAR QUE NÃO TINHA ARMA',
 'SSA-023':'AINDA É O MESMO NAVIO?','SSA-024':'A SOMBRA DO SOL DECIDIU',
 'SSA-025':'A FÍSICA DO GATO','SSA-026':'NINGUÉM VÊ DO ESPAÇO',
 'SSA-027':'TALVEZ NEM TEVE PERU','SSA-028':'SÓ 6 GRAMAS DE OURO',
 'SSA-029':'NASCEU COMO XINGAMENTO','SSA-030':'SEU CÉREBRO É ENGANADO',
 'SSA-031':'O MESMO ESTÁDIO, 66 ANOS DEPOIS','SSA-032':'A FÍSICA DA FOLHA SECA',
 'SSA-033':'O NOME ERA DO CIENTISTA','SSA-034':'NÃO COMEÇA NO ESTÔMAGO'}

if __name__=='__main__':
    for eid,ep in EPS.items():
        d=f'{BASE}/{eid}'; os.makedirs(d,exist_ok=True)
        rot=dict(id=eid,chamada=CHAMADAS.get(eid,''),**ep)
        json.dump(rot,open(f'{d}/roteiro.json','w'),ensure_ascii=False,indent=1)
        print(eid,'ok',DATAS.get(eid))
