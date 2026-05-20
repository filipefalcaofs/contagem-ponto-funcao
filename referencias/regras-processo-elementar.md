# Regras de Processo Elementar e Funções Transacionais (Parte 1)

Extraído do CPM IFPUG 4.3.1 PT-BR (páginas 48–56).


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