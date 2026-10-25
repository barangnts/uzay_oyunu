from uzay_oyunu.dekoratorler import sure_olc


def test_sure_olc_sonuc_ve_meta() -> None:

    @sure_olc
    def ornek_toplam(a: int, b: int = 5) -> int:
        return a + b

    assert ornek_toplam(10, 20) == 30

    assert ornek_toplam(a=3, b=7) == 10

    assert ornek_toplam.__name__ == "ornek_toplam"
    assert ornek_toplam.__doc__ == "Toplama docstring."