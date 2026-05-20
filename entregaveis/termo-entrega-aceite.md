# Termo de Entrega e Aceite

Template: [../templates/termo-entrega-aceite-modelo.docx](../templates/termo-entrega-aceite-modelo.docx)

Exemplo de JSON: [../templates/contagem-exemplo.json](../templates/contagem-exemplo.json)

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
| Grupo | F1 | Módulo - Autenticação… | (vazio) |
| Item | (vazio) | Nome da função - TIPO | 4,00 |
| Total | (vazio) | TOTAL DE PONTOS DE FUNÇÃO | 0,00 |

- PF Local = coluna P da planilha (aba Funções), formatado `1.234,56`
- Nome do item inclui sufixo `- EE`, `- CE`, etc., quando não estiver no nome

## Campos JSON (`termo`)

```json
{
  "termo": {
    "sistema": "NOME DO SISTEMA – DESCRIÇÃO COMPLETA",
    "nome_curto": "NOME DO SISTEMA",
    "total_pf": 0,
    "data": "Cidade-UF, dd de mês de aaaa",
    "cliente": "NOME DO CLIENTE – LINHA 1",
    "cliente_linha2": "NOME DO CLIENTE – LINHA 2",
    "cliente_contratante": "NOME DO CLIENTE",
    "processo_licitatorio": "000/0000",
    "contrato": "000/0000",
    "processo_administrativo": "000/0000",
    "planilha_anexa": "contagem-desenvolvimento.xlsx",
    "elaborado_por": "NOME DO ELABORADOR",
    "elaborado_cargo": "Cargo do elaborador"
  }
}
```

## Geração

```bash
python scripts/gerar_termo_aceite.py contagem.json -o termo.docx --pdf termo.pdf
```

O PDF usa HTML/CSS institucional Sudoeste + Playwright (Chromium), com rodapé da empresa e paginação. O DOCX clona o template preservando formatação das linhas de grupo/item.

## Coerência obrigatória

- Total do termo = Sumário!G49 da planilha = total informado na proposta
- Nomes dos pacotes F1…Fn idênticos entre planilha e termo
- Planilha anexa referenciada pelo nome real do arquivo entregue
