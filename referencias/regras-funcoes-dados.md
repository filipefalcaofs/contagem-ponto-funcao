# Regras de Funções de Dados — ALI/AIE (Parte 1)

Extraído do CPM IFPUG 4.3.1 PT-BR (páginas 40–47).


---
## Página 40

4  Abreviaturas  Parte 1 – FSM 
NOTA O tamanho funcional de um projeto de melhor ia pode incluir o tamanho da funcionalidade de 
conversão  
3.47 
tamanho funcional do projeto de desenvolvimento 
medida da funcionalidade oferecida aos usuários pela primeira release do software, conforme medida 
pela contagem de pontos de função do projeto de desenvolvimento  
NOTA O tamanho funcional de um projeto de desenv olvimento inclui o tamanho da funcionalidade de 
conversão. 
3.48 
tipo de entidade associativo 
tipo de entidade contendo atributos que descrevem um relacionamento muitos-para-muitos entre dois 
outros tipos de entidade 
3.49 
tipo de entidade atributivo 
tipo de entidade que descreve um ou mais atributos de outro tipo de entidade 
3.50 
tipo de função 
cinco tipos de componentes funcionais básicos identificados neste Padrão Internacional 
NOTA Os cinco tipos de função são:  Entrada Externa, Saída Externa, Consulta Externa, Arquivo Lógico 
Interno e Arquivo de Interface Externa.  
3.51 
usuário 
qualquer pessoa ou coisa que se comunique ou interaja com o software a qualquer tempo 
EXEMPLOS Exemplos de coisas incluem, mas não est ão limitados a: aplicações de software, animais, 
sensores ou outros hardwares. 
[ISO/IEC 14143-1:2007, definition 3.11] 
3.52 
visão do usuário 
Requisitos Funcionais do Usuário, conforme percebidos pelo usuário  
NOTA Os desenvolvedores traduzem a visão do usuário para software, a fim de fornecer uma solução. 
4 Abreviaturas 
AIE  Arquivo de Interface Externa 
ALI  Arquivo Lógico Interno 
ALR Arquivo Lógico Referenciado (tipo de arquivo referenciado) 
APF  Análise de Ponto de Função 
CE  Consulta Externa 
CFB Componente Funcional Básico 
DER Dado Elementar Referenciado (tipo de dado elementar) 
EE  Entrada Externa  
PF  Ponto de Função 
8 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 41

Parte 1 – FSM  5  Processo de Medição 
RL
R Registro Lógico Referenciado (tipo de registro elementar) 
SE  Saída Externa 
5 Processo de Medição 
5.1 Visão Geral  
Para conduzir uma contagem de pontos de função devem  ser executadas as s eguintes atividades, a 
fim de identificar e classificar os componentes funcionais básicos (ALI, AIE, EE, SE, CE): 
a) reunir a documentação disponí vel em conformidade com 5.2, 
b) determinar o escopo e a fronteira da contag em, identificando os Requisitos Funcionais do 
Usuário em conformidade com 5.3, 
c) medir as funções de dados de acordo com 5.4, 5.6 e 5.7, 
NOTA A funcionalidade de conversão (se aplicável) é medida conforme 5.6; a funcionalidade de melhoria 
(se aplicável) é medida conforme 5.7.  
d) medir as funções de transação conforme 5.5, 5.6 e 5.7, 
NOTA A funcionalidade de conversão (se aplicável) é medida conforme 5.6; a funcionalidade de melhoria 
(se aplicável) é medida conforme 5.7. 
e) calcular o tamanho funcional de acordo com 5.8, 
f) documentar a contagem de pontos de função conforme 5.9, e 
g) reportar o resultado da contagem de pontos de função conforme 5.10. 
NOTA A Figura 1 fornece uma visão geral, gráfica,  do processo de contagem de pontos de função. 
 
 
 
Medir funções de 
dados 
Determinar o escopo e a 
fronteira da contagem, 
identificando os requisitos 
funcionais do usuário 
Calcular tamanho 
funcional 
Documentar e 
reportar 
Medir funções de 
tran
sação 
Reunir a 
documen
tação 
disponível 
 
 
 
 
Figura 1 — Visão geral, gráfica, do processo de contagem de pontos de função 
5.2 Reunir a documentação disponível 
A documentação de suporte a uma contagem de pontos  de função deve descrever a funcionalidade 
entregue pelo software ou a funcionalidade impactada pelo projeto de software medido.  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 9
 

---
## Página 42

