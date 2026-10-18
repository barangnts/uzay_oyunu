# Uzay Oyunu - Python Projesi

## Öğrenci Bilgileri
* **Ad Soyad:** Baran Güntaş
* **Öğrenci Numarası:** 20253004023
* **Bölüm:** Bilişim Sistemleri ve Teknolojileri

## Proje Hakkında
Bu depo, modüler fonksiyonlar, argüman yönetimi, değişken kapsamı (scope), closure, lambda ve dekoratör yapılarını içeren Python uzay oyunu ödevini içermektedir.

* **Önbelleksiz rota_sayisi (adım=20):** ~2.34 saniye
* **@lru_cache Önbellekli rota_sayisi (adım=20):** ~0.00004 saniye
* **cache_info() Çıktısı:** `CacheInfo(hits=105, misses=21, maxsize=None, currsize=21)`

## Meşgul Bekleme (Busy Waiting) ve time.sleep Farkı
`zamanlayici()` üreteci `while True` döngüsü içinde sürekli `time.perf_counter()` kontrolü yaptığı için işlemciyi (CPU) %100 yük altında tutar; buna "meşgul bekleme" (busy waiting) denir. 
`time.sleep()` ise işletim sistemine o anki iş parçacığını (thread) uyutmasını bildirir. Bu süreçte işlemci döngüde sıkışıp kalmaz, boşa çıkar ve diğer sistem işlerini yürütür; kaynak israfı engellenmiş olur.