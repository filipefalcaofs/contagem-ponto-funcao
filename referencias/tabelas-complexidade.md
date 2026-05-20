# Tabelas de Complexidade e Tamanho Funcional (Parte 1 — FSM)

Extraído do CPM IFPUG 4.3.1 PT-BR (páginas 44–58).


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
 

---
## Página 48

5  Processo de Medição  Parte 1 – FSM 
EXEMPLO Quando é identificado um processo elementar para Incluir Empregado, o fato de um empregado 
poder ou não ter dependentes não faz com o que o processo elementar seja dividido em dois. O processo 
elementar ainda é Incluir Empregado, havendo variação na lógica de processamento e nos DERs para dar conta 
dos dependentes.  
b) Não dividir um processo elementar com várias formas de lógica de processamento em vários 
processos elementares.  
NOTA 4  Um processo elementar que recebe e valida dados do usuário, lê e filtra dados de um ALI, classifica 
e apresenta os resultados ao usuário não pode ser dividido em vários processos elementares.  
5.5.2.3  
Várias formas de lógica de processamento para  a execução de um processo elementar estão 
identificadas na Tabela 3:  
Tabela 3 — Formas de lógica de processamento 
Formas de lógica de processamento 
1. Validações são executadas 
EXEMPLO 1 Ao acrescentar um novo empregado a uma organizaçã o, o respectivo processo valida o DER referente ao 
tipo de empregado.  
2. Fórmulas e cálculos matemáticos são executados 
EXEMPLO 2 Ao emitir relatório com todos os empregados de uma organização, o processo calcula o número total de 
empregados mensalistas, empregados horistas e o total geral.  
3. Valores equivalentes são convertidos 
EXEMPLO 3 Com base em uma tabela, a idade do empregado é convertida para um grupo de faixas de idade.  
4. Dados são filtrados e selecionados segundo critério s especificados para comparar vários conjuntos de 
dados  
EXEMPLO 4 A fim de gerar uma lista de empregados segund o as tarefas alocadas aos mesmos, um processo 
elementar utiliza o número da tarefa presente nas alocações para selecionar e listar os empregados alocados a cada 
tarefa.  
5. Condições são analisadas para determinar as aplicáveis 
EXEMPLO 5 A lógica de processamento utilizada pelo proc esso elementar na inclusão de um empregado depende do 
mesmo ser mensalista ou horista. A ent rada dos DERs (e a lógica de proce ssamento resultante) com base em uma 
escolha distinta (mensalista ou horista) é parte de um processo elementar neste exemplo. 
6. Um ou mais ALIs são atualizados  
EXEMPLO 6 Ao incluir um empregado, o processo elem entar atualiza o ALI de emprega do para manter os dados 
referentes a empregado.  
7. Um ou mais ALIs ou AIEs são referenciados  
EXEMPLO 7 Ao incluir um empregado, o AIE de moeda é re ferenciado para obter a taxa  de conversão para o dólar 
norte-americano, a fim de determinar o salário-hora dos empregados.  
8. Dados ou informações de controle são recuperados  
EXEMPLO 8 Para permitir a visualização de uma lista de empregados, informações dos empregados são recuperadas 
de uma função de dados. 
16 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 49

Parte 1 – FSM  5  Processo de Medição 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 17
 
Form
as de lógica de processamento 
9. Dados derivados são criados a partir de transfor mação dos dados existentes, com o objetivo de criar 
dados adicionais 
EXEMPLO 9 A fim de determinar (derivar) o número de matr ícula de um paciente (por exemplo, SMIJO01), os 
seguintes dados são concatenados:  
— as primeiras três letras do sobrenome do paciente (por exemplo, SMI para Smith); 
— as duas primeiras letras do primeiro nome do paciente (por exemplo, JO para John);  
— um número de sequência de dois dígitos (começando com 01). 
10. É alterado o comportamento da aplicação  
EXEMPLO 10 O comportamento do processo elementa r de pagamento dos empregados é alterado quando uma 
mudança é feita para efetuar o pagamento sexta-feira sim, sexta-feira não, ao invés de fazê-lo no dia 15 e no último dia do 
mês, resultando em 26 períodos de pagamento ao invés de 24.  
11. Preparar e apresentar informações fora da fronteira 
EXEMPLO 11 Uma lista de empregados é formatada e apresentada ao usuário. 
12. Existe a capacidade de receber dados e informações de controle que entram pela fronteira da aplicação 
EXEMPLO 12 Um usuário entra com informações para incluir um pedido de cliente na aplicação. 
13. Classificar ou arrumar um conjunto de dados. Esta forma de lógica de processamento não impacta a 
identificação do tipo ou contribui para a unicidade de um processo elementar; isto é, a orientação dos 
dados não constitui unicidade 
EXEMPLO 13 A lista de empregados é classificada em ordem alfabética ou de localização. 
EXEMPLO 14 Em uma tela de entrada de pedidos, as info rmações do cabeçalho do pedido são colocadas na parte 
superior da tela, enquanto os detalhes do pedido são colocados abaixo. 
NOTA 1 Versões anteriores deste Padrão Internaci onal (ISO/IEC 20926:2003) utilizar am erradamente os termos 
“reclassificar” e “rearrumar”; a utilização dos termos “classificar” e “arrumar” é uma correção e não uma alteração. 
 
