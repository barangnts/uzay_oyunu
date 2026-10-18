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