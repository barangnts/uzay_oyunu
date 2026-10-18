import itertools
from uzay_oyunu.akis import fibonacci


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