5  Processo de Medição  Parte 1 – FSM 
Deve ser o
btida documentação suficiente para conduzir a contagem de pontos de função, ou acesso 
a especialistas no assunto capazes de fornecer in formações adicionais para suprir quaisquer falhas 
na documentação.  
NOTA A documentação adequada pode incluir requisitos , modelos de dados/objetos, diagramas de classes, 
diagramas de fluxos de dados, casos de uso, descrições de procedimentos, formatos de relatórios, manuais de 
usuário e outros artefatos do desenvolvimento de software.  
5.3 Determinar o escopo e fronteira da contagem, identificando os Requisitos 
Funcionais do Usuário 
Para determinar o escopo e fronteira da contagem e i dentificar os Requisitos Funcionais do Usuário, 
devem ser executadas as seguintes atividades:  
a) identificar o propósito da contagem, 
NOTA 1 Uma contagem de pontos de função é conduzi da a fim de fornecer uma resposta para uma questão 
de negócio, sendo a questão de negócio que determina o propósito.  
NOTA 2 O propósito da contagem determina o escopo da contagem. 
EXEMPLO 1 O propósito da contagem poderi a ser a determinação do tamanho de uma release de software 
específica.  
EXEMPLO 2 O propósito da contagem poderia ser a determinação do tamanho de uma aplicação, como 
parte do esforço da organização para determinar o tamanho de seu portfolio de software.  
b) identificar o tipo de contagem, com base  no propósito, como um dos seguintes:  
1) uma contagem de pontos de funç ão de projeto de desenvolvimento; 
2) uma contagem de pontos  de função de aplicação; 
3) uma contagem de pontos de funç ão de um projeto de melhoria, 
c) determinar o escopo da contagem, com base no propósito e tipo de contagem, 
d) determinar a fronteira de cada aplicação contida no escopo da contagem com base na visão do 
usuário e não em considerações técnicas  
EXEMPLO 3 Se o propósito for estimar o custo de uma melhoria nas aplicações de Recursos Humanos (RH) 
e Benefícios, então: 
— o tipo de contagem é uma contagem de projeto de melhoria; 
— o escopo deverá incluir as funções transacionais e de dados incluídas, alteradas ou excluídas referentes 
tanto à aplicação de RH quanto à de Benefícios, assim co mo quaisquer requisitos de conversão referentes 
a cada aplicação; 
— a visão do usuário é que RH e Benefícios são áreas f uncionais diferentes, por esse motivo são aplicações 
separadas; 
— existe uma fronteira entre as aplicações de RH e de Benefícios, assim como entre cada aplicação e o 
usuário. 
e) os requisitos do usuário podem incluir uma mist ura de requisitos funcionais e não-funcionais; 
identificar quais requisitos são funcionais e excluir os não-funcionais. 
10 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 43

Parte 1 – FSM  5  Processo de Medição 
5.4 Medir funções de dados 
5.4.1 Visão Geral  
A funcion
alidade de dados satisfaz os Requisitos Funcionais do Usuário referentes a  armazenar e/ou 
referenciar dados. Toda a funcionalidade de dados dentro do escopo da contagem deve ser avaliada 
para identificar cada grupo lógico de dados. 
Devem ser executadas as seguintes atividade para medir as funções de dados 
a) identificar e agrupar todos os dados l ógicos em funções de dados conforme 5.4.2, 
b) classificar cada função de dados como um ALI ou AIE, de acordo com 5.4.3, 
c) contar os DERs para cada função de dados conforme 5.4.4, 
d) contar os RLRs para cada funç ão de dados de acordo com 5.4.5, 
e) determinar a complexidade funcional de cada  função de dados em conformidade com 5.4.6, e 
f) determinar o tamanho funcional de cada função de dados conforme 5.4.7. 
5.4.2 Identificar e agrupar todos os dados lógicos em funções de dados 
NOTA 1 As funções de dados são ma is facilmente identificáveis utilizando-se um modelo lógico de dados; no 
entanto, isto não impede a utilização do processo de medição em am bientes onde forem utilizadas técnicas 
alternativas para a modelagem de dados ou objetos. A terminologia da modelagem de dados é utilizada para 
documentar as regras referentes às funções de dados, mas a mesma abor dagem pode ser aplicada a outras 
técnicas.  
Para identificar as funções de dados, devem ser executadas as seguintes atividades 
a) identificar todos os dados ou informações de co ntrole logicamente relacionados e reconhecidos 
pelo usuário, dentro do escopo da contagem,  
b) excluir entidades que não sejam mantidas por nenhuma aplicação,  
c) agrupar entidades que sejam entidades dependentes,  
NOTA 2 Entidades independentes são consideradas  como grupos lógicos de dados distintos. 
d) excluir as entidades abaixo, denominadas dados de código: 
1) entidade de dados de substituição, que cont ém um código e um nome ou descrição 
explicativos; 
2) entidade de ocorrência única, que contém um ou mais atributos que raramente ou nunca 
mudam; 
3) entidade que contém dados basicamente estáticos, ou que muito raramente mudam; 
4) entidade de valores default, que contém valores para popular atributos; 
5) entidade de valores válidos, que contém valo res disponíveis para seleção ou validação; 
6) entidade que contém uma faixa de dados para validação, 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 11
 

