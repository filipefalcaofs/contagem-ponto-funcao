# Parte 3 — Arquivos Lógicos

Extraído do CPM IFPUG 4.3.1 PT-BR.

---
## Página 157

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Passo 1: Identificar Arquivos Lógicos 
Background 
 Na APF, um arquivo lógico é um grupo de dados conforme visto pelo 
usuário. Um arquivo lógico é composto de uma ou mais entidades de dados. 
Este capítulo fornece orientações sobre como agrupar as entidades candidatas 
identificadas em um ou mais arquivos lógicos. 
 O processo consiste dos seguintes passos, todos os quais são explicados em 
detalhe nos seguintes parágrafos desta seção: 
Passo 1  
Subpasso 
1. Identifique todos os dados ou informações de controle reconhecidos pelo usuário 
logicamente relacionados no escopo da contagem 
2. Exclua as entidades não mantidas por qualquer aplicação. 
3. Agrupe em arquivos lógicos as entidades relacionadas que forem entidades dependentes  
4. Exclua aquelas entidades referenciadas como dados de código 
5. Exclua as entidades que não contenham atributos exigidos pelo usuário 
6. Remova as entidades associativas que contenham atributos adicionais não exigidos pelo 
usuário e entidades associativas que contenham apenas chaves estrangeiras; agrupe os 
atributos chave estrangeira com as entidades principais. 
 O passo mais difícil é o agrupamento de dados (subpasso 3). O agrupamento 
final de dados em arquivos lógicos é o resultado do efeito combinado de dois 
métodos de agrupamento: 
 Método a) é orientado pelo processo, baseado nas transações de usuário 
na aplicação 
 Método b) é orientado pelos dados, baseado nas regras de negócio 
Contudo, como as transações do usuário também são (ou deveriam ser) 
baseadas em regras de negócio, cada método apoia o outro. Essa abordagem 
dupla pode revelar eventuais deficiências na especificação funcional e torna o 
processo de identificação de arquivos lógicos confiável e passível de 
repetição. 
 
Subpasso 
1.1 
Identificar dados ou informações de controle logicamente 
relacionados reconhecidos pelo usuário dentro do escopo da 
contagem 
 Antes de tomar a decisão sobre quais entidades devem ser agrupadas em 
arquivos lógicos como um conjunto, deve-se determinar quais entidades 
candidatas devem ser consideradas para o agrupamento lógico das entidades 
(subpasso 1.3) e quais devem ser excluídas. Os passos a seguir ajudarão a 
identificar essas entidades de uma maneira passível de repetição. 
 
2-10 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 158

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
 Os princípios de orientação geral da Parte I – Medir Funções de Dados são 
claros: considere apenas entidades significativas e requeridas pelo usuário. 
Preste atenção especial quando da identificação de arquivos lógicos a partir de 
um modelo (normalizado) de dados: 
 Não assuma que todas as entidades são arquivos lógicos; por exemplo, 
arquivos de índice, entidades em um modelo de dados físico.  
 Arquivos lógicos podem existir em uma perspectiva do usuário, mas em 
alguns casos podem não ser identificados no modelo (normalizado) de 
dados; por exemplo, arquivos históricos contendo dados agregados. Não 
esqueça de incluir esses arquivos lógicos no restante do processo.
 
 
Subpasso 
1.2 
Exclua entidades não mantidas por qualquer aplicação 
 Determine quais entidades não são mantidas por um processo elementar nesta 
ou em outra aplicação. Exclua essas entidades de considerações 
usubsequentes, pois as mesmas não são contadas. 
 
Subpasso 
1.3 
Agrupe em arquivos lógicos as entidades relacionadas que são 
entidades dependentes  
 Para cada entidade de dados restante, identifique como as entidades 
relacionadas devem ser agrupadas em arquivos lógicos, os quais refletem a 
“visão do usuário”; isto é, determine se as entidades de dados constituem por 
si mesmas um arquivo lógico independente ou se as entidades relacionadas 
devem ser agrupadas em um único arquivo lógico. 
Identifique a visão do usuário (= visão de negócio) do agrupamento de dados 
investigando:  
a) Como os dados são acessados como um grupo por processos elementares 
dentro da fronteira da aplicação (Subpasso 1.3a, página 2-14) 
b) Os relacionam
entos entre as entidades e a sua interdependência baseada 
nas regras de negócio (Subpasso1.3b, da página 2-15 até a 2-24).  
 
Subpasso 
1.4 
Excluir entidades referenciadas como dados de código 
 Filtrar dados de código. Dados de código são incluídos como resposta a um 
requisito não-funcional do usuário (requisitos de qualidade, implementação 
física e/ou razão técnica). Dados de código são explicados em detalhe na 
Parte 3 – Capítulo 1 “Dados de Código”. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-11 
---
## Página 159

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Subpasso 
1.5 
Excluir entidades que não contenham atributos requeridos pelo 
usuário 
 Determinar quais entidades não contém atributos reconhecidos e requeridos 
