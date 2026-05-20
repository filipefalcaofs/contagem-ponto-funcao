# Parte 3 — Atividade de Conversão

Extraído do CPM IFPUG 4.3.1 PT-BR.

---
## Página 249

  Parte 3 Capítulo 5 
 
 
 
 
 
 
 
 
Atividade de Conversão de Dados 
 
Introdução Esta seção aborda a funcionalidade que será avaliada quando existem 
requisitos para migrar ou converter os dados em conjunto com um novo 
desenvolvimento ou projeto de melhoria ou para trocar uma aplicação para 
uma plataforma diferente. Parte 4 do CPM fornece outros exemplos de 
funções de dados e funções transacionais para conversão de dados.  
 
Conteúdo Este capítulo irá discutir o seguinte como ilustrações de diferentes cenários de 
conversão: 
 
Tópico Página 
Funcionalidade de Conversão 5-2 
Cenário 1: Conversão de Dados em Projetos de Melhoria 5-3 
Cenário 2: Conversão de Dados co m AIEs Referenciados 5-3 
Cenário 3: Atribuição de Valores Padrão 5-3 
O Que Não É Funcionalidade de Conversão 5-4 
Resumo 5-4  
Janeiro 2010 Manual de Práticas de Contagem de Pontos de Função 5-1 
---
## Página 250

0BAtividade de Conversão de Dados  Parte 3 – Práticas de Contagem 
Funcionalidade de Conversão 
 Conversão de dados da aplicação é baseada na visão do usuário dos dados. Os 
usuários identificam os requisitos de dados com base em necessidades 
distintas, tais como Emprego, Contabilidade, Clientes ou Dados de 
Inventário. A visão do usuário destes dados abrange todos os atributos 
associados com o grupo de dados, tal como definido na aplicação. Este grupo 
de dados reconhecível pelo usuário e os dados associados atributos tornam-se 
a base para um grupo lógico de dados que cumpre uma exigência específica 
do usuário. Este é um arquivo lógico que exige que todos os seus atributos de 
dados devem ser mantidos como parte do todo (ligados e não independentes).  
 
Atributos adicionais podem ser necessários por causa de exigências de 
negócios novas ou alteradas. Como parte da melhoria, pode ser necessário 
para converter e popular os atributos de dados adicionados como parte do 
projeto de melhoria. A visão do processo de conversão baseia-se na aplicação 
original, os arquivos lógicos que estão sendo convertidos e os requisitos de 
dados da nova aplicação.  
 
O processo de conversão é executado contra todos os dados como visto pelo 
usuário para criar um arquivo lógico atualizado que cumpre os requisitos 
específicos do usuário para os novos / convertido dados da aplicação. 
 
Aplicar as regras de identificação de PE padrão para identificar a 
funcionalidade de conversão.  O processo elementar inclui todos os relatórios 
de exceção, os relatórios de erros, relatórios de conversão ou relatórios de 
controle necessários para garantir a integridade dos dados que estão sendo 
convertidos. Os ALIs da aplicação nova ou alterada, são populados com os 
dados convertidos e os requisitos de usuário determinam o que é exigido a 
partir da aplicação antiga para cumprir os requisitos funcionais do usuário do 
projeto. 
 
5-2 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 
---
## Página 251

Parte 3 – Práticas de Contagem  0BAtividade de Conversão de Dados 
Cenário 1: Conversão de Dados em Projetos de Melhoria 
 O projeto envolve a integrar em uma aplicação corporativa a função 