---
## Página 44

5  Processo de Medição  Parte 1 – FSM 
NOTA 3 As entidades acima referidas como dados de código podem conter outros atributos para fins de 
auditoria e para definir datas efetivas. A presença desses atributos não altera a natureza dessas entidades.  
e) excluir entidades que não contenham atributos requeridos pelo usuário, e 
f) remover entidades associativas que contenham at ributos adicionais não requeridos pelo usuário 
e entidades associativas que cont enham apenas chaves estrangeiras; agrupar os atributos 
referentes a chaves estrangeiras com as entidades primárias.  
NOTA 4 Atributos referentes a chav es estrangeiras são dados requeridos pelo usuário para estabelecer um 
relacionamento com outra função de dados. 
5.4.3 Classificar cada função de dados como um ALI ou AIE  
Uma fun
ção de dados deve ser classificada como 
a) Arquivo Lógico Interno (ALI), se for mantida pela aplicação medida, ou 
b) Arquivo de Interface Externa (AIE) se for 
— referenciada, mas não mantida, pela aplicação medida, e  
— identificada como um ALI em uma ou mais outras aplicações. 
5.4.4 Contar os DERs para cada função de dados 
A fim de contar o
s DERs - Dados Elementares  Referenciados (tipos de dado elementares) 
correspondentes a uma função de dados, devem ser executadas as seguintes atividades 
a) contar um DER para cada at ributo único, reconhecido pelo usuário e não repetido, mantido na 
função de dados ou recuperado da mesma por meio da execução de todos os processos 
elementares pertinentes ao escopo da contagem,  
NOTA 1 Por exemplo, dentro de um ALI ou AIE, c ontar um único DER para os 12 campos repetidos 
referentes aos valores do Orçamento Mensal. Contar um DER adicional para identificar o mês aplicável. 
b) quando duas ou mais aplicações mantiverem e/ou referenciarem a mesma função de dados, 
contar apenas os DERs utilizados pela aplicação medida,  
NOTA 2 Os atributos não referenciados pela aplicação medida não são contados. 
c) contar um DER para cada atributo requerido pelo usuário para estabelecer um relacionamento 
com outra função de dados, e 
d) revisar os atributos relacionados a fim de det erminar se os mesmos devem ser agrupados e 
contados como um único DER, ou como vários DERs. O agrupamento irá depender de como os 
processos elementares utilizam os atributos dentro da aplicação  
EXEMPLO Os atributos (primeiro nome, nome do me io, sobrenome) são agrupados e contados como 
— nome (primeiro nome, nome do meio, sobrenome) se esses atributos sempre forem utilizados juntos,  
— primeiros nomes (primeiro nome e inicial do meio) e sobrenome se, além do que está acima, o sobrenome 
for utilizado independentemente, ou  
— primeiro nome, inicial do meio e sobrenome, se os três puderem ser utilizados independentemente. 
12 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 45

Parte 1 – FSM  5  Processo de Medição 
5.4.5 Contar os RLRs para cada função de dados  
A fim de co
ntar RLRs - Registros Lógicos Referenciados (tipos de arquivo referenciados) para uma 
função de dados, devem ser executadas as seguintes atividades  
a) contar um RLR para cada função de dados (i.e., por default, cada função de dados possui um 
subgrupo de DERs que é contado como um RLR),  
b) contar um RLR adicional para cada um dos se guintes subgrupos lógicos de DERs (dentro da 
função de dados) que contenham mais de um DER:  
1) entidade associativa co m atributos não-chave; 
2) subtipo (sem ser o primeiro subtipo); 
3) entidade atributiva, em um relacionamento que não seja 1-1obrigatório 
NOTA 1 Um relacionamento 1-1 obrigatório é um re lacionamento entre duas entidades onde cada uma se 
relaciona com uma e somente uma instância da entidade relacionada.  
NOTA 2 Se um modelo de dados não estiver disponível, procurar grupos de dados r epetidos para identificar 
RLRs.  
EXEMPLO 1 Uma fatura possui um cabeçalho com informa ções do cliente e vários itens referentes às 
compras (por exemplo, número do item, descrição, preço, peso). O cabeçalho é contado como um RLR. Os itens 
constituem um grupo repetido e são contados como um RLR adicional. 
EXEMPLO 2 Um único atributo repetido tal como vá rios números de conta para o mesmo cliente não 
constitui um grupo repetido, sendo contado como um único DER e não como um RLR.  
EXEMPLO 3 Um grupo de DERs ocorrendo várias vezes, tal como ano, mês e valor orçado é um grupo 
repetido, mas é contado como três DERs e não como um RLR.  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 13
 

