---
name: contagem-ponto-funcao
description: Use when the user asks for contagem de ponto de função, APF, IFPUG, análise de pontos de função, preencher planilha de contagem, gerar termo de entrega e aceite, proposta comercial, histórias de usuário HU, docs/requisitos/hus, estimar tamanho funcional, revisar TD/AR/TR, ALI/AIE/EE/CE/SE, DER/RLR/FTR, VAF/GSC, melhoria/enhancement, ou validar contagem para contrato/fiscal. Segue o CPM IFPUG 4.3.1 PT-BR integral e gera planilha, termo e proposta.
---

# Contagem de Ponto de Função — IFPUG CPM 4.3.1

## Fonte autoritativa

Toda contagem **deve** seguir o **Manual de Práticas de Contagem de Pontos de Função — IFPUG CPM 4.3.1 (PT-BR)**:

- Manual completo: [referencias/CPM-IFPUG-4.3.1-PT.pdf](referencias/CPM-IFPUG-4.3.1-PT.pdf)
- Índice de navegação: [referencias/indice-cpm.md](referencias/indice-cpm.md)

**Antes de classificar, pontuar ou entregar**, consulte as seções aplicáveis do manual. Este SKILL.md é um roteiro operacional; **não substitui** o CPM. Em divergência, prevalece o manual.

Extratos por tema (aceleram consulta; o PDF prevalece se houver diferença):

| Tema | Arquivo |
|------|---------|
| Fluxo Parte 2 | [referencias/fluxo-contagem-parte2.md](referencias/fluxo-contagem-parte2.md) |
| Funções de dados | [referencias/regras-funcoes-dados.md](referencias/regras-funcoes-dados.md) |
| Processo elementar / transações | [referencias/regras-processo-elementar.md](referencias/regras-processo-elementar.md) |
| Tabelas de complexidade e PF | [referencias/tabelas-complexidade.md](referencias/tabelas-complexidade.md) |
| Dados de código | [referencias/dados-codigo.md](referencias/dados-codigo.md) |
| Arquivos lógicos | [referencias/arquivos-logicos.md](referencias/arquivos-logicos.md) |
| Dados compartilhados | [referencias/dados-compartilhados.md](referencias/dados-compartilhados.md) |
| Melhoria / enhancement | [referencias/melhoria-enhancement.md](referencias/melhoria-enhancement.md) |
| Conversão de dados | [referencias/conversao-dados.md](referencias/conversao-dados.md) |
| VAF e 14 GSC | [referencias/vaf-gsc.md](referencias/vaf-gsc.md) |
| Glossário | [referencias/glossario-ifpug.md](referencias/glossario-ifpug.md) |

## Princípio

Conte pela visão funcional do usuário, conforme Parte 1 e Parte 2 do CPM. Código-fonte, rotas, endpoints, classes, migrations e tabelas físicas podem ajudar a tirar dúvidas, mas a contagem deve ser defensável por requisitos, telas, fluxos, regras de negócio, modelo conceitual e evidências funcionais.

Uma função só entra na contagem se for reconhecida pelo usuário e pertencer à fronteira definida (Cap. 5, Parte 2).

## Fluxo obrigatório (alinhado ao CPM)

1. **Tipo de contagem** — desenvolvimento, melhoria, aplicação/baseline ou estimativa (Parte 2, Cap. 4).
2. **Fronteira e escopo** — aplicação medida, usuários, sistemas externos (Parte 2, Cap. 5).
3. **Evidências funcionais** — requisitos, HUs (`hu-projeto.json` → pasta configurada), telas, fluxos, integrações.
4. **Grupos funcionais** — em linguagem de negócio.
5. **Funções de dados** — identificar ALI/AIE; contar DER e RLR; determinar complexidade (Parte 2 Cap. 6 + Parte 1 §5.4).
6. **Funções transacionais** — identificar processos elementares; classificar EE/CE/SE; contar DER e FTR (Parte 2 Cap. 7 + Parte 1 §5.5).
7. **Pontuação** — aplicar Tabelas 1–4 / Apêndice A ([tabelas-complexidade.md](referencias/tabelas-complexidade.md)).
8. **Ajuste (se aplicável)** — 14 GSC e VAF (Apêndice C).
9. **Melhoria (se aplicável)** — impacto, fator de conversão, taxa de ocorrência (Parte 3 Cap. 4).
10. **Revisão e planilha** — validar totais, justificativas e auditabilidade.