5.5.3 Classificar cada processo elementar como uma função de transação 
5.5.3.1  
Para cada p
rocesso elementar 
a) a intenção primária deve ser classificada como uma das seguintes: 
1) alterar o comportamento da aplicação; 
2) manter um ou mais ALIs; 
3) apresentar informações ao usuário, 
b) as formas de lógica de processamento requeri das para executar o processo elementar devem 
ser identificadas na lista apresentada em 5.5.2.3. 

---
## Página 50

5  Processo de Medição  Parte 1 – FSM 
5.5.3.2  
Cad
a processo elementar deve ser classificado como 
a) uma EE, se o mesmo: 
1) incluir lógica de processamento para re ceber dados ou informações de controle que 
entrem pela fronteira da aplicação; 
2) tiver um das seguintes intenções primárias 
i) manter um ou mais ALIs, ou  
ii) alterar o comportamento da aplicação, 
b) uma SE, se o mesmo tiver a intenção primária  de apresentar informações ao usuário e incluir 
pelo menos uma das seguintes formas de lógica de processamento:  
1) cálculos matemáticos são executados; 
2) um ou mais ALIs são atualizados; 
3) dados derivados são criados; 
4) o comportamento da aplicação é alterado, 
c) uma CE, se o mesmo tiver a intenção primária de apresentar informações ao usuário e: 
1) referenciar uma função de dados para recuperar dados ou informações de controle; 
2) não satisfizer os critérios pa ra ser classificado como uma SE. 
NOTA 1 A Tabela 4 apresenta um resumo do relacionamen to entre a intenção primária e o tipo de função de 
transação. 
Tabela 4 — Relacionamento entre a intenção primária e o tipo de função de transação 
 Tipo de função de transação  
Função EE SE CE 
Alterar o comportamento da aplicação IP F N/A 
Manter um ou mais ALIs IP F N/A 
Apresentar informações ao usuário F IP IP 
legenda  
IP  a intenção primária do tipo de função de transação 
F uma função do tipo de função de transação que às vezes 
está presente, mas que não é a intenção primária  
N/A o tipo de função de transação não pode executar este 
tipo de função  
 
NOTA 2 A Tabela 5 apresenta um resumo do relacionam ento entre as formas de processamento lógico e o 
tipo de função de transação. 
Tabela 5 — Relacionamento entre a lógica de processamento e o tipo de função de transação  
 Tipo de função de transação 
Forma de lógica de processamento EE SE CE 
1. Validações são executadas p p p 
2. Cálculos matemáticos são executados p o* n 
18 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 51

Parte 1 – FSM  5  Processo de Medição 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 19
 
 
Tipo de função de transação 
Forma de lógica de processamento EE SE CE 
3. Valores equivalentes são convertidos p p p 
4. Dados são filtrados e sele cionados utilizando-se critérios 
especificados  para comparar vários conjuntos de dados  
p p p 
5. Condições são analisadas para deter minar quais são aplicáveis  p p p 
6. Pelo menos um ALI é atualizado  o* o* n 
7. Pelo menos um ALI ou AIE é referenciado  p p o 
8. Dados ou informações de controle são recuperados p p o 
9. Dados derivados são criados p o* n 
10. O comportamento da aplicação é alterado o* o* n 
11. Informações são preparadas e então apresentadas fora da fronteira  p o o 
12. Dados ou informações de controle entrando pela fronteira da 
aplicação são recebidos  
o p p 
13. Um conjunto de dados é classificado ou arrumado  p p p 
 
legenda  
o é obrigatório que o tipo de função de transação execute a forma de lógica de processamento 
o* é obrigatório que o tipo de função de transação execute pelo menos uma destas (o*) formas de 
lógica de processamento  
p o tipo de função de transação pode executar a forma de lógica de processamento, mas a 
mesma não é obrigatória  
n o tipo de função de transação não pode executar a forma de lógica de processamento  
  
5.5.4 Contar ALRs para cada função de transação  
Para 
cada função de transação, um ALR deve ser contado para cada função de dados única que for 
acessada (lida e/ou gravada) pela função de transação.  
NOTA As atividades referentes à medição de funções de transação s ão apresentadas sequencialmente;  
contudo, na verdade as mesmas s ão iterativas. Para comparar dois processos elementares similares é 
necessária a identificação de ALRs, conforme dito em 5.5.2.2. 
5.5.5 Contar DERs para cada função de transação  
A fim de contar DE
Rs para uma função de transação, as seguintes atividades devem ser executadas 
a) Revisar tudo o que atravesse (entre e/ou saia) a fronteira, 
b) Contar um DER para cada atributo único, re conhecido pelo usuário e não repetido que atravesse 
(entre e/ou saia) a fronteira durante o processamento da função de transação, 
EXEMPLO 1 DERs que atravessam a fronteira incluem 
— atributos que o usuário introduz por meio de uma tela, bem como aqueles apresentados em um relatório ou 
tela, 
— atributos que entram pela fronteira da aplicação e que são necessários para especificar quando, o quê e/ou 
como os dados devem ser recuperados ou gerados pelo processo elementar,  
— atributos fornecidos pelo usuário da função de transação, ou apresentados a ele, e  
— atributos em um arquivo eletrônico que entrem ou saiam pela fronteira. 
c) Contar apenas um DER por função de trans ação para a habilidade de enviar uma mensagem de 
resposta da aplicação, mesmo que existam várias mensagens, 

---
## Página 52