---
## Página 46

5  Processo de Medição  Parte 1 – FSM 
5.4.6 Determinar a complexidade funcional de cada função de dados  
A complexid
ade funcional de cada função de dados deve ser determinada utilizando-se o número de 
DERs e RLRs, em conformidade com a Tabela 1. 
Tabela 1 — Complexidade das funções de 
dados 
  DERs 
  1 – 19 20 – 50 > 50 
1 Baixa Baixa Média 
2 – 5 Baixa Média Alta RLRs 
> 5 Média Alta Alta 
 
5.4.7 Determinar o tamanho funcional de cada função de dados 
O tamanho funci
onal de cada função de dados deve ser determinado utilizando-se o tipo e a 
complexidade funcional, de acordo com a Tabela 2.  
Tabela 2 — Tamanho das funções de 
dados 
  Tipo 
  ALI AIE 
Baixa 7 5 
Média 10 7 Complexidade 
funcional 
Alta 15 10 
 
5.5 Medir funções de transação 
5.5.1 Visão geral 
A funcio
nalidade de transação satisfaz os Requisitos Funcionais do Usuário que processam dados. 
Toda a funcionalidade de transação dentro do esc opo da contagem deve ser avaliada, a fim de 
identificar cada processo elementar único.  
Para medir funções de transação, as seguintes atividades devem ser executadas 
a) identificar cada processo elementar requeri do pelo usuário, em conformidade com 5.5.2, 
b) classificar cada função de transação como um a Entrada Externa (EE), Saída Externa (SE) ou 
Consulta Externa (CE), conforme 5.5.3, 
c) contar os ALRs - Arquivos Lógicos Referenciados (tipos de arquivo referenciados) para cada 
função de transação, de acordo com 5.5.4, 
14 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 47

Parte 1 – FSM  5  Processo de Medição 
d) 
contar os DERs - Dados Elementares Refere nciados (tipos de dado elementares) para cada 
função de transação, conforme 5.5.5, 
e) determinar a complexidade funcional de ca da função de transação de acordo com 5.5.6, e 
f) determinar o tamanho funcional de cada função de transação conforme 5.5.7. 
5.5.2 Identificar processos elementares 
5.5.2.1  
Para ide
ntificar cada processo elementar devem ser executadas as seguintes atividades 
a) Compor e/ou decompor os Requisitos Funcio nais do Usuário nas menores unidades de atividade 
que satisfaçam todos os itens abaixo: 
1) é significativa para o usuário; 
2) constitui uma transação completa; 
NOTA Aos usuários de versões anteriores deste Padr ão Internacional: o item 2 não é uma mudança, mas 
sim um refinamento para aumentar a especificidade a fim de promover interpretação consistente.  
3) é autocontida; 
4) deixa o negócio da aplicação contada em um estado consistente. 
EXEMPLO 1 Um Requisito Funcional do Usuário pode estabelecer que deve ser fornecida uma função para 
Manter Informações de Empregado. Esse requisito é decomposto em unidades de trabalho menores tais como 
Incluir Empregado, Alterar Empregado e Consultar Empregado.  
EXEMPLO 2 Os requisitos individuais podem estabelecer a necessidade de incluir diversos tipos de 
informações de empregado (por exem plo, endereço, salário e informaç ões de dependentes), mas a menor 
unidade de atividade significativa para o usuário é Incluir Empregado. 
b) Identificar um processo elementar para ca da unidade de atividade identificada, de modo a 
satisfazer todos os critérios em 5.5.2.1 a). 
5.5.2.2  
Para determinar processos elementares únicos devem ser executadas as seguintes atividades 
a) Ao comparar um possível processo elementar com um processo elementar já identificado, contar 
os dois processos elementares referidos como um único processo elementar se eles: 
1) demandarem o mesmo conjunto de DERs; 
2) demandarem o mesmo conjunto de ALRs; 
3) demandarem o mesmo conjunto de lógicas de processamento para executar o processo 
elementar (consultar a lista abaixo em 5.5.2.2 b), 
NOTA 1 As atividades referentes à medição das f unções de transação são mostradas sequencialmente; no 
entanto, as mesmas são de fato iterativas. ALRs e DERs são identificados de acordo com 5.5.4 e 5.5.5, mas são 
necessários para comparar dois processos elementares semelhantes. 
NOTA 2 Um processo elementar pode incluir variações pequenas em DERs ou ALRs, assim como múltiplas 
alternativas, variações ou ocorrências das lógicas de processamento abaixo. 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 15
 