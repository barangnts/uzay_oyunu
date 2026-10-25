from functools import lru_cache

from uzay_oyunu.dekoratorler import log_cagri, sinirla, sure_olc


def test_sure_olc_sonuc_ve_meta() -> None:

    @sure_olc
    def ornek_toplam(a: int, b: int = 5) -> int:
        return a + b

    assert ornek_toplam(10, 20) == 30

    assert ornek_toplam(a=3, b=7) == 10

    assert ornek_toplam.__name__ == "ornek_toplam"
    assert ornek_toplam.__doc__ == "Toplama docstring."

    from functools import lru_cache
from uzay_oyunu.dekoratorler import say


def test_say_ve_dekorator_sirasi() -> None:
    @say
    def fib1(n: int) -> int:
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    fib1(20)
    assert fib1.cagri == 21891

    @say
    @lru_cache(maxsize=None)
    def fib2(n: int) -> int:
        if n < 2:
            return n
        return fib2(n - 1) + fib2(n - 2)

    fib2(20)
    assert fib2.cagri == 39

    @lru_cache(maxsize=None)
    @say
    def fib3(n: int) -> int:
        if n < 2:
            return n
        return fib3(n - 1) + fib3(n - 2)

    fib3(20)
    assert fib3.__wrapped__.cagri == 21

    from uzay_oyunu.dekoratorler import log_cagri


def test_log_cagri_calisma_ve_sonuc(capsys) -> None:

    @log_cagri
    def yolculuk(hedef: str, hiz: int = 1) -> str:
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)
    assert sonuc == "orion hiz=3"

    yakalanan = capsys.readouterr().out
    assert "-> yolculuk('orion', hiz=3)" in yakalanan
    assert "<<- yolculuk orion hiz=3" in yakalanan

    import pytest
from uzay_oyunu.komutlar import (
    KOMUTLAR,
    envanter_komutu,
    harita_komutu,
    komut,
    yardim_komutu,
)


def test_komut_kayit_ve_tekrarlanan_hata() -> None:
    with pytest.raises(ValueError, match="zaten tanimli"):
        @komut("yardim", "tekrar eden komut")
        def sahte_komut(durum):
            pass


def test_komut_fonksiyonlari() -> None:
    ornek_durum = {
        "konum": "dünya",
        "baglantilar": {"dünya": ["orion", "sirius", "kara_delik"]},
        "credits": 250,
        "engines": 2,
        "copilot": True,
    }

    harita_sonuc = harita_komutu(ornek_durum)
    assert "orion" in harita_sonuc
    assert "kara_delik" in harita_sonuc

    envanter_sonuc = envanter_komutu(ornek_durum)
    assert "250" in envanter_sonuc
    assert "Motor: 2" in envanter_sonuc

    yardim_sonuc = yardim_komutu(ornek_durum)
    assert "yardim" in yardim_sonuc
    assert "envanter" in yardim_sonuc
    assert "harita" in yardim_sonuc

    from uzay_oyunu.dekoratorler import sinirla


def test_sinirla_dekoratoru_ve_yakit_harca() -> None:

    @sinirla(0, 100)
    def yakit_harca(miktar: int) -> int:
        return 100 - miktar

    assert yakit_harca(30) == 70

    assert yakit_harca(0) == 100
    assert yakit_harca(100) == 0

    with pytest.raises(ValueError, match="150 değeri 0-100 aralığında değil"):
        yakit_harca(150)

    with pytest.raises(ValueError, match="-5 değeri 0-100 aralığında değil"):
        yakit_harca(-5)