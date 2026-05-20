# Proposta Comercial

Template visual: [../templates/proposta-comercial-modelo.pdf](../templates/proposta-comercial-modelo.pdf)

Referência: `Proposta Comercial - SALUS - v3.pdf` (9 páginas)

## Seções obrigatórias

| # | Seção | Conteúdo |
|---|-------|----------|
| Capa | Título, sistema, cliente, data | PROPOSTA COMERCIAL + nome + DVIS/PMS |
| 1 | Objeto | Desenvolvimento e implantação do sistema (VISA + Portal) |
| 2 | Escopo — Ações Macro | 8–10 blocos com bullets de telas/integrações (visão comercial, não PF) |
| 3 | Metodologia de Contagem | CPM IFPUG 4.3.1, tipos EE/SE/CE/ALI/AIE, VAF se aplicável |
| 4 | Prazo de Entrega | Dias corridos a partir da OS |
| 5 | Estimativa em PF | Tabela resumo não ajustado + ajustado |
| 6 | Linguagem, Tecnologia e Frameworks | Stack (Laravel, Vue, PostgreSQL, testes) |
| 7 | Inteligência Artificial e Manutenção | Provedores, exclusões de orçamento |
| 8 | Carga Inicial do Banco de Dados | Referência + operacional legado |
| 9 | Condições Gerais | Validade 30 dias, aditivo por PF, entrega com código-fonte |

## Diferença escopo macro vs planilha

| Documento | Granularidade | Público |
|-----------|---------------|---------|
| Proposta §2 | Ações macro, telas, integrações | Comercial / gestor |
| Planilha | Processos elementares IFPUG | Fiscal / contador PF |
| Termo | Pacotes F1–Fn com PF Local | Aceite formal |

A proposta **não substitui** a planilha; referencia a metodologia e o total PF.

## Campos JSON (`proposta` + `escopo_macro`)

```json
{
  "proposta": {
    "titulo": "PROPOSTA COMERCIAL",
    "sistema": "SALUS — Sistema de Licenciamento Sanitário",
    "subtitulo": "DVIS/SMS — Prefeitura Municipal de Salvador",
    "cliente": "",
    "data": "09/04/2026",
    "objeto": "Desenvolvimento e implantação do SALUS...",
    "prazo": "40 (quarenta) dias corridos...",
    "metodologia_contagem": "CPM IFPUG 4.3.1...",
    "condicoes_gerais": ["..."]
  },
  "escopo_macro": [
    {
      "titulo": "1. Autenticação, Controle de Acesso e Perfil",
      "referencia": "HU.01 a HU.04",
      "itens": ["Tela de login do Painel VISA...", "..."]
    }
  ],
  "resumo_pf": {
    "ee": 329, "se": 123, "ce": 195, "ali": 306, "aie": 46,
    "total_nao_ajustado": 999,
    "vaf": 1.07,
    "total_ajustado": 1069
  },
  "secoes_adicionais": [
    {"titulo": "6. Linguagem, Tecnologia e Frameworks", "texto": "..."},
    {"titulo": "7. Inteligência Artificial e Manutenção", "itens": ["..."]},
    {"titulo": "8. Carga Inicial do Banco de Dados", "itens": ["..."]}
  ]
}
```

## Geração

```bash
python scripts/gerar_proposta_comercial.py contagem.json -o proposta.pdf
```

O PDF replica o layout SALUS v3: capa centrada, títulos Cambria `#005ca9` (28pt), referências em cinza, bullets `●`, tabelas PF com cabeçalho azul institucional, cabeçalho/rodapé paginados.

Referência visual: [templates/proposta-comercial-modelo.pdf](../templates/proposta-comercial-modelo.pdf)

## Coerência com contagem

- `resumo_pf.total_nao_ajustado` = planilha Sumário!G49
- Metodologia cita IFPUG 4.3.1 (mesma versão da skill)
- Escopo macro cobre funcionalidades contadas (sem listar rotas/endpoints)
