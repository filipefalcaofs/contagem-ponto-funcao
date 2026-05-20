# Parte 3 — Dados de Código

Extraído do CPM IFPUG 4.3.1 PT-BR.

---
## Página 290

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
 
Passo 1 Identificar as Funções de Dados (para a aplicação de RH) 
 Determine se as informações de Funcionário são uma função de dados para a 
aplicação RH. A tabela a seguir mostra o resumo da análise. 
Regras de Identificação de Função de 
Dados 
A regra se aplica? 
1. Identifique todos os dados ou 
informações de controle logicamente 
relacionados e reconhecidos pelo 
usuário dentro do escopo da contagem. 
Funcionário. 
2. Exclua entidades que não são mantidas 
por qualquer aplicação. 
Não existem entidades deste tipo. 
3. Agrupe entidades relacionadas que são 
entidades dependentes.  
Não existem entidades deste tipo. 
4. Exclua as entidades referidas como 
Dados de Código. 
Não existem entidades deste tipo. 
 
Passo 2 Classificar as Funções de Dados (para a aplicação de RH) 
 Determine se informações de Funcionário é classificada como um ALI para a 
aplicação de RH. 
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados 
são mantidos pela aplicação sendo 
medida 
A função de dados Funcionário é mantida 
dentro da aplicação de RH. 
2. Classificar como um AIE, se:  Classificado como um ALI; 
consequentemente, nenhum AIEs são 
identificados. 
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
 
 
 A análise mostra que as informações do Funcionário são um ALI para a 
aplicação de RH. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-32 
---
## Página 291

Parte 4 - Exemplos  2BExemplos de Contagem de ALI 
 
Passo 3 Contar os DERs (para a aplicação de RH) 
 Para os DERs, observe cada atributo associado com o ALI Funcionário na 
aplicação de RH e determine se as regras de contagem de DER se aplicam.   
Informações do Funcionário incluem: 
 Código do Funcionário 
 Nome do Funcionário 
 Endereço de correspondência do Funcionário  (Andar, Código do Edifício, 
Rua, Cidade, Estado e CEP) 
 Faixa Salarial do Funcionário 
 Cargo do Funcionário 
 Data elegível para Aposentadoria 
 Nível de Autorização de Segurança Organizacional 
 
 
 A análise dos DERs para o ALI Funcionário na aplicação de RH é mostrada 
abaixo: 
Regra de Contagem de DER para Função 
de Dados 
A regra se aplica?   
1. Conte um DER para cada atributo único 
reconhecido pelo usuário, não repetido 
mantido em ou recuperado de uma 
função de dados através da execução de 
todos os processos elementares dentro do 
escopo da contagem. 
Os seguintes atributos satisfazem esta regra: 
 Código do Funcionário  
 Nome do Funcionário 
 Endereço de Correspondência do 
Funcionário 
 Faixa Salarial do Funcionário 
 Cargo do Funcionário 
 Data elegivel para aposentadoria 
 Nível de Segurança Organizacional 
2. Conte somente aqueles DERs sendo 
usado pela aplicação sendo medida 
quando duas ou mais aplicações mantém 
e/ou referenciam a mesma função de 
dados. 
Somente o Código do Funcionário, Nome do 
Funcionário, Endereço de Correspondência 
do Funcionário, Faixa Salarial do 
Funcionário, Cargo do Funcionário, e Data 
elegível para aposentadoria são usados pela 
aplicação de RH. O atributo Nivel de 
Segurança Organizacional não é contado 
como DER, porque ele não é usado pela 
aplicação de RH. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-33 
---
## Página 292

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
 
3. Conte um DER para cada atributo 
requerido pelo usuário para estabelecer 
um relacionamento com outra função de 
dados. 
Não existem atributos deste tipo. 
4. Revise os atributos relacionados para 
determinar se eles são agrupados e 
contados como um único DER ou se eles 
são contados como múltiplos DERs; o 
agrupamento dependerá de como os 
processos elementares usam os atributos 
dentro da aplicação. 
Endereço de correspondência do empregado 
é contado como um único DER. 
 
  
Passo 4 Contar os RLRs (para a aplicação de RH) 
 Para os RLRs, identifique os subgrupos baseado nas regras de contagem de 
RLR. 
Regras de Contagem de RLR A regra se aplica?   
1. Conte um RLR para cada função de 
dados (isto é, por default, cada 
função de dados tem um subgrupo 
de DERs para ser contado como um 
RLR). 
Conte um RLR para o ALI Funcionário. 
2. Conte um RLR adicional para cada 
subgrupo lógico de DERs a seguir 
(dentro da função de dados) que 
contém mais do que um DER: 
 
 Entidade associativa com 
atributos não-chave 
Não existem entidades deste tipo. 
 Subtipo (subtipo diferente do 
primeiro subtipo) e  
Não existem entidades deste tipo. 
 Entidade atributiva, em um 
relacionamento diferente de 1-
1 mandatório. 
Não existem entidades deste tipo. 
  
  
 O total de RLR e DER para o ALI Funcionário na aplicação de RH é 
mostrado na tabela a seguir.   
RLRs DERs 
 Grupo de informações de Funcionário  Código do Funcionário 
 Nome do Funcionário 
 Endereço de Correspondência do Funcionário 
 Faixa Salarial do Funcionário 
 Cargo do Funcionário 
 Data elegivel para aposentadoria 
Total   1 RLR Total 6 DERs 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-34 
---
## Página 293

Parte 4 - Exemplos  2BExemplos de Contagem de ALI 
 
Passo 5 Determinar a Complexidade Funcional (para a aplicação de RH) 
 1 RLR e 6 DERs Complexidade é Baixa 
 
Passo 6 Determinar o Tamanho Funcional (para a aplicação de RH) 
 Tamanho Funcional de 1 ALI Baixo 7 PF 
 
 
Passo 1 Identificar as Funções de Dados (para a aplicação de Distribuição de 
Correspondência) 
 Determine se as informações de Funcionário são uma função de dados para a 
aplicação Distribuição de Correspondência.  A tabela a seguir mostra o 
resumo da análise. 
Regras de Identificação de Função de 
Dados 
A regra se aplica? 
1. Identifique todos os dados ou 
informações de controle logicamente 
relacionados e reconhecidos pelo 
usuário dentro do escopo da contagem. 
Funcionário. 
2. Exclua entidades que não são mantidas 
por qualquer aplicação. 
Não existem entidades deste tipo. 
3. Agrupe entidades relacionadas que são 
entidades dependentes.  
Não existem entidades deste tipo. 
4. Exclua as entidades referidas como 
Dados de Código. 
Não existem entidades deste tipo. 
5. Exclua entidades que não possuem 
atributos requeridos pelo usuário. 
Não existem entidades deste tipo. 
6. Remova as entidades associativas que 
contém atributos adicionais não 
requeridos pelo usuário e entidades 
associativas que contém somente 
chaves estrangeiras; agrupe os 
atributos chave estrangeira com as 
entidades primárias. 
Não existem entidades deste tipo. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-35 
---
## Página 294

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
 
Passo 2 Classificar as Funções de Dados (para a aplicação Distribuição de 
Correspondência) 
 Determine se informações de Funcionário é classificada como um ALI para a 
aplicação Distribuição de Correspondência. 
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados 
são mantidos pela aplicação sendo 
medida 
A função de dados Funcionário é mantida 
dentro da aplicação Distribuição de 
Correspondência. 
2. Classificar como um AIE, se: Classificado como um ALI; 
consequentemente, não existem AIEs 
identificados. 
 É referenciado, mas não mantido, 
pela aplicação sendo medida e 
 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
 
 
 A análise mostra que as informações do Funcionário são um ALI para a 
aplicação Distribuição de Correspondência. 
  
Passo 3 Contar os DERs (para a aplicação Distribuição de Correspondência) 
 Para os DERs, observe cada atributo associado com o ALI Funcionário na 
aplicação Distribuição de Correspondência e determine se as regras de 
contagem de DER se aplicam. 
Informações do Funcionário incluem: 
 Código do Funcionário 
 Nome do Funcionário 
 Endereço de correspondência do Funcionário (Andar, Código do Edifício, 
Rua, Cidade, Estado e CEP; na aplicação de Distribuição de 
Correspondência os atributos Andar e Código do Edifício são usados 
separadamente.) 
 Faixa Salarial do Funcionário 
 Cargo do Funcionário 
 Data elegível para Aposentadoria 
 Nível de Autorização de Segurança Organizacional 
 
 A análise dos DERs para as informações do Funcionário para a aplicação 