5  Processo de Medição  Parte 1 – FSM 
EXEMPLO 2 Se forem apresentadas diversas mensagen s de erro/confirmação ao usuário, somente um DER 
será contado. 
d) Contar apenas um DER por função de transação para a habilid ade de iniciar ações, mesmo que 
existam diversas maneiras de fazer isso, e  
EXEMPLO 3 Se o usuário puder iniciar a geração de um relatório clicando no botão OK ou pressionando 
uma tecla de função, apenas um DER será contado.  
e) Não contar os seguintes itens como DERs: 
— constantes literais tais como títulos de re latórios, identificadores de telas ou painéis, 
cabeçalhos de colunas ou títulos de atributos; 
— rótulos gerados pela aplicação tais como atributos referentes a data e hora; 
— variáveis de paginação, números de página e informações de posicionamento, por exemplo, 
‘Linhas 37 a 54 de 211’; 
— auxílios à navegação tais como a habilidade de navegar em uma lista utilizando “anterior”, 
“próximo”, “primeiro”, “último” e seus equivalentes gráficos; 
— atributos gerados dentro da fronteira por uma função de transação e salvos em um ALI sem 
sair pela fronteira; 
— atributos recuperados ou referenciados de um ALI ou AIE para participarem do 
processamento sem que saiam pela fronteira. 
NOTA As atividades referentes à medição de funções de transação s ão apresentadas sequencialmente;  
contudo, na verdade as mesmas s ão iterativas. Para comparar dois processos elementares similares é 
necessária a identificação dos DERs, conforme dito em 5.5.2.2. 
5.5.6  Determinar a complexidade funcional para cada função de transação 
A complexidade funcional de cada função de transa ção será determinada utilizando-se o número de 
ALRs e DERs, em conformidade com a Tabela 6 ou 7.  
Tabela 6 — Complexidade funcional das 
EE 
 Tabela 7 — Complexidade funcional das 
SE e CE 
  DERs    DERs 
  1 – 4 5 – 15 > 15    1 – 5 6 – 19 > 19 
0 – 1 Baixa Baixa Média  0 – 1 Baixa Baixa Média 
2 Baixa Média Alta  2 – 3 Baixa Média Alta ALRs 
> 2 Média Alta Alta  
ALRs 
> 3 Média Alta Alta 
      NOTA Uma CE tem no mínimo 1 ALR. 
5.5.7 Determinar o tamanho funcional de cada função de transação 
O tamanho funci
onal de cada função de transaç ão será determinado utilizando-se o tipo e a 
complexidade funcional, de acordo com a Tabela 8. 
20 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 53

Parte 1 – FSM  5  Processo de Medição 
Tabela 8 — 
Tamanho das funções de transação 
  Tipo 
  EE SE CE 
Baixa 3 4 3 
Média 4 5 4 Complexidade 
Funcional 
Alta 6 7 6 
 
5.6 Medir a funcionalidade de conversão  
O escopo da contagem de um projeto de desenv olvimento ou melhoria também pode incluir o 
tamanho funcional da funcionalidade de conversão requerida para o mesmo. As funções de 
transação de conversão e as funções de dados (que ainda não tenham sido contadas) deverão ser 
contadas em conformidade com 5.4 e 5.5.  
NOTA O escopo da contagem determinará se a func ionalidade de conversão deverá ser contada. 
5.7 Medir a funcionalidade correspondente a melhorias 
Os projetos de melhoria podem envolver inclusõe s, alterações e exclusões da funcionalidade 
existente. A funcionalidade corr espondente às melhorias deverá ser medida de acordo com o que 
segue:  
a) Não alterar a fronteira já estabeleci da para a(s) aplicação(ões) modificada(s). 
b) Contar as funções de dados incluídas, alteradas ou excluídas de acordo com 5.4. 
c) Contar as funções de transação que forem incluídas, alteradas ou excluídas de acordo com 5.5, 
e 
d) O tamanho funcional da aplicação poderá ser atualizado para refletir: 
1) a funcionalidade incluída, que aument ará o tamanho funcional da aplicação; 
2) a funcionalidade alterada, que poderá aumentar, diminuir ou não ter efeito sobre o 
tamanho funcional da aplicação; 
3) a funcionalidade excluída, que diminuir á o tamanho funcional da aplicação. 
NOTA 1 Uma alteração em uma função de dados pode envolver inclusão, alteração ou exclusão de DERs 
e/ou RLRs. 
NOTA 2 Uma alteração em uma função de transação pode envolver inclusão, alteração ou exclusão de DERs 
e/ou ALRs e/ou alteração na lógica de processamento.  
5.8 Calcular o tamanho funcional 
O objetivo e escopo da contagem deverão ser co nsiderados na seleção e utilização da fórmula 
apropriada para calcular o tamanho funcional.  
O tamanho funcional de um projeto de desenvolvimento deverá ser calculado utilizando-se a Fórmula 
(1): 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 21
 

---
## Página 54

