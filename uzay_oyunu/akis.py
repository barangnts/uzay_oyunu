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

        from typing import Iterator, Tuple


def satirlari_oku(dosya_yolu: str) -> Iterator[str]:
    
    with open(dosya_yolu, "r", encoding="utf-8") as dosya:
        for satir in dosya:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz


def ayristir(satirlar: Iterator[str]) -> Iterator[Tuple[str, str, int]]:
    
    for satir in satirlar:
        parcalar = satir.split()
        kaynak = parcalar[0]
        hedef = parcalar[2]
        yakit = int(parcalar[3])
        yield (kaynak, hedef, yakit)


def uzun_yolculuklar(kayitlar: Iterator[Tuple[str, str, int]], esik: int) -> Iterator[Tuple[str, str, int]]:
    
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit