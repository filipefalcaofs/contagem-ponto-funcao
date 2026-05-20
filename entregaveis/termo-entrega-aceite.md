# Termo de Entrega e Aceite

Template: [../templates/termo-entrega-aceite-modelo.docx](../templates/termo-entrega-aceite-modelo.docx)

Referência: `Termo de Entrega e Aceite - SIGVISA - 1047 PF.docx`

## Estrutura do documento

1. **Cabeçalho** — nome do sistema, título, número da entrega, tamanho funcional, data, cliente
2. **Metadados contratuais** — processo licitatório, contrato, processo administrativo
3. **Introdução** — formalização da entrega, referência à planilha anexa e ao IFPUG 4.3.1
4. **Pacotes de Trabalho Entregues** — tabela 3 colunas: Id. Func | Função | PF Local
5. **Total de Pontos de Função**
6. **Observações** — metodologia IFPUG e planilha para fiscal
7. **Aprovação** — elaborado por / homologado por, data e local

## Tabela de pacotes (regra)

| Linha | Col 1 | Col 2 | Col 3 |
|-------|-------|-------|-------|
| Grupo | F1 | Retaguarda - Autenticação… | (vazio) |
| Item | (vazio) | Nome da função - TIPO | 4,00 |
| Total | (vazio) | TOTAL DE PONTOS DE FUNÇÃO | 1.047,00 |

- PF Local = coluna P da planilha (aba Funções), formatado `1.047,00`
- Nome do item inclui sufixo `- EE`, `- CE`, etc., quando não estiver no nome

## Campos JSON (`termo`)

```json
{
  "termo": {
    "sistema": "SIGVISA – SISTEMA DE LICENCIAMENTO SANITÁRIO",
    "total_pf": 1047,
    "data": "Salvador-BA, 05 de maio de 2026",
    "cliente": "SMS – SECRETARIA MUNICIPAL DA SAÚDE",
    "cliente_linha2": "PMS – PREFEITURA MUNICIPAL DO SALVADOR – ESTADO DA BAHIA",
    "processo_licitatorio": "001/2023",
    "contrato": "255/2023",
    "processo_administrativo": "77751/2023",
    "planilha_anexa": "contagem-sigvisa-desenvolvimento.xlsx",
    "elaborado_por": "CLEILSON SANTANA GOMES",
    "elaborado_cargo": "CTO – CHIEF TECHNOLOGY OFFICER",
    "homologado_por": "",
    "homologado_cargo": ""
  }
}
```

## Geração

```bash
# DOCX (template Word fiel) + PDF (layout fiel)
python scripts/gerar_termo_aceite.py contagem.json -o termo.docx --pdf termo.pdf
```

O PDF usa HTML/CSS institucional + Playwright (Chromium), com rodapé Sudoeste e paginação. O DOCX clona o template original preservando formatação das linhas de grupo/item.

## Coerência obrigatória

- Total do termo = Sumário!G49 da planilha = total informado na proposta
- Nomes dos pacotes F1…Fn idênticos entre planilha e termo
- Planilha anexa referenciada pelo nome real do arquivo entregue
