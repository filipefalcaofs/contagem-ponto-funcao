# Histórias de Usuário — guia genérico

## Configuração por projeto

Cada projeto cliente possui um `hu-projeto.json` na raiz (criado por `init_hus.py`):

```json
{
  "nome_projeto": "Nome completo do sistema",
  "empresa": "Razão social da desenvolvedora",
  "pasta_hus": "docs/requisitos/hus",
  "cor_primaria": "#005ca9",
  "gerar_docx": true,
  "gerar_pdf": false,
  "gerar_consolidado": true
}
```

A pasta `pasta_hus` é relativa à raiz do projeto. Padrão recomendado: `docs/requisitos/hus`.

## Convenção de arquivos

| Arquivo | Função |
|---------|--------|
| `HU.NN - Título.md` | **Fonte de verdade** — editar sempre aqui |
| `HU.NN - Título.docx` | Gerado automaticamente pelo script |
| `HU.NN - Título.pdf` | Opcional (`--pdf` ou `"gerar_pdf": true`) |
| `screenshots/` | Evidências visuais referenciadas no MD |
| `MATRIZ-COBERTURA-HUS.md` | Rastreabilidade HU ↔ módulo ↔ status |

## Estrutura do Markdown

Ver [templates/hu-modelo.md](../templates/hu-modelo.md). Seções obrigatórias:

1. Cabeçalho `# HU.NN – TÍTULO` + `**PROJETO: ...**`
2. Histórico de revisão (tabela)
3. Visão geral
4. Sumário (links internos)
5. Épico e História (Como / quero / de modo que)
6. Pré-requisitos e Dependências (Passadas / Futuras)
7. Interface — telas, caminho no menu, cenários **Dado/Quando/Então**
8. Aprovação do requisito

## Comandos

```bash
# Inicializar projeto novo
python scripts/init_hus.py --projeto /caminho/cliente --nome "Sistema X"

# Uma HU
python scripts/gerar_hu_docx.py docs/requisitos/hus/HU.01\ -\ Login.md --projeto .

# Todas as HUs + consolidado
python scripts/atualizar_hus.py --projeto /caminho/cliente --pdf --consolidado
```

## Relação com contagem de PF

| Artefato | Granularidade |
|----------|---------------|
| HU | Regra de negócio, cenários, telas |
| Planilha IFPUG | Processos elementares (EE/CE/SE/ALI/AIE) |
| Proposta §2 | Escopo macro referenciando HUs |
| Termo F1–Fn | Pacotes de entrega com PF Local |

## Exemplo real

Configuração SIGVISA: [examples/sigvisa/hu-projeto.json](../examples/sigvisa/hu-projeto.json)

Matriz de referência (projeto SIGVISA): [referencias/MATRIZ-COBERTURA-HUS-SIGVISA.md](../referencias/MATRIZ-COBERTURA-HUS-SIGVISA.md)