Distribuição de Correspondência é mostrada abaixo: 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-36 
---
## Página 295

Parte 4 - Exemplos  2BExemplos de Contagem de ALI 
Regra de Contagem de DER para Função 
de Dados 
A regra se aplica?   
1. Conte um DER para cada atributo único 
reconhecido pelo usuário, não repetido 
mantido em ou recuperado de uma 
função de dados através da execução de 
todos os processos elementares dentro do 
escopo da contagem. 
Os seguintes atributos satisfazem esta regra: 
 Código do Funcionário  
 Andar 
 Código do Edifício 
 
2. Conte somente aqueles DERs sendo 
usado pela aplicação sendo medida 
quando duas ou mais aplicações mantém 
e/ou referenciam a mesma função de 
dados. 
Somente o Código do Funcionário, Andar, e 
Código do Edifício são usados pela aplicação 
Distribuição de Correspondência. 
3. Conte um DER para cada atributo 
requerido pelo usuário para estabelecer 
um relacionamento com outra função de 
dados. 
Não existem atributos deste tipo. 
4. Revise os atributos relacionados para 
determinar se eles são agrupados e 
contados como um único DER ou se eles 
são contados como múltiplos DERs; o 
agrupamento dependerá de como os 
processos elementares usam os atributos 
dentro da aplicação. 
Não existem atributos deste tipo. Embora o 
Endereço de Correspondência do 
Funcionário tenha sido considerado um 
único atributo na aplicação de RH, são 
contados dois atributos separados  (Andar e 
Código do Edifício) na aplicação de 
Distribuição de Correspondência. 
 
Passo 4 Contar os RLRs (para a aplicação Distribuição de Correspondência) 
 Para os RLRs, identifique os subgrupos baseado nas regras de contagem de 
RLR. 
Regras de Contagem de RLR A regra se aplica?   
1. Conte um RLR para cada função de 
dados (isto é, por default, cada 
função de dados tem um subgrupo 
de DERs para ser contado como um 
RLR). 
Conte um RLR para o ALI Funcionário. 
2. Conte um RLR adicional para cada 
subgrupo lógico de DERs a seguir 
(dentro da função de dados) que 
contém mais do que um DER: 
 
 Entidade associativa com 
atributos não-chave 
Não existem entidades deste tipo. 
 Subtipo (subtipo diferente do 
primeiro subtipo) e  
Não existem entidades deste tipo. 
 Entidade atributiva, em um 
relacionamento diferente de 1-
1 mandatório. 
Não existem entidades deste tipo. 
  
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-37 
---
## Página 296

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-38 
 O total de RLR e DER para o ALI Funcionário na aplicação de Distribuição 
de Correspondência é mostrado na tabela a seguir.   
RLRs DERs 
 Grupo de informações do Funcionário  Código do Funcionário 
 Andar 
 Código do Edifício 
  
Total   1 RLR Total 3 DERs 
 
 
Passo 5 Determinar a Complexidade Funcional (para a aplicação Distribuição de 
Correspondência) 
 1 RLRs e 3 DERs Complexidade é Baixa 
 
Passo 6 Determinar o Tamanho Funcional (para a aplicação Distribuição de 
Correspondência) 
 Tamanho Funcional de 1 ALI Baixo 7 PF 
---
## Página 297

 
 
 
 
 
 Exemplos de Contagem de AIE 
Introdução Esta seção utiliza a aplicação de Recursos Humanos (RH) juntamente com a 
aplicação de Segurança e uma aplicação de Pensão para ilustrar 
procedimentos utilizados para medir funções de dados.  Além desta seção, 
outros exemplos estão nos Estudos de Caso que são parte da documentação 
complementar do IFPUG. 
 
Conteúdo Esta seção inclui os seguintes exemplos: 
 
Tópico Page 
Resumo das Descrições dos Exemplos de Contagem de AIEs 1-40 
Exemplo: Referenciando dados de Outras Aplicações 1-41 
Exemplo: Referenciando dados de Uma Outra Aplicação 1-45 
Exemplo: Fornecendo Dados para Outras Aplicações 1-51 
Exemplo: Aplicação de Help 1-53 
Exemplo: Conversão de Dados 1-62 
Exemplo: Arquivo de Entrada de Transação 1-64 
Exemplo: Diferentes Usuários/Diferentes Visões do Usuário 1-66 
Exemplo: Múltipla utilização de Dados 1-71 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-39 
---
## Página 298

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
Resumo da Descrição dos Exemplos de AIEs 
 Os exemplos para AIEs são descritos na seguinte tabela:   
 
