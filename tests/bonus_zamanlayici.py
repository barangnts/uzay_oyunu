import time
from typing import Generator


def zamanlayici() -> Generator[float, None, None]:
    baslangic = time.perf_counter()
    while True:
        yield time.perf_counter() - baslangic


def calistir() -> None:
    saat = zamanlayici()
    son_tik = 0.0
    son_tak = 0.0
    baslangic = time.perf_counter()

    while time.perf_counter() - baslangic < 10.0:
        gecen = next(saat)
        if gecen - son_tik >= 2.0:
            print("tik")
            son_tik = gecen
        if gecen - son_tak >= 5.0:
            print("tak")
            son_tak = gecen


if __name__ == "__main__":
    calistir()