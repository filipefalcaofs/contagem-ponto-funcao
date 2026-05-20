# Proposta Comercial

Template visual: [../templates/proposta-comercial-modelo.pdf](../templates/proposta-comercial-modelo.pdf)

Exemplo de JSON: [../templates/contagem-exemplo.json](../templates/contagem-exemplo.json)

## Seções obrigatórias

| # | Seção | Conteúdo |
|---|-------|----------|
| Capa | Título, sistema, cliente, data | PROPOSTA COMERCIAL + nome do sistema + contratante |
| 1 | Objeto | Desenvolvimento e implantação conforme escopo acordado |
| 2 | Escopo — Ações Macro | Blocos com bullets de telas/integrações (visão comercial, não PF) |
| 3 | Metodologia de Contagem | CPM IFPUG 4.3.1, tipos EE/SE/CE/ALI/AIE, VAF se aplicável |
| 4 | Prazo de Entrega | Prazo acordado em contrato |
| 5 | Estimativa em PF | Tabela resumo não ajustado + ajustado |
| 6+ | Seções adicionais | Stack, IA, carga de dados, condições gerais (via JSON) |

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
    "sistema": "Nome do Sistema — Descrição Comercial",
    "subtitulo": "Cliente — Órgão contratante",
    "data": "dd/mm/aaaa",
    "objeto": "Desenvolvimento e implantação do sistema...",
    "prazo": "Prazo acordado em contrato..."
  },
  "escopo_macro": [
    {
      "titulo": "1. Autenticação e Controle de Acesso",
      "referencia": "HU.01 a HU.04",
      "itens": ["Tela de login...", "..."]
    }
  ],
  "resumo_pf": {
    "ee": 0, "se": 0, "ce": 0, "ali": 0, "aie": 0,
    "total_nao_ajustado": 0,
    "vaf": 1.0,
    "total_ajustado": 0
  }
}
```

## Geração

```bash
python scripts/gerar_proposta_comercial.py contagem.json -o proposta.pdf
```

Layout institucional Sudoeste: capa centrada, títulos Cambria `#005ca9`, referências em cinza, bullets, tabelas PF com cabeçalho azul, cabeçalho/rodapé paginados.

## Coerência com contagem

- `resumo_pf.total_nao_ajustado` = planilha Sumário!G49
- Metodologia cita IFPUG 4.3.1 (mesma versão da skill)
- Escopo macro cobre funcionalidades contadas (sem listar rotas/endpoints)
