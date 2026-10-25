from functools import lru_cache

from uzay_oyunu.dekoratorler import sure_olc


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