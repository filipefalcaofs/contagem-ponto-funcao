# Contagem de Ponto de Função + Histórias de Usuário

Skill autosuficiente para **contagem IFPUG CPM 4.3.1**, geração de **planilha**, **termo de aceite**, **proposta comercial** e **histórias de usuário (HU)** em qualquer projeto.

## Instalação

```bash
git clone https://github.com/filipefalcaofs/contagem-ponto-funcao.git
cd contagem-ponto-funcao
pip install -r requirements.txt
playwright install chromium
```

### Manual IFPUG (CPM 4.3.1 PT-BR)

O PDF completo (~2,7 MB) está em `referencias/CPM-IFPUG-4.3.1-PT.pdf`. Se clonar sem LFS, baixe o manual IFPUG CPM 4.3.1 em português e coloque nesse caminho.

## Uso no Cursor

```bash
git clone https://github.com/filipefalcaofs/contagem-ponto-funcao.git ~/.cursor/skills/contagem-ponto-funcao
```

Ou adicione como submódulo em projetos que usam a skill.

## Histórias de Usuário (qualquer projeto)

### 1. Inicializar estrutura no projeto cliente

```bash
cd /caminho/do/seu-projeto
python /caminho/contagem-ponto-funcao/scripts/init_hus.py \
  --nome "Meu Sistema — Descrição completa" \
  --empresa "Minha Empresa"
```

Cria:

- `hu-projeto.json` — configuração do projeto
- `docs/requisitos/hus/` — pasta das HUs (Markdown = fonte de verdade)
- `docs/requisitos/hus/HU.01 - Exemplo.md` — modelo
- `docs/requisitos/hus/MATRIZ-COBERTURA-HUS.md`

### 2. Editar HUs em Markdown

Padrão de arquivo: `HU.NN - Título descritivo.md`

Consulte `templates/hu-modelo.md` e `entregaveis/historias-usuario.md`.

### 3. Gerar DOCX / PDF

Uma HU:

```bash
python scripts/gerar_hu_docx.py docs/requisitos/hus/HU.01\ -\ Exemplo.md \
  --projeto . \
  --pdf docs/requisitos/hus/HU.01\ -\ Exemplo.pdf
```

Todas as HUs:

```bash
python scripts/atualizar_hus.py --projeto /caminho/do/projeto --pdf --consolidado
```

Consolidado:

```bash
python scripts/gerar_hu_consolidado.py --projeto /caminho/do/projeto
```

### Configuração (`hu-projeto.json`)

```json
{
  "nome_projeto": "Meu Sistema — Descrição",
  "empresa": "Sudoeste Informática",
  "pasta_hus": "docs/requisitos/hus",
  "cor_primaria": "#005ca9",
  "gerar_docx": true,
  "gerar_pdf": false,
  "gerar_consolidado": true
}
```

## Contagem de PF + entregáveis comerciais

```bash
python scripts/preencher_planilha.py contagem.json -o contagem.xlsx
python scripts/gerar_termo_aceite.py contagem.json -o termo.docx --pdf termo.pdf
python scripts/gerar_proposta_comercial.py contagem.json -o proposta.pdf
python scripts/gerar_pacote_completo.py contagem.json -d ./saida --prefixo projeto
```

Documentação detalhada: [SKILL.md](SKILL.md)

## Estrutura do repositório

```
├── SKILL.md                 # Instruções para agentes IA
├── README.md
├── requirements.txt
├── templates/
│   ├── hu-modelo.docx       # Layout Word
│   ├── hu-modelo.md         # Layout Markdown
│   ├── hu-projeto.exemplo.json
│   ├── planilha-contagem-modelo.xlsx
│   └── html/                # Templates PDF
├── scripts/
│   ├── hu_parser.py
│   ├── hu_docx_builder.py
│   ├── gerar_hu_docx.py
│   ├── atualizar_hus.py
│   ├── gerar_hu_consolidado.py
│   ├── init_hus.py
│   └── ...                  # Planilha, termo, proposta
├── referencias/             # Extratos CPM IFPUG
└── entregaveis/             # Guias por tipo de documento
```

## Licença

MIT — templates de documento: adapte textos institucionais ao seu cliente.