## Terminologia IFPUG (usar no registro)

| Termo CPM | Sinônimo comum | Uso |
|-----------|----------------|-----|
| DER | TD, dado elementar | Atributo reconhecido pelo usuário |
| RLR | TR, subgrupo | Registro lógico dentro de ALI/AIE |
| FTR / ALR | AR | Arquivo lógico referenciado por transação |
| ALI | ILF | Dados mantidos na fronteira |
| AIE | EIF | Dados referenciados, mantidos fora |
| EE / CE / SE | — | Funções transacionais |
| PF / TF | — | Pontos / tamanho funcional |

## Processo elementar (CPM Parte 1 §5.5.2)

Conte uma transação apenas se atender **todos** os critérios:

- Tem significado para o usuário.
- É uma transação completa.
- É autocontida.
- Deixa o negócio em estado consistente ou entrega resposta funcional completa.

Consultar Parte 2 Cap. 7 para unicidade e classificação EE vs CE vs SE. Em dúvida entre CE e SE, ler regras e exemplos da Parte 4.

## Tipos de função (resumo — detalhes no CPM)

| Tipo | Use quando |
|------|------------|
| `ALI` | Grupo lógico de dados mantido pela aplicação dentro da fronteira. |
| `AIE` | Grupo lógico usado pela aplicação, mantido por outro sistema. |
| `EE` | Processo elementar que mantém dados, altera estado ou dispara processo de negócio. |
| `CE` | Consulta simples, com entrada/saída, sem cálculo relevante e sem atualização de ALI. |
| `SE` | Saída com cálculo, derivação, relatório, arquivo, PDF, notificação funcional autônoma ou processamento relevante. |

## Pontuação (Apêndice A — consultar tabelas completas)

### Complexidade das funções de dados (Tabela 1)

| RLR \ DER | 1–19 | 20–50 | >50 |
|-----------|------|-------|-----|
| 1 | Baixa | Baixa | Média |
| 2–5 | Baixa | Média | Alta |
| >5 | Média | Alta | Alta |

### Tamanho das funções de dados (Tabela 2)

| Complexidade | ALI | AIE |
|--------------|-----|-----|
| Baixa | 7 | 5 |
| Média | 10 | 7 |
| Alta | 15 | 10 |

### Complexidade das funções transacionais (Tabelas 3–4)

Usar contagem de **FTR** e **DER** da transação conforme Parte 1 §5.5.3–5.5.4 e Apêndice A. Valores:

| Complexidade | EE | CE | SE |
|--------------|----|----|-----|
| Baixa | 3 | 3 | 4 |
| Média | 4 | 4 | 5 |
| Alta | 6 | 6 | 7 |

## Funções de dados — regras práticas (complemento ao CPM)

Agrupe por domínio funcional, não por tabela. Aplicar teste de independência (Parte 3 Cap. 2 + Parte 1):

- O grupo tem significado de negócio por si só?
- Excluída a ocorrência do pai, continua existindo com significado independente?
- É criado/excluído de forma independente?

Se dependente → `RLR` dentro do ALI/AIE principal, não ALI/AIE separado.

Dados de código/catálogos → Parte 3 Cap. 1. Dados compartilhados → Parte 3 Cap. 3.

Para cada ALI/AIE, registrar:

```text
DER considerados: [lista auditável]
RLR considerados: [subgrupos]
Justificativa CPM: [independência ou agrupamento]
Evidência funcional: [requisito, tela, fluxo]
Citação CPM: [Parte/Cap./seção ou página]
```

## Funções transacionais — registro

```text
Processo elementar: [verbo + objeto de negócio]
DER considerados: [entrada/saída reconhecidos pelo usuário]
FTR considerados: [ALI/AIE lidos/mantidos]
Justificativa EE/CE/SE: [critério CPM atendido]
Evidência funcional: [tela, requisito, fluxo]
Citação CPM: [Parte/Cap./seção ou página]
```

Use nomes funcionais: `Consultar estabelecimento na SEFAZ por CGA`, não nomes de rota ou método.

## O que não contar separadamente

Conforme CPM e práticas de contagem (Parte 3 + exemplos):

- Rotas, endpoints, controllers, services, componentes, jobs.
- Tabelas físicas isoladas, pivôs e campos técnicos sem significado funcional próprio.
- Abas, modais, botões, CSS, paginação, ordenação e máscaras (salvo processo elementar próprio).
- Callback técnico, health check, sessão, cache, fila, token interno.
- Busca auxiliar ou pré-validação quando não forem transações completas.
- Notificação automática consequência de EE já contado, salvo saída funcional autônoma exigida.

