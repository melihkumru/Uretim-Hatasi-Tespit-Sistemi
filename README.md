# Üretim Hatalı Bilye Kutusu Tespit Programı

Bu Python projesi, bilye üretiminde kalite kontrol sürecini simüle eden bir programdır. Kullanıcıdan alınan kutulardaki bilye kütlelerini analiz ederek hatalı kutuları tespit eder ve istatistiksel veriler sunar.

## 📌 Amaç

Her kutuda yer alan bilyelerin ağırlıkları incelenerek:
- Tüm bilyeleri aynı ağırlıkta olan **hatasız kutular**,
- İçinde yalnızca **bir bilyesi farklı olan kutular** (ağır ya da hafif),
- **İki veya daha fazla farklı bilyesi olan hatalı kutular** tespit edilir.

## 🔧 Özellikler

- Kullanıcıdan istenilen sayıda kutu ve bilye verisi alınabilir.
- Hatalı kutular otomatik olarak tespit edilir.
- Ağırlığı farklı olan bilyeler için:
  - Farklılık miktarı (mg cinsinden)
  - Yüzdelik sapma değeri
  - En büyük ve en küçük fark değerleri
- Bütün kutular için detaylı istatistikler hesaplanır:
  - Toplam bilye sayısı
  - İade edilen bilye sayısı
  - Ağır/hafif bilyeye sahip kutular
  - Tüm bilyeleri aynı olan kutular
- Ortalama sapma değerleri gösterilir.

## ▶️ Kullanım

1. Program çalıştırıldığında kullanıcıdan kutudaki bilye sayısı istenir.
2. Her bilye için ayrı ayrı kütle bilgisi girilir.
3. Program kutunun hatalı olup olmadığını belirler.
4. Kullanıcı isterse başka kutu girişi yapabilir.
5. Giriş tamamlandığında istatistiksel özet gösterilir.

## 📊 Hesaplanan Veriler

- Hatalı kutu sayısı ve oranı  
- İade edilen bilye sayısı  
- Hatasız kutu türleri ve oranları  
- Ağır ve hafif farklılıkların ortalama fark ve yüzdesi  
- Maksimum ve minimum sapma değerleri  

## 💡 Gereksinimler

- Python 3.x

Herhangi bir ek kütüphane gerektirmez. Sadece temel `input()` ve `print()` fonksiyonları kullanılmıştır.


## 👨‍💻 Geliştirici

Bu proje, bilye üretiminde kalite kontrol senaryosu için hazırlanmıştır. Öğrenciler ve yeni başlayan Python geliştiricileri için mantıksal algoritma geliştirme konusunda örnek teşkil eder.



