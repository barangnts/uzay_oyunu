from typing import Any, Callable, Dict, Tuple

KOMUTLAR: Dict[str, Tuple[Callable, str]] = {}


def komut(ad: str, aciklama: str = "") -> Callable:
    if ad in KOMUTLAR:
        raise ValueError(f"'{ad}' adli komut zaten tanimli!")

    def dekorator(fonk: Callable) -> Callable:
        KOMUTLAR[ad] = (fonk, aciklama)
        return fonk

    return dekorator


@komut("yardim", "komutlari listeler")
def yardim_komutu(durum: Dict[str, Any]) -> str:
    satirlar = [f"{ad:<10} {aciklama}" for ad, (_, aciklama) in KOMUTLAR.items()]
    return "\n".join(satirlar)


@komut("envanter", "esyalarini gosterir")
def envanter_komutu(durum: Dict[str, Any]) -> str:
    credits = durum.get("credits", 0)
    engines = durum.get("engines", 1)
    copilot = durum.get("copilot", False)
    copilot_metni = "Var" if copilot else "Yok"
    return f"Kredi: {credits} | Motor: {engines} | Yardimci Pilot: {copilot_metni}"


@komut("harita", "gidebilecegin gezegenleri gosterir")
def harita_komutu(durum: Dict[str, Any]) -> str:
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {}).get(konum, [])
    return ", ".join(baglantilar)