Habilidade em RH que uma divisão da empresa já tinha implementado como 
uma aplicação stand-alone. Há um requisito para capturar uma única vez 
todos os dados existentes de habilidade e preencher os dados existentes 
atributos em um ALI em um aplicativo de RH existente. Os dados de 
habilidades existentes a serem importados serão contados como uma EE. Há 
um relatório de controle e um relatório de erro que são gerados para garantir a 
integridade da migração. Este processo será executado como parte da 
implantação da nova funcionalidade. Há um processo elementar para a carga 
inicial dos novos atributos de dados em um ALI do sistema de RH, incluindo 
os relatórios de controle e de erro. O processo de conversão será contado 
como uma EE, que será incluído no Tamanho Funcional do Projeto de 
Melhoria, mas não será adicionado ao Tamanho Funcional da Aplicação 
porque o processo é executado uma única vez. 
Cenário 2: Conversão de Dados com AIEs Referenciados 
 O usuário solicitou que um ALI (ou parte de um ALI) seja populado de um 
ALI de outra aplicação. Nesse exemplo, foi solicitado validar os dados com 
um outro ALI de uma terceira aplicação. Isso é especificado como um 
processo que será executado uma única vez e os dados referenciados na 
terceira aplicação não serão utilizados no futuro. 
 
Os atributos a serem carregados servem como uma transação de entrada para 
popular o ALI que está recebendo e será contada como uma EE. Os dados 
referenciados na terceira aplicação para validação serão contados como um 
AIE e um ALR adicional. O ALI que está recebendo também será 
considerado como um ALR. Tanto a EE quanto o AIE devem ser incluídas na 
medição do projeto mas não devem ser adicionados ao tamanho funcional da 
aplicação. 
Cenário 3: Atribuição de Valores Padrão 
 Um projeto de melhoria solicita a inclusão de um DER em um ALI existente. 
O novo DER será populado com um valor padrão específico. Embora o ALI e 
qualquer transação modificada forem contadas como alteradas, não é contada 
uma funcionalidade de conversão. Nenhum dado atravessa a fronteira para 
estabelecer o valor padrão. 
Janeiro 2010 Manual de Práticas de Contagem de Pontos de Função 5-3 
---
## Página 252

0BAtividade de Conversão de Dados  Parte 3 – Práticas de Contagem 
5-4 Manual de Práticas de Contagem de Pontos de Função Janeiro 2010 
O Que Não É Funcionalidade de Conversão 
 Esta seção descreve vários casos que não são considerados Conversões..  
 Não conte atualizações de software devido à instalação de uma versão 
revista de pacotes de fornecedores como funcionalidade de conversão. 
 Não conte a migração de uma aplicação para uma nova plataforma 
como uma funcionalidade de conversão. 
 Não conte a conversão de dados realizada através de um utilitário de 
carga existente. Nenhuma funcionalidade foi desenvolvida para 
realizar a conversão. 
 Mesmo que um AIE para a aplicação que está sendo medida é 
alterado, não pode haver qualquer funcionalidade de conversão. 
Apenas a aplicação que tem contada a função de dados como um ALI 
pode contar com a funcionalidade de conversão. 
Resumo 
 Quando um ALI é adicionado ou modificado, existe a possibilidade que um 
processo de conversão possa ser solicitado para popular o novo ALI ou 
DER(s) em um ALI existente. Parte da análise é identificar o que está 
atravessando a fronteira da aplicação. No caso de novos desenvolvimentos, 
o(s) depósito(s) de dado(s) existente(s) ou ALI(s) do(s) sistema(s) sendo 
substituídos é considerado como cruzando a fronteira da aplicação. Quando 
uma melhoria envolve alterações em ALI e uma lógica de processamento é 
solicitada para popular o novo atributo (ex.: validações, comparações lógicas, 
etc.), o ALI existente pode ser considerado como cruzando a fronteira da 
aplicação com uma EE. Se um novo atributo em um ALI é populado somente 
com um valor padrão ou nulo, a conversão não deve ser contata porque nada 
atravessa a fronteira da aplicação.  
 
---
## Página 253

Parte 3 – Práticas de Contagem Índice 
 
 
 
 
 
 
 
 
 
Índice da Parte 3 
 
 
 
 
 
A 
Aproximação, 3-4 
Arquivo, 2-4 
definição, 3-3 
Arquivos de Índice, 2-9 
Arquivos de Sistema, 2-4 
Arquivos Lógicos 
Processo para estabelecimentos de agrupamentos, 
2-2 
Atribuição, 2-23 
Atributos, 2-6, 2-21 
Atributos de Chave, 2-23 
Chave estrangeira, 2-23 
Chave primaria, 2-23 
Chave secundária, 2-23 
Atributos não-chave, 2-10 
Atributo Técnico, 2-9, 2-24 
B 
Banco de dados relacional, 2-4 
C 
Campos repetidos, 2-27 
Carga 
definição, 3-3 
Cenário 4: Cópia/Carga de Imagem de uma Tabela 
Física – Nenhum Processamento Adicional 
Cenários, 3-13 
Cenários 
Cópia e Merge, 3-15 
Cópia/Carga de Imagem - Nenhum Processamento 
Adicional, 3-11 
Leitura, 3-7 
Cenário 4, 3-13 
Screen Scraping, 3-17 
Transação de Dados Padrão, 3-20 
Cópia Estática de Imagem, 3-9 
Atualizando o Mesmo Depósito de Dados, 3-18 
Conceito 
Entidade (in-)dependente, 2-12, 2-15 
relacionamento Opcional / Obrigatório, 2-12, 2-15 
Convenção para Nomenclatura dos Cenários, 3-5 
Copia 
definição, 3-3 
D 
Dados de Código 
definição, 1-6 
exemplos, 1-7 
identificando, 1-10 
características lógicas, 1-7 
origens, 1-8 
características físicas, 1-7 
o que é, 1-10 
o que não é, 1-13 
Dado Elementar, 2-4, 2-21 
Exemplo de endereço, 2-26 
Exemplo de chave estrangeira, 2-29 
Exemplo de atributos simples/multiplos, 2-25 
Exemplo de nomes, 2-26 
Exemplo de campos repetidos, 2-27 
Exemplo de campos de status, 2-28 
Exemplo de data do sistema, 2-29 
Janeiro 2010 Manual de Práticas de Contagem de Ponto de Função i-1 
---
## Página 254

Índice Parte 3 – Práticas de Contagem 
 
