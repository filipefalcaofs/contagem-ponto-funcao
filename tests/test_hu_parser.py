"""Testes do parser de Histórias de Usuário."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from hu_parser import parsear_markdown


MODELO = """# HU.01 – LOGIN DO SISTEMA
**PROJETO: Meu Projeto**

---

## Histórico de Revisão

| Data | Resumo das Alterações | Versão | Responsável |
|:---:|---|:---:|:---:|
| 01/01/2026 | Criação | 1.0 | Empresa X |

---

## Visão Geral

Texto da visão geral.

---

## Épico: Acesso

**Como** usuário **quero** entrar **de modo que** eu use o sistema.

## História de Usuário: Login

**Como** visitante **quero** autenticar **de modo que** acesse o painel.

## Pré-requisitos

- Cadastro ativo

## Dependências

**Passadas**

- Nenhuma

**Futuras**

- HU.02 - Dashboard

---

## Interface de Usuário

### Tela 1 — Login

**Caminho no menu:** /login

#### Comportamento Esperado Tela 1

**Cenário 1: Sucesso**
**Dado que** credenciais válidas
**Quando** clicar em Entrar
**Então** redireciona ao painel

---

## Aprovação do Requisito

Texto de aprovação.
"""


def test_parse_basico():
    hu = parsear_markdown(MODELO)
    assert hu.codigo == "HU.01"
    assert hu.titulo == "LOGIN DO SISTEMA"
    assert hu.projeto == "Meu Projeto"
    assert len(hu.historico) == 1
    assert "Texto da visão geral" in hu.visao_geral
    assert hu.epico_titulo.startswith("Épico")
    assert "usuário" in hu.epico_texto
    assert len(hu.telas) == 1
    assert len(hu.telas[0].cenarios) == 1
    assert hu.telas[0].cenarios[0].entao == "redireciona ao painel"
    assert hu.dependencias_futuras == ["HU.02 - Dashboard"]


if __name__ == "__main__":
    test_parse_basico()
    print("test_parse_basico: OK")
