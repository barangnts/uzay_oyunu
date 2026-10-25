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