reconhecido pelo usuário, 2-25 
Dados de Negócio 
definição, 1-4 
definições, 1-4 
exemplos, 1-5 
características lógicas, 1-4 
características físicas, 1-5 
Dados referenciados 
definição, 1-5 
exemplos, 1-6 
características lógicas, 1-5 
características físicas, 1-6 
Definições 
manutenção adaptativa, 4-20 
Entidade Associativa, 2-3 
Tipo de Entidade Associativa, 2-5 
Atributos, 2-6, 2-21 
Tipo de Entidade Atributiva, 2-6 
dados de código, 1-6 
copia, 3-3 
manutenção corretiva, 4-20 
Dado Elementar, 2-4, 2-21 
Tipo de Elemento de Dados, 2-24 
Ítem de Dado, 2-4 
Entidade, 2-3 
Entidade Subtipo, 2-3, 2-6 
Entidade Tipo, 2-3, 2-5 
arquivo, 3-3 
Arquivo, 2-4 
Arquivos de Sistema, 2-4 
imagem, 3-3 
carga, 3-3 
merge, 3-3 
Normalização, 2-6 
manutenção perfectiva, 4-20 
intenção primária, 3-2 
Registro, 2-4 
dados referenciados, 1-5 
refresh, 3-3 
Relacionamento, 2-6 
Diagrama da Solução 
Cenário 1, 3-8 
Cenário 2, 3-10 
Cenário 3, 3-12 
Cenário 4, 3-14 
Cenário 5, 3-16 
Cenário 6, 3-17 
Cenário 7, 3-19 
Cenário 8, 3-21 
E 
Entidade, 2-3 
não mantida, 2-9 
Entidade Associativa, 2-3, 2-10, 2-34 
contada como arquivo lógico, 2-36 
contada como RLR, 2-35 
não contada, 2-34 
Entidade Atributiva, 2-37 
obrigatória, 2-37 
opcional, 2-37 
Entidade de intersseção, 2-10 
Entidade dependete, 2-12 
Entidade independente, 2-12 
Entidade Key-to-key, 2-10 
Entidade Subtipo, 2-6 
Entidade Subtipo, 2-3 
Entidade Subtipo, 2-32 
Entidade Subtipo, 2-38 
Entidade Subtipo 
contada como RLR, 2-38 
Entidade Subtipo 
não contada, 2-39 
Entidade Tipo, 2-3, 2-5 
Exemplos 
funcionalidade adicionada, 4-14 
funcionalidade alterada, 4-15 
funcionalidade excluida, 4-15 
F 
Funcional, 3-5 
Funcionalidade Adicionada 
exemplo, 4-14 
identificação, 4-10 
Funcionalidade alterada 
exemplo, 4-15 
identificação, 4-10 
Funcionalidade de Conversão 
identificação, 4-11 
Funcionalidade de Conversão, 4-2 
Funcionalidade Excluida 
exemplo, 4-15 
identificação, 4-11 
G 
Grupos/dados repetidos 
contados como RLR, 2-40 
não contados como RLR, 2-40 
I 
Imagem 
definição, 3-3 
Importância pro negócio, 2-13 
Intenção Primária 
definição, 3-2 
Definições, 3-2 
Ítem de Dado, 2-4 
L 
Linha, 2-4 
M 
Manutenção Adaptativa 
definição, 4-20 
Manutenção Corretiva 
definição, 4-20 
Manutenção perfectiva 
definição, 4-20 
Merge 
i-2 Manual de Práticas de Contagem de Ponto de Função Janeiro 2010 
---
## Página 255

Parte 3 – Práticas de Contagem Índice 
Janeiro 2010 Manual de Práticas de Contagem de Ponto de Função i-3 
definição, 3-3 
Modelos físico de dados, 2-9 
N 
Nome do Atributo, 2-22 
Normalização, 2-6 
P 
Processo de Classificação 
Arquivos lógicos, 2-2 
Processo de Identificação 
Tipo de Elemento de Dados, 2-2 
Arquivos Lógicos, 2-2 
usando o Método de Processo Elementar, 2-9 
usando do Método de Entidade (In-)Dependente, 
2-9 
Tipos de Registros Elementares, 2-2 
Projeto de melhoria 
medindo funções de transação, 4-3 
lógica de processamento, 4-5 
Projeto de Melhoria 
Conversão de Dados, 4-3 
medindo funções de dados, 4-2 
R 
Registros, 2-4 
Refresh 
definição, 3-3 
Relacionamento, 2-6 
Obrigatório 1-1, 1-N, 2-6, 2-14 
origem, 2-14 
Opcional 1-(N), (1)-(N), (1)-N, 2-6, 2-14 
Requisitos de Manutenção, 4-21 
Resumo dos cenários, 3-5 
S 
Símbolos Usados no Diagrama da Solução, 3-4 
Solicitações Eventuais (ad hoc), 4-22 
Subgrupo, 2-31 
Suporte ao usuário final, 4-23 
T 
Tabela, 2-4 
Técnico, 3-6 
Tipo de Dado 
negócio, 1-4 
código, 1-6 
referência, 1-5 
Tipos de Dados de Código 
estático ou constante, 1-11 
substituição, 1-11 
valores válidos, 1-12 
Tipo de Elemento de Dados 
regras, 2-24 
Tipo de Entidade Associativa, 2-5, 2-32 
Tipo de Entidade Atributiva, 2-6, 2-32 
Tupla, 2-4 
V 
Visão de negócio. Veja Visão do Usuário 
Visão do usuário, 2-9 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
---
## Página 256

Índice Parte 3 – Práticas de Contagem 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Página intencionalmente deixada em branco 
 
