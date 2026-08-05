#!/usr/bin/env python3
"""Utilitários IFPUG compartilhados — complexidade e PF."""

from __future__ import annotations


def complexidade(tipo: str, td: int | float | None, ar: int | float | None) -> str:
    """Retorna L/A/H conforme fórmulas da planilha Sudoeste."""
    tipo = (tipo or "").upper()
    td = td or 0
    ar = ar or 0

    if tipo in ("ALI", "AIE"):
        if ar >= 6:
            return "H" if td >= 20 else "A"
        if ar >= 2:
            return "H" if td >= 51 else ("L" if td <= 19 else "A")
        return "L" if td <= 50 else "A"

    if tipo == "EE":
        # Tabela 6 do CPM: faixas de ALR 0-1 / 2 / >2 (ou seja, >= 3)
        if ar >= 3:
            return "H" if td >= 5 else "A"
        if ar == 2:
            return "H" if td >= 16 else ("L" if td <= 4 else "A")
        return "L" if td <= 15 else "A"

    if tipo in ("CE", "SE"):
        # Tabela 7 do CPM: faixas de ALR 0-1 / 2-3 / >3 (ou seja, >= 4)
        if ar >= 4:
            return "H" if td >= 6 else "A"
        if ar >= 2:
            return "H" if td >= 20 else ("L" if td <= 5 else "A")
        return "L" if td <= 19 else "A"

    return "L"


TABELA_PF: dict[str, dict[str, int]] = {
    "ALI": {"L": 7, "A": 10, "H": 15},
    "AIE": {"L": 5, "A": 7, "H": 10},
    "EE": {"L": 3, "A": 4, "H": 6},
    "CE": {"L": 3, "A": 4, "H": 6},
    "SE": {"L": 4, "A": 5, "H": 7},
}


def calcular_pf(tipo: str, td: int | float | None, ar: int | float | None) -> int:
    tipo = (tipo or "").upper()
    comp = complexidade(tipo, td, ar)
    return TABELA_PF.get(tipo, {}).get(comp, 0)
