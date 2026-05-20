#!/usr/bin/env python3
"""Gera DOCX (e opcionalmente PDF) de uma História de Usuário a partir do Markdown."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from hu_config import carregar_config, nome_saida
from hu_docx_builder import gerar_docx_hu
from hu_parser import parsear_arquivo
from render_hu import renderizar_hu_html

try:
    from gerar_pdf import html_para_pdf
except ImportError:
    html_para_pdf = None


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera DOCX/PDF de História de Usuário")
    parser.add_argument("markdown", type=Path, help="Arquivo HU.md")
    parser.add_argument("-o", "--saida", type=Path, help="DOCX de saída")
    parser.add_argument("--pdf", type=Path, help="PDF de saída")
    parser.add_argument("--projeto", type=Path, help="Raiz do projeto cliente")
    parser.add_argument("--config", type=Path, help="hu-projeto.json")
    parser.add_argument(
        "-t",
        "--template",
        type=Path,
        default=Path(__file__).resolve().parent.parent / "templates" / "hu-modelo.docx",
    )
    parser.add_argument("--json", type=Path, help="Exportar estrutura parseada em JSON")
    args = parser.parse_args()

    if not args.markdown.is_file():
        print(f"Arquivo não encontrado: {args.markdown}", file=sys.stderr)
        sys.exit(1)

    projeto = args.projeto or args.markdown.parent.parent.parent
    config = carregar_config(args.config, projeto)
    hu = parsear_arquivo(args.markdown, projeto_padrao=config.get("nome_projeto", ""))

    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        payload = {"config": config, "hu": hu.para_dict()}
        args.json.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    saida_docx = args.saida or nome_saida(args.markdown, "docx")
    gerar_docx_hu(hu, args.template, saida_docx, config)
    print(f"DOCX: {saida_docx}")

    if args.pdf:
        if html_para_pdf is None:
            print("Playwright não disponível para PDF.", file=sys.stderr)
            sys.exit(1)
        base = Path(__file__).resolve().parent.parent
        html_temp = args.pdf.with_suffix(".html")
        renderizar_hu_html(hu, config, html_temp, base)
        html_para_pdf(html_temp, args.pdf)
        html_temp.unlink(missing_ok=True)
        print(f"PDF: {args.pdf}")


if __name__ == "__main__":
    main()