pelo usuário, contendo apenas atributos não funcionais. Exemplos de 
atributos não funcionais são aqueles que existem como um resultado de um 
projeto ou consideração de implementação; por exexplo, índice de arquivos 
criados por razões de performance, tais como índices alternados (ver Parte 1 – 
Medir Funções de Dados). Excluir tais entidades de considerações 
posteriores; as mesmas não são contadas como um arquivo lógico ou RLR. 
 
Subpasso 
1.6 
Remover entidades associativas que contenham atributos 
adicionais não requeridos pelo usuário e entidades associativas 
que contenham apenas chaves estrangeiras; agrupar atributos de 
chaves estrangeiras com as entidades primárias 
1.6.1 Determinar quais entidades são entidades associativas. Uma entidade 
associativa contém chaves estrangeiras de entidades conectadas juntamente 
com outros atributos. Note que duas situações podem surgir como resultado: 
a) Os atributos adicionais não-chave são um resultado do projeto ou 
consideração de implementação, ou existem para satisfazer um requisito 
técnico (não requeridos pelo usuário; ex.: um campo de data/hora com o 
propósito de recuperação de dados). Estes atributos técnicos não são 
contados como elementos de dados. Trate estas entidades como entidades 
key-to-key (veja abaixo). 
b) Os atributos adicionais não-chave são necessários para satisfazer os 
requisitos funcionais do usuário e são requeridos pelo usuário. Estas 
entidades são avaliadas nas próximas sessões: Identificar Arquivos 
Lógicos (Passos 1.3a/1.3b). 
 Exemplo: 
 
 
 
 
Timestamp é normalmente um atributo técnico não reconhecido pelo usuário. Neste 
caso, para a entidade Itens do Pedido, aplica-se  a situação 1.3a. A entidade key-to-key 
é resolvida pela inclusão do Código do Produto como uma chave estrangeira no Pedido 
e do Código do Pedidono Produto (passo 1.6). 
 
2-12 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 160

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
1.6.2 Determinar quais entidades são entidades key-to-key (intersecção); por ex., 
eles possuem apenas chaves como elementos de dados e não têm nenhum 
outro atributo não-chave.  
Estas entidades normalmente representam a implementação de uma relação 
muitos para muitos (N:M) em um modelo de dados normalizado. Existem 
apenas por razões de modelagem de dados e projeto de banco de dados e não 
como resultado de um requisito do usuário.  
Exclua estas entidades de outras considerações; elas não são contadas como 
arquivo lógico ou RLR. De acordo com as regras (Parte 1), o atributo que faz 
referência (chave estrangeira) é contado como um elemento de dado em 
ambas entidades conectadas pela entidade key-to-key. Veja também as 
diretrizes na Sessão “Passo 3: Identificar Tipos de Elementos de Dados”.  
 
 
Verificação 
Final 
Verificar se todas as entidades restantes são resultado de requisitos funcionais 
do usuário. Estas entidades e as relações e interdependências entre as mesmas 
serão abordados na próxima sessão: Identificar Arquivos Lógicos (subpasso 
1.3a/1.3b). 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-13 
---
## Página 161

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Identificar Arquivos Lógicos Utilizando o Método de Processos 
Elementares (Subpasso 1.3a) 
 A visão de negócio do usuário sobre os dados é refletida em como as 
transações do usuário acessam os dados. 
 
 Reveja como os processos elementares dentro da fronteira da aplicação 
mantêm as entidades. Se várias entidades são sempre criadas juntas e 
excluídas juntas então esta é uma forte indicação de que as mesmas devem ser 
agrupadas dentro de um único arquivo lógico. Reveja também os processos 
elementares usados para extrair os dados, para determinar se o processo de 
extração acessa o mesmo grupo de entidades. Nota: as transações que 
modificam dados frequentemente têm como alvo apenas uma entidade no 
grupo; dessa forma, as transações de modificação não fornecem uma 
orientação tão eficaz para agrupamento de dados quanto as transações de 
inclusão e exclusão. 
 
Exemplo Um pedido de compra do cliente é um grupo único de dados a partir da 
perspectiva do negócio do usuário; ele é composto dos Dados Básicos do 
Pedido (cliente, endereço, data, etc.) e dos detalhes sobre cada item pedido. A 
partir da perspectiva do negócio, um pedido não pode ser criado sem pelo 
menos um item e se o pedido for excluído, tanto os dados básicos como todos 
os seus itens serão excluídos. Entretanto, os dados básicos e os itens podem 
ter transações de manutenção independentes; por ex., a alteração do status do 
pedido é uma função diferente da alteração dos itens do pedido. As funções 
de inclusão e exclusão indicam, a partir da perspectiva do usuário, que 
“pedido” é um arquivo lógico único que agrupa os dados básicos do pedido e 
os itens do pedido. 
 
 Utilize o subpasso 1.3a para validar os grupos de dados lógicos candidatos 
que foram identificados. 
 
2-14 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 162

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
 
Identificar Arquivos Lógicos Utilizando o Método de (In)Dependência de 
Entidades (Subpasso 1.3b) 
Introdução 
 O Método de (In)Dependência de Entidades, como definido e explicado nesta 
