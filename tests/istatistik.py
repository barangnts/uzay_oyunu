from functools import partial, reduce
from typing import Dict, List


def buyuk_harfli_map(gezegenler: List[str]) -> List[str]:
    return list(map(lambda g: g.upper(), gezegenler))

def buyuk_harfli_kavrama(gezegenler: List[str]) -> List[str]:
    return [g.upper() for g in gezegenler]

def baglantisi_cok_filter(baglantilar: Dict[str, List[str]]) -> List[str]:
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar.keys()))

def baglantisi_cok_kavrama(baglantilar: Dict[str, List[str]]) -> List[str]:
    return [g for g, komsular in baglantilar.items() if len(komsular) >= 2]

def toplam_baglanti_reduce(baglantilar: Dict[str, List[str]]) -> int:
    return reduce(lambda acc, g: acc + len(baglantilar[g]), baglantilar, 0)

def toplam_baglanti_sum(baglantilar: Dict[str, List[str]]) -> int:
    return sum(len(komsular) for komsular in baglantilar.values())

def yolculuk(kaynak: str, hedef: str, hiz: int = 1) -> str:
    return f"{kaynak} noktasından {hedef} noktasına hız={hiz} ile gidildi."

hizli_yolculuk = partial(yolculuk, hiz=3)