i-4 Manual de Práticas de Contagem de Ponto de Função Janeiro 2010 
---
## Página 257

 
 
 
 
 
 
Parte 4 – Exemplos
  
---
## Página 258

   
  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Página intencionalmente deixada em branco. 
---
## Página 259

 
 
 
 
 
 
 
 
Parte 4 Exemplos 
 
Introdução A Parte 4 apresenta exemplos de funções de dados e funções de transação 
para ilustrar as regras de contagem da Parte 1. Os exemplos fornecem:  
 Uma descrição das funções de dados ou de transação  
 A base para a medição  
 As tabelas para serem usadas na aplicação das regras de contagem 
 A identificação da complexidade funcional 
 A contribuição para o tamanho funcional 
 
  
Conteúdo A Parte 4 inclui as seguintes seções: 
 
Tópico Página
Exemplos de Contagem de Funções de Dados 1-3  
Exemplos de Contagem de ALI 1-7  
Exemplos de Contagem de AIE 1-39 
Exemplos de Contagem de Funções de Transação 2-1 
Exemplos de Identificação de Processo Elementar 2-7 
Exemplos de Contagem de EE 2-61 
Exemplos de Contagem de SE 2-103 
Exemplos de Contagem de CE 2-127 
 
 
 
 
 
 
 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-1 
---
## Página 260

 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-2 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Página intencionalmente deixada em branco 
 
---
## Página 261

  Parte 4 Capítulo 1 
 
 
 
 
 Exemplos de Contagem de Funções de Dados 
  
Introdução Esta seção utiliza vários exemplos a fim de ilustrar procedimentos para a 
medição de funções de dados, cada um independentemente, válido por si só. 
 
Nota: Cada exemplo mostra somente o requisito específico para a situação 
ilustrada, embora na prática devêssemos avaliar todos os requisitos e 
seu impacto funcional. 
Esta seção utiliza uma aplicação de Recursos Humanos (RH) com uma 
aplicação de Segurança e outra aplicação de Distribuição de Correspondência 
para ilustrar procedimentos para identificar e medir funções de dados.  Além 
desta seção, os exemplos estão nos Estudos de Caso, que são parte da 
documentação suplementar do IFPUG. 
Nota: Os exemplos desta seção e no decorrer deste manual têm dois 
propósitos: 
1. Ilustrar como as regras de contag em de pontos de função são aplicadas 
para um conjunto específico de requisitos do usuário. 
2. Permitir a você praticar utilizando os procedimentos de contagem. 
Cada contador deve: 
 Analisar os requisitos específicos do usuário que são aplicados em cada 
projeto ou aplicação sendo medida, e 
 Contar baseado naqueles requisitos. 
 
Conteúdo Esta seção explica a organização dos exemplos e inclui exemplos detalhados 
para contagem de ALIs e AIEs. 
 
Tópico Página
Exemplos de Contagem de Funções de Dados 1-3 
Exemplos de Contagem de ALI 1-7  
Exemplos de Contagem de AIE 1-39 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-3 
---
## Página 262

1BExemplos de Contagem de Funções de Dados  Parte 4 - Exemplos 
Organização dos Exemplos de Contagem 
 Esta seção explica como os exemplos são apresentados. 
Sumário da Organização 
 A seguinte lista sumariza a sequência da informação em exemplos detalhados.  
Para cada exemplo: 
1. As funções de dados são identificadas. 
2. As funções de dados são classificadas como ALIs ou AIEs. 
3. Os RLRs e DERs que contribuem para a complexidade funcional são 
identificados e contados. 
 
Diagrama da Organização 
 O seguinte diagrama ilustra a organização dos exemplos. 
 
Exemplo
Identifique AIEs
Conte RLRs/DERs
Exemplo
Identifique ALIs
Conte RLRs/DERs
 
Conte para Cada Exemplo 
 Cada exemplo inclui os seguintes componentes: 