Exemplo Descrição Resumida Página 
Referenciando Dados de 
Outras Aplicações para 
gerar saída 
Este exemplo identifica AIEs para uma aplicação 
que referencia dados mantidos por outra 
aplicação. Os dados são utilizados para gerar uma 
saída externa. 
1-41 
Referenciando Dados de 
Outra Aplicação para 
utilizar como parte de 
um processo de entrada 
Este exemplo também mostra dados referenciados 
a partir de outra aplicação. Identifica AIEs para 
uma aplicação que referencia dados mantidos por 
outra aplicação para utilização em uma entrada 
externa.. 
1-45  
Fornecendo Dados para 
Outras Aplicações 
Este é outro exemplo de contagem de dados 
referenciados a partir de uma aplicação diferente. 
1-51 
Aplicação de Help Este é um exemplo de contagem de uma 
facilidade de Help dentro da aplicação de RH. 
1-53 
Conversão de Dados Este é um exemplo de contagem na conversão de 
uma nova aplicação. 
1-62 
Arquivo de Entrada de 
Transação 
Este exemplo aplica as regras de contagem de 
AIE para um arquivo de entrada de transação 
processado para incluir cargos para a aplicação de 
Recursos Humanos. 
1-64 
Diferentes Usuários / 
Diferentes Visões do 
Usuário 
Este exemplo mostra que a visão difere quando 
um AIE é utilizado por diversas aplicações. 
1-66 
Uso Múltiplo de Dados Este exemplo ilustra várias utilizações para o 
mesmo dado. 
1-71 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-40 
---
## Página 299

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
Exemplo: Referenciando Dados de Outras Aplicações 
Requisitos do 
Usuário 
O usuário deseja que o sistema de Recursos Humanos forneça a habilidade 
para: 
1. Incluir, consultar e listar  informações do Funcionário 
2. Interface com o sistema de Ativo Fi xo para recuperar informações de 
localização de cada edifício. A informação de localização inclui as 
informações de nome e descrição. 
  
Passo 1 Identificar as Funções de Dados  
 A partir dos requisitos do usuário, existem dois grupos de informações: 
 Informações do Funcionário 
 Informações de Localização 
A tabela a seguir mostra o resumo da análise para determinar se Informações 
do Funcionário é uma função de dados. 
 
Regras de Identificação de Função de 
Dados 
A regra se aplica? 
1. Identifique todos os dados ou 
informações de controle logicamente 
relacionados e reconhecidos pelo 
usuário dentro do escopo da contagem. 
Funcionário e Localização. 
2. Exclua entidades que não são mantidas 
por qualquer aplicação. 
Não existem entidades deste tipo. 
3. Agrupe entidades relacionadas que são 
entidades dependentes. 
Não existem entidades deste tipo. 
Funcionário e Localização são entidades 
independentes uma da outra. 
4. Exclua as entidades referidas como 
Dados de Código. 
Não existem entidades deste tipo. 
5. Exclua entidades que não possuem 
atributos requeridos pelo usuário. 
Não existem entidades deste tipo. 
6. Remova as entidades associativas que 
contém atributos adicionais não 
requeridos pelo usuário e entidades 
associativas que contém somente 
chaves estrangeiras; agrupe os 
atributos chave estrangeira com as 
entidades primárias. 
Não existem entidades deste tipo. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-41 
---
## Página 300

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
 Baseado na análise, Funcionário e Localização são identificadas como função 
de dados. 
 
 
Passo 2 Classificar as Funções de Dados (para informações do Funcionário) 
 Determinar se informações do Funcionário é classificada como um AIE para a 
aplicação RH.   
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados 
são mantidos pela aplicação sendo 
medida 
A função de dados Funcionário é mantida 
dentro da aplicação. 
2. Classificar como um AIE, se:  Classificada como um ALI; 
consequentemente, nenhum AIE é 
identificado. 
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
 
 Baseado na análise, as informações de Funcionário não são externas à 