## Casos especiais — consultar manual antes de decidir

| Cenário | Onde no CPM |
|---------|-------------|
| Dados de domínio/código | Parte 3 Cap. 1 |
| ALI composto, subgrupos, históricos | Parte 3 Cap. 2 + Parte 4 Cap. 1 |
| Dados compartilhados entre aplicações | Parte 3 Cap. 3 |
| Projeto de melhoria / manutenção | Parte 3 Cap. 4 |
| Conversão de dados legados | Parte 3 Cap. 5 |
| CE vs SE (relatório, GUI) | Parte 4 Cap. 2 + Parte 1 §5.5 |
| PF ajustado | Apêndice C |

## TD/DER, AR/FTR auditáveis

Não use números "de cabeça". Aplicar regras de contagem de DER/RLR/FTR do CPM (Parte 1 §5.4–5.5 e Parte 4).

Checklist por função:

- [ ] Nome em linguagem de negócio.
- [ ] Tipo funcional justificado com critério CPM citado.
- [ ] DER/FTR listados conforme regras de contagem (não campos técnicos).
- [ ] ALI/AIE passou pelo teste de independência.
- [ ] Detalhes dependentes tratados como RLR, não ALI/AIE.
- [ ] Processo elementar ou arquivo lógico válido.
- [ ] Evidência funcional ou premissa declarada.
- [ ] Observação permite conferência sem código-fonte.

Se não for possível auditar, marque pendência. Não apresente como contagem detalhada definitiva.

## Planilhas oficiais

- Preserve abas, fórmulas, mesclagens e estrutura do modelo.
- Linhas de grupo = título, sem tipo, TD, AR/TR ou PF.
- Pontuação apenas nos itens abaixo do grupo.
- `Observações` em linguagem funcional com citação CPM quando relevante.

## Entregáveis comerciais (pacote completo)

A skill gera três documentos alinhados entre si. Templates institucionais Sudoeste:

| Entregável | Template | Documentação |
|------------|----------|--------------|
| Planilha XLSX | [templates/planilha-contagem-modelo.xlsx](templates/planilha-contagem-modelo.xlsx) | [entregaveis/planilha-contagem.md](entregaveis/planilha-contagem.md) |
| Termo DOCX | [templates/termo-entrega-aceite-modelo.docx](templates/termo-entrega-aceite-modelo.docx) | [entregaveis/termo-entrega-aceite.md](entregaveis/termo-entrega-aceite.md) |
| Termo PDF | [templates/html/termo-entrega-aceite.html](templates/html/termo-entrega-aceite.html) + CSS | layout fiel via Playwright |
| Proposta PDF | [templates/html/proposta-comercial.html](templates/html/proposta-comercial.html) + [proposta-comercial-modelo.pdf](templates/proposta-comercial-modelo.pdf) | [entregaveis/proposta-comercial.md](entregaveis/proposta-comercial.md) |

JSON de exemplo: [templates/contagem-exemplo.json](templates/contagem-exemplo.json)

### Fluxo de geração (obrigatório)

1. **Contar** — aplicar CPM 4.3.1; montar JSON com `identificacao`, `grupos[]`, `termo`, `proposta`, `escopo_macro`, `resumo_pf`.
2. **Planilha** — `python scripts/preencher_planilha.py contagem.json -o contagem.xlsx`
3. **Validar** — abrir XLSX; conferir Sumário, fórmulas e TD/AR auditáveis.
4. **Termo** — `python scripts/gerar_termo_aceite.py contagem.json -o termo.docx --pdf termo.pdf`
5. **Proposta** — `python scripts/gerar_proposta_comercial.py contagem.json -o proposta.pdf`
6. **Pacote completo** — `python scripts/gerar_pacote_completo.py contagem.json -d saida/ --prefixo contagem`
7. **Coerência** — total PF idêntico nos três documentos (usar PF Local da planilha no termo).

### Scripts

