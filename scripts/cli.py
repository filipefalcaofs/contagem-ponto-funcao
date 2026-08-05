#!/usr/bin/env python3
"""CLI unificada da skill contagem-ponto-funcao.

Uso:

  python scripts/cli.py info
  python scripts/cli.py pacote contagem.json -d ./saida --prefixo projeto
  python scripts/cli.py planilha contagem.json -o contagem.xlsx
  python scripts/cli.py termo contagem.json -o termo.docx --pdf termo.pdf
  python scripts/cli.py proposta contagem.json -o proposta.pdf
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
SKILL_ROOT = SCRIPTS.parent


def _run(script: str, args: list[str]) -> int:
    cmd = [sys.executable, str(SCRIPTS / script), *args]
    return subprocess.call(cmd)


def cmd_info(_: argparse.Namespace) -> int:
    print(f"SKILL_ROOT={SKILL_ROOT}")
    print(f"SCRIPTS={SCRIPTS}")
    cpm = SKILL_ROOT / "referencias" / "CPM-IFPUG-4.3.1-PT.pdf"
    planilha = SKILL_ROOT / "templates" / "planilha-contagem-modelo.xlsx"
    print(f"CPM_PDF={'ok' if cpm.is_file() else 'AUSENTE'}")
    print(f"PLANILHA_MODELO={'ok' if planilha.is_file() else 'AUSENTE'}")
    print(
        "HU_SKILL=https://github.com/filipefalcaofs/historias-usuario "
        "(use a skill irmã para Histórias de Usuário)"
    )
    return 0


def cmd_pacote(args: argparse.Namespace) -> int:
    argv = [str(args.json), "-d", str(args.dir)]
    if args.prefixo:
        argv.extend(["--prefixo", args.prefixo])
    return _run("gerar_pacote_completo.py", argv)


def cmd_planilha(args: argparse.Namespace) -> int:
    return _run("preencher_planilha.py", [str(args.json), "-o", str(args.saida)])


def cmd_termo(args: argparse.Namespace) -> int:
    argv = [str(args.json), "-o", str(args.saida)]
    if args.pdf:
        argv.extend(["--pdf", str(args.pdf)])
    return _run("gerar_termo_aceite.py", argv)


def cmd_proposta(args: argparse.Namespace) -> int:
    return _run("gerar_proposta_comercial.py", [str(args.json), "-o", str(args.saida)])


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="contagem-ponto-funcao",
        description="Contagem IFPUG CPM 4.3.1 — planilha, termo e proposta",
    )
    sub = parser.add_subparsers(dest="comando", required=True)

    p_info = sub.add_parser("info", help="Mostra caminhos da skill")
    p_info.set_defaults(func=cmd_info)

    p_pac = sub.add_parser("pacote", help="Gera planilha + termo + proposta")
    p_pac.add_argument("json", type=Path)
    p_pac.add_argument("-d", "--dir", type=Path, required=True, help="Diretório de saída")
    p_pac.add_argument("--prefixo", default="contagem")
    p_pac.set_defaults(func=cmd_pacote)

    p_pl = sub.add_parser("planilha", help="JSON → XLSX")
    p_pl.add_argument("json", type=Path)
    p_pl.add_argument("-o", "--saida", type=Path, required=True)
    p_pl.set_defaults(func=cmd_planilha)

    p_te = sub.add_parser("termo", help="JSON → Termo DOCX/PDF")
    p_te.add_argument("json", type=Path)
    p_te.add_argument("-o", "--saida", type=Path, required=True)
    p_te.add_argument("--pdf", type=Path)
    p_te.set_defaults(func=cmd_termo)

    p_pr = sub.add_parser("proposta", help="JSON → Proposta PDF")
    p_pr.add_argument("json", type=Path)
    p_pr.add_argument("-o", "--saida", type=Path, required=True)
    p_pr.set_defaults(func=cmd_proposta)

    args = parser.parse_args()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
