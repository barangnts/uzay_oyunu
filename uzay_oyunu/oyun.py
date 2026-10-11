from typing import List


def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    esyalar: List[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("güçlü motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""
    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: List[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    for sira, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{sira}] {hedef}")
    return "\n".join(satirlar)

import json
from typing import Any, Dict


def galaksi_kur(
    gezegenler: List[str],
    baglantilar: Dict[str, List[str]],
    baslangic: str,
    **kwargs: Any
) -> Dict[str, Any]:
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde bulunamadı!")

    yakit = kwargs.get("yakit", 50)

    return {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }


def galaksi_yukle(dosya_yolu: str = "uzay_oyunu/galaksi.json") -> Dict[str, Any]:
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        veri = json.load(dosya)
    return galaksi_kur(**veri)