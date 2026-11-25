"""Gera os roteiros do lote 4 (SSA-052 a SSA-065, 08/12 19h a 15/12/2026 12h). Não rode depois de produzir: sobrescreve roteiros.
Calendário e fontes dos eventos: semanas/2026-12-08/calendario.md"""
import json,os,sys
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
def carimbo(txt,data,pos,e=None,**k): return dict(t='carimbo',txt=txt,data=data,pos=pos,e=e,**k)
def cal(titulo,inicio,pos,e=None,**k): return dict(t='cal',titulo=titulo,inicio=inicio,pos=pos,e=e,**k)
EPS={}

# ------------------------------------------------------------ 052 EDUCAÇÃO FÍSICA (08/12 · Mundial de Clubes de vôlei feminino em SP, 08–13/12)
EPS['SSA-052']=dict(materia='EDUCAÇÃO FÍSICA',titulo='O vôlei foi inventado porque o basquete cansava demais',
 fontes=["FIVB, 'History of volleyball' (fivb.com).","Volleyball Hall of Fame, 'History of volleyball' (volleyhall.org).","Olympics.com (COI), 'Volleyball: a brief history'.","FIVB (08/09/2026): Mundial de Clubes feminino em São Paulo, 8 a 13/12/2026."],
 capa=dict(elementos=[obj('bola',[520,660],w=420,ang=-4),bloco('o plano era cansar menos que o basquete',[520,1120],size=62,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("O vôlei foi inventado porque o basquete cansava demais."),f("E o primeiro nome dele nem era vôlei.")],
   elementos=[obj('bola',[520,620],None,w=380,ang=-4,balanca=True),bloco('CANSAVA DEMAIS',[520,960],None,size=88,cor='tinta',ang=-3),nota('nem era vôlei!',[640,1130],[1,'nome'],cor='laranja',size=60)]),
  dict(id='c2',fonte='Fonte: FIVB; Volleyball Hall of Fame',frases=[f("Estados Unidos, 1895.","Estados Unidos, mil oitocentos e noventa e cinco."),f("William Morgan era diretor de educação física da Associação Cristã de Moços, na cidade de Holyoke.","Uíliam Mórgan era diretor de educação física da Associação Cristã de Moços, na cidade de Rôliôk."),f("Quatro anos antes, James Naismith tinha inventado o basquete.","Quatro anos antes, Djeims Neismith tinha inventado o basquete.")],
   elementos=[tira('EUA · 1895',[520,440],None,size=56),tira('WILLIAM MORGAN',[360,620],[1,'Morgan'],size=50),tira('ACM · HOLYOKE',[640,760],[1,'Holyoke'],size=48),
     tira('BASQUETE · 1891',[520,1000],[2,'basquete'],size=56,ang=4)]),
  dict(id='c3',fonte='Fonte: FIVB; Volleyball Hall of Fame',frases=[f("Só que o basquete era puxado demais para os alunos mais velhos, muitos deles homens de negócios."),f("Morgan queria um jogo mais leve, pra jogar dentro do ginásio, sem tanta correria.")],
   elementos=[obj('corredor',[330,640],None,w=300,ang=-4),bloco('puxado\ndemais',[700,600],[0,'puxado'],size=72,cor='tinta',maxw=420),tira('alunos mais velhos',[520,880],[0,'velhos'],size=46),nota('um jogo mais leve',[560,1080],[1,'leve'],cor='laranja',size=62)]),
  dict(id='c4',fonte='Fonte: FIVB; Volleyball Hall of Fame',frases=[f("Ele subiu uma rede a 1,98 metro do chão.","Ele subiu uma rede a um metro e noventa e oito do chão."),f("Testou a câmara de borracha de uma bola de basquete, mas ela era leve e lenta demais."),f("A bola de basquete inteira era pesada. A saída foi uma bola nova, feita pela Spalding.","A bola de basquete inteira era pesada. A saída foi uma bola nova, feita pela Spólding.")],
   camera=dict(push=0.06),elementos=[num('1,98 m',[520,560],[0,'1,98'],size=170),tira('altura da rede',[520,720],[0,'rede'],size=46),tira('câmara: leve demais',[330,900],[1,'leve'],size=42),
     tira('bola inteira: pesada',[680,1000],[2,'pesada'],size=42),obj('bola',[300,1100],[2,'nova'],w=180)]),
  dict(id='c5',fonte='Fonte: Volleyball Hall of Fame; Olympics.com',frases=[f("O nome original era Mintonette.","O nome original era Mintonét."),f("Em 1896, depois de uma demonstração, o professor Alfred Halstead sugeriu outro: volley ball, por causa da bola rebatida no ar.","Em mil oitocentos e noventa e seis, depois de uma demonstração, o professor Álfred Rólsted sugeriu outro: vóli bol, por causa da bola rebatida no ar."),f("Em 1964, em Tóquio, o vôlei virou esporte olímpico.","Em mil novecentos e sessenta e quatro, em Tóquio, o vôlei virou esporte olímpico.")],
   elementos=[bloco('MINTONETTE',[520,500],None,size=90,cor='tinta',ang=-3),risco([300,500],[740,500],[1,'sugeriu']),bloco('VOLLEY BALL',[520,720],[1,'volley'],size=84),nota('1896',[800,830],[1,'1896'],cor='laranja',size=60),
     obj('medalha',[330,1020],[2,'olímpico'],w=210),tira('TÓQUIO 1964',[660,1020],[2,'Tóquio'],size=50)]),
  dict(id='c6',fonte='Fonte: FIVB (08/09/2026)',frases=[f("E hoje? São Paulo recebe o Mundial de Clubes de vôlei feminino, de 8 a 13 de dezembro.","E hoje? São Paulo recebe o Mundial de Clubes de vôlei feminino, de oito a treze de dezembro."),f("Com 2 times brasileiros: Osasco e Sesi Bauru.","Com dois times brasileiros: Osasco e Sési Baurú."),f("O jogo leve de 1895 hoje vale título mundial.","O jogo leve de mil oitocentos e noventa e cinco hoje vale título mundial.")],
   elementos=[tira('MUNDIAL DE CLUBES · SP',[520,450],None,size=48),cal('DEZEMBRO',2,[520,720],[0,'8 a 13'],ndias=31,riscar=[8,9,10,11,12,13],riscar_em=[0,'8 a 13'],escala=0.5,ang=-2),
     tira('OSASCO',[320,960],[1,'Osasco'],size=50),tira('SESI BAURU',[700,1000],[1,'Bauru'],size=50),nota('vale título mundial',[540,1140],[2,'mundial'],cor='laranja',size=54)]),
  dict(id='c7',frases=[f("Então: o vôlei nasceu pra cansar menos que o basquete. E hoje decide mundial."),f("Osasco ou Bauru: quem vai mais longe? Comenta."),ASS],
   elementos=[obj('bola',[520,620],None,w=340,ang=3),bloco('Osasco ou Bauru?',[520,1000],[1,'Osasco'],size=74),nota('comenta!',[780,1150],[1,'Comenta'],cor='laranja')])])

