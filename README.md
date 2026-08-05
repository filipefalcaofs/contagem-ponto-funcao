# Skill: Contagem de Ponto de Função (IFPUG CPM 4.3.1)

Skill autocontida para **contar** um sistema pelo IFPUG CPM 4.3.1 e **gerar** os entregáveis comerciais.

## O que a skill faz

1. **Analisa** o projeto (requisitos, HUs, telas, fluxos, código como apoio)
2. **Produz** o JSON de contagem (`contagem-*.json`) com grupos, ALI/AIE, EE/CE/SE, TDs, complexidades e PF
3. **Gera** a partir desse JSON:
   - Planilha de contagem (XLSX)
   - Termo de Entrega e Aceite (DOCX + PDF)
   - Proposta Comercial (PDF)

O JSON é o **artefato intermediário** da contagem (fonte de verdade editável/auditável). Os scripts **não** inventam a contagem sozinhos — o agente (ou o analista) monta o JSON seguindo o CPM; depois os scripts materializam planilha/termo/proposta.

Funciona em **qualquer projeto**.

> Histórias de Usuário (HU) ficam na skill irmã:  
> [filipefalcaofs/historias-usuario](https://github.com/filipefalcaofs/historias-usuario)

## Instalação (Cursor)

```bash
git clone https://github.com/filipefalcaofs/contagem-ponto-funcao.git ~/.cursor/skills/contagem-ponto-funcao
pip install -r ~/.cursor/skills/contagem-ponto-funcao/requirements.txt
playwright install chromium
```

Confirme:

```bash
python3 ~/.cursor/skills/contagem-ponto-funcao/scripts/cli.py info
```

### Manual IFPUG (CPM 4.3.1 PT-BR)

O PDF completo (~2,7 MB) está em `referencias/CPM-IFPUG-4.3.1-PT.pdf`. Se o clone não trouxer o arquivo, baixe o manual IFPUG CPM 4.3.1 em português e coloque nesse caminho.

## Fluxo completo

```text
Projeto (requisitos/HUs/telas)
        ↓  agente segue SKILL.md (CPM 4.3.1)
contagem-projeto.json          ← gera / atualiza este arquivo
        ↓  scripts
planilha.xlsx + termo + proposta
```

Schema de referência: [`templates/contagem-exemplo.json`](templates/contagem-exemplo.json)

## Uso com agente (Cursor)

Com a skill instalada, peça:

> Conte os pontos de função deste projeto: monte o JSON IFPUG e gere planilha, termo e proposta.

O agente deve seguir [`SKILL.md`](SKILL.md): tipo de contagem → fronteira → dados → transações → JSON → XLSX/termo/proposta.

## Scripts (a partir do JSON já montado)

```bash
SKILL=~/.cursor/skills/contagem-ponto-funcao

# Pacote completo (planilha + termo + proposta)
python3 $SKILL/scripts/cli.py pacote contagem.json -d ./saida --prefixo projeto

# Ou scripts individuais
python3 $SKILL/scripts/preencher_planilha.py contagem.json -o contagem.xlsx
python3 $SKILL/scripts/gerar_termo_aceite.py contagem.json -o termo.docx --pdf termo.pdf
python3 $SKILL/scripts/gerar_proposta_comercial.py contagem.json -o proposta.pdf
```

Há também o caminho inverso (planilha editada → JSON): `scripts/extrair_planilha_para_json.py`.

## Histórias de Usuário

Para HU no padrão Sudoeste (capa, logo, faixa, PDF):

```bash
git clone https://github.com/filipefalcaofs/historias-usuario.git ~/.cursor/skills/historias-usuario
pip install -r ~/.cursor/skills/historias-usuario/requirements.txt

python3 ~/.cursor/skills/historias-usuario/scripts/cli.py init \
  --projeto /caminho/do/projeto --nome "Sistema X" --sem-exemplo
python3 ~/.cursor/skills/historias-usuario/scripts/cli.py atualizar \
  --projeto /caminho/do/projeto --pdf --consolidado
```

Os scripts `*_hu*` desta skill permanecem só por compatibilidade; preferir `historias-usuario`.

## Estrutura do repositório

```
contagem-ponto-funcao/
├── SKILL.md                 # Instruções para agentes
├── README.md
├── requirements.txt
├── scripts/
│   ├── cli.py               # entrada única
│   ├── preencher_planilha.py
│   ├── gerar_termo_aceite.py
│   ├── gerar_proposta_comercial.py
│   ├── gerar_pacote_completo.py
│   └── ...
├── templates/               # Planilha, termo, proposta, JSON exemplo
├── referencias/             # Extratos CPM + PDF IFPUG
└── entregaveis/             # Guias por tipo de documento
```

## Dependências

Ver [`requirements.txt`](requirements.txt). Sistema: Python 3.9+, Playwright (Chromium) para PDFs institucionais.

## Licença

MIT — adapte textos institucionais e identidade visual ao seu cliente.
