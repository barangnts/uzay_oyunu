import functools
import time
from typing import Any, Callable


def sure_olc(fonk: Callable) -> Callable:
    @functools.wraps(fonk)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonk(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{fonk.__name__}: {sure:.4f} sn")
        return sonuc

    return sarmalayici

def say(fonk: Callable) -> Callable:
    @functools.wraps(fonk)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        sarmalayici.cagri += 1
        return fonk(*args, **kwargs)

    sarmalayici.cagri = 0
    return sarmalayici

def log_cagri(fonk: Callable) -> Callable:
    @functools.wraps(fonk)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        arg_listesi = [repr(a) for a in args]
        arg_listesi.extend(f"{k}={repr(v)}" for k, v in kwargs.items())
        arg_metni = ", ".join(arg_listesi)
        print(f"-> {fonk.__name__}({arg_metni})")

        sonuc = fonk(*args, **kwargs)

        print(f"<<- {fonk.__name__} {sonuc}")
        return sonuc

    return sarmalayici