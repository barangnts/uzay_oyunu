from typing import Any


def gorev_kaydi(baslik: str, *adimlar: str, oncelik: str = "normal", **ekler: Any) -> str:
    """Görev bilgilerini formatlanmış bir metne dönüştürür.

    Args:
        baslik: Görev başlığı.
        *adimlar: Görev adımları.
        oncelik: Görev önceliği (Yalnızca adıyla verilebilir).
        **ekler: Göreve ait ek meta veriler.

    Returns:
        str: Formatlanmış görev kaydı.
    """
    satirlar = [f"[{oncelik.upper()}] {baslik}"]

    for sira, adim in enumerate(adimlar, start=1):
        satirlar.append(f"{sira}. {adim}")

    for anahtar, deger in ekler.items():
        satirlar.append(f"{anahtar}: {deger}")

    metin = "\n".join(satirlar)
    print(metin)
    return metin


if __name__ == "__main__":
    # Normal çağrı
    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="YÜKSEK",
        sorumlu="Ayşe",
    )

    print("\n--- Argüman Açma ile Çağrı ---")
    # Listeyi (*) ve sözlüğü (**) açarak çağırma
    ornek_adimlar = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ornek_ekler = {"sorumlu": "Ayşe"}
    gorev_kaydi("Kara deliğe atla", *ornek_adimlar, oncelik="YÜKSEK", **ornek_ekler)