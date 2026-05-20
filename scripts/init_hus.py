#!/usr/bin/env python3
"""Inicializa estrutura de HUs em um projeto novo."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path


def init_projeto(
    projeto: Path,
    nome_projeto: str,
    empresa: str = "Sudoeste Informática",
    pasta_hus: str = "docs/requisitos/hus",
    copiar_template_md: bool = True,
) -> Path:
    pasta = projeto / pasta_hus
    pasta.mkdir(parents=True, exist_ok=True)
    (pasta / "screenshots").mkdir(exist_ok=True)

    config = {
        "nome_projeto": nome_projeto,
        "empresa": empresa,
        "pasta_hus": pasta_hus,
        "padrao_arquivo": "HU.{num:02d} - {titulo}",
        "cor_primaria": "#005ca9",
        "gerar_docx": True,
        "gerar_pdf": False,
        "gerar_consolidado": True,
    }
    config_path = projeto / "hu-projeto.json"
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8")

    base = Path(__file__).resolve().parent.parent
    if copiar_template_md:
        modelo = base / "templates" / "hu-modelo.md"
        destino = pasta / "HU.01 - Exemplo.md"
        if modelo.is_file() and not destino.exists():
            texto = modelo.read_text(encoding="utf-8")
            texto = texto.replace("NOME DO PROJETO", nome_projeto)
            texto = texto.replace("Sudoeste Informática", empresa)
            destino.write_text(texto, encoding="utf-8")

    matriz = pasta / "MATRIZ-COBERTURA-HUS.md"
    if not matriz.exists():
        matriz.write_text(
            "# Matriz de Cobertura — Histórias de Usuário\n\n"
            "| HU | Título | Status | Módulo | Observações |\n"
            "|----|--------|--------|--------|-------------|\n"
            "| HU.01 | Exemplo | Rascunho | — | — |\n",
            encoding="utf-8",
        )

    print(f"Config: {config_path}")
    print(f"Pasta HUs: {pasta}")
    return pasta


def main() -> None:
    parser = argparse.ArgumentParser(description="Inicializa HUs em um projeto")
    parser.add_argument("--projeto", type=Path, default=Path.cwd())
    parser.add_argument("--nome", required=True, help="Nome completo do projeto")
    parser.add_argument("--empresa", default="Sudoeste Informática")
    parser.add_argument("--pasta", default="docs/requisitos/hus")
    args = parser.parse_args()

    init_projeto(args.projeto.resolve(), args.nome, args.empresa, args.pasta)


if __name__ == "__main__":
    main()