seção, fornece um método reproduzível para identificar corretamente 
Arquivos Lógicos (ALs) a partir de um modelo de dados. Nesta seção, o 
termo “entidade” refere-se a uma entidade em um modelo de dados 
normalizado (normalmente na terceira forma normal). 
A Seção “Tipos de Relacionamentos” explica os diferentes tipos de 
relacionamentos e as diferenças entre os conceitos “relacionamento 
obrigatório/opcional” e “entidades dependentes /independentes ”. 
A Seção “(In)Dependência de Entidades Ilustrada para Todos os Tipos de 
Relacionamentos” explica o método em mais detalhes para cada tipo de 
relacionamento.  
A Seção “Resumo: de Entidades para Arquivos Lógicos via (In)Dependência 
de Entidades” resume os tipos de relacionamentos e as condições para quando 
contar um AL. 
 
 O Método de Dependência de Entidades agrupa entidades pela avaliação dos 
relacionamentos e interdependências das entidades em comparação com as 
regras de negócio. Os princípios do guia são entidades independentes e 
entidades dependentes. 
 
Entidades 
Independent
es 
Entidade independente significa uma entidade que é significativa ou tem 
sentido para o negócio por si só, sem a presença de outras entidades. 
 
Entidades 
Dependentes  
Entidade dependente significa uma entidade que não é significativa ou não 
tem sentido para o negócio por si só, sem a presença de outras entidades, de 
modo que: 
 uma ocorrência da entidade X deve estar ligada a uma ocorrência da 
entidade Y 
 a eliminação de uma ocorrência da entidade Y resulta na eliminação de 
todas as ocorrências relacionadas da entidade X  
 
Nota Não confunda o conceito de entidade independente/entidade dependente com 
o conceito de relacionamento opcional/obrigatório. Os exemplos na Seção 
“(In)Dependência de Entidade Ilustrada para Todos os Tipos de 
Relacionamentos” mostram claramente que estes são conceitos diferentes. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-15 
---
## Página 163

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
 
Determinar 
Dependência 
Para determinar se a entidade B é dependente ou independente da entidade A, 
é preciso determinar:  
“B é significativa para o negócio independentemente da ocorrência de A 
ligada a ela?” 
 
 Um teste simples para determinar a situação (entidade dependente ou 
independente) é o seguinte. Mesmo que não haja requisito do usuário para a 
exclusão, (ainda assim) faça a pergunta:  
“Suponha que nós quiséssemos excluir uma ocorrência “a” da entidade A; o 
que aconteceria à ocorrência “b” da entidade B ligada a “a”?” 
 
 Dependendo das regras do negócio, distinguimos duas situações 
essencialmente diferentes: 
 
Situação 1 Se,  de acordo com as regras de negócio, uma ocorrência de B não tem 
significado/importância independente  para o usuário e pode também ser 
excluída, então aparentemente a ocorrência de B não tem significado para o 
usuário independentemente da ocorrência correspondente de A. A entidade B 
é considerada uma entidade dependente de A. As entidades A e B devem ser 
agrupadas juntas no mesmo arquivo lógico. 
 
Situação 2 Se a ocorrência de B tem significado para o negócio mesmo 
independentemente da ocorrência correspondente de A, as regras de negócio 
não permitirão a exclusão da ocorrência de B. As entidades A e B serão 
consideradas arquivos lógicos separados. 
 
 Avaliar o modelo de dados de um sistema de informação por meio da 
avaliação de todos os pares de entidades ligadas resulta na identificação dos 
arquivos lógicos. 
 
 Na Seção “Entidades (In)Dependentes Ilustrada para Todos os Tipos de 
Relacionamento” este método é explicado em mais detalhes para diferentes 
tipos de relacionamentos. 
A Seção “Resumo: de Entidades para Arquivos Lógicos via (In-) 
Dependência de Entidades ” resume como contar cada tipo de relacionamento 
na APF. 
 
2-16 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 164

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
Tipos de Relacionamentos  
 Antes de assumir como conclusivos os princípios da (In)Dependência de 
Entidades para todos os tipos de relacionamento, deve-se entender claramente 
os diferentes tipos/naturezas dos relacionamentos. Esta seção explica os 
diferentes tipos, assim como os conceitos de “opcional” e “obrigatório”.  
 
Exemplo Duas entidades, Função e Funcionário, por exemplo, podem ser conectadas 
entre si via um relacionamento; por ex.: “ocupa”. 
 
Natureza do  
Relacioname
nto 
A natureza do relacionamento determina quantos funcionários podem 
trabalhar em uma função de acordo com o modelo de dados (0, 1 ou mais) e 
em quantas funções um funcionário pode trabalhar (0, 1 ou mais). 
 
1 : N Assuma que as regras de negócio determinem que 
vários funcionários (no mínimo 1) podem ser utilizados 
em uma função, e que um funcionário tem que trabalhar 
em uma (e apenas uma) função. Neste caso dizemos 
que o relacionamento entre Função e Funcionário é 1:N 
 
 
 
1 : (N) É mais provável que as regras de negócio determinem 
que uma função pode estar vaga, isto é, nenhum 
funcionário tenha sido alocado para a função. Neste 
caso o relacionamento entre Função e Funcionário é 
opcional e definido como 1:(N). 
 
 
 
