#!/usr/bin/env python3
"""Renderiza templates HTML Jinja2 para documentos comerciais."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from ifpug_calc import calcular_pf


def formatar_pf_br(valor: float | int) -> str:
    return f"{float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def preparar_contexto(dados: dict[str, Any]) -> dict[str, Any]:
    ctx = dict(dados)
    grupos = []
    total = 0.0

    for idx, grupo in enumerate(dados.get("grupos", []), start=1):
        itens_fmt = []
        for item in grupo.get("itens", []):
            pf = item.get("pf_local") or item.get("pf")
            if pf is None:
                pf = calcular_pf(item.get("tipo", ""), item.get("td"), item.get("ar"))
            pf = float(pf or 0)
            total += pf
            nome = item["nome"]
            tipo = item.get("tipo", "")
            if tipo and f" - {tipo}" not in nome:
                nome_exibicao = f"{nome} - {tipo}"
            else:
                nome_exibicao = nome
            itens_fmt.append({
                **item,
                "nome_exibicao": nome_exibicao,
                "pf_fmt": formatar_pf_br(pf),
            })
        grupos.append({
            "id": grupo.get("id") or f"F{idx}",
            "nome": grupo["nome"],
            "itens": itens_fmt,
        })

    termo = dict(dados.get("termo", {}))
    if termo.get("total_pf") is not None:
        total = float(termo["total_pf"])
    ctx["grupos"] = grupos
    ctx["total_pf"] = total
    ctx["total_pf_fmt"] = formatar_pf_br(total)
    ctx["termo"] = termo
    ctx["proposta"] = dados.get("proposta", {})
    ctx["escopo_macro"] = dados.get("escopo_macro", [])
    ctx["resumo_pf"] = dados.get("resumo_pf", {})
    ctx["secoes_adicionais"] = dados.get("secoes_adicionais", [])
    ctx["metodologia_contagem"] = dados.get(
        "metodologia_contagem",
        dados.get("proposta", {}).get("metodologia_contagem", ""),
    )
    ctx["identificacao"] = dados.get("identificacao", {})
    return ctx


def renderizar(template_nome: str, dados: dict[str, Any], templates_dir: Path) -> str:
    css = (templates_dir / "html" / "documentos.css").read_text(encoding="utf-8")
    env = Environment(
        loader=FileSystemLoader(str(templates_dir / "html")),
        autoescape=select_autoescape(["html"]),
    )
    env.filters["formatar_pf"] = formatar_pf_br
    template = env.get_template(template_nome)
    return template.render(estilos=css, **preparar_contexto(dados))


def renderizar_arquivo(template_nome: str, json_path: Path, saida_html: Path, base_dir: Path | None = None) -> Path:
    base = base_dir or Path(__file__).resolve().parent.parent
    with json_path.open(encoding="utf-8") as f:
        dados = json.load(f)
    html = renderizar(template_nome, dados, base / "templates")
    saida_html.parent.mkdir(parents=True, exist_ok=True)
    saida_html.write_text(html, encoding="utf-8")
    return saida_html