5  Processo de Medição  Parte 1 – FSM 
DFP = AD
D + CFP (1) 
onde 
DFP é a contagem de pontos de função do projeto de desenvolvimento; 
ADD é o tamanho das funções a serem entregues ao usuário pelo projeto de desenvolvimento; 
CFP é o tamanho da funcionalidade de conversão. 
O tamanho funcional de uma aplicação, medido apó s o projeto de desenvolvimento, ou a qualquer 
tempo no ciclo de vida da aplicação deverá ser calculado utilizando-se a Fórmula (2):  
AFP = ADD (2) 
onde 
AFP é a contagem de pontos de função da aplicação; 
ADD é o tamanho das funções a serem entregues ao usuário pelo projeto de desenvolvimento (excluído o 
tamanho de qualquer funcionalidade de conversão), ou a funcionalidade existente no momento da contagem 
da aplicação.  
O tamanho funcional de um projeto de melhoria deverá ser calculado utilizando-se a Fórmula (3): 
EFP = ADD + CHGA + CFP + DEL (3) 
onde 
EFP é a contagem de pontos de função do projeto de melhoria; 
ADD é o tamanho das funções incluídas pelo projeto de melhoria; 
CHGA é o tamanho das funções alteradas pelo projeto de melhoria – conforme as mesmas estão / estarão 
após a implementação; 
CFP é o tamanho da funcionalidade de conversão; 
DEL é o tamanho das funções excluídas pelo projeto de melhoria. 
O tamanho funcional de uma aplicação após um projeto de melhoria deverá ser calculado utilizando-
se a Fórmula (4): 
AFPA = (AFPB + ADD + CHGA) - (CHGB + DEL) (4) 
onde 
AFPA é a contagem de pontos de função da aplicação após o projeto de melhoria; 
AFPB é a contagem de pontos de função da aplicação antes do projeto de melhoria; 
ADD é o tamanho das funções incluídas pelo projeto de melhoria; 
CHGA é o tamanho das funções alteradas pelo projet o de melhoria – como estão / estarão após a 
implementação;  
CHGB é o tamanho das funções alteradas pelo projeto de melhoria – como estão / estavam antes do início 
do projeto; 
22 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 

---
## Página 55

Parte 1 – FSM  5  Processo de Medição 
DEL é o tamanho das funções excluídas pelo projeto de melhoria. 
5.9 Documentar a contagem de pontos de função 
A contagem de pontos de função deve ser documentada como segue: 
 o propósito e o tipo da contagem; 
 o escopo da contagem e a fronteira da aplicação; 
 a data da contagem; 
 uma lista de todas as funções de dados e de transação, incluindo o respectivo tipo e 
complexidade, bem como o número de pontos de função atribuído a cada uma; 
 o resultado da contagem (ver 5.10); 
 quaisquer suposições feitas e questões resolvidas. 
A documentação da contagem de pontos de função também pode incluir o seguinte:: 
 a identificação da documentação de origem na qual a contagem foi baseada; 
 a identificação dos participantes, seus papéis e qualificações; 
 para cada função de dados, o número de DERs e RLRs; 
 para cada função de transação, o número de DERs e de ALRs; 
 uma referência cruzada de todas as funções  de dados para as funções de transação; 
 uma referência cruzada de todas as funções de dados para as abstrações relacionadas na 
documentação de origem; 
 uma referência cruzada de todas as funções de transação para as abstrações relacionadas na 
documentação de origem. 
NOTA 1 Negociar o nível de documentação com o cliente e informar ao mesmo os custos e benefícios 
relacionados. 
NOTA 2 Uma Contagem de Pontos de Função comple tamente documentada facilitará a rastreabilidade, 
usabilidade e manutenibilidade; contudo, um cliente pode estar interessado apenas no resultado final. 
5.10 Reportar o resultado da contagem de pontos de função 
NOTA A prática de reportar consistentemente os resu ltados das contagens de pontos de função permitirá 
que os leitores identifiquem o padrão com o qual as mesmas mantém conformidade.  
5.10.1 5.10.1        
Os re
sultados que mantenham conformidade com este Padrão Internacional deverão ser reportados 
como segue: 
S FP (IFPUG–IS) 
onde 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 23
 

---
## Página 56

5  Processo de Medição  Parte 1 – FSM 
24 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 
S é o resultado da contag em de pontos de função; 
FP é a unidade de tamanho do método FSM do IFPUG; 
IS é este Padrão Internacional (ISO/IEC 20926:200x).  
EXEMPLO 250 FP (IFPUG-ISO/IEC 20926:200x) 
5.10.2 5.10.2       
Os re
sultados que mantiverem conformidade com uma customização local deste Padrão 
Internacional deverão ser reportados como: 
S FP (IFPUG–IS–c) 
onde 
c representa um ou mais caracteres indicando que o resultado não mantém conformidade plena com 
este Padrão Internacional. 
EXEMPLO 250 FP (IFPUG–ISO/IEC 20926:200x–a) 

---
## Página 57

Part 1 – FSM  Anexo A 
 
Anexo A 
(informativo) 
 
Tabelas consolidadas de complexidade e tamanho funcional 
 
Para maior conveniência, as tabelas de complexidade e tamanho funcional são repetidas nas 
Tabelas A.1 a A.5.  
Tabela A.1 — Complexidade das funções 
de dados 
 Tabela A.2 — Tamanho das funções de 
dados 
  DERs    Tipo 
  1 – 19 20 – 50 > 50    ALI AIE 
1 Baixa Baixa Média  Baixa 7 5 
2 – 5 Baixa Média Alta  Média 10 7 RLRs 
> 5 Média Alta Alta  
Complexidade 
funcional 
Alta 15 10 
 
Tabela A.3 — Complexidade funcional das 
EEs 
 Tabela A.4 — Complexidade funcional das 
SEs e CEs 
  DERs    DERs 
  1 – 4 5 – 15 > 15    1 – 5 6 – 19 > 19 
0 – 1 Baixa Baixa Média  0 – 1 Baixa Baixa Média 
2 Baixa Média Alta  2 – 3 Baixa Média Alta ALRs 
> 2 Média Alta Alta  
ALRs 
> 3 Média Alta Alta 
      NOTA Uma CE tem no mínimo 1 ALR. 
 
Tabela A.5 — Tamanho das funções de transação 
  Tipo 
  EE SE CE 