1. Base para a medição 
2. Tabela aplicando as regras de contagem 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-4 
---
## Página 263

Parte 4 - Exemplos  1BExemplos de Contagem de Funções de Dados 
 
Diagrama dos 
Componentes 
O diagrama abaixo ilustra os componentes para cada exemplo e o fluxo de 
informação. 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Para cada ALI ou AIE identificado, 
Conte RLRs e DERs 
Xxxxxxxxxxxxxxxxxxxx  
Explicação ..... 
Xxxxxxxxxxxxxxxxxxxx  
Explicação ..... 
Xxxxxxxxxxxxxxxxxxxx  Explicação ..... 
Regras de Contagem As Regras se Aplicam?
 
 
Xxxxxxxxxxxxxxxxxxxxxxxxxxxx 
  Sim ou Não. Explicação ..... 
Xxxxxxxxxxxxxxxxxxxxxxxxxxxx   Sim ou Não. Explicação ..... 
Xxxxxxxxxxxxxxxxxxxxxxxxxxxx   Sim ou Não. Explicação ..... 
Xxxxxxxxxxxxxxxxxxxxxxxxxxxx   Sim ou Não. Explicação ..... 
Regras de Contagem As Regras se Aplicam? 
 
 
Identificar ALI ou AIE 
 Tabela de Regras de Contagem 
 
Requisitos do Usuário 
1. Xxxxxxxxxxxxxxx 
2. Xxxxxxxxxxxxxxx 
Base para a Medição
3. X
xxxxxxxxxxxxxx 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-5 
---
## Página 264

1BExemplos de Contagem de Funções de Dados  Parte 4 - Exemplos 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-6 
  
Base para a 
Medição 
A base para a medição inicia cada exemplo.  Como mostrado no diagrama de 
componentes, a medição pode ser baseada nos seguintes componentes: 
 Requisitos do usuário 
 Modelo de dados e de processo 
 Janelas, telas ou relatórios. 
Nota: Nem todos os componentes no diagrama estão incluídos em todos os 
exemplos. Em alguns exemplos, apenas os requisitos são base para a 
medição. Outros exemplos incluem um modelo de dados ou processo, 
janelas, telas, e relatórios. 
 
  
Tabela de 
Regras de 
Contagem 
A análise para identificar funções é apresentada em uma tabela que lista as 
regras de contagem para o tipo de função. As regras são aplicadas aos 
componentes que formam a base para a medição. A análise é explicada na 
tabela na coluna “A Regra se Aplica? 
Nota: Se todas as regras se aplicam, o exemplo é contado como um ALI ou 
AIE. 
A próxima tabela mostra as regras e a explicação para a complexidade para 
cada tipo de função identificado. 
---
## Página 265

 
 
 
 
 
 
 
 
 Exemplos de Contagem de ALI 
 
Introdução Esta seção usa a aplicação de Recursos Humanos (RH) para ilustrar os 
procedimentos para identificar e medir funções de dados. Além desta seção, 
outros exemplos estão nos Estudos de Caso que são parte da documentação 
complementar do IFPUG. 
 
  
Conteúdo 
 
Esta seção inclui os seguintes exemplos: 
 
Tópico Página
Resumo das Descrições dos Exemplos de Contagem de ALIs 1-8  
Exemplo: Dados de Auditoria para Consultas e Relatórios 1-9 
Exemplo: Definição de Relatório 1-15 
Exemplo: Índice Alternativo 1-20 
Exemplo: Dados Compartilhados por Aplicações 1-21 
Exemplo: Diferentes Usuários/Diferentes Visões dos Dados 1-30 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-7 
---
## Página 266

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
Resumo das Descrições dos Exemplos de Contagem de ALIs 
 Os exemplos para ALIs são descritos na seguinte tabela: 
 