aplicação de RH. Elas são mantidas internamente; portanto, não é um AIE. 
 
Passo 2 Classificar as Funções de Dados (para informações de Localização) 
 Determinar se as informações de Localização são classificadas como um AIE 
para a aplicação de RH. 
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados são 
mantidos pela aplicação sendo medida 
As informações de Localização não são 
mantidas na aplicação de RH. 
2. Classificar como um AIE, se:   
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
A função de dados Localização é 
referenciada, mas não mantida, pela 
aplicação de RH para uso no relatório de 
funcionários. 
 É identificado em um ALI em uma 
ou mais outras aplicações 
Inicialmente, não está claro se as 
informações de Localização são mantidas 
em outra aplicação. Depois de perguntar aos 
usuários, fomos informados que eles 
incluem a informação na aplicação de Ativo 
Fixo utilizando uma tela. Portanto, as 
informações de Localização são um ALI 
para a aplicação Ativo Fixo e um AIE para a 
aplicação de RH. 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-42 
---
## Página 301

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
 
 
 Baseado na análise, as informações de Localização são classificadas como um 
AIE para a aplicação de RH.   
 
Passo 3 Contar os DERs (para Localização) 
 Para os DERs, observe cada atributo associado com o AIE Localização e 
determine se as regras de contagem de DER se aplicam.   
Os atributos a seguir são referenciados a partir do AIE Localização: 
 Código do Edifício 
 Nome do Edifício 
 Descrição do Edifício 
 Linha 1 
 Linha 2 
 Linha 3 
 Cidade 
 Estado 
 País 
 
 A tabela a seguir mostra a análise resumida da contagem de DER. 
Regra de Contagem de DER para Função 
de Dados 
A regra se aplica?   
1. Conte um DER para cada atributo único 
reconhecido pelo usuário, não repetido 
mantido em ou recuperado de uma 
função de dados através da execução de 
todos os processos elementares dentro do 
escopo da contagem. 
Código do Edifício, Nome do Edifício, 
Descrição do Edifício, Cidade, Estado e País. 
As linhas repetidas de Descrição do Edifício 
são contadas como um único DER. 
2. Conte somente aqueles DERs sendo 
usado pela aplicação sendo medida 
quando duas ou mais aplicações mantém 
e/ou referenciam a mesma função de 
dados. 
Não existem atributos deste tipo.  
3. Conte um DER para cada atributo 
requerido pelo usuário para estabelecer 
um relacionamento com outra função de 
dados. 
Não existem atributos deste tipo.  
4. Revise os atributos relacionados para 
determinar se eles são agrupados e 
contados como um único DER ou se eles 
são contados como múltiplos DERs; o 
agrupamento dependerá de como os 
processos elementares usam os atributos 
dentro da aplicação. 
Não existem atributos deste tipo.  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-43 
---
## Página 302

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
 
Passo 4 Contar os RLRs (para Localização) 
 Para os RLRs, identifique os subgrupos baseado nas regras de contagem de 
RLR. 
Regras de Contagem de RLR A regra se aplica?   
1. Conte um RLR para cada função de 
dados (isto é, por default, cada 
função de dados tem um subgrupo 
de DERs para ser contado como um 
RLR). 
Conte um RLR para o AIE Localização. 
2. Conte um RLR adicional para cada 
subgrupo lógico de DERs a seguir 
(dentro da função de dados) que 
contém mais do que um DER: 
 
 Entidade associativa com 
atributos não-chave 
Não existem entidades deste tipo. 
 Subtipo (subtipo diferente do 
primeiro subtipo) e  
Não existem entidades deste tipo. 
 Entidade atributiva, em um 
relacionamento diferente de 1-
1 mandatório. 
Não existem entidades deste tipo. 
  
 
 O total de RLR e DER para o AIE Localização é mostrado na tabela a 
seguir. 
RLRs DERs 
 dados de Localização  Código do Edifício 
 Nome do Edifício 
 Descrição do Edifício (linhas repetidas) 
  Cidade 
  Estado 
  País 
Total   1 RLR Total 6 DERs 
 
Passo 5 Determinar a Complexidade Funcional (para Localização) 
 1 RLR e 6 DERs Complexidade é Baixa 
 
