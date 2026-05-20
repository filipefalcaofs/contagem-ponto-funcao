"""Renderiza HU em HTML (Jinja2) para PDF."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader, select_autoescape

from hu_parser import HistoriaUsuario


def renderizar_hu_html(
    hu: HistoriaUsuario,
    config: dict[str, Any],
    saida: Path,
    base_dir: Path,
) -> None:
    templates = base_dir / "templates" / "html"
    env = Environment(
        loader=FileSystemLoader(str(templates)),
        autoescape=select_autoescape(["html", "xml"]),
    )
    template = env.get_template("hu-documento.html")
    empresa = config.get("empresa", "Sudoeste Informática")
    textos_aprovacao = hu.aprovacao_paragrafos or [
        t.format(empresa=empresa) for t in config.get("texto_aprovacao", [])
    ]
    html = template.render(
        hu=hu,
        config=config,
        textos_aprovacao=textos_aprovacao,
        cor_primaria=config.get("cor_primaria", "#005ca9"),
    )
    saida.parent.mkdir(parents=True, exist_ok=True)
    saida.write_text(html, encoding="utf-8")


def renderizar_hu_de_arquivo(
    markdown: Path,
    config: dict[str, Any],
    saida: Path,
    base_dir: Path,
) -> None:
    from hu_parser import parsear_arquivo

    hu = parsear_arquivo(markdown, projeto_padrao=config.get("nome_projeto", ""))
    renderizar_hu_html(hu, config, saida, base_dir)


def renderizar_hu_json(json_path: Path, saida: Path, base_dir: Path) -> None:
    dados = json.loads(json_path.read_text(encoding="utf-8"))
    config = dados.get("config", {})
    hu_dict = dados["hu"]
    from hu_parser import HistoriaUsuario, HistoricoRevisao, Tela, Cenario

    hu = HistoriaUsuario(
        codigo=hu_dict["codigo"],
        titulo=hu_dict["titulo"],
        projeto=hu_dict.get("projeto", ""),
        visao_geral=hu_dict.get("visao_geral", ""),
        sumario=hu_dict.get("sumario", []),
        epico_titulo=hu_dict.get("epico_titulo", ""),
        epico_texto=hu_dict.get("epico_texto", ""),
        historia_titulo=hu_dict.get("historia_titulo", ""),
        historia_texto=hu_dict.get("historia_texto", ""),
        pre_requisitos=hu_dict.get("pre_requisitos", []),
        dependencias_passadas=hu_dict.get("dependencias_passadas", []),
        dependencias_futuras=hu_dict.get("dependencias_futuras", []),
        aprovacao_paragrafos=hu_dict.get("aprovacao_paragrafos", []),
        assinaturas=hu_dict.get("assinaturas", []),
    )
    hu.historico = [HistoricoRevisao(**h) for h in hu_dict.get("historico", [])]
    for t in hu_dict.get("telas", []):
        tela = Tela(
            numero=t["numero"],
            titulo=t["titulo"],
            caminho_menu=t.get("caminho_menu", ""),
            screenshot=t.get("screenshot", ""),
        )
        tela.cenarios = [Cenario(**c) for c in t.get("cenarios", [])]
        hu.telas.append(tela)
    renderizar_hu_html(hu, config, saida, base_dir)