Exemplo Descrição Resumida Página 
Dados de Auditoria Este exemplo mostra a análise e medição de 
dados que são mantidos para fins de auditoria.  
1-9 
Definição de 
Relatório 
Este exemplo mostra a contagem de definições 
de relatórios definidos pelo usuário, mantidas 
dentro de uma aplicação. 
1-15 
Índice Alternativo Este exemplo ilustra a análise dos requisitos do 
usuário para o exemplo de definição de relatório 
com foco nos requisitos para implementação 
física.  
1-20 
Dados 
Compartilhados por 
Aplicações 
Este exemplo mostra a contagem de dados que 
são mantidos por mais de uma aplicação. 
1-21 
Diferentes Usuários/ 
Diferentes Visões 
dos Dados 
Este exemplo mostra que duas aplicações podem 
contar o mesmo arquivo com diferentes DERs. 
1-30 
 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-8 
---
## Página 267

Parte 4 - Exemplos  2BExemplos de Contagem de ALI 
Exemplo: Dados de Auditoria para Consultas e Relatórios 
Requisitos do 
Usuário 
Uma análise dos seguintes requisitos de segurança do usuário mostra uma 
necessidade para dados de auditoria: 
1. Permitir ou recusar o acesso do usuário para cada tela da aplicação. 
2. Alterar o acesso do usuário para cada tela. 
3. Informar qualquer inclusão ou alteração de segurança de tela, utilizando 
os seguintes dados: 
 Identificação do usuário que está incluindo ou alterando a informação 
de segurança 
 O usuário da tela em que a segurança foi incluída ou alterada 
 O usuário e a imagem antes e depois de uma alteração feita na 
segurança da tela 
 A data e a hora que ocorreu a inclusão ou a alteração. 
4. Capturar dados de auditoria para monitorar e informar diariamente 
atividades da segurança. Este requisito foi determinado quando um 
projeto foi implementado para satisfazer os requisitos do usuário de 
segurança de telas. 
MER  
 
 
 
Segurança
de Tela
Auditoria de
Segurança 
Aplicação RH
Legenda:
Entida
de Tipo
Entidade Atributiva
Relacionamento Opcional Um-Para-Muitos
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-9 
---
## Página 268

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
 
Diagrama de Fluxo de Dados  
  
Usuário 
Informações para Incluir 
Segurança de Tela 
Solicitação de Relatório
Permissão de acesso,
id.janela 
Segu-
rança
Informações para Alterar Segurança de Tela
Relação das 
1.3 
de Tela
1.2
Incluir Segurança
1.1
de Tela
Id.usuário, SS#,  
Inf.Alt.
de Tela
Alterar Segurança
Screen 
de Tela 
Segurança 
Screen
Segurança
Auditoria de 
de Tela
Alterações da 
Segurança 
data, hora, id.usuário, 
antes, depois
id.usuário,
antes, depois 
data, hora,  
Informações do Relatório
id.usuário,
antes, depois
data, hora, 
 
 
  Depó
sito de Dados 
 
  Processo 
 
  Fluxo de Dados 
 
 
  Usuár
io ou Aplicação 
 
 
Legenda:  
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-10 
---
## Página 269

Parte 4 - Exemplos  2BExemplos de Contagem de ALI 
 
Passo 1 Identificar as Funções de Dados 
 Use as regras de Identificação de Funções de Dados para determinar se 
Auditoria de Segurança de Tela é uma função de dados. A tabela a seguir 
mostra a análise dos dados para Auditoria de Segurança de Tela 
Regras de Identificação de Função de 
Dados 
A regra se aplica? 
1. Identifique todos os dados ou 
informações de controle logicamente 
relacionados e reconhecidos pelo 
usuário dentro do escopo da contagem. 
Segurança de Tela e Auditoria de Segurança 
de Tela. 
2. Exclua entidades que não são mantidas 
por qualquer aplicação. 
Não existem entidades deste tipo. 
3. Agrupe entidades relacionadas que são 
entidades dependentes.  
Segurança de Tela e Auditoria de Segurança 
de Tela são relacionadas. Auditoria de 
Segurança de Tela é dependente de Segurança 
de Tela. Elas são agrupadas numa única 
função de dados. 
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
 
 A Auditoria de Segurança de Tela não é contada como uma função de dados 