Passo 6 Determinar o Tamanho Funcional (para Localização) 
 Tamanho Funcional de 1 AIE Baixo 5 PF 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-44 
---
## Página 303

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
Exemplo: Referenciando Dados de uma Outra Aplicação 
Requisitos do 
Usuário 
O usuário requer que a aplicação de Recursos Humanos forneça as seguintes 
habilidades: 
 Todos os funcionários horistas devem ser pagos em dólares dos Estados 
Unidos. 
 Quando o usuário incluir ou alterar informações do funcionário, a 
aplicação de Recursos Humanos deve acessar a o sistema Monetário para 
recuperar a taxa de conversão. Depois de recuperar a taxa de conversão, 
a aplicação de RH converte a taxa-hora padrão da localização do 
funcionário para a taxa-hora dos EUA utilizando o seguinte cálculo: 
larEUATaxaHoraDosãoTaxaConver
drãoTaxaHoraPa   
  
Modelo de 
Dados 
O diagrama a seguir mostra os relacionamentos para este exemplo.  
 
Sistema Monetário
TAXA DE 
CONVERSÃO
Dependente
Aplicação de RH
FUNC_ASSALARIADO
FUNC_HORISTA
FUNCIONÁRIO
 
 
 
Legend
a: 
Relacionamento Obrigatório de Um-para-muitos
Relacionamento Opcional de Um-para-muitos
Entidade Atributiva
Entidade Tipo
Entidade Subtipo
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-45 
---
## Página 304

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
 
 As informações de conversão de moeda incluem: 
MOEDA 
Taxa_Base_Para_Conversão_Moeda 
País 
 
  
Passo 1 Identificar as Funções de Dados 
 Para os requisitos, existem dois grupos de informações: 
 Informações de Conversão de Moeda 
 Informações de Funcionário 
A tabela a seguir mostra o resumo da análise para determinar se Informações 
de Conversão de Moeda é uma função de dados.   
Regras de Identificação de Função de 
Dados 
A regra se aplica? 
1. Identifique todos os dados ou 
informações de controle logicamente 
relacionados e reconhecidos pelo 
usuário dentro do escopo da contagem. 
Conversão de Moeda, Funcionário e 
Dependente. 
2. Excluir entidades que não são mantidas 
por qualquer aplicação. 
Não existem entidades deste tipo. 
3. Agrupe entidades relacionadas que são 
entidades dependentes. 
A entidade Moeda de Conversão é 
independente das outras entidades. 
Dependente é uma entidade dependente da 
entidade Funcionário. 
4. Exclua as entidades referidas como 
Dados de Código. 
Embora Conversão de Moeda possa parecer 
uma instância de dados de código, Código do 
País e Taxa de Conversão não são 
substituíveis (isto é, não podem ser 
substituído um pelo outro). Informações de 
Conversão de Moeda também mudam 
regularmente, de modo que não satisfazem os 
critérios de serem essencialmente estáticos.  
5. Exclua entidades que não possuem 
atributos requeridos pelo usuário. 
Não existem entidades deste tipo. 
6. Remova as entidades associativas que 
contém atributos adicionais não 
requeridos pelo usuário e entidades 
associativas que contém somente 
chaves estrangeiras; agrupe os 
atributos chave estrangeira com as 
entidades primárias. 
Não existem entidades deste tipo. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-46 
---
## Página 305

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
 
 Baseado na análise, Conversão de Moeda e Funcionário são identificadas 
como função de dados. Dependente não é uma função de dados própria, mas é 
parte da função de dados Funcionário. 
 
 
Passo 2 Classificar as Funções de Dados (para Funcionário) 
 A tabela a seguir mostra a análise para determinar se informações do 
Funcionário é classificada como um AIE.   
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados 
são mantidos pela aplicação sendo 
medida 
Informações do Funcionário são mantidas pela 
aplicação de RH. 
2. Classificar como um AIE, se:   
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
Classificado como um ALI; 
consequentemente, nenhum AIEs são 
identificados. 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
 
 Baseado na análise, as informações de Funcionário não são externas à 
aplicação de RH. Elas são mantidas internamente; portanto, não são um AIE. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-47 
---
## Página 306

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
 
Passo 2 Classificar as Funções de Dados (para Conversão de Moeda) 
 A tabela a seguir mostra a análise para determinar se informações de 