(1) : N Se as regras de negócio determinam que um 
funcionário pode existir sem uma função, mas uma 
função sempre tem um funcionário a ela alocado, 
definimos o relacionamento entre Função e Funcionário 
como (1):N 
 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-17 
---
## Página 165

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
(1) : (N) Na situação onde uma função pode estar vaga e um 
funcionário pode existir sem uma função, ambos os 
lados do relacionamento são opcionais. O 
relacionamento entre Função e Funcionário é definido 
como (1):(N). 
 
 
 
 
Conceito “Obrigatório/Opcional” versus “(In)Dependência  de Entidades”. 
 Para deixar clara a diferença entre os conceitos de “relacionamento 
obrigatório/opcional” e “dependência/independência de entidades”, assuma, 
como um exemplo, a seguinte extensão das regras de negócio “funcionário(s) 
não é(são) permitido(s) sem uma função” (relacionamento do tipo 1:N e 
1:(N)). 
 
 Quando uma função se torna obsoleta, isto não significa que os funcionários 
não são mais significativos para o negócio. Um funcionário tem significado 
para o negócio independente da função relacionada. Funcionário é uma 
entidade independente de função. Devido ao relacionamento obrigatório com 
função, todos os funcionários têm que ser alocados a uma nova função, antes 
de a função poder ser excluída. 
 
 Então pode acontecer que uma ocorrência da entidade B (ex. Funcionário) 
possa ter um link obrigatório com uma ocorrência da entidade A (por ex. 
Função) no relacionamento A:B entre as entidades A e B, mas aquela 
entidade B é por si só significativa para o negócio. Neste caso, quando 
alguém quiser excluir uma ocorrência da entidade A, tem-se que antes 
reatribuir uma ocorrência ligada de B para outra ocorrência de A. 
 
(In)Dependência de Entidade Ilustrada para Todos os Tipos de Relacionamento 
 
(In)Dependência de Entidade em um Relacionamento (1):(N)  
(1) : (N) Se um relacionamento entre duas entidades A e B é bilateralmente opcional, 
as entidades podem existir independentemente e (todas ocorrências de) A e B 
são significativas para o negócio independentemente da(s) ocorrência(s) 
relacionada(s) com a outra entidade. 
 
 Então, A e B são consideradas entidades independentes uma da outra. A APF 
conta as entidades A e B como dois arquivos lógicos separados, conforme 
indicado na tabela da Seção “Resumo: de Entidades para Arquivos Lógicos 
via (In-)Dependência de Entidades”. 
 
2-18 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 166

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
(In)Dependência de Entidade em um Relacionamento 1:(N)  
1 : (N) Em um relacionamento 1:(N) entre duas entidades A e B (veja figura 1), pode 
existir uma ocorrência da entidade A para nenhuma, uma ou muitas 
ocorrências da entidade B relacionadas. Por outro lado, cada ocorrência de B 
tem que ser associada a uma ocorrência de A. 
 
Exemplo No relacionamento 1:(N) entre Funcionário e Filho (ou Dependente) em uma 
Aplicação de RH, um Funcionário deve ter 0, 1 ou muitos Dependentes a ele 
relacionados, mas um Dependente tem que estar relacionado a um (e apenas 
um) Funcionário (veja figura 2). 
 
 Como B deve ser relacionado a um A, isto levanta a questão se B é 
dependente ou independente de A. 
 
 Para determinar se a entidade B é dependente ou independente de A, é 
necessário responder: 
“B é significativo para o negócio independentemente do A a ela  
relacionado?”  
 
 Veja um teste simples para diferenciar a dependência e independência de 
entidades. 
Mesmo que não existam requisitos do usuário para exclusão, faça a seguinte 
pergunta:   
“Suponha que desejamos excluir uma ocorrência da entidade A; o que 
acontecerá com as ocorrências relacionadas da entidade B que têm um 
relacionamento obrigatório com uma ocorrência de A?” 
 
 As regras de negócio podem resultar em duas possibilidades: 
 
Situação 1 Se a exclusão de A for permitida, todas as ocorrências de B relacionadas 
também deverão ser excluídas, pois o negócio não está mais interessado nas 
ocorrências de B. Por exemplo (veja figura 2): Uma aplicação de RH mantém 
informações sobre funcionários e seus dependentes. Assuma que as regras de 
negócio definiram que quando um Funcionário (A) deixa a companhia, não 
tem mais sentido para o negócio manter a informação sobre os dependentes 
(B). 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-19 
---
## Página 167

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Situação 2 A exclusão de A não é permitida enquanto ocorrências de B ainda estiverem a 
ela relacionadas, pois o negócio está ainda interessado nas ocorrências de B, 
mesmo além do contexto do A correspondente. Por exemplo (veja figura 3): 
Uma organização adota crianças e designa cada criança a um funcionário. O 
funcionário é a pessoa de contato entre a companhia e a criança. No caso de 
um funcionário deixar a companhia, as informações sobre a criança associada 
(do funcionário desligado) ainda são significativas para o negócio. Então, 
antes que se permita a exclusão do Funcionário (A), tem-se que 
primeiramente atribuir a Criança associada (B) a outro Funcionário (A) (pois 
a natureza deste relacionamento não permite uma Criança sem um 
relacionamento com Funcionário). 
 
 Na situação (1) dizemos que B é uma entidade dependente de A, e na situação 