# ------------------------------------------------------------ 053 LITERATURA
EPS['SSA-053']=dict(materia='LITERATURA',titulo='Sherlock Holmes nunca disse "Elementar, meu caro Watson"',
 fontes=["Encyclopaedia Britannica, 'Sherlock Holmes'.","Quote Investigator (14/07/2016), 'Elementary, My Dear Watson'.","DOYLE, Arthur Conan. 'The Crooked Man' (1893), em The Memoirs of Sherlock Holmes (Project Gutenberg).","Arthur Conan Doyle Encyclopedia, 'The Return of Sherlock Holmes (movie 1929)'."],
 capa=dict(elementos=[obj('lupa',[520,660],w=420,ang=-6),bloco('a frase mais famosa dele não está nos livros',[520,1120],size=60,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("A frase mais famosa do Sherlock Holmes não está em nenhum livro dele.","A frase mais famosa do Xérloc Rólms não está em nenhum livro dele."),f("Elementar, meu caro Watson. Nunca foi escrita assim.","Elementar, meu caro Uótson. Nunca foi escrita assim.")],
   elementos=[obj('lupa',[520,620],None,w=380,ang=-6,balanca=True),bloco('"Elementar, meu caro Watson"',[520,960],[1,'Elementar'],size=58,maxw=800,cor='tinta'),nota('nunca escrita!',[680,1130],[1,'Nunca'],cor='laranja',size=60)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Holmes estreou em 1887, num livro chamado Um Estudo em Vermelho.","Rólms estreou em mil oitocentos e oitenta e sete, num livro chamado Um Estudo em Vermelho."),f("O autor, o escocês Arthur Conan Doyle, escreveu 4 romances e 56 contos com o detetive.","O autor, o escocês Ártur Cónan Dóil, escreveu quatro romances e cinquenta e seis contos com o detetive.")],
   elementos=[jornal("BEETON'S CHRISTMAS ANNUAL",'1887','A STUDY IN SCARLET',[340,740],None,w=400,ang=-3),tira('CONAN DOYLE',[700,620],[1,'Conan'],size=48),
     tira('4 romances',[700,820],[1,'romances'],size=48),tira('56 contos',[700,960],[1,'56'],size=52)]),
  dict(id='c3',fonte='Fonte: Britannica; Quote Investigator',frases=[f("E em nenhum desses 60 textos aparece a frase completa.","E em nenhum desses sessenta textos aparece a frase completa."),f("Nenhum. Nem uma vez.")],
   elementos=[num('60',[520,620],None,size=300),tira('textos de Conan Doyle',[520,860],None,size=46),bloco('frase completa: 0',[520,1060],[1,'Nem'],size=80,cor='tinta',ang=-3)]),
  dict(id='c4',fonte='Fonte: Conan Doyle, The Crooked Man (1893)',frases=[f("O que existe são pedaços."),f("No conto O Corcunda, de 1893, Watson fica impressionado, e Holmes responde só: Elementar.","No conto O Corcunda, de mil oitocentos e noventa e três, Uótson fica impressionado, e Rólms responde só: Elementar."),f("E meu caro Watson aparece várias vezes, mas em outras frases.","E meu caro Uótson aparece várias vezes, mas em outras frases.")],
   camera=dict(push=0.06),elementos=[bloco('só pedaços',[520,480],None,size=80),obj('livro',[320,760],[1,'Corcunda'],w=300,ang=-4),tira('"Elementary," said he.',[680,700],[1,'Elementar'],size=40),
     tira('"my dear Watson"',[640,1000],[2,'meu caro'],size=46),nota('em outras frases',[560,1140],[2,'outras'],cor='laranja',size=54)]),
  dict(id='c5',fonte='Fonte: Quote Investigator; A. C. Doyle Encyclopedia',frases=[f("A frase inteira já aparecia em jornais e em livros de outros autores no começo do século 20.","A frase inteira já aparecia em jornais e em livros de outros autores no começo do século vinte."),f("Mas quem espalhou de vez foi o cinema: em 1929, o primeiro filme falado do Holmes terminava com ela.","Mas quem espalhou de vez foi o cinema: em mil novecentos e vinte e nove, o primeiro filme falado do Rólms terminava com ela.")],
   elementos=[jornal('THE GLOBE','1908','"ELEMENTARY..."',[340,720],None,w=380,ang=-4),tira('outros autores',[700,620],[0,'outros'],size=46),tv([660,960],[1,'cinema'],w=300),tira('1929 · filme falado',[420,1120],[1,'1929'],size=46)]),
  dict(id='c6',fonte='Fonte: Encyclopaedia Britannica',frases=[f("E hoje? Isso tem nome: citação apócrifa. Uma frase famosa que a pessoa nunca disse."),f("A internet tá cheia delas."),f("Inclusive, já mostramos aqui: a maçã também nunca caiu na cabeça do Newton.","Inclusive, já mostramos aqui: a maçã também nunca caiu na cabeça do Níuton.")],
   elementos=[verb('apócrifo','adjetivo','de autoria falsa ou duvidosa; atribuído a quem não disse.',[520,560],[0,'apócrifa'],w=700),obj('celular',[300,920],[1,'internet'],w=230,ang=-4),
     obj('maca',[700,920],[2,'maçã'],w=230),nota('nunca caiu!',[640,1130],[2,'nunca'],cor='laranja',size=56)]),
  dict(id='c7',frases=[f("Então: Holmes disse elementar, e disse meu caro Watson. Só nunca disse as duas coisas juntas.","Então: Rólms disse elementar, e disse meu caro Uótson. Só nunca disse as duas coisas juntas."),f("Agora você sabe: a frase mais famosa dele veio do cinema."),ASS],
   elementos=[obj('lupa',[520,620],None,w=340,ang=4),bloco('nunca as duas juntas',[520,980],[0,'juntas'],size=70,maxw=780),nota('veio do cinema',[640,1140],[1,'cinema'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 054 BIOLOGIA
EPS['SSA-054']=dict(materia='BIOLOGIA',titulo='A palavra vacina vem de vaca',
 fontes=["Jenner Institute (Universidade de Oxford), 'About Edward Jenner'.","MORABIA, A. Journal of the Royal Society of Medicine (2018), sobre 'An inquiry into the causes and effects of the Variolae Vaccinae' (Jenner, 1798).","CAVAILLON, J.-M.; LEGOUT, S. 'Louis Pasteur: Between Myth and Reality', Biomolecules (2022).","OMS (08/05/2020), 'Commemorating smallpox eradication'."],
 capa=dict(elementos=[obj('frasco',[520,660],w=380,ang=-4),bloco('tudo começou com uma ordenhadeira',[520,1120],size=64,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Toda vez que você toma vacina, está falando de vaca."),f("E não é trocadilho: é a origem da palavra.")],
   elementos=[obj('frasco',[520,620],None,w=360,ang=-4,balanca=True),bloco('VACINA = VACA?',[520,960],None,size=90,cor='tinta',ang=-3),nota('não é trocadilho',[620,1130],[1,'trocadilho'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: Jenner Institute (Univ. de Oxford)',frases=[f("Inglaterra, fim do século 18. A varíola matava e deixava marcas em muita gente.","Inglaterra, fim do século dezoito. A varíola matava e deixava marcas em muita gente."),f("E o médico Edward Jenner conhecia uma história do campo.","E o médico Édward Djêner conhecia uma história do campo."),f("Quem ordenhava vaca e pegava a varíola bovina parecia não pegar a varíola humana.")],
   elementos=[tira('INGLATERRA · SÉC. XVIII',[520,440],None,size=46),tira('EDWARD JENNER',[520,600],[1,'Jenner'],size=52),bloco('varíola bovina',[330,860],[2,'bovina'],size=64,maxw=420),
     seta([520,880],[640,880],[2,'humana']),bloco('varíola humana?',[740,980],[2,'humana'],size=56,cor='tinta',maxw=360)]),
  dict(id='c3',fonte='Fonte: Jenner Institute (Univ. de Oxford)',frases=[f("Em maio de 1796, uma ordenhadeira chamada Sarah Nelmes apareceu com feridas na mão.","Em maio de mil setecentos e noventa e seis, uma ordenhadeira chamada Séra Nélms apareceu com feridas na mão."),f("Ela tinha pegado a doença de uma vaca chamada Blossom.","Ela tinha pegado a doença de uma vaca chamada Blóssom.")],
   elementos=[cal('MAIO 1796',0,[520,700],None,ndias=31,escala=0.5,ang=-3),tira('SARAH NELMES',[330,980],[0,'Sarah'],size=48),tira('vaca: BLOSSOM',[680,1080],[1,'Blossom'],size=48)]),
  dict(id='c4',fonte='Fonte: Jenner Institute; Morabia (2018)',frases=[f("No dia 14 de maio, Jenner fez arranhões no braço de James Phipps, um menino de 8 anos, e passou ali o material daquelas feridas.","No dia catorze de maio, Djêner fez arranhões no braço de Djeims Fips, um menino de oito anos, e passou ali o material daquelas feridas."),f("Em julho, expôs o menino à varíola humana. E ele não ficou doente.")],
   camera=dict(push=0.06),elementos=[carimbo('14 MAIO','1796',[300,520],None,r=100,ang=-8),tira('JAMES PHIPPS · 8 anos',[600,620],[0,'Phipps'],size=44),
     tira('julho: contato com a varíola',[520,860],[1,'julho'],size=42),bloco('não ficou doente',[520,1060],[1,'não ficou'],size=74,cor='tinta')]),
  dict(id='c5',fonte='Fonte: Jenner Institute; Cavaillon & Legout (2022)',frases=[f("Em latim, vaca é vacca. E a varíola da vaca era variolae vaccinae.","Em latim, vaca é váca. E a varíola da vaca era variólai vaquínai."),f("Daí veio a palavra vacinação."),f("Em 1881, o francês Louis Pasteur propôs usar a palavra pra todas as imunizações, em homenagem a Jenner.","Em mil oitocentos e oitenta e um, o francês Luí Pastér propôs usar a palavra pra todas as imunizações, em homenagem a Djêner.")],
   elementos=[verb('vacca','latim, subst. fem.','vaca. Daí "variolae vaccinae": varíola da vaca.',[520,560],[0,'vacca'],w=700),bloco('VACINAÇÃO',[520,830],[1,'vacinação'],size=86),
     tira('PASTEUR · 1881',[330,1040],[2,'Pasteur'],size=48),nota('pra todas',[720,1080],[2,'todas'],cor='laranja',size=58)]),
  dict(id='c6',fonte='Fonte: OMS (2020)',frases=[f("E hoje? A varíola foi a primeira doença humana erradicada do planeta."),f("A OMS declarou isso oficialmente em 1980.","A OMS declarou isso oficialmente em mil novecentos e oitenta."),f("E tudo começou com uma vaca e uma ordenhadeira.")],
   elementos=[obj('globo',[520,640],None,w=340,ang=-4),carimbo('OMS','1980',[760,880],[1,'1980'],r=110,ang=-10),bloco('1ª doença humana erradicada',[480,1080],[0,'primeira'],size=58,maxw=760)]),
  dict(id='c7',frases=[f("Então: vacina vem de vaca, por causa de uma ordenhadeira, uma vaca e um menino."),f("Salva esse pra lembrar na prova de biologia."),ASS],
   elementos=[obj('frasco',[520,620],None,w=320,ang=3),bloco('vacina vem de vaca',[520,980],[0,'vaca'],size=74),nota('salva esse!',[740,1140],[1,'Salva'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 055 MATEMÁTICA (10/12 · cerimônia do Nobel, 130 anos da morte de Nobel)
EPS['SSA-055']=dict(materia='MATEMÁTICA',titulo='Não existe Nobel de Matemática (e a culpa não é de uma traição)',
 fontes=["Nobelprize.org, 'Full text of Alfred Nobel's will' (27/11/1895).","Nobelprize.org, 'The Nobel Prize award ceremonies and banquets'.","Snopes, 'Why is there no Nobel Prize in mathematics?'.","Universidade de Waterloo, Math FAQ, 'Why is there no Nobel in mathematics?'.","Encyclopaedia Britannica, 'Fields Medal' e 'Abel Prize'."],
 capa=dict(elementos=[obj('medalha',[520,660],w=380,ang=-4),bloco('a fofoca sobre isso é falsa',[520,1120],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Hoje tem entrega do Prêmio Nobel. E nenhum deles é de matemática."),f("Tem uma fofoca famosa pra explicar isso. Mas ela é falsa.")],
   elementos=[obj('medalha',[520,620],None,w=360,ang=-4,balanca=True),bloco('NOBEL DE MATEMÁTICA?',[520,950],None,size=70,cor='tinta',ang=-3,maxw=800),nota('a fofoca é falsa',[620,1130],[1,'falsa'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: nobelprize.org',frases=[f("Alfred Nobel, o sueco que inventou a dinamite, assinou o testamento em 1895.","Álfred Nobél, o sueco que inventou a dinamite, assinou o testamento em mil oitocentos e noventa e cinco."),f("Ali, criou 5 prêmios: física, química, medicina, literatura e paz.","Ali, criou cinco prêmios: física, química, medicina, literatura e paz."),f("O de economia só veio em 1968, criado pelo banco central da Suécia.","O de economia só veio em mil novecentos e sessenta e oito, criado pelo banco central da Suécia.")],
   elementos=[jornal('TESTAMENTO','PARIS · 1895','ALFRED NOBEL',[330,720],[0,'testamento'],w=380,ang=-3),tira('física',[720,520],[1,'física'],size=44),tira('química',[720,620],[1,'química'],size=44),
     tira('medicina',[720,720],[1,'medicina'],size=44),tira('literatura',[720,820],[1,'literatura'],size=44),tira('paz',[720,920],[1,'paz'],size=44),tira('economia: só em 1968',[520,1100],[2,'1968'],size=44)]),
  dict(id='c3',fonte='Fonte: Snopes; Univ. de Waterloo',frases=[f("A fofoca diz que a esposa de Nobel o traiu com um matemático sueco, Gösta Mittag-Leffler.","A fofoca diz que a esposa de Nobél o traiu com um matemático sueco, Iêsta Mítag-Léfler."),f("E que, de vingança, ele deixou a matemática de fora.")],
   elementos=[tira('A FOFOCA',[520,450],None,size=56),bloco('a esposa\ntraiu?',[330,660],[0,'esposa'],size=70,cor='tinta',maxw=420),tira('MITTAG-LEFFLER',[660,820],[0,'Mittag'],size=44),nota('vingança!',[560,1000],[1,'vingança'],cor='laranja',size=72)]),
  dict(id='c4',fonte='Fonte: Snopes; nobelprize.org',frases=[f("Só tem um problema: Alfred Nobel nunca se casou.","Só tem um problema: Álfred Nobél nunca se casou."),f("E não existe nenhuma prova histórica dessa história com o matemático.")],
   camera=dict(congela=dict(de=[0,'nunca'],ate=[1,0.9])),elementos=[bloco('NUNCA SE CASOU',[520,560],[0,'nunca'],size=86,cor='tinta',ang=-3),risco([260,760],[780,760],[0,'casou']),bloco('nenhuma prova',[520,960],[1,'prova'],size=78)]),
  dict(id='c5',fonte='Fonte: Snopes; Univ. de Waterloo',frases=[f("O motivo real ninguém sabe com certeza."),f("A explicação mais citada é simples: Nobel premiou áreas que interessavam a ele."),f("E a matemática pura, ao que tudo indica, não era uma delas.")],
   elementos=[bloco('motivo real?',[520,500],None,size=84),nota('ninguém sabe\ncom certeza',[640,700],[0,'ninguém'],cor='laranja',size=58),obj('lampada',[320,960],[1,'interessavam'],w=240),bloco('não era\numa delas',[700,1000],[2,'não era'],size=62,cor='tinta',maxw=380)]),
  dict(id='c6',fonte='Fonte: Britannica; nobelprize.org',frases=[f("E hoje, 10 de dezembro, a entrega acontece no dia da morte de Nobel, em 1896.","E hoje, dez de dezembro, a entrega acontece no dia da morte de Nobél, em mil oitocentos e noventa e seis."),f("E os matemáticos? Ganharam os prêmios deles: a Medalha Fields, desde 1936, só pra quem tem menos de 40 anos.","E os matemáticos? Ganharam os prêmios deles: a Medalha Fílds, desde mil novecentos e trinta e seis, só pra quem tem menos de quarenta anos."),f("E o Prêmio Abel, entregue na Noruega desde 2003.","E o Prêmio Abél, entregue na Noruega desde dois mil e três.")],
   elementos=[cal('DEZEMBRO',2,[520,690],[0,'10 de'],ndias=31,riscar=[10],riscar_em=[0,'10 de'],escala=0.5,ang=-2),tira('FIELDS · desde 1936 · até 40 anos',[520,940],[1,'Fields'],size=40),tira('ABEL · desde 2003',[520,1080],[2,'Abel'],size=46)]),
  dict(id='c7',frases=[f("Então: não tem Nobel de matemática, e a culpa não é de nenhuma traição."),f("Se você pudesse criar um Nobel novo, seria de quê?"),ASS],
   elementos=[obj('medalha',[520,620],None,w=320,ang=3),bloco('um Nobel novo de quê?',[520,1000],[1,'Nobel'],size=68,maxw=780)])])

# ------------------------------------------------------------ 056 HISTÓRIA (10/12 · The Game Awards)
EPS['SSA-056']=dict(materia='HISTÓRIA',titulo='Um dos primeiros videogames foi feito pra animar visita de laboratório',
 fontes=["Brookhaven National Laboratory, 'The First Video Game?' (bnl.gov).","American Physical Society, APS News (2008), 'October 1958: Physicist Invents First Video Game'.","The Game Awards, 'TGA returns December 10, 2026'."],
 capa=dict(elementos=[tv([520,660],w=420,ang=-3),bloco('um jogo de tênis numa tela de 13 cm',[520,1120],size=64,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Um dos primeiros videogames da história foi feito pra animar a visita a um laboratório."),f("E ninguém pediu patente.")],
   elementos=[tv([520,620],None,w=400,ang=-3,balanca=True),bloco('PRA ANIMAR A VISITA',[520,960],None,size=72,cor='tinta',ang=-3,maxw=800),nota('sem patente!',[680,1130],[1,'patente'],cor='laranja',size=60)]),
  dict(id='c2',fonte='Fonte: Brookhaven National Laboratory',frases=[f("Estados Unidos, outubro de 1958. Laboratório Nacional de Brookhaven.","Estados Unidos, outubro de mil novecentos e cinquenta e oito. Laboratório Nacional de Brúk-rêiven."),f("Todo ano, o laboratório abria as portas pra visitantes."),f("E o físico William Higinbotham achou que um jogo ia deixar a visita bem menos parada.","E o físico Uíliam Ríguinbótam achou que um jogo ia deixar a visita bem menos parada.")],
   elementos=[tira('BROOKHAVEN · OUT. 1958',[520,450],None,size=48),tira('dia de visitas',[520,620],[1,'visitantes'],size=50),tira('WILLIAM HIGINBOTHAM',[520,820],[2,'Higinbotham'],size=44),nota('menos parada',[620,1020],[2,'parada'],cor='laranja',size=62)]),
  dict(id='c3',fonte='Fonte: Brookhaven National Laboratory',frases=[f("A ideia: um jogo de tênis, chamado Tennis for Two.","A ideia: um jogo de tênis, chamado Ténis for Tú."),f("O cérebro era um pequeno computador analógico."),f("E a tela, um osciloscópio de só 5 polegadas. Uns 13 centímetros.","E a tela, um osciloscópio de só cinco polegadas. Uns treze centímetros.")],
   elementos=[bloco('TENNIS FOR TWO',[520,560],None,size=80,cor='tinta',ang=-3),obj('computador',[330,860],[1,'computador'],w=280),tira('computador analógico',[330,1050],[1,'analógico'],size=40),
     num('13 cm',[720,850],[2,'13'],size=140),tira('de tela',[720,990],[2,'tela'],size=44)]),
  dict(id='c4',fonte='Fonte: Brookhaven National Laboratory',frases=[f("A quadra aparecia de lado, com a rede no meio."),f("Cada jogador tinha um botão e um controle de girar pra escolher o ângulo da raquetada."),f("Centenas de visitantes fizeram fila pra jogar.")],
   camera=dict(push=0.06),elementos=[tv([520,620],None,w=380),seta([300,860],[740,860],[0,'quadra']),tira('botão + controle de girar',[520,960],[1,'botão'],size=42),bloco('fila de centenas',[520,1120],[2,'fila'],size=64)]),
  dict(id='c5',fonte='Fonte: Brookhaven Lab; APS News (2008)',frases=[f("Higinbotham não pediu patente. E disse depois que, se tivesse pedido, ela seria do governo americano.","Ríguinbótam não pediu patente. E disse depois que, se tivesse pedido, ela seria do governo americano."),f("Depois de 2 anos, o jogo foi desmontado e as peças foram usadas em outras coisas.","Depois de dois anos, o jogo foi desmontado e as peças foram usadas em outras coisas.")],
   elementos=[bloco('PATENTE?',[520,500],None,size=90,cor='tinta'),risco([330,500],[710,500],[0,'não pediu']),nota('seria do governo',[620,700],[0,'governo'],cor='laranja',size=58),
     num('2',[330,960],[1,'2 anos'],size=220),tira('anos depois: desmontado',[680,980],[1,'desmontado'],size=40)]),
  dict(id='c6',fonte='Fonte: The Game Awards (2026); Brookhaven Lab',frases=[f("E hoje, 10 de dezembro, tem o The Game Awards, uma das maiores premiações de games do mundo.","E hoje, dez de dezembro, tem o The Gueim Auórds, uma das maiores premiações de games do mundo."),f("E o próprio laboratório diz: não dá pra dar o título de primeiro videogame a uma invenção só."),f("Mas o tênis de 1958 está entre os pioneiros.","Mas o tênis de mil novecentos e cinquenta e oito está entre os pioneiros.")],
   elementos=[tira('THE GAME AWARDS · 10/12',[520,450],None,size=46),obj('celular',[300,760],[0,'games'],w=230,ang=-4),bloco('1º videogame?',[680,740],[1,'primeiro'],size=60,maxw=400),bloco('entre os pioneiros',[520,1060],[2,'pioneiros'],size=72,cor='tinta')]),
  dict(id='c7',frases=[f("Então: um dos primeiros videogames nasceu pra animar uma visita, numa tela de 13 centímetros.","Então: um dos primeiros videogames nasceu pra animar uma visita, numa tela de treze centímetros."),f("E você, qual foi o primeiro videogame que jogou na vida?"),ASS],
   elementos=[tv([520,620],None,w=360,ang=3),bloco('qual foi o seu primeiro?',[520,1000],[1,'primeiro'],size=66,maxw=780)])])

# ------------------------------------------------------------ 057 SOCIOLOGIA (11/12 · 80 anos da UNICEF)
EPS['SSA-057']=dict(materia='SOCIOLOGIA',titulo='O "E" da sigla UNICEF não significa mais nada',
 fontes=["UNICEF, '1946–2006: Sixty Years for Children'.","UNICEF, 'Emerging from the ashes of war (1946–1979)'.","UNICEF (2016), 'UNICEF commemorates 70 years of tireless work'.","Nobelprize.org, 'UNICEF – Facts' (Nobel da Paz 1965).","Encyclopaedia Britannica, 'UNICEF'."],
 capa=dict(elementos=[bloco('UNICEF',[520,640],size=150,cor='tinta',ang=-3),bloco('uma letra que ficou sem sentido',[520,1110],size=66,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Na sigla UNICEF tem uma letra que não significa mais nada.","Na sigla Unicéf tem uma letra que não significa mais nada."),f("E ela é uma lembrança do fim de uma guerra.")],
   elementos=[bloco('UNICEF',[520,620],None,size=150,cor='tinta',ang=-3,balanca=True),nota('o E?',[700,820],None,cor='laranja',size=80),tira('fim de uma guerra',[520,1080],[1,'guerra'],size=50)]),
  dict(id='c2',fonte='Fonte: UNICEF',frases=[f("11 de dezembro de 1946. A Segunda Guerra tinha acabado havia pouco mais de um ano.","Onze de dezembro de mil novecentos e quarenta e seis. A Segunda Guerra tinha acabado havia pouco mais de um ano."),f("E muitas crianças na Europa, na China e no Oriente Médio precisavam de comida, remédio e roupa.")],
   elementos=[carimbo('11 DEZ','1946',[330,560],None,r=110,ang=-8),tira('pós-guerra',[700,600],None,size=52),obj('globo',[520,880],[1,'Europa'],w=280),tira('comida · remédio · roupa',[520,1100],[1,'comida'],size=44)]),
  dict(id='c3',fonte='Fonte: UNICEF; Britannica',frases=[f("A Assembleia Geral da ONU criou um fundo especial."),f("Nome em inglês: United Nations International Children's Emergency Fund.","Nome em inglês: Iunáited Nêixons Internéxonal Tchíldrens Imérdjenci Fând."),f("Ou seja: Fundo Internacional de Emergência das Nações Unidas para a Infância.")],
   elementos=[tira('ONU · ASSEMBLEIA GERAL',[520,450],None,size=46),tira('United Nations International',[520,620],[1,'United'],size=42),tira("Children's EMERGENCY Fund",[520,740],[1,'Emergency'],size=42),
     bloco('EMERGÊNCIA',[520,1000],[2,'Emergência'],size=90,cor='tinta',ang=-3)]),
  dict(id='c4',fonte='Fonte: UNICEF',frases=[f("O E era de emergência."),f("A ideia era um socorro rápido pra um momento de crise.")],
   camera=dict(push=0.06),elementos=[num('E',[520,640],None,size=320),bloco('= emergência',[520,920],None,size=80),nota('socorro rápido',[620,1100],[1,'socorro'],cor='laranja',size=60)]),
  dict(id='c5',fonte='Fonte: UNICEF; Britannica',frases=[f("Só que a necessidade não acabou. Em 1953, o fundo virou permanente.","Só que a necessidade não acabou. Em mil novecentos e cinquenta e três, o fundo virou permanente."),f("Saíram do nome as palavras internacional e emergência. Ficou Fundo das Nações Unidas para a Infância."),f("Mas a sigla já era famosa. E ficou do jeito que estava.")],
   elementos=[tira('1953 · PERMANENTE',[520,450],None,size=50),tira('International',[330,640],[1,'internacional'],size=46),risco([200,640],[470,640],[1,'Saíram']),tira('Emergency',[700,640],[1,'emergência'],size=46),risco([590,640],[810,640],[1,'Saíram']),
     bloco('a sigla ficou',[520,960],[2,'sigla'],size=80,cor='tinta',ang=-3)]),
  dict(id='c6',fonte='Fonte: UNICEF; nobelprize.org',frases=[f("E hoje? A UNICEF faz 80 anos neste 11 de dezembro.","E hoje? A Unicéf faz oitenta anos neste onze de dezembro."),f("Em 1965, ganhou o Nobel da Paz.","Em mil novecentos e sessenta e cinco, ganhou o Nobel da Paz."),f("E continua com a sigla de quando era só uma emergência.")],
   elementos=[num('80',[520,620],None,size=280),tira('anos · 11/12/2026',[520,820],[0,'80'],size=46),obj('medalha',[330,1040],[1,'Nobel'],w=200),tira('NOBEL DA PAZ · 1965',[680,1040],[1,'1965'],size=40)]),
  dict(id='c7',frases=[f("Então: o E da UNICEF lembra uma emergência que virou permanente.","Então: o E da Unicéf lembra uma emergência que virou permanente."),f("Manda pra aquele amigo que adora saber o que significa cada sigla."),ASS],
   elementos=[bloco('UNICEF',[520,620],None,size=140,cor='tinta',ang=3),bloco('manda pro amigo\ndas siglas',[520,1000],[1,'Manda'],size=62,maxw=740)])])

# ------------------------------------------------------------ 058 GEOGRAFIA (11/12 · Dia Internacional das Montanhas)
EPS['SSA-058']=dict(materia='GEOGRAFIA',titulo='O Everest é a montanha mais alta? Depende de onde você mede',
 fontes=["Al Jazeera (08/12/2020), 'Mt Everest: Nepal, China announce revised height at 8,848.86 metres'.","NOAA Ocean Service, 'What is the highest point on Earth as measured from Earth's center?'.","USGS, 'How big are Hawaiian volcanoes?' e 'Mauna Kea'.","Encyclopaedia Britannica, 'Is Mount Everest really the tallest mountain in the world?'.","ONU, Resolução A/RES/57/245 (2002); FAO, 'International Mountain Day'."],
 capa=dict(elementos=[obj('montanha',[520,680],w=460),bloco('depende de onde você mede',[520,1120],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("O Everest é a montanha mais alta do mundo. Ou não."),f("Depende de onde você começa a medir.")],
   elementos=[obj('montanha',[520,640],None,w=440,balanca=True),bloco('OU NÃO?',[520,980],None,size=100,cor='tinta',ang=-3),nota('depende!',[700,1140],[1,'Depende'],cor='laranja',size=62)]),
  dict(id='c2',fonte='Fonte: Al Jazeera (2020)',frases=[f("Medido a partir do nível do mar, o Everest ganha fácil: 8.848,86 metros.","Medido a partir do nível do mar, o Everest ganha fácil: oito mil oitocentos e quarenta e oito vírgula oitenta e seis metros."),f("Esse número foi anunciado por China e Nepal juntos, em 2020.","Esse número foi anunciado por China e Nepal juntos, em dois mil e vinte.")],
   elementos=[tira('EVEREST · do nível do mar',[520,450],None,size=46),num('8.848,86 m',[520,700],[0,'8.848'],size=140),tira('CHINA + NEPAL · 2020',[520,960],[1,'China'],size=48)]),
  dict(id='c3',fonte='Fonte: USGS',frases=[f("Agora olha o Mauna Kea, um vulcão no Havaí.","Agora olha o Mauna Kêa, um vulcão no Havaí."),f("Acima do mar, ele tem só uns 4.200 metros.","Acima do mar, ele tem só uns quatro mil e duzentos metros."),f("Só que ele começa lá embaixo, no fundo do oceano, uns 6 mil metros abaixo da superfície.","Só que ele começa lá embaixo, no fundo do oceano, uns seis mil metros abaixo da superfície.")],
   elementos=[tira('MAUNA KEA · HAVAÍ',[520,450],None,size=50),obj('montanha',[330,720],[0,'vulcão'],w=300),tira('~4.200 m acima do mar',[700,660],[1,'4.200'],size=40),
     seta([700,800],[700,1060],[2,'fundo'],cor='laranja'),tira('~6.000 m debaixo d\'água',[560,1120],[2,'6 mil'],size=40)]),
  dict(id='c4',fonte='Fonte: NOAA; USGS',frases=[f("Da base até o topo, o Mauna Kea passa de 10.200 metros.","Da base até o topo, o Mauna Kêa passa de dez mil e duzentos metros."),f("Uns 1.300 metros a mais que o Everest inteiro.","Uns mil e trezentos metros a mais que o Everest inteiro.")],
   camera=dict(push=0.06,zooms=[dict(e=[0,'10.200'],escala=1.12,alvo=[520,640],dur=0.7)]),elementos=[num('10.200 m',[520,640],[0,'10.200'],size=170),tira('da base ao topo',[520,820],[0,'base'],size=46),bloco('+1.300 m que o Everest',[520,1040],[1,'1.300'],size=64,cor='tinta',maxw=800)]),
  dict(id='c5',fonte='Fonte: NOAA; Britannica',frases=[f("E tem uma terceira resposta. A Terra não é uma bola perfeita: é mais larga na linha do Equador."),f("Por isso o pico do Chimborazo, no Equador, é o ponto mais distante do centro da Terra.","Por isso o pico do Chimborázo, no Equador, é o ponto mais distante do centro da Terra."),f("Fica uns 2 quilômetros mais longe do centro que o topo do Everest.","Fica uns dois quilômetros mais longe do centro que o topo do Everest.")],
   elementos=[obj('globo',[330,640],None,w=300),nota('mais larga\nno Equador',[720,620],[0,'larga'],cor='laranja',size=56),tira('CHIMBORAZO · EQUADOR',[520,880],[1,'Chimborazo'],size=46),bloco('+2 km do centro',[520,1070],[2,'2 quilômetros'],size=70,cor='tinta')]),
  dict(id='c6',fonte='Fonte: ONU, Res. 57/245; FAO',frases=[f("E hoje, 11 de dezembro, é o Dia Internacional das Montanhas.","E hoje, onze de dezembro, é o Dia Internacional das Montanhas."),f("A ONU criou a data em 2002. E ela é celebrada desde 2003.","A ONU criou a data em dois mil e dois. E ela é celebrada desde dois mil e três.")],
   elementos=[cal('DEZEMBRO',2,[520,690],[0,'11 de'],ndias=31,riscar=[11],riscar_em=[0,'11 de'],escala=0.5,ang=-2),bloco('DIA DAS MONTANHAS',[520,950],[0,'Dia'],size=62,maxw=820),tira('ONU · 2002',[700,1130],[1,'2002'],size=48)]),
  dict(id='c7',frases=[f("Então: o mais alto do nível do mar é o Everest. Da base ao topo, o Mauna Kea. E o mais longe do centro, o Chimborazo.","Então: o mais alto do nível do mar é o Everest. Da base ao topo, o Mauna Kêa. E o mais longe do centro, o Chimborázo."),f("Pra você, qual merece o título? Comenta."),ASS],
   elementos=[obj('montanha',[520,600],None,w=380),tira('EVEREST',[300,860],[0,'Everest'],size=46),tira('MAUNA KEA',[720,920],[0,'Mauna'],size=46),tira('CHIMBORAZO',[460,1020],[0,'Chimborazo'],size=46),nota('qual merece?',[680,1140],[1,'merece'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 059 FÍSICA (12/12 · 125 anos do sinal transatlântico de Marconi)
EPS['SSA-059']=dict(materia='FÍSICA',titulo='A primeira mensagem de rádio a cruzar o Atlântico era só a letra S',
 fontes=["IEEE / ETHW, 'Milestones: Reception of Transatlantic Radio Signals, 1901'.","Museum of the History of Science (Oxford), 'Marconi: the Atlantic crossing'.","Parks Canada, 'Signal Hill National Historic Site: communications'.","The Canadian Encyclopedia, 'Guglielmo Marconi'.","Nobelprize.org, 'The Nobel Prize in Physics 1909' e biografia de Marconi."],
 capa=dict(elementos=[obj('pipa',[520,660],w=400,ang=-4),num('• • •',[520,1080],size=200,cor='tinta')]),
 cenas=[
  dict(id='c1',frases=[f("A primeira mensagem de rádio a atravessar o Atlântico tinha uma letra só."),f("E até hoje tem gente que duvida que ela chegou.")],
   elementos=[radio([520,620],None,w=380,ang=-3,balanca=True),bloco('UMA LETRA SÓ',[520,960],None,size=90,cor='tinta',ang=-3),nota('será que chegou?',[620,1130],[1,'duvida'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: IEEE/ETHW; nobelprize.org',frases=[f("12 de dezembro de 1901. Signal Hill, na Terra Nova, hoje parte do Canadá.","Doze de dezembro de mil novecentos e um. Sígnal Ríl, na Terra Nova, hoje parte do Canadá."),f("O italiano Guglielmo Marconi, de 27 anos, esperava um sinal mandado da Inglaterra, de Poldhu, na Cornualha.","O italiano Guliélmo Marcôni, de vinte e sete anos, esperava um sinal mandado da Inglaterra, de Póldu, na Cornualha.")],
   elementos=[carimbo('12 DEZ','1901',[300,540],None,r=110,ang=-8),tira('SIGNAL HILL',[680,560],None,size=50),tira('MARCONI · 27 anos',[520,800],[1,'Marconi'],size=48),tira('POLDHU · CORNUALHA',[520,960],[1,'Poldhu'],size=46),seta([260,1100],[800,1100],[1,'Inglaterra'])]),
  dict(id='c3',fonte='Fonte: Parks Canada; IEEE/ETHW; Museu de Oxford',frases=[f("Eram uns 3.500 quilômetros de oceano.","Eram uns três mil e quinhentos quilômetros de oceano."),f("Pra antena ficar bem alta, ele prendeu um fio de uns 150 metros numa pipa.","Pra antena ficar bem alta, ele prendeu um fio de uns cento e cinquenta metros numa pipa."),f("Antes disso, os balões falharam e uma pipa foi levada pelo vento.")],
   elementos=[num('3.500 km',[520,520],[0,'3.500'],size=150),obj('pipa',[330,860],[1,'pipa'],w=320,ang=-6),tira('fio de ~150 m',[700,800],[1,'150'],size=46),nota('levada\npelo vento',[700,1040],[2,'vento'],cor='laranja',size=56)]),
  dict(id='c4',fonte='Fonte: Museu de História da Ciência de Oxford',frases=[f("A mensagem combinada era a letra S do código Morse: só 3 pontinhos.","A mensagem combinada era a letra S do código Morse: só três pontinhos."),f("E Marconi e o assistente, George Kemp, disseram ter ouvido os cliques no fone.","E Marcôni e o assistente, Djórdj Kémp, disseram ter ouvido os cliques no fone.")],
   camera=dict(push=0.06,zooms=[dict(e=[0,'3 pontinhos'],escala=1.12,alvo=[520,640],dur=0.7)]),elementos=[bloco('S',[520,480],None,size=120,cor='tinta'),num('• • •',[520,660],[0,'3 pontinhos'],size=220),tira('código Morse',[520,860],[0,'Morse'],size=48),tira('GEORGE KEMP',[520,1040],[1,'Kemp'],size=48)]),
  dict(id='c5',fonte='Fonte: IEEE/ETHW; The Canadian Encyclopedia',frases=[f("Só que o sinal era fraco demais pra ser registrado em fita."),f("As únicas testemunhas foram os dois. Por isso, até hoje tem físico que duvida que ele ouviu mesmo.")],
   elementos=[bloco('sem registro',[520,520],None,size=84,cor='tinta',ang=-3),tira('testemunhas: 2',[520,760],[1,'testemunhas'],size=52),nota('ouviu mesmo?',[600,1000],[1,'duvida'],cor='laranja',size=70)]),
  dict(id='c6',fonte='Fonte: nobelprize.org (1909)',frases=[f("Dúvida ou não, a ideia pegou. Em 1909, Marconi dividiu o Nobel de Física pelo telégrafo sem fio.","Dúvida ou não, a ideia pegou. Em mil novecentos e nove, Marcôni dividiu o Nobel de Física pelo telégrafo sem fio."),f("E hoje, 12 de dezembro, aquele S faz 125 anos.","E hoje, doze de dezembro, aquele S faz cento e vinte e cinco anos."),f("Celular, wi-fi e rádio do carro funcionam com ondas de rádio, atravessando o ar do mesmo jeito.","Celular, uai-fai e rádio do carro funcionam com ondas de rádio, atravessando o ar do mesmo jeito.")],
   elementos=[obj('medalha',[300,560],[0,'Nobel'],w=210),tira('NOBEL · 1909',[680,560],[0,'1909'],size=48),num('125',[520,860],[1,'125'],size=200),obj('celular',[760,1060],[2,'Celular'],w=180,ang=6),tira('ondas de rádio',[400,1110],[2,'ondas'],size=44)]),
  dict(id='c7',frases=[f("Então: 125 anos atrás, um oceano foi atravessado por 3 pontinhos.","Então: cento e vinte e cinco anos atrás, um oceano foi atravessado por três pontinhos."),f("Agora você sabe que toda conversa sem fio começou com um S."),ASS],
   elementos=[radio([520,620],None,w=340,ang=3),num('• • •',[520,940],[0,'3 pontinhos'],size=180,cor='tinta'),nota('começou com um S',[620,1130],[1,'começou'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 060 ARTE
EPS['SSA-060']=dict(materia='ARTE',titulo='Van Gogh achou A Noite Estrelada um fracasso',
 fontes=["Encyclopaedia Britannica, 'The Starry Night'.","MoMA Learning, 'Vincent van Gogh. The Starry Night. 1889'.","THOMSON, Richard. 'Vincent van Gogh: The Starry Night' (MoMA, PDF).","Getty, 'Van Gogh's Shelter'.","Carta de Van Gogh a Émile Bernard (nov. 1889), via WebExhibits."],
 capa=dict(elementos=[obj('moldura',[520,660],w=420,ang=-3),bloco('o próprio pintor não gostou',[520,1120],size=70,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("Um dos quadros mais famosos do mundo foi chamado de fracasso pelo próprio pintor."),f("A Noite Estrelada, de Van Gogh.","A Noite Estrelada, de Van Gógui.")],
   elementos=[obj('moldura',[520,620],None,w=400,ang=-3,balanca=True),nota('fracasso?',[720,860],None,cor='laranja',size=70),bloco('A NOITE ESTRELADA',[480,1080],[1,'Noite'],size=66,cor='tinta')]),
  dict(id='c2',fonte='Fonte: Getty; Britannica',frases=[f("Em 1889, depois de crises de saúde, Vincent van Gogh se internou por vontade própria num hospital psiquiátrico.","Em mil oitocentos e oitenta e nove, depois de crises de saúde, Vincent van Gógui se internou por vontade própria num hospital psiquiátrico."),f("Ficava em Saint-Rémy-de-Provence, no sul da França.","Ficava em Sã Remí de Provâns, no sul da França.")],
   elementos=[tira('1889',[520,450],None,size=60),bloco('por vontade\nprópria',[520,700],[0,'vontade'],size=72,maxw=600),tira('SAINT-RÉMY · SUL DA FRANÇA',[520,1000],[1,'Saint'],size=42)]),
  dict(id='c3',fonte='Fonte: Britannica; MoMA',frases=[f("Da janela com grades do quarto, ele via o campo e o céu antes do amanhecer."),f("Mas ele não podia pintar no quarto."),f("Então pintou A Noite Estrelada de memória e de imaginação, em outra sala, em junho de 1889.","Então pintou A Noite Estrelada de memória e de imaginação, em outra sala, em junho de mil oitocentos e oitenta e nove.")],
   elementos=[nota('janela com grades',[520,480],None,size=62),bloco('não podia\npintar no quarto',[520,720],[1,'não podia'],size=64,cor='tinta',maxw=640),tira('de memória',[330,980],[2,'memória'],size=50),tira('JUNHO 1889',[700,1060],[2,'junho'],size=50)]),
  dict(id='c4',fonte='Fonte: MoMA',frases=[f("Por isso o quadro não é um retrato fiel da vista."),f("Ele mudou a vila e a igreja."),f("E aquele céu cheio de redemoinhos também saiu da cabeça dele.")],
   camera=dict(push=0.07),elementos=[obj('moldura',[520,640],None,w=360,ang=2),tira('a vila: mudada',[300,890],[1,'vila'],size=46),tira('a igreja: mudada',[720,1010],[1,'igreja'],size=46),nota('céu inventado',[520,1140],[2,'céu'],cor='laranja',size=58)]),
  dict(id='c5',fonte='Fonte: Britannica; carta a Émile Bernard (1889)',frases=[f("Meses depois, numa carta ao pintor Émile Bernard, ele escreveu que tinha se deixado levar e pintado estrelas grandes demais.","Meses depois, numa carta ao pintor Emíl Bernár, ele escreveu que tinha se deixado levar e pintado estrelas grandes demais."),f("E chamou aquilo de mais um fracasso.")],
   elementos=[jornal('LETTRE','NOV. 1889','À ÉMILE BERNARD',[330,720],None,w=380,ang=-4,marca=[0,'estrelas']),bloco('estrelas\ngrandes demais',[700,640],[0,'grandes'],size=56,maxw=400),bloco('mais um fracasso',[560,1060],[1,'fracasso'],size=72,cor='tinta',ang=-3)]),
  dict(id='c6',fonte='Fonte: MoMA; Britannica',frases=[f("E hoje? A Noite Estrelada está no Museu de Arte Moderna de Nova York desde 1941.","E hoje? A Noite Estrelada está no Museu de Arte Moderna de Nova York desde mil novecentos e quarenta e um."),f("E aparece em caneca, camiseta e capinha de celular no mundo inteiro.")],
   elementos=[tira('MoMA · NOVA YORK',[520,450],None,size=50),carimbo('ACERVO','1941',[330,700],[0,'1941'],r=110,ang=-8),obj('celular',[700,780],[1,'celular'],w=240,ang=6),nota('no mundo inteiro',[520,1080],[1,'mundo'],cor='laranja',size=60)]),
  dict(id='c7',fonte='Fonte: Britannica',frases=[f("Então: o quadro que ele chamou de fracasso virou uma das pinturas mais famosas da história."),f("Você já fez algo que achou ruim e depois todo mundo elogiou?"),ASS],
   elementos=[obj('moldura',[520,620],None,w=360,ang=3),bloco('achou ruim e\ntodo mundo elogiou?',[520,1010],[1,'elogiou'],size=58,maxw=760)])])

# ------------------------------------------------------------ 061 QUÍMICA
EPS['SSA-061']=dict(materia='QUÍMICA',titulo='O sal de cozinha é um metal que pega fogo na água + um gás venenoso',
 fontes=["Royal Society of Chemistry, Periodic Table: 'Sodium' (podcast) e 'Chlorine'.","Royal Society of Chemistry (Education), 'Alkali metals'.","Encyclopaedia Britannica, 'Sodium: chemical properties'.","LibreTexts Chemistry, 'The Reaction of Sodium with Chlorine'.","OMS, 'Salt reduction' (fact sheet).","Agência Brasil (26/11/2019), com dados da Pesquisa Nacional de Saúde."],
 capa=dict(elementos=[obj('saleiro',[520,660],w=380,ang=-4),bloco('metal que pega fogo + gás venenoso',[520,1120],size=60,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("O sal da sua comida junta um metal que pega fogo e um gás venenoso."),f("E mesmo assim você come isso todo dia.")],
   elementos=[obj('saleiro',[520,620],None,w=360,ang=-4,balanca=True),bloco('Na + Cl',[520,960],None,size=110,cor='tinta',ang=-3),nota('todo dia!',[720,1130],[1,'todo dia'],cor='laranja',size=60)]),
  dict(id='c2',fonte='Fonte: Royal Society of Chemistry; Britannica',frases=[f("O primeiro ingrediente é o sódio. Um metal tão mole que dá pra cortar com faca."),f("Na água, ele reage com violência, solta hidrogênio e pode até pegar fogo."),f("Por isso, no laboratório, ele fica guardado no óleo.")],
   elementos=[verb('sódio (Na)','metal, subst. masc.','macio, prateado; reage com violência com a água.',[520,560],[0,'sódio'],w=700),nota('pega fogo!',[330,860],[1,'fogo'],cor='laranja',size=72),
     obj('frasco',[720,920],[2,'óleo'],w=230),tira('guardado no óleo',[520,1110],[2,'guardado'],size=46)]),
  dict(id='c3',fonte='Fonte: Royal Society of Chemistry',frases=[f("O segundo é o cloro: um gás amarelo-esverdeado, de cheiro sufocante."),f("E muito venenoso.")],
   elementos=[verb('cloro (Cl)','gás, subst. masc.','amarelo-esverdeado, denso, de cheiro sufocante.',[520,600],None,w=700),bloco('MUITO VENENOSO',[520,980],[1,'venenoso'],size=80,cor='tinta',ang=-3)]),
  dict(id='c4',fonte='Fonte: LibreTexts Chemistry',frases=[f("Quando os dois se encontram, o sódio entrega um elétron pro cloro."),f("O sódio fica positivo, o cloro fica negativo, e os dois se atraem."),f("Isso é uma ligação iônica. E o resultado é o cloreto de sódio: o sal de cozinha.")],
   camera=dict(push=0.06),elementos=[tira('Na',[300,520],None,size=70),tira('Cl',[740,520],None,size=70),seta([380,520],[660,520],[0,'elétron'],cor='laranja'),tira('Na+',[300,720],[1,'positivo'],size=60),tira('Cl-',[740,720],[1,'negativo'],size=60),
     bloco('LIGAÇÃO IÔNICA',[520,940],[2,'ligação'],size=72,cor='tinta'),tira('NaCl = sal',[520,1110],[2,'cloreto'],size=52)]),
  dict(id='c5',fonte='Fonte: OMS; Royal Society of Chemistry',frases=[f("E tudo muda. Nem metal que pega fogo, nem gás venenoso: um cristal branco, estável, que vai na comida."),f("E o corpo precisa do sódio, por exemplo, pra transmitir os impulsos nervosos.")],
   elementos=[obj('saleiro',[330,680],None,w=300,ang=-4),bloco('cristal\nestável',[720,640],[0,'cristal'],size=66,maxw=360),obj('coracao',[700,960],[1,'corpo'],w=200),tira('impulsos nervosos',[400,1080],[1,'impulsos'],size=44)]),
  dict(id='c6',fonte='Fonte: OMS; Pesquisa Nacional de Saúde (2019)',frases=[f("E hoje? A OMS recomenda menos de 5 gramas de sal por dia.","E hoje? A OMS recomenda menos de cinco gramas de sal por dia."),f("Segundo a Pesquisa Nacional de Saúde, o brasileiro come em média 9,3 gramas. Quase o dobro.","Segundo a Pesquisa Nacional de Saúde, o brasileiro come em média nove vírgula três gramas. Quase o dobro.")],
   elementos=[tira('OMS: menos de',[330,460],None,size=48),num('5 g',[330,640],[0,'5 gramas'],size=170),tira('Brasil: média de',[720,780],[1,'brasileiro'],size=44),num('9,3 g',[720,960],[1,'9,3'],size=170),nota('quase o dobro',[480,1140],[1,'dobro'],cor='laranja',size=56)]),
  dict(id='c7',frases=[f("Então: o sal é um metal que pega fogo e um gás venenoso que, juntos, viraram tempero."),f("Salva esse pra lembrar de ligação iônica na prova."),ASS],
   elementos=[obj('saleiro',[520,620],None,w=320,ang=3),bloco('Na + Cl = tempero',[520,980],[0,'tempero'],size=72),nota('salva esse!',[740,1140],[1,'Salva'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 062 FÍSICA (13/12 · pico das Gemínidas, madrugada de 13 para 14/12)
EPS['SSA-062']=dict(materia='FÍSICA',titulo='A melhor chuva de meteoros do ano vem de um asteroide',
 fontes=["NASA Science, 'Geminids'.","NASA, Watch the Skies (12/12/2024), 'It's an asteroid! It's a comet! It's the Geminids'.","International Meteor Organization, 'Meteor Shower Calendar 2026'.","Star Walk (2026), 'Geminídeas 2026'.","Agência Gov/EBC (12/2024), Gemínidas no Brasil (Exoss/Observatório Nacional)."],
 capa=dict(elementos=[obj('meteoro',[520,660],w=440),bloco('não é de cometa',[520,1110],size=80,maxw=760)]),
 cenas=[
  dict(id='c1',frases=[f("A melhor chuva de meteoros do ano vem de um asteroide, e não de um cometa."),f("E o pico é nesta madrugada.")],
   elementos=[obj('meteoro',[520,620],None,w=420,balanca=True),bloco('ASTEROIDE, NÃO COMETA',[520,960],None,size=66,cor='tinta',ang=-3,maxw=800),nota('nesta madrugada!',[620,1130],[1,'madrugada'],cor='laranja',size=58)]),
  dict(id='c2',fonte='Fonte: NASA',frases=[f("Estrela cadente não é estrela. É poeira e pedrinha entrando na atmosfera muito rápido e queimando."),f("E quase toda chuva de meteoros vem de um cometa: a Terra passa pela trilha de poeira que ele deixou.")],
   elementos=[tira('ESTRELA CADENTE',[520,480],None,size=52),nota('não é estrela!',[680,600],[0,'não é'],cor='laranja',size=52),obj('meteoro',[330,760],[0,'poeira'],w=300),nota('queimando',[720,760],[0,'queimando'],cor='laranja',size=60),tira('quase sempre: trilha de cometa',[520,1060],[1,'cometa'],size=40)]),
  dict(id='c3',fonte='Fonte: NASA',frases=[f("As Gemínidas são a exceção. Elas vêm do 3200 Faetonte, classificado como asteroide.","As Gemínidas são a exceção. Elas vêm do três mil e duzentos Faetônte, classificado como asteroide."),f("Ele foi descoberto em 1983, por um satélite.","Ele foi descoberto em mil novecentos e oitenta e três, por um satélite."),f("Tem astrônomo que chama ele de cometa de pedra.")],
   elementos=[bloco('EXCEÇÃO',[520,480],None,size=84,cor='tinta',ang=-3),tira('3200 FAETONTE',[520,660],[0,'Faetonte'],size=56),tira('descoberto em 1983',[520,800],[1,'1983'],size=46),nota('"cometa de pedra"',[540,1020],[2,'pedra'],cor='laranja',size=64)]),
  dict(id='c4',fonte='Fonte: NASA; IMO',frases=[f("Os pedacinhos dele entram na atmosfera a uns 35 quilômetros por segundo.","Os pedacinhos dele entram na atmosfera a uns trinta e cinco quilômetros por segundo."),f("Em condições perfeitas, dá pra ver até uns 120 meteoros por hora.","Em condições perfeitas, dá pra ver até uns cento e vinte meteoros por hora.")],
   camera=dict(push=0.06),elementos=[num('35 km/s',[520,580],[0,'35'],size=170),dict(t='contador',de=0,ate=120,fmt='{n} por hora',pos=[520,920],e=[1,'120'],size=96),tira('em condições perfeitas',[520,1100],[1,'perfeitas'],size=44)]),
  dict(id='c5',fonte='Fonte: IMO; Agência Gov/EBC',frases=[f("Mas aqui no hemisfério sul, o ponto de onde eles parecem sair, na constelação de Gêmeos, fica baixo no céu."),f("Então dá pra ver menos meteoros. E o melhor horário é de madrugada, depois da meia-noite.")],
   elementos=[obj('globo',[330,680],None,w=280),tira('HEMISFÉRIO SUL',[700,580],None,size=46),nota('Gêmeos: baixo\nno céu',[700,780],[0,'baixo'],cor='laranja',size=54),bloco('depois da\nmeia-noite',[520,1040],[1,'meia-noite'],size=66,cor='tinta',maxw=600)]),
  dict(id='c6',fonte='Fonte: IMO (2026); Star Walk',frases=[f("E hoje? O pico das Gemínidas é entre 13 e 14 de dezembro.","E hoje? O pico das Gemínidas é entre treze e catorze de dezembro."),f("E a Lua vai estar fininha, quase sem atrapalhar."),f("Procure um lugar escuro, longe das luzes da cidade, e olhe pro céu.")],
   elementos=[cal('DEZEMBRO',2,[520,690],[0,'13 e 14'],ndias=31,riscar=[13,14],riscar_em=[0,'13 e 14'],escala=0.5,ang=-2),tira('Lua fininha',[330,960],[1,'Lua'],size=50),nota('lugar escuro',[680,1080],[2,'escuro'],cor='laranja',size=58)]),
  dict(id='c7',frases=[f("Então: as estrelas cadentes de dezembro são pedaços de um asteroide."),f("Marca quem vai acordar de madrugada pra ver com você."),ASS],
   elementos=[obj('meteoro',[520,620],None,w=380),bloco('marca quem vai\nver com você',[520,1010],[1,'Marca'],size=62,maxw=740)])])

# ------------------------------------------------------------ 063 HISTÓRIA (14/12 · 115 anos de Amundsen no Polo Sul)
EPS['SSA-063']=dict(materia='HISTÓRIA',titulo='Amundsen chegou primeiro ao Polo Sul com o que aprendeu no Ártico',
 fontes=["Fram Museum (frammuseum.no), 'The South Pole expedition' e 'Gjøa'.","The Canadian Encyclopedia, 'Roald Amundsen'.","The Antarctic Sun (USAP/NSF), sobre a barraca Polheim.","Polar Record (Cambridge University Press), sobre as cartas de Amundsen a Scott.","History.com, 'Amundsen reaches South Pole' e 'Scott reaches the South Pole'."],
 capa=dict(elementos=[obj('bandeira',[520,660],w=420),bloco('o truque veio do Ártico',[520,1110],size=74,maxw=780)]),
 cenas=[
  dict(id='c1',frases=[f("O primeiro homem no Polo Sul venceu com o que aprendeu no Ártico."),f("E ele escondeu o destino até da própria tripulação.")],
   elementos=[obj('bandeira',[520,620],None,w=400,balanca=True),bloco('POLO SUL',[520,950],None,size=100,cor='tinta',ang=-3),nota('destino escondido',[620,1130],[1,'escondeu'],cor='laranja',size=56)]),
  dict(id='c2',fonte='Fonte: Fram Museum',frases=[f("Roald Amundsen era norueguês.","Roáld Ámundsen era norueguês."),f("Entre 1903 e 1906, ele cruzou o Ártico do Canadá e conviveu com os inuítes.","Entre mil novecentos e três e mil novecentos e seis, ele cruzou o Ártico do Canadá e conviveu com os inuítes."),f("Aprendeu a guiar cães, construir iglu e, principalmente, a se vestir como eles.")],
   elementos=[tira('ROALD AMUNDSEN',[520,450],None,size=52),tira('ÁRTICO · 1903–1906',[520,600],[1,'1903'],size=48),tira('guiar cães',[300,800],[2,'cães'],size=46),tira('construir iglu',[720,880],[2,'iglu'],size=46),bloco('roupa inuíte',[520,1080],[2,'vestir'],size=74,cor='tinta')]),
  dict(id='c3',fonte='Fonte: Fram Museum',frases=[f("Em 1910, o navio Fram saiu da Noruega. O plano anunciado era o Ártico.","Em mil novecentos e dez, o navio Fram saiu da Noruega. O plano anunciado era o Ártico."),f("Mas na ilha da Madeira, Amundsen contou à tripulação: o destino agora era o Polo Sul.")],
   elementos=[tira('NAVIO FRAM · 1910',[520,450],None,size=52),bloco('ÁRTICO',[520,640],[0,'Ártico'],size=84),risco([360,640],[680,640],[1,'Madeira']),tira('ILHA DA MADEIRA',[520,860],[1,'Madeira'],size=48),bloco('POLO SUL',[520,1060],[1,'Polo Sul'],size=84,cor='tinta')]),
  dict(id='c4',fonte='Fonte: Fram Museum; The Canadian Encyclopedia',frases=[f("Ao mesmo tempo, o britânico Robert Scott também tentava chegar lá.","Ao mesmo tempo, o britânico Róbert Scót também tentava chegar lá."),f("Amundsen partiu pro polo com 4 companheiros, esquis e 52 cães puxando 4 trenós.","Amundsen partiu pro polo com quatro companheiros, esquis e cinquenta e dois cães puxando quatro trenós.")],
   camera=dict(push=0.06),elementos=[tira('x ROBERT SCOTT',[520,460],None,size=50),num('5',[300,700],[1,'4 companheiros'],size=200),tira('homens no total',[300,860],[1,'companheiros'],size=40),num('52',[720,700],[1,'52'],size=200),tira('cães',[720,860],[1,'cães'],size=44),tira('4 trenós · esquis',[520,1060],[1,'trenós'],size=46)]),
  dict(id='c5',fonte='Fonte: Fram Museum; The Antarctic Sun',frases=[f("Em 14 de dezembro de 1911, os 5 chegaram ao Polo Sul.","Em catorze de dezembro de mil novecentos e onze, os cinco chegaram ao Polo Sul."),f("Montaram uma barraca chamada Polheim, casa do polo em norueguês, e deixaram uma carta pro Scott.","Montaram uma barraca chamada Pól-reim, casa do polo em norueguês, e deixaram uma carta pro Scót.")],
   elementos=[carimbo('14 DEZ','1911',[330,560],None,r=110,ang=-8),obj('bandeira',[720,600],[0,'chegaram'],w=260),verb('Polheim','norueguês','"casa do polo": a barraca deixada no Polo Sul.',[520,900],[1,'Polheim'],w=680),nota('carta pro Scott',[600,1130],[1,'carta'],cor='laranja',size=56)]),
  dict(id='c6',fonte='Fonte: Polar Record; History.com',frases=[f("Scott só chegou em 17 de janeiro de 1912, mais de um mês depois. E achou a barraca norueguesa lá.","Scót só chegou em dezessete de janeiro de mil novecentos e doze, mais de um mês depois. E achou a barraca norueguesa lá."),f("E hoje, 14 de dezembro, a chegada de Amundsen faz 115 anos.","E hoje, catorze de dezembro, a chegada de Ámundsen faz cento e quinze anos.")],
   elementos=[tira('SCOTT · 17/01/1912',[520,460],None,size=50),bloco('+ de 1 mês\ndepois',[520,680],[0,'mês'],size=72,cor='tinta',maxw=560),num('115',[520,980],[1,'115'],size=200),tira('anos',[760,1110],[1,'anos'],size=44)]),
  dict(id='c7',frases=[f("Então: o Polo Sul foi conquistado com roupa, cachorro e esqui, coisas aprendidas no Ártico."),f("Você encararia uma viagem de meses até o meio da Antártida?"),ASS],
   elementos=[obj('bandeira',[520,620],None,w=360),bloco('você encararia?',[520,1000],[1,'encararia'],size=76)])])

# ------------------------------------------------------------ 064 FILOSOFIA
EPS['SSA-064']=dict(materia='FILOSOFIA',titulo='Sócrates nunca escreveu "só sei que nada sei"',
 fontes=["Stanford Encyclopedia of Philosophy, 'Socrates'.","Encyclopaedia Britannica, 'Socrates'.","PLATÃO. Apologia de Sócrates, 21a–d (trad. H. N. Fowler, 1914; Perseus/Perseids).","FINE, Gail. Oxford Studies in Ancient Philosophy, v. 35 (2008), sobre a frase 'só sei que nada sei'.","KRUGER, J.; DUNNING, D. Journal of Personality and Social Psychology, 77(6), 1999."],
 capa=dict(elementos=[obj('livro',[520,660],w=420,ang=-4),bloco('não foi bem assim que ele disse',[520,1120],size=64,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Sócrates nunca escreveu uma linha. E a frase mais famosa dele não é bem dele."),f("Só sei que nada sei.")],
   elementos=[obj('livro',[520,620],None,w=380,ang=-4,balanca=True),risco([300,620],[740,620],[0,'nunca']),bloco('"Só sei que nada sei"',[520,980],[1,'Só sei'],size=70,cor='tinta',maxw=800)]),
  dict(id='c2',fonte='Fonte: Britannica; Stanford Encyclopedia',frases=[f("Atenas, século 5 antes de Cristo.","Atenas, século cinco antes de Cristo."),f("Sócrates passava o dia fazendo pergunta atrás de pergunta pras pessoas. Mas não deixou nada escrito."),f("O que a gente sabe dele vem de outros: Platão, Xenofonte e uma comédia de Aristófanes.","O que a gente sabe dele vem de outros: Platão, Csenofonte e uma comédia de Aristófanes.")],
   elementos=[tira('ATENAS · SÉC. V a.C.',[520,450],None,size=50),bloco('nada escrito',[520,650],[1,'nada'],size=80,cor='tinta',ang=-3),tira('PLATÃO',[300,900],[2,'Platão'],size=48),tira('XENOFONTE',[700,960],[2,'Xenofonte'],size=48),tira('ARISTÓFANES',[480,1100],[2,'Aristófanes'],size=48)]),
  dict(id='c3',fonte='Fonte: Platão, Apologia 21a',frases=[f("Segundo Platão, um amigo dele, Querefonte, foi ao oráculo de Delfos e perguntou: tem alguém mais sábio que Sócrates?","Segundo Platão, um amigo dele, Kerefônte, foi ao oráculo de Délfos e perguntou: tem alguém mais sábio que Sócrates?"),f("A resposta foi: ninguém.")],
   elementos=[tira('ORÁCULO DE DELFOS',[520,450],None,size=50),bloco('alguém mais sábio?',[520,680],[0,'sábio'],size=70,maxw=780),bloco('NINGUÉM',[520,960],[1,'ninguém'],size=110,cor='tinta',ang=-3)]),
  dict(id='c4',fonte='Fonte: Platão, Apologia 21b–d',frases=[f("Sócrates estranhou e foi conversar com gente famosa por ser sábia."),f("E concluiu: essa pessoa acha que sabe o que não sabe."),f("Eu, pelo menos, não acho que sei o que não sei.")],
   camera=dict(push=0.06),elementos=[tira('os "sábios" de Atenas',[520,460],None,size=46),nota('acha que sabe',[330,700],[1,'acha que sabe'],cor='laranja',size=60),nota('...mas não sabe',[700,820],[1,'não sabe'],size=58),
     bloco('eu não acho\nque sei',[520,1060],[2,'não acho'],size=68,cor='tinta',maxw=600)]),
  dict(id='c5',fonte='Fonte: Platão, Apologia 21d; Gail Fine (2008)',frases=[f("É isso que está no texto de Platão: não sei, e também não acho que sei."),f("A versão curta, só sei que nada sei, não aparece assim em nenhuma obra dele."),f("Foi um resumo que pegou.")],
   elementos=[tira('APOLOGIA · 21d',[520,450],None,size=50),bloco('"não sei, e não\nacho que sei"',[520,680],[0,'não sei'],size=62,maxw=700),tira('só sei que nada sei',[520,920],[1,'versão curta'],size=46),risco([300,925],[740,915],[1,'não aparece']),nota('um resumo que pegou',[560,1120],[2,'resumo'],cor='laranja',size=54)]),
  dict(id='c6',fonte='Fonte: Kruger & Dunning (1999)',frases=[f("E hoje? Em 1999, dois psicólogos da Universidade Cornell testaram algo parecido.","E hoje? Em mil novecentos e noventa e nove, dois psicólogos da Universidade Córnel testaram algo parecido."),f("Quem foi pior em testes de lógica e gramática achou que tinha ido acima da média."),f("Ficou conhecido como efeito Dunning-Kruger.","Ficou conhecido como efeito Dâning-Crúguer.")],
   elementos=[tira('CORNELL · 1999',[520,450],None,size=50),tira('os piores nos testes...',[520,620],[1,'pior'],size=46),bloco('...se acharam\nacima da média',[520,840],[1,'acima'],size=64,cor='tinta',maxw=640),tira('EFEITO DUNNING-KRUGER',[520,1090],[2,'Dunning'],size=44)]),
  dict(id='c7',frases=[f("Então: Sócrates nunca disse só sei que nada sei. Ele disse que não fingia saber."),f("Agora você sabe: admitir que não sabe já é meio caminho."),ASS],
   elementos=[obj('livro',[520,620],None,w=340,ang=3),bloco('não fingia saber',[520,980],[0,'fingia'],size=74),nota('meio caminho',[680,1140],[1,'meio'],cor='laranja',size=56)])])

# ------------------------------------------------------------ 065 LÍNGUA PORTUGUESA (15/12 · Dia de Zamenhof)
EPS['SSA-065']=dict(materia='LÍNGUA PORTUGUESA',titulo='Uma língua inventada por um oftalmologista tem falantes nativos',
 fontes=["Encyclopaedia Britannica, 'L. L. Zamenhof'.","Europeana, 'How Esperanto started and developed'.","Ethnologue, 'Esperanto' (L1: ~1.000, Corsetti et al. 2004).","UNESCO, Resolução IV.1.4.422 (Montevidéu, 1954).","PARDUE, David. 'Spiritism and Esperanto in Brazil', Esperantologio / Esperanto Studies, n. 2 (2001)."],
 capa=dict(elementos=[obj('livro',[520,660],w=400,ang=-4),bloco('tem gente que aprendeu desde bebê',[520,1120],size=62,maxw=800)]),
 cenas=[
  dict(id='c1',frases=[f("Uma língua inventada por um oftalmologista tem gente que fala desde bebê."),f("É o esperanto.")],
   elementos=[obj('livro',[520,620],None,w=380,ang=-4,balanca=True),bloco('ESPERANTO',[520,960],[1,'esperanto'],size=100,cor='tinta',ang=-3),nota('desde bebê!',[700,1130],[0,'bebê'],cor='laranja',size=60)]),
  dict(id='c2',fonte='Fonte: Encyclopaedia Britannica',frases=[f("Ludwik Zamenhof nasceu em 15 de dezembro de 1859, em Bialystok, hoje na Polônia.","Lúdvik Zamenróf nasceu em quinze de dezembro de mil oitocentos e cinquenta e nove, em Biauístok, hoje na Polônia."),f("Era médico de olhos. E sonhava com uma segunda língua que fosse de todos os povos.")],
   elementos=[tira('L. L. ZAMENHOF',[520,450],None,size=52),carimbo('15 DEZ','1859',[330,700],[0,'15 de'],r=110,ang=-8),tira('BIALYSTOK',[700,700],[0,'Bialystok'],size=48),tira('médico de olhos',[520,920],[1,'médico'],size=48),nota('uma língua de todos',[560,1110],[1,'todos'],cor='laranja',size=54)]),
  dict(id='c3',fonte='Fonte: Europeana; Britannica',frases=[f("Em 1887, ele publicou um livrinho em Varsóvia, assinado com um apelido: Doktoro Esperanto.","Em mil oitocentos e oitenta e sete, ele publicou um livrinho em Varsóvia, assinado com um apelido: Doktôro Esperânto."),f("Na língua nova, isso quer dizer: doutor esperançoso. Aquele que tem esperança."),f("O apelido pegou e virou o nome da língua.")],
   elementos=[jornal('LINGVO INTERNACIA','VARSÓVIA · 1887','D-RO ESPERANTO',[300,780],None,w=340,ang=-3),verb('esperanto','esperanto, subst.','aquele que tem esperança.',[700,560],[1,'esperança'],w=420),bloco('virou o nome',[680,1020],[2,'nome'],size=60,cor='tinta',maxw=420)]),
  dict(id='c4',fonte='Fonte: Europeana',frases=[f("A gramática básica cabia em 16 regras.","A gramática básica cabia em dezesseis regras."),f("Sem verbo irregular. Substantivo termina em o, adjetivo termina em a."),f("Bom dia, por exemplo, é bonan tagon.","Bom dia, por exemplo, é bonân tágon.")],
   camera=dict(push=0.06),elementos=[num('16',[520,580],[0,'16'],size=240),tira('regras',[520,760],[0,'regras'],size=48),tira('sem verbo irregular',[520,880],[1,'irregular'],size=44),bloco('bonan tagon',[520,1070],[2,'bonan'],size=74)]),
  dict(id='c5',fonte='Fonte: Ethnologue',frases=[f("E aí vem o curioso: tem casais que se conheceram pelo esperanto e criaram os filhos falando a língua."),f("Segundo o Ethnologue, são uns mil falantes nativos.","Segundo o Etnólog, são uns mil falantes nativos.")],
   elementos=[nota('casais do esperanto',[520,500],None,cor='laranja',size=62),obj('coracao',[330,760],[0,'casais'],w=220),tira('filhos falando a língua',[680,780],[0,'filhos'],size=40),dict(t='contador',de=0,ate=1000,fmt='~{n} nativos',pos=[520,1040],e=[1,'mil'],size=90)]),
  dict(id='c6',fonte='Fonte: UNESCO (1954); Pardue (2001)',frases=[f("Em 1954, a UNESCO reconheceu o papel do esperanto na troca cultural entre países.","Em mil novecentos e cinquenta e quatro, a UNESCO reconheceu o papel do esperanto na troca cultural entre países."),f("O Brasil tem um dos maiores movimentos esperantistas do mundo."),f("E hoje, 15 de dezembro, aniversário de Zamenhof, é o dia mais comemorado pelos esperantistas.","E hoje, quinze de dezembro, aniversário de Zamenróf, é o dia mais comemorado pelos esperantistas.")],
   elementos=[tira('UNESCO · 1954',[520,450],None,size=52),obj('globo',[330,720],[1,'Brasil'],w=260),tira('BRASIL: um dos maiores',[700,700],[1,'maiores'],size=40),cal('DEZEMBRO',2,[560,1000],[2,'15 de'],ndias=31,riscar=[15],riscar_em=[2,'15 de'],escala=0.42,ang=-2)]),
  dict(id='c7',fonte='Fonte: Ethnologue; Britannica',frases=[f("Então: uma língua criada num livrinho de 1887 virou língua materna de gente de verdade.","Então: uma língua criada num livrinho de mil oitocentos e oitenta e sete virou língua materna de gente de verdade."),f("Se você inventasse uma língua, qual seria a primeira palavra?"),ASS],
   elementos=[obj('livro',[520,620],None,w=340,ang=3),bloco('qual seria a\nprimeira palavra?',[520,1010],[1,'primeira'],size=62,maxw=740)])])

# ------------------------------------------------------------ grava os roteiro.json
CHAMADAS={
 'SSA-052':'FEITO PRA CANSAR MENOS','SSA-053':'ELE NUNCA DISSE ISSO',
 'SSA-054':'VACINA VEM DE VACA?','SSA-055':'CADÊ O NOBEL DE MATEMÁTICA?',
 'SSA-056':'QUEM INVENTOU ISSO?','SSA-057':'O QUE SIGNIFICA ESSE E?',
 'SSA-058':'QUAL É A MAIS ALTA?','SSA-059':'SÓ 3 PONTINHOS',
 'SSA-060':'ELE ACHOU UM FRACASSO','SSA-061':'VOCÊ COME ISSO TODO DIA',
 'SSA-062':'ISSO NÃO É COMETA','SSA-063':'O TRUQUE DO POLO SUL',
 'SSA-064':'VOCÊ APRENDEU ISSO ERRADO?','SSA-065':'UMA LÍNGUA INVENTADA'}
DATAS={'SSA-052':('2026-12-08','19:00'),
 'SSA-053':('2026-12-09','12:00'),'SSA-054':('2026-12-09','19:00'),
 'SSA-055':('2026-12-10','12:00'),'SSA-056':('2026-12-10','19:00'),
 'SSA-057':('2026-12-11','12:00'),'SSA-058':('2026-12-11','19:00'),
 'SSA-059':('2026-12-12','12:00'),'SSA-060':('2026-12-12','19:00'),
 'SSA-061':('2026-12-13','12:00'),'SSA-062':('2026-12-13','19:00'),
 'SSA-063':('2026-12-14','12:00'),'SSA-064':('2026-12-14','19:00'),
 'SSA-065':('2026-12-15','12:00')}
EVENTOS={'SSA-052':'Mundial de Clubes de vôlei feminino da FIVB em São Paulo (08–13/12)',
 'SSA-055':'Cerimônia do Nobel (10/12) e 130 anos da morte de Alfred Nobel',
 'SSA-056':'The Game Awards (10/12)',
 'SSA-057':'80 anos da UNICEF (11/12/1946)',
 'SSA-058':'Dia Internacional das Montanhas (11/12, ONU/FAO)',
 'SSA-059':'125 anos do sinal transatlântico de Marconi (12/12/1901)',
 'SSA-062':'Pico das Gemínidas (13–14/12)',
 'SSA-063':'115 anos de Amundsen no Polo Sul (14/12/1911)',
 'SSA-065':'Dia de Zamenhof / do Esperanto (15/12)'}

def valida(k,ep):
    """confere palavras-chave de entrada (e) contra a legenda e o tamanho do gancho."""
    erros=[]
    for c in ep['cenas']:
        frs=c['frases']
        def ok(e):
            if e is None: return
            fi,x=e
            if fi>=len(frs): erros.append(f'{k} {c["id"]}: frase {fi} não existe'); return
            if isinstance(x,str) and x.lower() not in frs[fi][0].lower(): erros.append(f'{k} {c["id"]}: "{x}" não está na frase {fi}')
        for el in c['elementos']:
            ok(el.get('e'))
            if el.get('t')=='jornal' and 'marca' in el: ok(el['marca'])
            if el.get('t')=='cal' and 'riscar_em' in el: ok(el['riscar_em'])
        cam=c.get('camera',{})
        for z in cam.get('zooms',[]): ok(z['e'])
        if 'congela' in cam: ok(cam['congela']['de']); ok(cam['congela']['ate'])
    g=ep['cenas'][0]['frases'][0][0]
    if len(g.split())>16: erros.append(f'{k}: gancho com {len(g.split())} palavras')
    return erros

if __name__=='__main__':
    so=sys.argv[1:]  # opcional: IDs específicos
    errs=[e for k,ep in EPS.items() for e in valida(k,ep)]
    if errs: print('\n'.join(errs)); sys.exit(1)
    for k,ep in EPS.items():
        if so and k not in so: continue
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