Conversão de Moeda são classificadas como AIE.   
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados são 
mantidos pela aplicação sendo medida 
Conversão de Moeda não é mantida pela 
aplicação de RH. 
2. Classificar como um AIE, se:  
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
A função de dados Conversão de Moeda é 
referenciada pela aplicação de RH para uso 
no cálculo da remuneração do empregado. 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
Embora Conversão de Moeda possa parecer 
uma instância de dados de código, Código 
do País e Taxa de Conversão não são 
substituíveis (isto é, não podem ser 
substituído um pelo outro). Informações de 
Conversão de Moeda também mudam 
regularmente, de modo que não satisfazem 
os critérios de serem essencialmente 
estáticos. 
 
 
 Como a aplicação Sistema Monetário fornece a taxa de conversão para a 
aplicação de RH, o grupo de dados de conversão de moeda é um AIE para a 
aplicação de RH. 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-48 
---
## Página 307

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
 
Passo 3 Contar os DERs (para Conversão de Moeda) 
 Para os DERs, observe cada atributo associado com o AIE Conversão de 
Moeda e determine se as regras de contagem de DER se aplicam.  A tabela a 
seguir mostra o resumo da análise da contagem de DER. 
Regra de Contagem de DER para Função 
de Dados 
A regra se aplica?   
1. Conte um DER para cada atributo único 
reconhecido pelo usuário, não repetido 
mantido em ou recuperado de uma 
função de dados através da execução de 
todos os processos elementares dentro do 
escopo da contagem. 
Taxa de Conversão, Moeda. 
2. Conte somente aqueles DERs sendo 
usado pela aplicação sendo medida 
quando duas ou mais aplicações mantém 
e/ou referenciam a mesma função de 
dados. 
Todos os atributos são referenciados pela 
aplicação de RH. 
3. Conte um DER para cada atributo 
requerido pelo usuário para estabelecer 
um relacionamento com outra função de 
dados. 
Não existem atributos deste tipo. 
4. Revise os atributos relacionados para 
determinar se eles são agrupados e 
contados como um único DER ou se eles 
são contados como múltiplos DERs; o 
agrupamento dependerá de como os 
processos elementares usam os atributos 
dentro da aplicação. 
Não existem atributos deste tipo. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-49 
---
## Página 308

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
 
 
Passo 4 Contar os RLRs (para Conversão de Moeda) 
 Para os RLRs, identifique os subgrupos baseado nas regras de contagem de 
RLR. 
Regras de Contagem de RLR A regra se aplica?   
1. Conte um RLR para cada função de 
dados (isto é, por default, cada 
função de dados tem um subgrupo de 
DERs para ser contado como um 
RLR). 
Conte um RLR para o AIE Conversão de Moeda.
2. Conte um RLR adicional para cada 
subgrupo lógico de DERs a seguir 
(dentro da função de dados) que 
contém mais do que um DER: 
 
 Entidade associativa com 
atributos não-chave 
Não existem entidades deste tipo. 
 Subtipo (subtipo diferente do 
primeiro subtipo) e  
Não existem entidades deste tipo. 
 Entidade atributiva, em um 
relacionamento diferente de 1-1 
mandatório. 
Não existem entidades deste tipo. 
   
 O total de RLR e DER para o AIE informações de Conversão de Moeda é 
mostrado na tabela a seguir.   
RLRs DERs 
 Informações de Conversão  Taxa de Conversão 
 Moeda 
Total  1 RLR Total 2 DERs 
 
Passo 5 Determinar a Complexidade Funcional (para Conversão de Moeda) 
 1 RLR e 2 DERs Complexidade é Baixa 
 
Passo 6 Determinar o Tamanho Funcional (para Conversão de Moeda) 
 Tamanho Funcional de 1 AIE Baixo 5 PF 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-50 
---
## Página 309

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
Exemplo: Fornecendo Dados para Outras Aplicações 
Requisitos do 
Usuário 
O usuário tem os seguintes requisitos para o sistema Monetário:  
 Manter taxa de conversão de outras moedas para o dólar americano. 
 Fornecer uma interface para habilitar outras aplicações, como Recursos 
Humanos, a recuperar informação de conversão. 
  
Passo 1 Identificar as Funções de Dados 
 Para este exemplo, determinar se informações de Conversão de Moeda é uma 