(2) que B é uma entidade independente de A. 
 
 A APF conta as entidades A e B como um único arquivo lógico na situação 
(1) (dependência), enquanto na situação (2) A e B são arquivos lógicos 
separados (independência) conforme indicado na tabela da Seção “Resumo: 
de Entidades para Arquivos Lógicos via (In-)Dependência de Entidades”. 
 
 Ilustração do relacionamento 1:(N): 
 
 
  
  
Fig. 1: 
Cada entidade do tipo 
A pode referenciar 0, 1 
ou muitas entidades do 
tipo B. Uma entidade 
do tipo B tem que 
referenciar exatamente 
uma entidade do tipo A. 
Fig. 2: 
A aplicação de RH 
mantém informações 
sobre funcionários e seus 
dependentes. 
 
 
Fig. 3: 
A aplicação de RH 
mantém informações 
sobre Funcionários e 
sobre as Crianças 
Adotadas que são 
designadas para um 
Funcionário. 
 As figuras 2 e 3 possuem modelos de dados 
similares, mas diferentes regras de negócio resultam 
em diferentes arquivos lógicos identificados. 
 
 
 
 
 
2-20 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 168

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
(In)Dependência de Entidade em um Relacionamento (1):N  
(1) : N Um relacionamento (1):N entre duas entidades A e B (veja figura 4) pode ser 
tratado de forma similar. Estes tipos de relacionamentos, entretanto, 
raramente aparecem na prática. 
 
 Em um relacionamento (1):N entre duas entidades A e B, cada A deve ser 
atribuído a 1 ou muitos Bs. Por outro lado, um B pode (mas não 
necessariamente) ser atribuído a uma ocorrência de A. 
 
Exemplo Em um relacionamento (1):N entre Comitê e Membro da Organização, um 
Comitê tem que ter membros (pelo menos 1).  Um membro da organização 
pode (mas não necessariamente) servir em um Comitê (veja figuras 5 e 6). 
 
 Devido a uma ocorrência de A ter que estar relacionada a uma de B, levanta-
se a questão se A é dependente ou independente de B. 
 
 Para determinar se a entidade A é dependente ou independente de B, precisa-
se responder: 
“A é significativa para o negócio independentemente da entidade B a ela 
relacionada?”  
 
 Veja a seguir um teste simples para diferenciar a dependência e 
independência de entidades. 
Mesmo que não existam requisitos do usuário para exclusão, faça a pergunta:  
 “Assuma que temos uma ocorrência da entidade A à qual estão relacionadas 
uma ou mais ocorrências da entidade B. Suponha que desejamos excluir a 
última ocorrência relacionada à entidade B; o que aconteceria com esta 
ocorrência de A, que possui um relacionamento obrigatório com pelo menos 
uma ocorrência de B?” 
 
 As regras de negócio podem resultar em duas possibilidades: 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-21 
---
## Página 169

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Situação 1 Quando o último B é excluído, o A relacionado é também excluído pois o 
negócio não se interessa mais por ele. Por exemplo (veja a figura 5): Uma 
organização tem comitês aos quais membros são atribuídos. 
A regra de negócio é que um comitê deve ter membros, mas nem todos os 
membros precisam participar de um comitê. Uma regra de negócio adicional é 
que a organização encerra um comitê assim que não haja mais membros 
participando do mesmo; pode-se dizer que os comitês são vistos como grupos 
de trabalho “ad hoc”. 
Neste caso quando o último membro de um comitê sai do comitê, não tem 
sentido para o negócio manter informações sobre o comitê. Os dados do 
comitê são excluídos assim que o último membro deixa o comitê. 
 
Situação 2 A exclusão do último B não é possível enquanto exista algum A ainda 
referenciado por ele, pois o negócio está ainda interessado neste específico A, 
mesmo além do contexto dos Bs que o referenciam. Por exemplo (veja figura 
6), uma organização tem comitês aos quais membros são atribuídos. 
A regra de negócio é que um comitê deve ter membros, mas nem todos os 
membros precisam participar de um comitê. Comitês são vistos como parte da 
estrutura organizacional. Eles têm significado para o negócio além dos 
membros que os servem. 
Antes que o último membro de um específico comitê deixe o comitê, um 
novo membro tem que ser atribuído àquele comitê pois a natureza do 
relacionamento não permite um comitê sem membros. 
 
 Na situação (1), A é aparentemente não significativo para o negócio a menos 
que ele esteja relacionado a um ou mais Bs, enquanto na situação (2) ele é 
significativo. 
 
Na situação (1) nós dizemos que A é uma entidade dependente de B e na 
situação (2) que A é uma entidade independente de B . 
 
