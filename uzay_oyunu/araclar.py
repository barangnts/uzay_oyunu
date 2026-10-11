import time
from typing import Any, Callable, Dict, List


def hamle_sayaci() -> Callable[[], int]:
    sayac = 0

    def artir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return artir


def en_bagli_gezegenler(galaksi: Dict[str, Any]) -> List[str]:
    baglantilar: Dict[str, List[str]] = galaksi.get("baglantilar", {})
    gezegenler: List[str] = list(baglantilar.keys())

    return sorted(gezegenler, key=lambda g: (-len(baglantilar[g]), g))


def sure_olc(fonksiyon: Callable) -> Callable:
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic
        print(f"[{fonksiyon.__name__}] Çalışma süresi: {gecen_sure:.6f} saniye")
        return sonuc

    return sarmalayici