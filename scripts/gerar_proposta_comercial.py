#!/usr/bin/env python3
"""Gera Proposta Comercial com layout fiel ao modelo SALUS (PDF via Playwright)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from render_documento import renderizar_arquivo
from gerar_pdf import cabecalho_proposta, html_para_pdf, rodape_paginado


def gerar_proposta(json_path: Path, saida_pdf: Path, base_dir: Path) -> None:
    with json_path.open(encoding="utf-8") as f:
        dados = json.load(f)

    proposta = dados.get("proposta", {})
    sistema = proposta.get("sistema", "Sistema")
    cabecalho_txt = proposta.get(
        "cabecalho_pdf",
        f"Proposta Comercial — {sistema}",
    )

    html_temp = saida_pdf.with_suffix(".html")
    renderizar_arquivo("proposta-comercial.html", json_path, html_temp, base_dir)
    html_para_pdf(
        html_temp,
        saida_pdf,
        cabecalho=cabecalho_proposta(cabecalho_txt),
        rodape=rodape_paginado(),
    )
    html_temp.unlink(missing_ok=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera Proposta Comercial PDF")
    parser.add_argument("json", type=Path)
    parser.add_argument("-o", "--saida", type=Path, required=True, help="PDF de saída")
    args = parser.parse_args()
    base = Path(__file__).resolve().parent.parent
    gerar_proposta(args.json, args.saida, base)
    print(f"Proposta PDF: {args.saida}")


if __name__ == "__main__":
    main()