A APF conta as entidades A e B como um único arquivo lógico na situação 
(1) (dependência), enquanto na situação (2) A e B são arquivos lógicos 
separados (independência), como indicado na tabela da Seção “Resumo: de 
Entidades para Arquivos Lógicos via (In-)Dependência de Entidades”. 
 
2-22 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 170

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
 Ilustração do relacionamento (1):N: 
 
 
  
  
Fig. 4: 
Cada entidade do tipo A 
tem que ser referenciada 
por 1 ou mais entidades 
do tipo B; uma entidade 
do tipo B pode, mas não 
necessariamente, 
referenciar uma entidade 
do tipo A. 
Fig. 5: 
Membros de uma 
organização podem (mas 
não necessariamente) estar 
ativos em um comitê de 
trabalho. Um Comitê tem 
que ter (um ou mais) 
membros participando. 
Fig. 6: 
Membros de uma 
organização podem (mas 
não necessariamente) estar 
ativos em um comitê de 
trabalho. Um Comitê tem 
que ter (um ou mais) 
membros participando. 
 As figuras 5 e 6, tem modelo de dados similares, mas 
regras de negócio diferentes resultando em diferentes 
arquivos lógicos identificados. 
 
(In)Dependência de Entidade em um Relacionamento 1:N 
1 : N Em um relacionamento 1:N entre duas entidades A e B, 
cada entidade B tem que ser atribuída a um e apenas um 
A, e a cada A tem que ser atribuído pelo menos a um B. 
Aplicam-se as mesmas regras de dependência e 
independência das entidades. 
 
 
 
 
Situação 1 Se B não é significativo para o negócio independentemente do A a ele 
relacionado, então B é considerado uma entidade dependente de A. 
 
Situação 2 Se B é significativo para o negócio independentemente do A a ele 
relacionado, então B é considerado uma entidade independente de A. 
 
 A APF conta as entidades A e B como um arquivo lógico na situação (1) 
(dependência), enquanto que na situação (2) A e B são arquivos lógicos 
separados (independência), como indicado na tabela da Seção “Resumo: de 
Entidades para Arquivos Lógicos via (In-)Dependência de Entidades”. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-23 
---
## Página 171

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Resumo: De Entidades para Arquivos Lógicos via (In)Dependência de Entidades  
 Na tabela abaixo, A e B são duas entidades de um modelo de dados 
(normalizado) que devem ser contadas de acordo com esta Seção e que são 
interconectadas via um relacionamento. A tabela resume como as diversas 
situações são contadas. 
 
 Tipo de Relacionamento 
entre duas entidades, A e 
B 
Quando esta Condição Existe Então conte como 
Arquivo Lógico (AL) 
(1) : (N) (A e B são independentes) 2 ALs 
Se B é entidade dependente de 
A 
1 AL 
1  :  N 
Se B é entidade independente de 
A 
2 ALs 
Se B é entidade dependente de 
A 
1 AL 
1  : (N) 
Se B é entidade independente de 
A 
2 ALs 
Se A é entidade dependente de 
B 
1 AL 
(1) :  N 
Se A é entidade independente de 
B 
2 ALs 
(1) : (1) (A e B são independentes) 2 ALs 
1  :  1 (A e B são dependentes) 1 AL 
Se B é entidade dependente de 
A 
1 AL 
1  : (1) 
Se B é entidade independente de 
A 
2 ALs 
(N) : (M) (A e B são independentes) 2 ALs 
Se B é entidade dependente de 
A 
1 AL 
N  :  M 
Se B é entidade independente de 
A 
2 ALs 
Se B é entidade dependente de 
A 
1 AL 
N  : (M) 
Se B é entidade independente de 
A 
2 ALs 
 
 
Legenda AL = Arquivo lógico (ALI ou AIE) 
(..) = Lado opcional do relacionamento 
 
2-24 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 172

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
Notas 1. Na dúvida, decida por entidades independentes. 
 
2. Em algumas situações mais que duas entidades podem também formar um 
arquivo lógico. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-25 
---
## Página 173

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Passo 2: Classificar Arquivos Lógicos 
 Os arquivos lógicos identificados precisam ser validados segundo as regras de 
contagem de ALI/AIE na Parte 1. 
 
Classifique um arquivo lógico como um Arquivo Lógico Interno (ALI) se 
processos elementares dentro da fronteira da aplicação que está sendo 
contada, mantém (criam, alteram ou excluem) elementos de dados dentro do 
arquivo. 
 
Classifique um arquivo lógico como um Arquivo de Interface Externa (AIE) 
se processos elementares dentro da fronteira da aplicação sendo contada 
apenas referenciam os elementos de dados dentro do arquivo, e o arquivo 
lógico é mantido por um processo elementar em outra aplicação. 
 
Se um arquivo lógico identificado não é mantido por um processo elementar 
(dentro desta aplicação ou em outra), então o arquivo lógico não é contado de 
modo algum. 
Passo 3: Identifique Tipos de Dados Elementares 
 O dado elementar é a menor unidade que tem significado para o usuário e 
representa um fato específico sobre um negócio, por exemplo: 
 
Nome do Dado Elementar Valor do Dado Elementar 
Taxa $900 
Data do Nascimento 15 Jan 1965 
Nome InfoMerge  
 
