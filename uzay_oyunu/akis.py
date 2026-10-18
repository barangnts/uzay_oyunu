from typing import Generator


def fibonacci() -> Generator[int, None, None]:

    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def yakit_gostergesi(yakit: int, tuketim: int) -> Generator[int, None, None]:

    kalan = yakit
    while kalan > 0:
        kalan = max(0, kalan - tuketim)
        yield kalan