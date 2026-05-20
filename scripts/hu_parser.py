"""Parser de Histórias de Usuário em Markdown."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Cenario:
    titulo: str
    dado: str
    quando: str
    entao: str


@dataclass
class Tela:
    numero: int
    titulo: str
    caminho_menu: str = ""
    screenshot: str = ""
    cenarios: list[Cenario] = field(default_factory=list)


@dataclass
class HistoricoRevisao:
    data: str
    resumo: str
    versao: str
    responsavel: str


@dataclass
class HistoriaUsuario:
    codigo: str
    titulo: str
    projeto: str = ""
    historico: list[HistoricoRevisao] = field(default_factory=list)
    visao_geral: str = ""
    sumario: list[str] = field(default_factory=list)
    epico_titulo: str = ""
    epico_texto: str = ""
    historia_titulo: str = ""
    historia_texto: str = ""
    pre_requisitos: list[str] = field(default_factory=list)
    dependencias_passadas: list[str] = field(default_factory=list)
    dependencias_futuras: list[str] = field(default_factory=list)
    telas: list[Tela] = field(default_factory=list)
    aprovacao_paragrafos: list[str] = field(default_factory=list)
    assinaturas: list[dict[str, str]] = field(default_factory=list)
    arquivo_origem: str = ""

    def para_dict(self) -> dict[str, Any]:
        return {
            "codigo": self.codigo,
            "titulo": self.titulo,
            "projeto": self.projeto,
            "historico": [h.__dict__ for h in self.historico],
            "visao_geral": self.visao_geral,
            "sumario": self.sumario,
            "epico_titulo": self.epico_titulo,
            "epico_texto": self.epico_texto,
            "historia_titulo": self.historia_titulo,
            "historia_texto": self.historia_texto,
            "pre_requisitos": self.pre_requisitos,
            "dependencias_passadas": self.dependencias_passadas,
            "dependencias_futuras": self.dependencias_futuras,
            "telas": [
                {
                    "numero": t.numero,
                    "titulo": t.titulo,
                    "caminho_menu": t.caminho_menu,
                    "screenshot": t.screenshot,
                    "cenarios": [c.__dict__ for c in t.cenarios],
                }
                for t in self.telas
            ],
            "aprovacao_paragrafos": self.aprovacao_paragrafos,
            "assinaturas": self.assinaturas,
            "arquivo_origem": self.arquivo_origem,
        }


RE_TITULO = re.compile(r"^#\s*HU\.(\d+)\s*[–—-]\s*(.+)$", re.IGNORECASE)
RE_PROJETO = re.compile(r"^\*\*PROJETO:\s*(.+?)\*\*\s*$", re.IGNORECASE)
RE_COMO_QUERO = re.compile(
    r"\*\*Como\*\*\s*(.+?)\s*\*\*quero\*\*\s*(.+?)\s*\*\*,?\s*de modo que\*\*\s*(.+?)\.?\s*$",
    re.IGNORECASE | re.DOTALL,
)
RE_CAMINHO = re.compile(r"^\*\*Caminho no menu:\*\*\s*(.+)$", re.IGNORECASE)
RE_SCREENSHOT = re.compile(r"^\*\[(.+?)\]\((.+?)\)\*\s*$|^\*\[(.+?)\]\*\s*$", re.IGNORECASE)
RE_CENARIO = re.compile(r"^\*\*Cenário\s*\d+:\s*(.+?)\*\*\s*$", re.IGNORECASE)
RE_DADO = re.compile(r"^\*\*Dado que\*\*\s*(.+)$", re.IGNORECASE)
RE_QUANDO = re.compile(r"^\*\*Quando\*\*\s*(.+)$", re.IGNORECASE)
RE_ENTAO = re.compile(r"^\*\*Então\*\*\s*(.+)$", re.IGNORECASE)
RE_TELA = re.compile(r"^###\s*Tela\s*(\d+)\s*[—–-]\s*(.+)$", re.IGNORECASE)
RE_COMPORTAMENTO = re.compile(r"^####\s*Comportamento Esperado Tela\s*(\d+)", re.IGNORECASE)


def parsear_arquivo(caminho: Path, projeto_padrao: str = "") -> HistoriaUsuario:
    texto = caminho.read_text(encoding="utf-8")
    return parsear_markdown(texto, projeto_padrao=projeto_padrao, arquivo_origem=str(caminho))


def parsear_markdown(
    texto: str,
    projeto_padrao: str = "",
    arquivo_origem: str = "",
) -> HistoriaUsuario:
    linhas = texto.splitlines()
    hu = HistoriaUsuario(codigo="", titulo="", arquivo_origem=arquivo_origem)

    for linha in linhas[:8]:
        linha_strip = linha.strip()
        m = RE_TITULO.match(linha_strip)
        if m:
            hu.codigo = f"HU.{int(m.group(1)):02d}"
            hu.titulo = m.group(2).strip()
        m_proj = RE_PROJETO.match(linha_strip)
        if m_proj:
            hu.projeto = m_proj.group(1).strip()

    if not hu.projeto:
        hu.projeto = projeto_padrao

    secoes = _split_secoes(texto)

    if "Histórico de Revisão" in secoes:
        hu.historico = _parse_historico(secoes["Histórico de Revisão"])

    if "Visão Geral" in secoes:
        hu.visao_geral = _texto_limpo(secoes["Visão Geral"])

    if "Sumário" in secoes:
        hu.sumario = _parse_sumario(secoes["Sumário"])

    for chave, secao in secoes.items():
        chave_lower = chave.lower()
        if chave_lower.startswith("épico") or chave_lower.startswith("epico"):
            hu.epico_titulo = chave
            hu.epico_texto = _extrair_como_quero(secao) or _texto_limpo(secao)
        elif "história de usuário" in chave_lower or "historia de usuario" in chave_lower:
            hu.historia_titulo = chave
            hu.historia_texto = _extrair_como_quero(secao) or _texto_limpo(secao)

    if "Pré-requisitos" in secoes:
        hu.pre_requisitos = _parse_lista(secoes["Pré-requisitos"])

    if "Dependências" in secoes:
        passadas, futuras = _parse_dependencias(secoes["Dependências"])
        hu.dependencias_passadas = passadas
        hu.dependencias_futuras = futuras

    if "Interface de Usuário" in secoes:
        hu.telas = _parse_interface(secoes["Interface de Usuário"])

    if "Aprovação do Requisito" in secoes:
        paragrafos, assinaturas = _parse_aprovacao(secoes["Aprovação do Requisito"])
        hu.aprovacao_paragrafos = paragrafos
        hu.assinaturas = assinaturas

    return hu


def _split_secoes(texto: str) -> dict[str, str]:
    secoes: dict[str, str] = {}
    atual: str | None = None
    buffer: list[str] = []

    for linha in texto.splitlines():
        if linha.startswith("## "):
            if atual is not None:
                secoes[atual] = "\n".join(buffer).strip()
            atual = linha[3:].strip()
            buffer = []
        elif linha.startswith("# ") and not linha.startswith("## "):
            continue
        elif atual is not None:
            buffer.append(linha)

    if atual is not None:
        secoes[atual] = "\n".join(buffer).strip()
    return secoes


def _parse_historico(secao: str) -> list[HistoricoRevisao]:
    itens: list[HistoricoRevisao] = []
    for linha in secao.splitlines():
        if not linha.strip().startswith("|"):
            continue
        if "---" in linha or "Data" in linha and "Versão" in linha:
            continue
        partes = [p.strip() for p in linha.strip("|").split("|")]
        if len(partes) >= 4 and partes[0]:
            itens.append(
                HistoricoRevisao(
                    data=partes[0],
                    resumo=partes[1],
                    versao=partes[2],
                    responsavel=partes[3],
                )
            )
    return itens


def _parse_sumario(secao: str) -> list[str]:
    itens: list[str] = []
    for linha in secao.splitlines():
        linha = linha.strip()
        if linha.startswith("- "):
            rotulo = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", linha[2:].strip())
            itens.append(rotulo)
    return itens


def _parse_lista(secao: str) -> list[str]:
    itens: list[str] = []
    for linha in secao.splitlines():
        linha = linha.strip()
        if linha.startswith("- "):
            itens.append(linha[2:].strip())
        elif linha and linha.lower() not in {"nenhuma", "nenhum"} and not linha.startswith("**"):
            itens.append(linha)
    return itens


def _parse_dependencias(secao: str) -> tuple[list[str], list[str]]:
    passadas: list[str] = []
    futuras: list[str] = []
    modo: str | None = None
    for linha in secao.splitlines():
        linha_strip = linha.strip()
        if linha_strip.lower() == "**passadas**":
            modo = "passadas"
            continue
        if linha_strip.lower() == "**futuras**":
            modo = "futuras"
            continue
        if linha_strip.startswith("- "):
            item = linha_strip[2:].strip()
            if modo == "passadas":
                passadas.append(item)
            elif modo == "futuras":
                futuras.append(item)
        elif linha_strip.lower() in {"nenhuma", "nenhum"} and modo:
            continue
    return passadas, futuras


def _parse_interface(secao: str) -> list[Tela]:
    telas: list[Tela] = []
    tela_atual: Tela | None = None
    cenario_parcial: dict[str, str] = {}

    for linha in secao.splitlines():
        linha_strip = linha.strip()
        if not linha_strip or linha_strip == "---":
            continue

        m_tela = RE_TELA.match(linha_strip)
        if m_tela:
            if tela_atual and cenario_parcial:
                tela_atual.cenarios.append(_cenario_de_parcial(cenario_parcial))
                cenario_parcial = {}
            tela_atual = Tela(numero=int(m_tela.group(1)), titulo=m_tela.group(2).strip())
            telas.append(tela_atual)
            continue

        if tela_atual is None:
            continue

        m_caminho = RE_CAMINHO.match(linha_strip)
        if m_caminho:
            tela_atual.caminho_menu = m_caminho.group(1).strip()
            continue

        m_shot = RE_SCREENSHOT.match(linha_strip)
        if m_shot:
            if m_shot.group(2):
                tela_atual.screenshot = m_shot.group(2)
            else:
                tela_atual.screenshot = m_shot.group(3) or m_shot.group(1) or ""
            continue

        if linha_strip.startswith("*[") and "screenshot" in linha_strip.lower():
            tela_atual.screenshot = ""
            continue

        m_cen = RE_CENARIO.match(linha_strip)
        if m_cen:
            if cenario_parcial:
                tela_atual.cenarios.append(_cenario_de_parcial(cenario_parcial))
            cenario_parcial = {"titulo": m_cen.group(1).strip()}
            continue

        m_dado = RE_DADO.match(linha_strip)
        if m_dado:
            cenario_parcial["dado"] = m_dado.group(1).strip()
            continue
        m_quando = RE_QUANDO.match(linha_strip)
        if m_quando:
            cenario_parcial["quando"] = m_quando.group(1).strip()
            continue
        m_entao = RE_ENTAO.match(linha_strip)
        if m_entao:
            cenario_parcial["entao"] = m_entao.group(1).strip()
            continue

    if tela_atual and cenario_parcial:
        tela_atual.cenarios.append(_cenario_de_parcial(cenario_parcial))

    return telas


def _cenario_de_parcial(parcial: dict[str, str]) -> Cenario:
    return Cenario(
        titulo=parcial.get("titulo", ""),
        dado=parcial.get("dado", ""),
        quando=parcial.get("quando", ""),
        entao=parcial.get("entao", ""),
    )


def _parse_aprovacao(secao: str) -> tuple[list[str], list[dict[str, str]]]:
    paragrafos: list[str] = []
    assinaturas: list[dict[str, str]] = []
    for linha in secao.splitlines():
        linha_strip = linha.strip()
        if not linha_strip:
            continue
        if linha_strip.startswith("|"):
            if "---" in linha_strip or "Data" in linha_strip and "Assinatura" in linha_strip:
                continue
            partes = [p.strip() for p in linha_strip.strip("|").split("|")]
            if len(partes) >= 4:
                assinaturas.append(
                    {
                        "data": partes[0],
                        "setor": partes[1],
                        "nome": partes[2],
                        "assinatura": partes[3],
                    }
                )
            continue
        if not linha_strip.startswith("#"):
            paragrafos.append(linha_strip)
    return paragrafos, assinaturas


def _extrair_como_quero(secao: str) -> str:
    for linha in secao.splitlines():
        linha = linha.strip()
        m = RE_COMO_QUERO.match(linha)
        if m:
            return (
                f"Como {m.group(1).strip()} quero {m.group(2).strip()}, "
                f"de modo que {m.group(3).strip()}."
            )
    return ""


def _texto_limpo(secao: str) -> str:
    linhas = []
    for linha in secao.splitlines():
        linha = linha.strip()
        if not linha or linha == "---":
            continue
        if linha.startswith("- ") or linha.startswith("|"):
            continue
        if linha.startswith("**Passadas**") or linha.startswith("**Futuras**"):
            continue
        linhas.append(linha)
    return " ".join(linhas).strip()