2-26 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 174

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
Termos e Definições de Dados Elementares  
 Ao iniciar o estudo de um modelo de dados lógico, começamos considerando 
esses elementos de dados como atributos. Um atributo representa um fato 
específico sobre uma entidade ou um relacionamento. Na tabela abaixo as 
entidades são mostradas em MAIÚSCULO, os atributos em minúsculo: 
Representação Exemplo 
ENTIDADE_atributo CURSO_taxa 
ENTIDADE.atributo COMPANHIACLIENTE.nome 
 
 
 Atributos/elementos de dados podem ser encontrados em: 
 Visões do usuário (relatórios, telas) 
 Dicionários de dados (modelos do negócio, modelos de dados) 
 Arquivos existentes (estrutura de registros em programas, layouts de 
arquivos) 
 
Quando estiver revendo os dados, o analista de dados segue esta premissa 
básica: todos os elementos de dados reconhecidos pelo usuário devem ser 
tratados como um atributo, e dessa forma devem ser mostrados em relação a 
uma entidade específica.  
 
O atributo pode ter as seguintes propriedades: nome (sinônimo), 
característica, propósito  (uso), origem, valores válidos, valor 
(estrutura), unidade, e dependências. Iremos explorar estas propriedades 
antes de rever o mapeamento de DERs para atributos/elementos de 
dados da Análise de Pontos de Função do IFPUG. 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-27 
---
## Página 175

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
 
Nome do 
Atributo 
Um nome único que resume as características apresentadas. Ele contém os 
seguintes componentes:  
origem (entidade/relacionamento) seguido por um ponto  
descritivo (adjetivo do atributo) seguido por um hífen  
classe (atributo base) 
 
Muitas tecnologias não aceitam espaços. Então vários nomes são 
concatenados com hífens.  
Exemplo: 
COMPANHIA_CLIENTE.endereço-entrega 
SEMINARIO_MATRICULA. efetividade-avaliação 
 
Característica  A propriedade do ambiente sendo medido ou representado. O nome da 
entidade que tem a característica é sempre presente; por exemplo, Endereço-
Entrega: endereço em que os materiais serão entregues para a 
COMPANHIA-CLIENTE. 
 
Propósito Fazer a pergunta “Como o atributo é utilizado pelo negócio” justifica o 
atributo. 
 
Exemplo: CURSO.data-qualificação  
Propósito: Usado nas seções de recapitulação de planejamento 
 
Dependências As situações onde outros valores de atributos no modelo influenciam ou 
restringem o valor deste atributo. Por exemplo, CURSO-grau final não pode 
existir antes do término do curso, mas tem que existir ao término do mesmo. 
 
2-28 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 176

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
Atributos 
Chave 
Fornecem o relacionamento entre uma entidade e outra. Existem diferentes 
tipos de chaves no modelo de dados, ex.: chaves primárias, chaves 
secundárias e chaves estrangeiras. 
Uma Chave Primária (PK) é o identificador único de uma entidade. 
Chaves Secundárias (SK) são atributos que fornecem acesso mais rápido às 
informações, como: 
 LIVROESCOLAR.preço (SK) 
 LIVROESCOLAR.nome-editora (SK). 
Chaves Secundárias não fazem parte da informação do modelo de dados 
(modelo de dados lógico) mas são usados principalmente para auxiliar no 
acesso (implementação física). 
Chaves Estrangeiras (FK) são atributos usados para representar 
relacionamentos de uma entidade com outra. 
 
Atribuição O último conceito de modelagem de dados que devemos considerar antes da 
análise dos  DERs é Atribuição, que prescreve/descreve onde os atributos 
residem, dentro da entidade ou dentro do relacionamento. Existem algumas 
regras comuns de atribuição que são seguidas na modelagem de dados: 
1. Um atributo é atribuído à sua melhor “origem” única, que é indicada 
na propriedade de característica no FORMULÁRIO DE DEFINIÇÃO 
DE ATRIBUTO. 
2. O identificador único (chave primária) de uma entidade será atribuído 
também a cada relacionamento em que ele participa. 
Existem algumas diretrizes adicionais a serem seguidas ao tentar colocar um 
atributo na entidade mais apropriada: 
1. Se a definição do atributo referir-se a uma entidade, aloque o atributo 
àquela entidade  
2. Se a definição do atributo referir-se a diversas entidades, então crie 
um relacionamento e aloque o atributo ao relacionamento ou à 
entidade à qual ele se aplicar. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-29 
---
## Página 177

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Mapeando Elementos de Dados para Tipos de Elementos de Dados da 
APF  
 Agora que nós já revisamos os conceitos de elementos de dados e atributos na 
perspectiva da modelagem de dados, podemos relacionar estes conceitos às 
definições e regras de Pontos de Função do IFPUG: 
 
 Conceito de 