função de dados para a aplicação Sistema Monetário.  A tabela a seguir 
mostra o resumo da análise.   
Regras de Identificação de Função de 
Dados 
A regra se aplica? 
1. Identifique todos os dados ou 
informações de controle logicamente 
relacionados e reconhecidos pelo usuário 
dentro do escopo da contagem. 
Conversão de Moeda. 
2. Exclua entidades que não são mantidas 
por qualquer aplicação. 
Não existem entidades deste tipo. 
3. Agrupe entidades relacionadas que são 
entidades dependentes. 
Não existem entidades deste tipo. 
4. Exclua as entidades referidas como 
Dados de Código. 
Embora Conversão de Moeda possa parecer 
uma instância de dados de código, Código 
do País e Taxa de Conversão não são 
substituíveis (isto é, não podem ser 
substituído um pelo outro). Informações de 
Conversão de Moeda também mudam 
regularmente, de modo que não satisfazem 
os critérios de serem essencialmente 
estáticos. 
5. Exclua entidades que não possuem 
atributos requeridos pelo usuário. 
Não existem entidades deste tipo. 
6. Remova as entidades associativas que 
contém atributos adicionais não 
requeridos pelo usuário e entidades 
associativas que contém somente chaves 
estrangeiras; agrupe os atributos chave 
estrangeira com as entidades primárias. 
Não existem entidades deste tipo. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-51 
---
## Página 310

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
 
Passo 2 Classificar as Funções de Dados (para Conversão de Moeda) 
 A tabela a seguir mostra a análise para determinar se informações de 
Conversão de Moeda é classificada como um AIE.   
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados 
são mantidos pela aplicação sendo 
medida 
A aplicação Sistema Monetário mantém os 
dados de Conversão de Moeda através de 
transações a partir de um serviço online. 
2. Classificar como um AIE, se: Classificado como um ALI; 
consequentemente, nenhum AIEs são 
identificados. 
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
 
 As informações de Conversão de Moeda não são externas à aplicação Sistema 
Monetário; portanto, ela é contada como um ALI ao invés de um AIE para a 
aplicação Sistema Monetário. Veja o exemplo anterior neste capítulo para 
rever como a referência a Conversão de Moeda pode ser contada como um 
AIE. 
 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-52 
---
## Página 311

Parte 4 - Exemplos  3BExemplos de Contagem de AIE 
Exemplo: Aplicação de Help  
Requisitos do 
Usuário 
O usuário requer ao sistema de Help fornecer: 
1. A habilidade de descrever a forma como cada tela é utilizada para 
realizar cada função de negócios disponível na mesma. 
2. A habilidade de alterar o Help de tela. 
3. A habilidade para estabelecer uma definição, valores default, e valores 
válidos para cada atributo na aplicação de Recursos Humanos. 
4. A habilidade de alterar o Help de campo. 
5. A habilidade para a aplicação de Recursos Humanos recuperar o Help de 
tela e de campo para apresentação. 
O Help de tela e Help de campo são mantidos independentemente. Pode 
existir uma entrada em um tipo de help sem existir em outro. 
 
 
Diagrama de 
Fluxo de 
Dados 
O diagrama a seguir ilustra o fluxo de dados para este exemplo.   
  
 
Usuário 
  HELP DE TELA 
Alterar 
Help de campo
Incluir Help de Tela
cod.tela, descrição do help  
Alterar help de tela 
A lterar help de campo Alterações nas infor mações 
de Help  de campo 
2.4
HELP DE CAMPO Incluir help de campo 
Incluir Help de 
camp o 
2.3 cod.tela, cod.campo, descrição, 
Valores válidos, valores default 
Alterar 
2.2 
Help de Tela 
Incluir
2.1 
Help de Tela 
Aplicação
de 
Re curs os 
Huma nos 
 
cod.tela,
cod.campo, 
Descrição, 
Valores válidos, 
Valores default 
Alterações nas 
informações de 
Help de tela 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-53 
---
## Página 312

3BExemplos de Contagem de AIE  Parte 4 - Exemplos 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-54 
Legend:
User or Application
Data Stored F
P
low of Data
rocess
 
 
  
 
 
 
rocess
Fluxo de Daepósito de Da
suário ou Aplicação P o 
dos D dos 
U
Legenda: 