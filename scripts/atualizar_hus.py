#!/usr/bin/env python3
"""Atualiza DOCX/PDF de todas as HUs Markdown de um projeto."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from hu_config import carregar_config, listar_hus_md, nome_saida, pasta_hus
from hu_docx_builder import gerar_docx_hu
from hu_parser import parsear_arquivo
from render_hu import renderizar_hu_html

try:
    from gerar_pdf import html_para_pdf
except ImportError:
    html_para_pdf = None


def atualizar_pasta(
    projeto: Path,
    config_path: Path | None = None,
    template: Path | None = None,
    gerar_pdf: bool | None = None,
    consolidado: bool | None = None,
) -> list[Path]:
    base = Path(__file__).resolve().parent.parent
    config = carregar_config(config_path, projeto)
    pasta = pasta_hus(projeto, config)
    arquivos = listar_hus_md(pasta)

    if not arquivos:
        print(f"Nenhuma HU encontrada em {pasta}", file=sys.stderr)
        return []

    tpl = template or (base / "templates" / "hu-modelo.docx")
    fazer_pdf = config.get("gerar_pdf", False) if gerar_pdf is None else gerar_pdf
    fazer_consolidado = config.get("gerar_consolidado", False) if consolidado is None else consolidado

    gerados: list[Path] = []
    for md in arquivos:
        hu = parsear_arquivo(md, projeto_padrao=config.get("nome_projeto", ""))
        docx = nome_saida(md, "docx")
        gerar_docx_hu(hu, tpl, docx, config)
        gerados.append(docx)
        print(f"OK DOCX: {docx.name}")

        if fazer_pdf and html_para_pdf:
            pdf = nome_saida(md, "pdf")
            html_temp = pdf.with_suffix(".html")
            renderizar_hu_html(hu, config, html_temp, base)
            html_para_pdf(html_temp, pdf)
            html_temp.unlink(missing_ok=True)
            gerados.append(pdf)
            print(f"OK PDF:  {pdf.name}")

    if fazer_consolidado:
        from gerar_hu_consolidado import gerar_consolidado

        destino = pasta / f"HUs-{projeto.name.upper()}-CONSOLIDADO.docx"
        gerar_consolidado(arquivos, tpl, destino, config, projeto)
        gerados.append(destino)
        print(f"OK CONSOLIDADO: {destino.name}")

    print(f"\n{len(arquivos)} HU(s) processada(s).")
    return gerados


def main() -> None:
    parser = argparse.ArgumentParser(description="Atualiza DOCX/PDF de todas as HUs")
    parser.add_argument("--projeto", type=Path, default=Path.cwd(), help="Raiz do projeto")
    parser.add_argument("--config", type=Path, help="hu-projeto.json")
    parser.add_argument("-t", "--template", type=Path, help="Template DOCX")
    parser.add_argument("--pdf", action="store_true", help="Gerar PDF de cada HU")
    parser.add_argument("--consolidado", action="store_true", help="Gerar DOCX consolidado")
    parser.add_argument("--sem-docx", action="store_true", help="Não gerar DOCX (apenas PDF)")
    args = parser.parse_args()

    if args.sem_docx:
        print("--sem-docx ainda não suportado; DOCX é sempre gerado.", file=sys.stderr)

    atualizar_pasta(
        args.projeto.resolve(),
        config_path=args.config,
        template=args.template,
        gerar_pdf=args.pdf,
        consolidado=args.consolidado,
    )


if __name__ == "__main__":
    main()
