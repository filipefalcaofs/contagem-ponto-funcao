#!/usr/bin/env python3
"""Gera pacote completo: planilha + termo (DOCX/PDF) + proposta (PDF)."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

import openpyxl

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

from preencher_planilha import escrever_grupos, limpar_dados_funcoes, preencher_identificacao
from gerar_termo_aceite import gerar_docx as gerar_termo_docx, gerar_pdf as gerar_termo_pdf
from gerar_proposta_comercial import gerar_proposta


def gerar_planilha(dados: dict, template: Path, saida: Path) -> None:
    saida.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(template, saida)
    wb = openpyxl.load_workbook(saida)
    preencher_identificacao(wb["Contagem"], dados.get("identificacao", {}))
    limpar_dados_funcoes(wb["Funções"])
    escrever_grupos(wb["Funções"], dados.get("grupos", []))
    wb.save(saida)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera entregáveis completos de contagem APF")
    parser.add_argument("json", type=Path)
    parser.add_argument("-d", "--dir", type=Path, required=True, help="Diretório de saída")
    parser.add_argument("--prefixo", default="contagem", help="Prefixo dos arquivos gerados")
    args = parser.parse_args()

    base = Path(__file__).resolve().parent.parent
    templates = base / "templates"
    args.dir.mkdir(parents=True, exist_ok=True)

    prefixo = args.prefixo
    planilha = args.dir / f"contagem-{prefixo}-desenvolvimento.xlsx"
    termo_docx = args.dir / f"Termo de Entrega e Aceite - {prefixo.upper()}.docx"
    termo_pdf = args.dir / f"Termo de Entrega e Aceite - {prefixo.upper()}.pdf"
    proposta_pdf = args.dir / f"Proposta Comercial - {prefixo.upper()}.pdf"

    with args.json.open(encoding="utf-8") as f:
        dados = json.load(f)

    gerar_planilha(dados, templates / "planilha-contagem-modelo.xlsx", planilha)
    gerar_termo_docx(dados, templates / "termo-entrega-aceite-modelo.docx", termo_docx)
    gerar_termo_pdf(args.json, base, termo_pdf)
    gerar_proposta(args.json, proposta_pdf, base)

    print("\nPacote gerado:")
    print(f"  Planilha:  {planilha}")
    print(f"  Termo DOCX: {termo_docx}")
    print(f"  Termo PDF:  {termo_pdf}")
    print(f"  Proposta PDF: {proposta_pdf}")


if __name__ == "__main__":
    main()
