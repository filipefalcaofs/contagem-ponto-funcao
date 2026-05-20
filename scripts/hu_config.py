"""Configuração de projeto para geração de HUs (genérico)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

CONFIG_PADRAO: dict[str, Any] = {
    "nome_projeto": "NOME DO PROJETO",
    "empresa": "Sudoeste Informática",
    "pasta_hus": "docs/requisitos/hus",
    "padrao_arquivo": "HU.{num:02d} - {titulo}",
    "cor_primaria": "#005ca9",
    "texto_aprovacao": [
        (
            "A {empresa} esclarece que o desenvolvimento das funcionalidades descritas neste "
            "documento foi realizado de acordo com os requisitos e especificações fornecidos "
            "pelo cliente. Nossa equipe seguiu rigorosamente as instruções recebidas, "
            "garantindo que o sistema esteja alinhado com o que foi solicitado."
        ),
        (
            "Para evitar possíveis retrabalhos ou ajustes futuros, sugerimos que o cliente "
            "revise atentamente os requisitos apresentados, verificando se eles atendem "
            "plenamente às suas necessidades e expectativas, bem como se estão em conformidade "
            "com eventuais normas aplicáveis ao seu negócio."
        ),
        (
            "Reafirmamos nosso compromisso de entregar um software de qualidade que agregue "
            "valor às operações do cliente, e a validação cuidadosa dos requisitos é um passo "
            "importante para garantir o sucesso do projeto."
        ),
    ],
    "gerar_docx": True,
    "gerar_pdf": False,
    "gerar_consolidado": False,
}

PADRAO_ARQUIVO_MD = re.compile(
    r"^HU\.(\d+)\s*[-–—]\s*(.+)\.md$",
    re.IGNORECASE,
)


def mesclar_config(dados: dict[str, Any] | None) -> dict[str, Any]:
    cfg = dict(CONFIG_PADRAO)
    if dados:
        cfg.update({k: v for k, v in dados.items() if v is not None})
    return cfg


def carregar_config(caminho: Path | None = None, projeto: Path | None = None) -> dict[str, Any]:
    candidatos: list[Path] = []
    if caminho:
        candidatos.append(caminho)
    if projeto:
        candidatos.extend(
            [
                projeto / "hu-projeto.json",
                projeto / "docs" / "requisitos" / "hu-projeto.json",
                projeto / ".hu-projeto.json",
            ]
        )
    for arquivo in candidatos:
        if arquivo.is_file():
            dados = json.loads(arquivo.read_text(encoding="utf-8"))
            return mesclar_config(dados)
    return mesclar_config(None)


def pasta_hus(projeto: Path, config: dict[str, Any]) -> Path:
    pasta = Path(config.get("pasta_hus", "docs/requisitos/hus"))
    if pasta.is_absolute():
        return pasta
    return projeto / pasta


def listar_hus_md(pasta: Path) -> list[Path]:
    if not pasta.is_dir():
        return []
    arquivos = [p for p in pasta.glob("HU.*.md") if PADRAO_ARQUIVO_MD.match(p.name)]
    return sorted(arquivos, key=_ordenar_hu)


def _ordenar_hu(caminho: Path) -> tuple[int, str]:
    m = PADRAO_ARQUIVO_MD.match(caminho.name)
    if not m:
        return (9999, caminho.name)
    return (int(m.group(1)), caminho.name)


def nome_saida(caminho_md: Path, extensao: str) -> Path:
    return caminho_md.with_suffix(f".{extensao.lstrip('.')}")