| Script | Função |
|--------|--------|
| [scripts/preencher_planilha.py](scripts/preencher_planilha.py) | JSON → XLSX a partir do template |
| [scripts/extrair_planilha_para_json.py](scripts/extrair_planilha_para_json.py) | XLSX → JSON (recalcular PF se fórmulas sem cache) |
| [scripts/gerar_termo_aceite.py](scripts/gerar_termo_aceite.py) | JSON → Termo DOCX (template fiel) + PDF (HTML/Playwright) |
| [scripts/gerar_proposta_comercial.py](scripts/gerar_proposta_comercial.py) | JSON → Proposta PDF (layout institucional via HTML/Playwright) |
| [scripts/gerar_pdf.py](scripts/gerar_pdf.py) | HTML → PDF com cabeçalho/rodapé paginado |
| [scripts/render_documento.py](scripts/render_documento.py) | JSON → HTML (Jinja2 + CSS institucional) |
| [scripts/gerar_pacote_completo.py](scripts/gerar_pacote_completo.py) | Gera planilha + termo + proposta de uma vez |
| [scripts/docx_utils.py](scripts/docx_utils.py) | Edição de DOCX preservando formatação do template |
| [scripts/ifpug_calc.py](scripts/ifpug_calc.py) | Cálculo de complexidade e PF (espelha fórmulas da planilha) |
| [scripts/hu_parser.py](scripts/hu_parser.py) | Markdown → estrutura HU |
| [scripts/hu_docx_builder.py](scripts/hu_docx_builder.py) | Estrutura HU → DOCX (template Word) |
| [scripts/gerar_hu_docx.py](scripts/gerar_hu_docx.py) | Uma HU: MD → DOCX (+ PDF opcional) |
| [scripts/atualizar_hus.py](scripts/atualizar_hus.py) | Todas as HUs do projeto: MD → DOCX/PDF |
| [scripts/gerar_hu_consolidado.py](scripts/gerar_hu_consolidado.py) | Consolida HUs em um DOCX |
| [scripts/init_hus.py](scripts/init_hus.py) | Inicializa pasta e config em projeto novo |
| [scripts/render_hu.py](scripts/render_hu.py) | HU → HTML (PDF via Playwright) |

Dependências: ver [requirements.txt](requirements.txt). Após instalar, executar `playwright install chromium`.

### Histórias de Usuário (qualquer projeto)

1. **Inicializar** — `python scripts/init_hus.py --nome "Projeto X" --projeto /caminho/cliente`
2. **Configurar** — `hu-projeto.json` na raiz do projeto cliente (ver [templates/hu-projeto.exemplo.json](templates/hu-projeto.exemplo.json))
3. **Editar** — arquivos `HU.NN - Título.md` na pasta configurada (Markdown = fonte de verdade)
4. **Gerar** — `python scripts/atualizar_hus.py --projeto /caminho/cliente --pdf --consolidado`

Guia: [entregaveis/historias-usuario.md](entregaveis/historias-usuario.md) | Template MD: [templates/hu-modelo.md](templates/hu-modelo.md) | Template DOCX: [templates/hu-modelo.docx](templates/hu-modelo.docx)

## Exemplo de configuração

Arquivo de exemplo: [examples/exemplo-projeto/hu-projeto.json](examples/exemplo-projeto/hu-projeto.json)

Ao contar PF ou redigir proposta, referenciar HUs no §2 (`Referência: HU.NN`).

### Regras de coerência entre documentos

- **Planilha** = fonte auditável (TD, AR, observações, CPM).
- **Termo** = espelho dos pacotes F1–Fn com PF Local; referencia planilha anexa.
- **Proposta** = escopo macro comercial (§2) + totais PF (§3/§5); não lista processos elementares.
- Divergência de total → corrigir planilha primeiro, regenerar termo e proposta.

## Revisão final

1. Conferir tipo de contagem e fronteira documentados.
2. Verificar ausência de PF em linhas de grupo.
3. Recalcular totais (não ajustado e ajustado, se aplicável).
4. Eliminar duplicidades e itens auxiliares indevidos.
5. Reavaliar ALI/AIE suspeitos (item, histórico, vínculo, anexo) como RLR.
6. Confirmar DER/RLR/FTR auditáveis em cada função.
7. Confrontar casos limítrofes com exemplos da Parte 4.
8. Informar nível: indicativa, estimativa ou detalhada.

## Resposta ao usuário

Ao finalizar, informar:

- arquivos gerados (planilha, termo, proposta);
- tipo de contagem e fronteira;
- quantidade de funções contáveis por tipo;
- total de PF não ajustado e PF Local (termo);
- premissas e citações CPM relevantes;
- limitações ou pendências de auditoria.
