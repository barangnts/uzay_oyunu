import itertools
from tests.istatistik import toplam_baglanti_reduce
from tests.istatistik import toplam_baglanti_reduce
from uzay_oyunu.akis import fibonacci, rota_sayaci


def test_fibonacci_yontemleri_ve_tuketim() -> None:
    
    g = fibonacci()
    assert (next(g), next(g), next(g)) == (0, 1, 1)


    ilk_12 = list(itertools.islice(fibonacci(), 12))
    assert ilk_12 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

   
    kucuk_100 = list(itertools.takewhile(lambda x: x < 100, fibonacci()))
    assert kucuk_100 == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

   
    gen = fibonacci()
    parca_1 = list(itertools.islice(gen, 3))  
    parca_2 = list(itertools.islice(gen, 3))  
    assert parca_1 != parca_2
    assert parca_2 == [2, 3, 5]

    import pytest
from uzay_oyunu.akis import yakit_gostergesi


def test_yakit_gostergesi_ve_tukenme() -> None:
    
    assert list(yakit_gostergesi(100, 30)) == [70, 40, 10, 0]

    gosterge = yakit_gostergesi(20, 20)
    assert next(gosterge) == 0
    with pytest.raises(StopIteration):
        next(gosterge)

        from uzay_oyunu.akis import ayristir, satirlari_oku, uzun_yolculuklar


def test_seyir_boru_hatti() -> None:
    
    dosya = "veri/seyir.txt"
    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(dosya)))
    assert toplam_yakit == 88

    kayitlar = ayristir(satirlari_oku(dosya))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]

    from uzay_oyunu.akis import rota_sayaci


def test_rota_sayaci_onbellek() -> None:
    
    baglantilar = {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "sirius", "orion"],
        "sirius": ["dünya", "centauri", "kara_delik"],
        "orion": ["centauri", "kara_delik"],
        "kara_delik": ["sirius", "orion"],
    }
    say = rota_sayaci(baglantilar)
    assert (say("dünya", 3), say("dünya", 10), say("dünya", 40)) == (9, 2185, 16832258606399)

    from uzay_oyunu.istatistik import (
    baglantisi_cok_filter,
    baglantisi_cok_kavrama,
    buyuk_harfli_kavrama,
    buyuk_harfli_map,
    hizli_yolculuk,
    toplam_baglanti_reduce,
    toplam_baglanti_sum,
)


def test_istatistik_fonksiyonel() -> None:
    gezegenler = ["dünya", "centauri", "sirius", "orion", "kara_delik"]
    baglantilar = {
        "dünya": ["centauri", "sirius"],
        "centauri": ["dünya", "sirius", "orion"],
        "sirius": ["dünya", "centauri", "kara_delik"],
        "orion": ["centauri", "kara_delik"],
        "kara_delik": ["sirius", "orion"],
    }

    assert buyuk_harfli_map(gezegenler) == buyuk_harfli_kavrama(gezegenler)
    assert buyuk_harfli_map(gezegenler) == ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]

    assert baglantisi_cok_filter(baglantilar) == baglantisi_cok_kavrama(baglantilar)

    assert toplam_baglanti_reduce(baglantilar) == toplam_baglanti_sum(baglantilar)
   
    sonuc = hizli_yolculuk("dünya", "sirius")
    assert "hız=3" in sonuc