porque ela é dependente de Segurança de Tela. Auditoria de Segurança de 
Tela é parte da função de dados Segurança de Tela. 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-11 
---
## Página 270

2BExemplos de Contagem de ALI  Parte 4 - Exemplos 
 
Passo 2 Classificar as Funções de Dados  
 A tabela a seguir mostra a análise para determinar se a informação de 
Segurança de Tela é classificada como um ALI. 
Regras para Classificação da Função de 
Dados 
A regra se aplica? 
1. Classificar como um ALI se os dados 
são mantidos pela aplicação sendo 
medida 
A função de dados Segurança de Tela é 
mantida dentro da aplicação.  
2. Classificar como um AIE, se:  Classificada como um ALI; 
consequentemente, nenhum AIE é 
identificado. 
 É referenciado, mas não mantido, 
pela aplicação sendo medida e  
 
 É identificado em um ALI em uma 
ou mais outras aplicações 
 
 
 Baseado na análise, a informação de Segurança de Tela é classificada como 
um ALI.   
 
Passo 3 Contar os DERs 
 Para os DERs, observe cada atributo associado com o ALI Segurança de 
Tela e determine se as regras de contagem de DER se aplicam.   
O ALI Segurança de Tela inclui: 
 Id.usuário 
 SS# 
 Id.Janela 
 Permissão de Acesso 
 Data da Alteração 
 Hora da Alteração 
 Imagem antes 
o Id.usuário antes 
o Id.janela antes 
o Permissão de acesso antes 
 Imagem depois 
o Id.usuário depois 
o Id.janela depois 
o Permissão de acesso depois 
 
 
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-12 
---
## Página 271

Parte 4 - Exemplos  2BExemplos de Contagem de ALI 
 
 A análise dos DERs para o ALI Segurança de Tela é mostrada abaixo: 
Regras de Contagem de DER para Função 
de Dados 
A regra se aplica?   
1. Conte um DER para cada atributo único 
reconhecido pelo usuário, não repetido 
mantido em ou recuperado de uma função 
de dados através da execução de todos os 
processos elementares dentro do escopo da 
contagem. 
Id usuário, SS#, Id janela, Permissão de 
acesso, Data da Alteração e Hora da 
Alteração. 
2. Conte somente aqueles DERs sendo usado 
pela aplicação sendo medida quando duas 
ou mais aplicações mantém e/ou 
referenciam a mesma função de dados. 
Não existem atributos deste tipo.  
3. Conte um DER para cada atributo 
requerido pelo usuário para estabelecer um 
relacionamento com outra função de dados. 
Não existem atributos deste tipo. 
4. Revise os atributos relacionados para 
determinar se eles são agrupados e 
contados como um único DER ou se eles 
são contados como múltiplos DERs; o 
agrupamento dependerá de como os 
processos elementares usam os atributos 
dentro da aplicação. 
Id usuário antes, Id janela antes e Permissão 
de acesso antes  são agrupados e contados 
como Imagem Antes. O mesmo também é 
feito para os atributos Imagem Depois.  
  
Passo 4 Contar os RLRs 
 Para os RLRs, identifique os subgrupos baseado nas regras de contagem de 
RLR.  
Regras de Contagem de RLR A regra se aplica?   
1. Conte um RLR para cada função de 
dados (isto é, por default, cada função 
de dados tem um subgrupo de DERs 
para ser contado como um RLR). 
Conte um RLR para o ALI Segurança de Tela. 
 
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
Auditoria de Segurança de Tela é uma entidade 
atributiva num relacionamento 1-M opcional. 
Conte um RLR adicional para Auditoria de 
Segurança de Tela. 
  
Janeiro de 2010 Manual de Práticas de Contagem de Pontos de Função 1-13 