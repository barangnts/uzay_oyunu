from typing import List, Optional


def yakit_ekle(miktar: int, depo: Optional[List[int]] = None) -> List[int]:
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo


def test_varsayilan_depo_izolasyonu() -> None:
    ilk_depo = yakit_ekle(10)
    ikinci_depo = yakit_ekle(20)

    # İkinci depoda sadece 20 olmalı, 10 sızmamalı
    assert ilk_depo == [10]
    assert ikinci_depo == [20]