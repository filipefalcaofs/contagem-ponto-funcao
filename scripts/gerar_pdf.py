#!/usr/bin/env python3
"""Converte HTML em PDF com layout fiel via Playwright (Chromium)."""

from __future__ import annotations

import argparse
from pathlib import Path

from playwright.sync_api import sync_playwright


def html_para_pdf(
    html_path: Path,
    pdf_path: Path,
    *,
    cabecalho: str | None = None,
    rodape: str | None = None,
) -> Path:
    html_path = html_path.resolve()
    pdf_path.parent.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(html_path.as_uri(), wait_until="networkidle")
        page.emulate_media(media="print")
        page.pdf(
            path=str(pdf_path),
            format="Letter",
            print_background=True,
            margin={"top": "16mm", "bottom": "14mm", "left": "14mm", "right": "14mm"},
            display_header_footer=bool(cabecalho or rodape),
            header_template=cabecalho or "<span></span>",
            footer_template=rodape or "<span></span>",
        )
        browser.close()

    return pdf_path


def cabecalho_proposta(titulo_curto: str) -> str:
    return f"""
    <div style="font-size:8px; font-family:Arial,sans-serif; color:#000; width:100%; padding:0 18mm;">
      {titulo_curto}
    </div>
    """


def rodape_paginado(extra: str = "") -> str:
    bloco_extra = f"<span style='float:left'>{extra}</span>" if extra else ""
    return f"""
    <div style="font-size:8px; font-family:Arial,sans-serif; color:#000; width:100%; padding:0 18mm;">
      {bloco_extra}
      <span style="float:right">Página <span class="pageNumber"></span> de <span class="totalPages"></span></span>
    </div>
    """


def rodape_termo() -> str:
    return rodape_paginado(
        "Avenida da França, nº. 393, 2º andar – Comércio – Salvador – BA – CEP: 40.010-000 | CNPJ: 09.543.618/0001-72"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="HTML → PDF via Playwright")
    parser.add_argument("html", type=Path)
    parser.add_argument("-o", "--saida", type=Path, required=True)
    parser.add_argument("--tipo", choices=["termo", "proposta", "generico"], default="generico")
    parser.add_argument("--cabecalho", default="")
    args = parser.parse_args()

    cabecalho = args.cabecalho or None
    rodape = None
    if args.tipo == "proposta":
        cabecalho = cabecalho or cabecalho_proposta(args.cabecalho or "Proposta Comercial")
        rodape = rodape_paginado()
    elif args.tipo == "termo":
        rodape = rodape_termo()

    html_para_pdf(args.html, args.saida, cabecalho=cabecalho, rodape=rodape)
    print(f"PDF gerado: {args.saida}")


if __name__ == "__main__":
    main()
