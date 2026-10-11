# Değişken Kapsamı (Scope) İncelemeleri

## 1. Değişebilir Varsayılan Argüman Tuzağı (Mutable Default Argument)
* **Neden Oluşur:** Python'da varsayılan parametreler fonksiyon tanımlandığı an belleğe alınır. `depo=[]` nesnesi tek bir liste olarak kalır ve tüm çağrılarda paylaşılır.
* **Çözüm:** Parametreye `None` atanmalı ve fonksiyon içinde `if depo is None: depo = []` kalıbı kullanılmalıdır.

## 2. UnboundLocalError Sebebi
* **Neden Oluşur:** Bir fonksiyon içinde değişkene bir değer atanıyorsa (`=`), Python bu değişkeni baştan sona yerel (local) kabul eder. Değer atanmadan önce değişkene erişilmeye çalışıldığında hata fırlatılır.
* **Çözüm:** Global değişkenlere doğrudan müdahale etmek yerine parametre olarak alıp yeni değeri `return` etmek gerekir.