Baixa 3 4 3 
Média 4 5 4 Complexidade 
funcional 
Alta 6 7 6 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 25 
 

---
## Página 58

Anexo A  Parte 1 – FSM 
26 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Esta página foi deixada em branco intencionalmente. 

# Anexo A — Tabelas consolidadas

Extraído do CPM IFPUG 4.3.1 PT-BR (páginas 57–58).


---
## Página 57

Part 1 – FSM  Anexo A 
 
Anexo A 
(informativo) 
 
Tabelas consolidadas de complexidade e tamanho funcional 
 
Para maior conveniência, as tabelas de complexidade e tamanho funcional são repetidas nas 
Tabelas A.1 a A.5.  
Tabela A.1 — Complexidade das funções 
de dados 
 Tabela A.2 — Tamanho das funções de 
dados 
  DERs    Tipo 
  1 – 19 20 – 50 > 50    ALI AIE 
1 Baixa Baixa Média  Baixa 7 5 
2 – 5 Baixa Média Alta  Média 10 7 RLRs 
> 5 Média Alta Alta  
Complexidade 
funcional 
Alta 15 10 
 
Tabela A.3 — Complexidade funcional das 
EEs 
 Tabela A.4 — Complexidade funcional das 
SEs e CEs 
  DERs    DERs 
  1 – 4 5 – 15 > 15    1 – 5 6 – 19 > 19 
0 – 1 Baixa Baixa Média  0 – 1 Baixa Baixa Média 
2 Baixa Média Alta  2 – 3 Baixa Média Alta ALRs 
> 2 Média Alta Alta  
ALRs 
> 3 Média Alta Alta 
      NOTA Uma CE tem no mínimo 1 ALR. 
 
Tabela A.5 — Tamanho das funções de transação 
  Tipo 
  EE SE CE 
Baixa 3 4 3 
Média 4 5 4 Complexidade 
funcional 
Alta 6 7 6 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 25 
 

---
## Página 58

Anexo A  Parte 1 – FSM 
26 Manual de Práticas de Contagem de Pontos de Função Janeiro de 2010
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Esta página foi deixada em branco intencionalmente. 

# Apêndice A — Tabela de cálculo

Extraído do CPM IFPUG 4.3.1 PT-BR (páginas 502–510).


---
## Página 502

  Parte 5 – Apêndices e Glossário 
A-2 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 
Tabela de cálculo de Tamanho Funcional  
 A tabela seguinte é fornecida para facilitar o cálculo da contribuição para o 
tamanho funcional.  
 
Tipo de 
Função 
 Complexidade  
Funcional 
Totais 
Complexidade 
Totais 
Tipos de Função 
ALI  Baixa X 7 =    
  Média X 10 =    
  Alta X 15 =    
       
AIE  Baixa X 5 =    
  Média X 7 =    
  Alta X 10 =    
       
EE  Baixa X 3 =    
  Média X 4 =    
  Alta X 6 =    
       
CE  Baixa X 3 =    
  Média X 4 =    
  Alta X 6 =    
       
SE  Baixa X 4 =    
  Média X 5 =    
  Alta X 7 =    
       
       
Tamanho Funcional Total   
   
 
 
 
 
 
 

---
## Página 503

  Parte 5 Apêndice B  
 
 
 
 
 
 
 
Apêndice B: A mudança da versão anterior 
 
Introdução Este apêndice inclui informações sobre as mudanças e melhorias incluídas no 
CPM 4.3, o processo de tomada de decisão e recomendações para os usuários 
do novo manual.   
  
Conteúdo Este capítulo inclui o seguinte: 
 
Tópico Página 
Introdução B-2 
Áreas das principais mudanças de estrutura do CPM 4.3 B-3 
Controle de Versão B-3 
Visão geral das mudanças B-4 
Background B-12 
Estudo de Impacto B-12 
Conversão do CPM 4.2 para o 4.3 B-12 
Impacto nos Usuários do 4.2.1 mudando para o 4.3 B-14 
Recomendações B-14 
 
Janeiro 2010 Manual de Práticas de Contagem de Pontos de Função B-1 

---
## Página 504

0BApêndice B: A mudança da versão anterior  Parte 5 – Apêndices e Glossário 
Introdução  
Desde a versão do Manual de Práticas de Contagem do IFPUG (CPM) 4.2 em 2004, o Comitê de 
Práticas de Contagem (CPC) criou a nova versão da Parte 1 (regras) para substituir o padrão ISO 
(ISO 20926:2004); isto é, o IFPUG CPM 4.1 não ajustado.  A criação do novo padrão ISO exigiu 
mudanças no texto das demais partes (o guia de implementação) para manter a consistência.   
 
O processo do CPC de revisão do CPM é o seguinte: 
1. A edição é submetida ao CPC pelos membros. 
2. A edição é designada aos membros CPC para pesquisa. 
3. O CPC revisa e discute a edição. 
4. O CPC apresenta a solução proposta para os membros. 
5. Um estudo de impacto é iniciado. 
6. A decisão final é tomada. 
7. Os membros do IFPUG são informados da decisão por meio da publicação MetricViews e 
apresentações nas conferências do IFPUG. 
8. As mudanças tornam-se efetivas em um novo CPM. 
9. Os estudos de casos são revisados para refletir o novo CPM. 
 
 
B-2 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 

---
## Página 505

Parte 5 – Apêndices e Glossário   0BApêndice B: A mudança da versão anterior 
Áreas das principais mudanças de estrutura do CPM 
4.3 
As áreas das principais mudanças de estrutura do CPM 4.3 são: 
 
 Substituir a Parte 1 existente pela Parte 1 com o novo padrão ISO (ISO/IEC 20926:2010) 
 Criar a Ponte – Aplicando Método de Tamanho Funcional do IFPUG (agora Parte 2) que 
provê um guia na aplicação do processo e regras, tal como definido no Padrão ISO (agora 
Parte 1) 
 Aperfeiçoar as partes restantes a fim de ficarem consistentes com a Parte 1 revisada 
 Práticas de Contagem (Parte 3) 
 Exemplos (Parte 4) 
 Apêndices e Glossário (Parte 5) 
 
 
 
 
 
Controle de Versão  
O CPC escolheu dar o nome IFPUG CPM 4.3 a esta versão, ao invés de 4.2.2 ou 5.0 por duas 
razões:   
 Uma versão com nome de 4.2.2 poderia sugerir que apenas a grafia foi corrigida; versão 4.3 
chama mais atenção para a Parte 1 reescrita. 
 Uma versão com nome de 5.0 poderia sugerir uma mudança das regras principais. O CPM 
4.3 ainda é uma evolução da metodologia de Albrecht que forma a base de todas as versões 
anteriores do CPM do IFPUG.  Esta versão provê esclarecimento adicional das versões 
anteriores. 
Janeiro 2010 Manual de Práticas de Contagem de Pontos de Função B-3 

---
## Página 506

0BApêndice B: A mudança da versão anterior  Parte 5 – Apêndices e Glossário 
Visão geral das mudanças  
Além de substituir a Parte 1 existente com o padrão ISO, outros pequenos esclarecimentos foram 
incluídos no CPM 4.3. Para facilitar usuários que desejam alinhar seu CPM atual escrito em uma 
língua estrangeira, todas as mudanças foram listadas abaixo. 
Parte 1: Processo e Regras 
A fim de manter o guia de implementação do método FSM do IFPUG com o Padrão ISO 
revisado (ISO/IEC 14143-1:2007), parte da terminologia teve que ser revisada. As regras e 
diretrizes permanecem essencialmente inalteradas; contudo, a seqüência de ações e a redação foi 
ligeiramente alterada. Não se deve supor que o tamanho funcional seja alterado. Todos os 
capítulos na Parte 1 (agora Parte 2) incluem alterações de redação, exemplos adicionais e 
orientação a fim de ser consistente e adequado ao Padrão ISO de FSM atualizado, que foi 
lançado em 2007 e é agora a Parte 1. As CGSs e o Fator de Ajuste foram retirados desta parte e 
estão incluídos nos apêndices a fim de se adequar ao Padrão ISO de FSM, que não os reconhece 
como parte do FSM. Detalhes adicionais são indicados abaixo, por capítulo.  
Parte 1, Capítulo 1: Introdução 
O título d
este capítulo foi alterado para “A Ponte – Aplicando o Método de Medição de 
Tamanho Funcional do IFPUG”. O capítulo 1 contem apenas uma Introdução; as mudanças que 
refletem o conteúdo dos demais capítulos estão na nova Parte 2.  
Parte 1, Capítulo 2: Visão Geral da Análise de Pontos de Função 
O título d
este capítulo foi alterado para “Visão Geral do Método FSM do IFPUG”. Houve uma 
alteração extensiva da redação a fim de ser consistente e em conformidade com o Padrão ISO de 
FSM atualizado. As seguintes definições e regras foram ligeiramente reescritas: 
 
O diagrama de processo e diretrizes neste capítulo foram alterados para refletir que o primeiro 
passo no processo de contagem de pontos de função é obter a documentação disponível, de 
acordo com o Padrão ISO de FSM.  
 
O tamanho funcional agora representa o tamanho do software obtido pela quantificação dos 
requisitos funcionais do usuário, substituindo o termo “pontos de função não ajustados”. 
Qualquer discussão sobre “não-ajustado” ou “ajustado” está agora incluída no apêndice a fim de 
se adequar ao padrão ISO de FSM, que não reconhece as CGSs ou o VAF como parte do FSM. 
Parte 1, Capítulo 3: Visão do Usuário  
O título d
este capítulo foi alterado para “Obter a documentação disponível”. Este capítulo 
apresenta o conceito de papel do usuário e a abordagem de medição durante o ciclo de vida de 
uma aplicação; contudo, virtualmente todo o capítulo permanece inalterado exceto pelo título. 
B-4 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 

---
## Página 507

Parte 5 – Apêndices e Glossário   0BApêndice B: A mudança da versão anterior 
Parte 1, Capítulo 4: Determinar o Tipo de Contagem  
O título deste capítulo foi alterado para “Determinar o Tipo de Contagem”. Foi revisada a 
redação para as definições de contagem de pontos de função de projeto de desenvolvimento, 
contagem de pontos de função de projeto de melhoria e contagem de pontos de função de 
aplicação, para ser consistente e adequado ao Padrão ISO de FSM atualizado.  
Parte 1, Capítulo 5: Identificar o Escopo da Contag em e Fronteira da Aplicação   
O título deste capítulo foi alterado para “Determinar o Escopo da Contagem e a Fronteira e 
Identificar os Requisitos Funcionais do Usuário”. Há algumas pequenas alterações de redação a 
fim de ser consistente e adequado ao Padrão ISO de FSM atualizado, mas a grande maioria do 
capítulo permanece inalterada.  
Parte 1, Capítulo 6: Contar Funções de Dados  
O título d
este capítulo foi alterado para “Medir Funções de Dados” para refletir que as regras 
estão realmente contidas na nova Parte 1 e para refletir que este capítulo provê orientações de 
implementação para medir Funções de Dados. As regras contidas são repetidas da Parte 1 para 
facilitar a utilização, e evitar a necessidade de folhear as partes adiante e anteriores. 
Parte 1, Capítulo 7: Contar Funções de Transação  
O título d
este capítulo foi alterado para “Medir Funções de Transação” para refletir que as regras 
estão realmente contidas na nova Parte 1, e para refletir que este capítulo provê orientações  de 
implementação para medir Funções de Transação. Tal como no Capítulo 6, as regras contidas são 
repetidas da Parte 1 para facilitar a utilização, e evitar a necessidade de folhear as partes adiante 
e anteriores. Itens específicos incluem: 
 Orientação adicional e esclarecimento sobre as regras do FSM para processos elementares  
 Regras simplificadas para DER e ALR   
Parte 1, Capítulo 8: Determinar o Fator de Ajuste 
O conteúdo com
pleto deste capítulo foi movido para o Apêndice C a fim de alinhar o Guia de 
Implementação com o FSM do IFPUG que não inclui as CGSs e o VAF.  
Parte 1, Capítulo 9: Calcular a Contagem  de Pontos de Função Ajustada 
As fórmulas previamente contidas neste capítulo foram movidas para o Apêndice C e Parte 3 
Capítulo 4 Melhoria e Atividade de Manutenção, a fim de alinhar o Guia de Implementação com 
o FSM do IFPUG, que não inclui as CGSs e o VAF.  
Janeiro 2010 Manual de Práticas de Contagem de Pontos de Função B-5 

---
## Página 508

0BApêndice B: A mudança da versão anterior  Parte 5 – Apêndices e Glossário 
Parte 2: Práticas de Contagem 
Todos os capítulos na Parte 2 (agora Parte 3) incluem pequenas alterações de redação a fim de 
manter a consistência com a reorganização da Parte 1 e /ou manter a conformidade com o Padrão 
ISO de FSM atualizado. Um novo capítulo (Capítulo 5) foi acrescentado para prover 
compreensão clara da atividade de contagem de Conversão de Dados. Detalhes adicionais estão 
indicados por capítulo abaixo. 
Parte 2, Capítulo 1: Dados de Código 
A APF do I
FPUG está em conformidade com o Padrão ISO FSM. A decisão de não contar 
Dados de Código e de e criar o capítulo Dados de Código na Parte 2 do CPM 4.2 teve origem 
nos requisitos do Padrão ISO de FSM (ISO/IEC 14143-1:1998) de não contar requisitos técnicos 
e de qualidade. 
 
Em 2007, a ISO publicou uma nova versão da FSM Padrão (ISO/IEC 14143-1:2007). 
Conseqüentemente, o capítulo Dados de Código precisou ser atualizado para refletir as alterações 
de redação no Padrão ISO de FSM.  
 
Não há alterações nas regras nem nas orientações deste capítulo, mas há pequenas alterações de 
redação para manter a conformidade com o Padrão ISO de FSM atualizado. 
 
 Incluída a definição ISO de Tamanho Funcional 
 Atualizada a definição Requisitos Funcionais do Usuário 
 Substituídos os termos Requisitos de Qualidade e Requisitos Técnicos pelo termo ISO 
Requisitos Não-Funcionais do Usuário e incluída a definição ISO para este conceito 
 A seção Metodologia foi ligeiramente reescrita para refletir as mudanças no passo 
“Identificar Arquivos Lógicos” no Capítulo 2: Arquivos Lógicos abaixo. 
Parte 2, Capítulo 2: Arquivos Lógicos 
Este cap
ítulo foi criado no CPM 4.2 para prover práticas de contagem e orientação adicional na 
identificação e avaliação de Arquivos Lógicos.  
 
No CPM 4.3, a Parte 1 foi substituída pelo padrão ISO de APF do IFPUG  
 
Algumas alterações para o padrão ISO de FSM têm conseqüência (pequena) no capítulo 
Arquivos Lógicos: 
 No processo de identificação de Arquivos Lógicos, o passo1 anterior (“Remoção de Dados 
de Código antes da avaliação dos Arquivos Lógicos”) tornou-se agora parte do passo1 
“Identificar Arquivos Lógicos”, que é o local mais adequado.  
 Além disto, o passo 2 anterior (“Identificar Arquivos Lógicos e Classificar”) foi decomposto 
em dois passos “1. Identificar Arquivos Lógicos” e “2. Classificar Arquivos Lógicos” 
 Passos 3 e 4 (identificando RLRs e DERs) foram inter-cambiados 
 Os subpassos do passo1 tornaram-se melhor visualizados, através da denominação efetiva 
dos mesmos como sub-passos.  
B-6 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 

---
## Página 509

Parte 5 – Apêndices e Glossário   0BApêndice B: A mudança da versão anterior 
 
Estas alterações na estrutura têm algumas conseqüências (pequenas) na estrutura do capítulo 
Arquivos Lógicos. 
 
Isto é particularmente verdade para o intercambio dos passos Identificando DERs e Identificando 
RLRs, e tornou necessário o intercambio das páginas relacionadas a estes passos. Isto também 
foi necessário para combinar as tabelas “Considerando Registros Lógicos Referenciados em 
conjunto com Arquivos Lógicos via (In-) Dependência de Entidade” (CPM 4.2, página 2-34) e 
“Considerando Dados Elementares Referenciados em conjunto com Arquivos Lógicos via (In-) 
Dependência de Entidade” (CPM 4.2, página 2-46) em uma nova tabela “Considerando Registros 
Lógicos Referenciados e Dados Elementares Referenciados em conjunto com Arquivos Lógicos 
via (In-) Dependência de Entidade” 
 
Há ligeiras alterações de redação para adequação ao padrão ISO de FSM atualizado (ISO/IEC 
14143-1:2007) tal como explicado em mais detalhes na seção acima, dedicada a Parte 2, Capítulo 
1 Dados de Código. 
 
Requisitos de Qualidade e Requisitos Técnicos foram substituídos pelo novo termo ISO 
Requisitos Nâo-Funcionais do Usuário. 
 
Não se deve supor que, nenhuma destas alterações na estrutura e redação tenha qualquer 
influência no resultado de qualquer contagem.  
Parte 2, Capítulo 3: Dados Compartilhados 
Este cap
ítulo foi criado no CPM 4.2 para prover práticas de contagem e orientação adicional na 
identificação e avaliação de dados compartilhados entre aplicações.  
 
As únicas alterações neste capítulo foram duas referências a outras partes do CPM, que agora são 
diferentes. 
Parte 2, Capítulo 4: Projetos de Melhoria e Atividades de Manutenção  
Este cap
ítulo foi criado no CPM 4.2 para prover práticas de contagem e orientação adicional na 
aplicação da Análise de Pontos de Função para atividades pós desenvolvimento. A contagem de 
projetos de melhoria, apresentada antes, na Parte 1, Capítulo 9 do CPM 4.1, é agora inteiramente 
contemplada (incluindo fórmulas aplicáveis) neste capítulo.   
 
Alem das atualizações de referências a outras partes do CPM, as definições e exemplos primários 
para cada uma das formas de lógica de processamento foram ajustados para serem consistentes 
com os da nova Parte 2. Termos foram ajustados para consistência com as Partes 1 e 2, como por 
exemplo, alteração de “campo” para “atributo”. 
 
Alterações específicas na seção Lógica de Processamento neste capítulo incluem o seguinte: 
 
3. Valores Equivalentes: Exemplo alterado em resposta aos comentários do Bulletin 
Board do IFPUG. 
4. Dados são Filtrados: Exemplo existente modificado para excluir a contagem de 
Janeiro 2010 Manual de Práticas de Contagem de Pontos de Função B-7 

---
## Página 510

0BApêndice B: A mudança da versão anterior  Parte 5 – Apêndices e Glossário 
uma mudança envolvendo apenas a substituição ou adição de valores, e 
acrescentados três novos exemplos em resposta aos comentários do Bulletin 
Board do IFPUG. 
 
11. Preparar e apresentar informações para fora da fronteira: Acrescentados três 
novos exemplos para refletir as respostas do CPC aos comentários do Bulletin 
Board do IFPUG. 
12. Aceitar informações que entram pela fronteira: Acrescentados dois novos 
exemplos para refletir as respostas do CPC aos comentários do Bulletin Board do 
IFPUG. 
13. Classificação (Dados são re-classificados ou re-arranjados): Acrescentados dois 
novos exemplos para refletir as respostas do CPC aos comentários do Bulletin 
Board do IFPUG. 
 
Em Considerações e Dicas, foi incluída discussão relativa a Funções excluídas, e as dicas sobre 
CGSs foram movidas para o Apêndice C, onde as CGSs e VAF opcionais são contemplados. 
 
Na seção Melhoria versus Manutenção, qualquer referência as CGSs foi precedida com 
“opcional”. 
Parte 2, Capítulo 5: Atividade de Conver
 são de Dados (novo capítulo) 
Este novo capítulo contempla a funcionalidade a ser avaliada quando existem requisitos para 
migrar ou converter dados em conjunto com o novo desenvolvimento ou projeto melhoria, ou 
para migrar uma aplicação para uma plataforma diferente. A Parte 4 do CPM provê outros 
exemplos de Funções de Dados e de Funções de Transação para conversão de dados. 
Parte 3: Exemplos 
Em todos os capítulos na Parte 3 (agora Parte 4) foram feitas revisões nos quadros de regras 
nesta seção para estar consistente com as alterações de redação nas regras de funções de dados, 
processo elementar e função de transação. Detalhes adicionais são indicados por capítulo abaixo.  
Parte 3, Capítulo 1: Exemplos de Contagem de Funções de Dados  
 Exem
plo de ALI: Dados de Auditoria para consulta e Relatórios – Removidas referências a 
Manutenção de Segurança do Funcionário do Diagrama de Fluxo de Dados, pois estava 
confuso e não explicado adequadamente  
 Exemplo de ALI: Definição de relatório  – Adicionada explicação esclarecendo porque a 
Definição de relatório não é  uma instância de dados de código 
 Exemplo de ALI: Dados Compartilhados por aplicações– Exemplo esclarecido para garantir 
entendimento que a segurança descrita neste exemplo não é aplicação de segurança  (ou seja, 
determinando o que o usuário pode acessar na aplicação) 
 Exemplo de AIE: Fornecendo Dados para outras Aplicações – Adicionada explicação 
esclarecendo porque a  Conversão de moeda corrente não é uma instância de dados de código 
 Exemplo de AIE: Aplicação de Help  – Adicionada explicação, esclarecendo porque o  Help 
não é uma instância de dados de código; e também explicando porque  a Janela de Help e o 
Help de campo são Funções de Dados separadas 
B-8 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 