Modelagem de 
Dados  
Termo da 
Modelagem 
de Dados 
Termo de 
BD 
Relacional 
Termo da 
APF  
Conceito da APF 
Menor unidade 
de dados 
definida que tem 
significado no 
mundo real  
Item de 
Dados 
Atributo 
ou Coluna 
Tipo de 
Elemento 
de Dados 
(DER - 
Dado 
Elementar 
Referencia
do) 
Um tipo de 
elemento de 
dados (DER) é 
um campo 
reconhecido pelo 
usuário, único e 
não repetido 
Grupos de 
itens 
relacionados 
que são 
tratados como 
uma unidade 
Registro Linha ou 
Tupla 
Tipo de 
Registro 
Elementar 
(RLR - 
Registro 
Lógico 
Referencia
do) 
Um tipo de 
registro 
elementar (RLR) 
é um subgrupo 
de elementos de 
dados, 
reconhecido pelo 
usuário, dentro 
de um ALI ou 
AIE 
Coleção de 
registros de 
um mesmo 
tipo  
Arquivo Tabela Arquivo 
Lógico 
(Arquivo 
Lógico 
Interno – 
ALI ou 
Arquivo de 
Interface 
Externa – 
AIE) 
Arquivo se  
refere a um 
grupo de dados 
relacionados 
logicamente e 
não à 
implementação 
física deste 
grupo de dados 
 
 
 Tipos de Elementos de Dados (DERs) são campos ou atributos, 
reconhecidos pelo usuário, únicos e não repetidos.  
As seguintes regras se aplicam ao contar DERs em um arquivo lógico: 
 Conte um DER para cada campo único, reconhecido pelo usuário e 
não repetido, mantido em/ou recuperado de uma função de dados 
através da execução de todos os processos elementares dentro de um 
2-30 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 
---
## Página 178

Parte 3 – Práticas de Contagem  Arquivos Lógicos 
escopo de contagem 
 Conte apenas aqueles DERs que estão sendo usados pela aplicação 
que está sendo contada quando duas ou mais aplicações mantém e/ou 
referenciam a mesma função de dados  
 Conte um DER para cada atributo requerido pelo usuário para 
estabelecer um relacionamento com outra função de dados  
 Revise atributos relacionados para determinar se são agrupados e 
contados como um único DER ou se são contados como vários DERs; 
o agrupamento vai depender de como o processo elementar utiliza os 
atributos dentro da aplicação  
 
Não conte atributos que existam puramente para satisfazer um requisito 
técnico e não foram especificados pelo usuário. Exemplos destes atributos 
não funcionais são atributos resultantes de considerações de projeto ou de 
implementação. 
 Exemplo
: O campo PEDIDO_data é contado como um DER no Pedido já  
que ele precisa ser mantido para satisfazer um requisito do negócio do 
usuário. Entretanto, a marca (stamp) de data e hora de cada registro do pedido 
existe para satisfazer a integridade e a confiabilidade dos dados. A solução 
técnica para estes requisitos de qualidade foi copiar o banco de dados e 
disponibilizar para recuperação baseado nesta informação da marca (stamp). 
Consequentemente, a marca (stamp) de data e hora não deve ser contada 
como um DER. 
Outras Situações 
 A seguir exemplos de contagem de tipo de elementos de dados (DERs).  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 2-31 
---
## Página 179

Arquivos Lógicos  Parte 3 – Práticas de Contagem 
Atributos 
 Atributos que são compostos de diversos elementos de dados relacionados são 
armazenados separadamente. 
 
Devem os atributos serem contados como diversos elementos de dados ou 
como um único elemento de dados? As regras de DER na Parte 1 dizem para 
você “contar cada campo reconhecido pelo usuário”.  
 
Como você determina se ele é reconhecido pelo usuário como uma coisa ou 
várias coisas? Reveja as transações dentro da aplicação para determinar se o 
atributo é tratado como um item ou mais de um. 
 
Considere os seguintes itens na tomada de decisão: 
 
a) Se o atributo é sempre usado por inteiro, então ele é contado como um 
único elemento de dados (DER). Não devem existir situações em que um 
componente individual de um atributo é usado sem os outros. Baseado 
neste uso, o atributo é contado como um único elemento de dado. 
b) Se em algumas situações, apenas uma parte do atributo (ex. o sobrenome) 
é usada, então mais do que um elemento de dados deve ser contado. Olhe 
para o uso em componentes dentro da aplicação para determinar quantas 
partes reconhecidas existem. A opção não é necessariamente um ou todos. 
Baseado no que você está vendo, pode ser apropriado contar apenas dois 
DERs, ainda que existam na realidade cinco partes físicas. 
 
 c) Olhe para a existência de requisitos de ordenação ou de edições e critérios 
de seleção. Se uma lista ou relatório é ordenado ou selecionado por um 
simples componente do atributo, isto sugere independência de 
componentes na visão do usuário. 
Contando Nomes 
 Nom
e (primeiro nome, nome do meio, último nome) 
Muitas aplicações precisam manter informações sobre os nomes das pessoas.   
O nome deve ser contado como vários elementos de dados ou um  elemento 
de dados único?  
Reveja as transações dentro da aplicação para determinar se o nome é tratado 
como um item ou mais do que um item. Por exemplo: Nos Estudos de Caso 
1,2 e 3, veja como o Nome do Funcionário é usado em várias funções de 
transação. 
2-32 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010 