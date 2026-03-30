# Geometria Descritiva e Geometria Projetiva
## Desambiguação e História

> Documento de referência para cursos de arquitetura e engenharia.  
> Todas as afirmações são acompanhadas de fontes primárias verificáveis.

---

## 1. A Confusão

Nos currículos de arquitetura e engenharia, os termos **geometria descritiva** e **geometria projetiva** são frequentemente tratados como sinônimos ou como nomes alternativos para a mesma disciplina. A confusão tem raiz histórica documentada: conforme registrado no [MathWorld — Projective Geometry](https://mathworld.wolfram.com/ProjectiveGeometry.html), em literatura mais antiga a geometria projetiva chegou a ser chamada de *"higher geometry"*, *"geometry of position"* ou simplesmente *"descriptive geometry"* (Cremona, 1960, pp. v-vi).

Mas são disciplinas distintas, com origens, objetos de estudo e métodos diferentes. Entender essa distinção é fundamental para qualquer estudante que trabalhe com representação espacial, modelagem 3D ou geometria computacional.

---

## 2. Geometria Descritiva

### Definição

A [geometria descritiva](https://mathworld.wolfram.com/DescriptiveGeometry.html) é um **método de representação gráfica**: um conjunto de técnicas para representar objetos tridimensionais em superfícies bidimensionais através de [projeções ortogonais](https://mathworld.wolfram.com/OrthographicProjection.html) sobre planos perpendiculares entre si. Seu objeto não é a teoria matemática da projeção — é a **técnica construtiva**.

### Origem: Gaspard Monge (1746–1818)

A geometria descritiva foi sistematizada por [Gaspard Monge](https://en.wikipedia.org/wiki/Gaspard_Monge), matemático francês considerado seu fundador. Monge desenvolveu o método ainda jovem, como professor na academia militar de Mézières, ao resolver graficamente um problema de posicionamento de fortalezas que, pelos métodos aritméticos da época, exigia cálculos extensos. O método foi tão eficaz que [o comandante inicialmente recusou recebê-lo, por ser rápido demais — e depois de verificado, foi classificado como segredo militar](https://www.maths.tcd.ie/pub/HistMath/People/Napoleonic/RouseBall/RB_ModGeom.html).

A formalização pública veio com a obra *Géométrie Descriptive* (1798), que segundo a [Britannica](https://www.britannica.com/biography/Gaspard-Monge-comte-de-Peluse) provou ser útil não apenas a matemáticos, mas também a artistas, arquitetos, engenheiros militares, carpinteiros e entalhadores de pedra.

### O que ela estuda

- Representação de sólidos 3D em dois planos ortogonais (planta e elevação)
- Determinação de formas e propriedades a partir de suas projeções
- Técnicas de estereotomia (corte de pedras para construção)
- Interseções, desenvolvimentos e planificações de superfícies

### Vínculo com a prática construtiva

Um aspecto fundamental, apontado em [estudo acadêmico sobre Monge](https://www.histoireconstruction.fr/wp-content/uploads/2015/09/Sakarovitch_2009_Gaspard-Monge.pdf), é que **ao contrário da geometria projetiva, a descritiva permanece ligada à técnica construtiva da qual nasceu**. Monge desenvolvia teoria de corte de pedras com base em sua teoria geométrica — a geometria era instrumento de construção, não fim em si mesma.

---

## 3. Geometria Projetiva

### Definição

A [geometria projetiva](https://mathworld.wolfram.com/ProjectiveGeometry.html) é um **ramo matemático autônomo** que estuda as propriedades de figuras geométricas que permanecem invariantes sob [transformações projetivas](https://mathworld.wolfram.com/ProjectiveTransformation.html) — transformações que incluem perspectiva central, projeção cônica e mudanças de ponto de vista. Nela, conceitos euclidianos como distância e ângulo perdem relevância; o que importa é a **estrutura de incidência**: quais pontos pertencem a quais retas, quais retas se encontram em quais pontos.

Uma de suas contribuições mais radicais é a introdução dos [pontos no infinito](https://mathworld.wolfram.com/PointatInfinity.html): na geometria projetiva, retas paralelas *se encontram* — em um ponto ideal no infinito. Isso unifica casos que na geometria euclidiana precisam ser tratados separadamente.

### Origem: Girard Desargues (1591–1661) — um arquiteto

Aqui está o fato que poucos currículos mencionam: **o fundador da geometria projetiva era arquiteto e engenheiro**.

[Girard Desargues](https://en.wikipedia.org/wiki/Girard_Desargues) era um matemático e engenheiro francês, nascido em Lyon em 1591. Conforme documentado pelo [MacTutor History of Mathematics](https://mathshistory.st-andrews.ac.uk/Biographies/Desargues/) (Universidade de St Andrews), Desargues é reconhecido como um dos fundadores da geometria projetiva. Segundo a [Britannica](https://www.britannica.com/biography/Girard-Desargues), presume-se que trabalhou como engenheiro até dedicar-se à arquitetura por volta de 1645, projetando mansões e edificações em Paris e Lyon.

Seu interesse pela geometria nasceu diretamente de problemas práticos de perspectiva em arquitetura e arte. Conforme o [MacTutor](https://mathshistory.st-andrews.ac.uk/Biographies/Desargues/):

> *"É muito provável que tenha sido de seu trabalho com perspectiva e assuntos relacionados que as novas ideias de Desargues surgiram."*

A obra fundante é o *Brouillon project d'une atteinte aux événements des rencontres d'un cône avec un plan* (1639) — em português: *Rascunho de um ensaio sobre os resultados de tomar seções planas de um cone*. Conforme a [Encyclopedia.com](https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/girard-desargues-and-projective-geometry), nessa obra Desargues estabeleceu os princípios da geometria projetiva como alternativa à geometria euclidiana tradicional.

### O eclipse de 200 anos

O destino inicial da obra de Desargues é um dos episódios mais curiosos da história da matemática. Apenas 50 cópias do *Brouillon project* foram impressas. A obra era notoriamente difícil: Desargues introduziu mais de 70 novos termos, a maioria baseada em referências botânicas obscuras — dos quais apenas *involução* sobreviveu ao uso corrente. Conforme a [Encyclopedia.com](https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/girard-desargues-and-projective-geometry), Blaise Pascal foi um dos poucos capazes de compreendê-la.

Além da dificuldade, a ascensão da geometria analítica de Descartes desviou a atenção dos matemáticos para métodos algébricos. A geometria projetiva de Desargues caiu em esquecimento por quase dois séculos.

### Redescobrimento: Jean-Victor Poncelet (1788–1867)

A geometria projetiva foi formalmente reconstituída como disciplina matemática autônoma por [Jean-Victor Poncelet](https://en.wikipedia.org/wiki/Jean-Victor_Poncelet), engenheiro militar e ex-aluno de Monge na École Polytechnique. O contexto é notável: Poncelet estava preso na Rússia durante a retirada napoleônica de 1812, sem livros. Reconstruindo a geometria de memória, desenvolveu as bases do que publicaria em 1822 como *Traité des propriétés projectives des figures*.

Conforme registrado pela [Encyclopedia.com](https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/projective-geometry-leads-unification-all-geometries), esta obra preparou o terreno para a reformulação e unificação de toda a geometria, que culminaria no trabalho de [Felix Klein](https://en.wikipedia.org/wiki/Felix_Klein) em 1872. A própria [Britannica](https://www.britannica.com/biography/Girard-Desargues) documenta que Poncelet, ao desenvolver a geometria projetiva, reconheceu ter sido precedido por Desargues em certos aspectos — embora não tenha sido diretamente inspirado por ele.

O [MacTutor](https://mathshistory.st-andrews.ac.uk/Biographies/Desargues/) aponta ainda o elo entre as duas disciplinas: **quando a geometria projetiva foi reinventada pelos alunos de Monge, o ponto de partida foi a geometria descritiva** — técnica que tem muito em comum com perspectiva.

---

## 4. Quadro Comparativo

| | Geometria Descritiva | Geometria Projetiva |
|---|---|---|
| **Natureza** | Método de representação | Ramo matemático teórico |
| **Fundador** | Gaspard Monge (1798) | Girard Desargues (1639) / Poncelet (1822) |
| **Formação do fundador** | Matemático / engenheiro militar | Arquiteto e engenheiro / engenheiro militar |
| **Objeto** | Representar 3D em 2D por projeção ortogonal | Estudar invariantes sob transformações projetivas |
| **Distância e ângulo** | Preservados (projeção ortogonal) | Irrelevantes |
| **Paralelas** | Permanecem paralelas | Encontram-se no infinito |
| **Vínculo com prática** | Forte — nasce da estereotomia | Rompe com a prática gráfica |
| **Usado em** | Desenho técnico, plantas, cortes | Geometria computacional, visão computacional, perspectiva teórica |

---

## 5. Por que a Confusão Persiste

Há razões estruturais para a confusão, além da equivalência terminológica histórica:

1. **Ambas usam projeção como conceito central** — mas a descritiva usa projeção *ortogonal* como ferramenta de representação, enquanto a projetiva usa projeção *central* como objeto de estudo matemático.

2. **A descritiva tem fundamento projetivo** — as propriedades que a geometria descritiva explora são casos particulares de propriedades projetivas mais gerais. Isso levou gerações de professores a tratar as duas como a mesma coisa.

3. **A nomenclatura em inglês** — conforme o [MathWorld](https://mathworld.wolfram.com/ProjectiveGeometry.html), em literatura mais antiga *projective geometry* era chamada de *descriptive geometry*. Esse uso histórico contaminou traduções e currículos.

4. **O redescobrimento de Poncelet partiu da descritiva** — os alunos de Monge que reconstruíram a geometria projetiva vieram do ambiente intelectual da geometria descritiva, tornando as fronteiras ainda mais porosas nos textos do século XIX.

---

## 6. Referências

- [Girard Desargues](https://en.wikipedia.org/wiki/Girard_Desargues) — Wikipedia
- [Girard Desargues](https://www.britannica.com/biography/Girard-Desargues) — Britannica
- [Girard Desargues — Biography](https://mathshistory.st-andrews.ac.uk/Biographies/Desargues/) — MacTutor, Universidade de St Andrews
- [Girard Desargues and Projective Geometry](https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/girard-desargues-and-projective-geometry) — Encyclopedia.com
- [Gaspard Monge](https://www.britannica.com/biography/Gaspard-Monge-comte-de-Peluse) — Britannica
- [Gaspard Monge](https://www.ebsco.com/research-starters/history/gaspard-monge) — EBSCO Research Starters
- [Gaspard Monge — Founder of Constructive Geometry](https://www.histoireconstruction.fr/wp-content/uploads/2015/09/Sakarovitch_2009_Gaspard-Monge.pdf) — Sakarovitch, 2009
- [Projective Geometry](https://mathworld.wolfram.com/ProjectiveGeometry.html) — MathWorld (Wolfram)
- [Projective Geometry Leads to the Unification of All Geometries](https://www.encyclopedia.com/science/encyclopedias-almanacs-transcripts-and-maps/projective-geometry-leads-unification-all-geometries) — Encyclopedia.com
- [The Creation of Modern Geometry](https://www.maths.tcd.ie/pub/HistMath/People/Napoleonic/RouseBall/RB_ModGeom.html) — Trinity College Dublin
- [Jean-Victor Poncelet](https://en.wikipedia.org/wiki/Jean-Victor_Poncelet) — Wikipedia
- [Felix Klein](https://en.wikipedia.org/wiki/Felix_Klein) — Wikipedia
