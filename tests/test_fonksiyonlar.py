from uzay_oyunu.oyun import envanter_metni, hedef_menusu


def test_envanter_metni_dolu() -> None:
    sonuc = envanter_metni(credits=True, engines=False, copilot=True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"


def test_envanter_metni_bos() -> None:
    assert envanter_metni(False, False, False) == ""


def test_hedef_menusu() -> None:
    hedefler = ["centauri", "sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen