# Planilha de Contagem — Modelo Sudoeste

Template: [../templates/planilha-contagem-modelo.xlsx](../templates/planilha-contagem-modelo.xlsx)

Exemplo de JSON: [../templates/contagem-exemplo.json](../templates/contagem-exemplo.json)

## Abas (não alterar estrutura)

| Aba | Função |
|-----|--------|
| `Contagem` | Identificação, tipo, propósito, fatores I/A/E/T, R$/PF |
| `Funções` | Detalhamento auditável (grupos + itens contáveis) |
| `Sumário` | Totais automáticos por tipo e complexidade (fórmulas) |

## Aba `Contagem` — campos principais

| Célula | Campo |
|--------|-------|
| F7 | Empresa |
| F8 | Aplicação |
| F9 | Projeto |
| F10 | DV Número |
| F11 | Responsável |
| N10 | Versão |
| F12 | Revisor |
| W11 | Data da contagem |
| T7 | R$/PF |
| K20 | Propósito da contagem |
| L14–L17 | Marcar `x` no tipo: Estimativa / Desenvolvimento / Melhoria / Baseline |
| W15–W18 | Fatores I/A/E/T (ADD/CHG/DEL/TST) |

## Aba `Funções` — colunas (linha 11 = cabeçalho, dados a partir da 12)

| Coluna | Campo | Regra |
|--------|-------|-------|
| A | Id. numérico | Fórmula — não preencher manualmente |
| B | Id. Func (F1, F2…) | Fórmula — não preencher manualmente |
| C | Nome da função ou grupo | Grupo: só nome. Item: processo elementar |
| H | Tipo | EE, CE, SE, ALI, AIE — vazio na linha de grupo |
| I | (I/A/E/T) | I=inclusão, A=alteração, E=exclusão, T=teste |
| J | TD / DER | Número auditável |
| K | AR/TR ou FTR | Número auditável |
| N | Complexidade | Fórmula a partir de J/K/H |
| O | PF | Fórmula IFPUG |
| P | PF Local | Fórmula com fator da aba Contagem |
| Q | Observações | Justificativa funcional + citação CPM |

## Regras de preenchimento

1. **Linha de grupo** — preencher apenas coluna C (nome do pacote funcional). Sem tipo, TD, AR ou PF.
2. **Linha de item** — preencher C, H, I (se melhoria), J, K, Q. Deixar fórmulas em N, O, P intactas.
3. **Ordem didática** — Retaguarda → Portal → Público/Transversal.
4. **Nomenclatura** — `Módulo - verbo + objeto` (ex.: `Usuários - incluir registro`).
5. **ALI/AIE** — prefixo `Dados -` ou `Dados externos -` quando for função de dados.
6. **Não quebrar** mesclagens, fórmulas nem aba Sumário.

## Geração automatizada

```bash
python scripts/preencher_planilha.py contagem.json -o saida/contagem.xlsx
python scripts/extrair_planilha_para_json.py saida/contagem.xlsx -o contagem.json
```

## Validação antes de entregar

- [ ] Sumário!G49 = soma PF não ajustados
- [ ] Nenhuma linha de grupo com tipo ou PF
- [ ] Todos os itens com TD/AR auditáveis em Q
- [ ] Total coerente com termo e proposta
