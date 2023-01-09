karar = "e"
kutu_sayi = 0
hatali_kutu, iade_bilye, toplam_bilye, hepsi_ayni_kutu, agir_kutu, hafif_kutu = 0, 0, 0, 0, 0, 0
hepsi_ayni_kutu_bilye_say, hepsi_ayni_kutu_bilye_kutle, hepsi_ayni_kutu_agir_bilye_kutle, hepsi_ayni_kutu_agir_bilye_say = 0, 0, 0, 0
toplam_ag_farki_deger_AK, toplam_ag_farki_yuzde_AK, deger_farki, deger_yuzdesi = 0, 0, 0, 0
toplam_haf_farki_deger_HK, toplam_haf_farki_yuzde_HK = 0, 0
ag_max_fark, haf_max_fark, ag_max_yuzde, haf_max_yuzde = 0, 0, 0, 0
ag_min_fark, haf_min_fark, ag_min_yuzde, haf_min_yuzde = 0, 0, 0, 0

haf_farki_var = 0
ag_farki_var = 0

while karar == "e" or karar == "E":
    bilye_sayi = int(input(f"{kutu_sayi + 1}.kutudaki bilye sayısını giriniz: "))

    # Burada Kullanıcı 10 veya yüksek bir sayı girmesini sağlıyoruz.
    while bilye_sayi < 10:
        print("Lütfen 10 veya üzeri sayıda bilye sayısı giriniz!")
        bilye_sayi = int(input(f"{kutu_sayi + 1}.kutudaki bilye sayısını giriniz: "))
    toplam_bilye += bilye_sayi
    bilye = 1
    farkli_bilye = 0
    ortak_k = 0
    kutle_1, kutle_2, kutle_3, kutle, farkli_kutle, agirlik_farki = 0, 0, 0, 0, 0, 0

    # Burada ise proje hatalı kutuları tespit ediyor, hatasız kutuların ise bilgilerini topluyoruz.
    while bilye <= bilye_sayi and farkli_bilye <= 1:
        deger_farki, deger_yuzdesi = 0, 0
        kutle = int(input(f"{kutu_sayi + 1}. kutudaki {bilye}. bilyenin kütlesini giriniz: "))
        # Kütlenin pozitif bir rakam girilmesini sağlıyoruz.
        while kutle <= 0:
            print("Lütfen bilyenin kütlesini pozitif bir sayı giriniz!")
            kutle = int(input(f"{kutu_sayi + 1}. kutudaki {bilye}. bilyenin kütlesini giriniz: "))

        # Burada ise hatalı kutuyu bulmak için algoritmamız yer alıyor.
        if bilye == 1:
            kutle_1 = kutle
        elif bilye == 2:
            kutle_2 = kutle
        elif bilye == 3:
            kutle_3 = kutle
            # İlk üç kutudan sonra ortak değer buluyoruz ya da o kutunun hatalı olduğunu tespit ediyoruz.
            if kutle_1 == kutle_2 == kutle_3:
                ortak_k = kutle_1
            elif kutle_1 == kutle_2:
                ortak_k = kutle_2
                farkli_kutle = kutle_3
                farkli_bilye += 1
            elif kutle_3 == kutle_2:
                ortak_k = kutle_3
                farkli_kutle = kutle_1
                farkli_bilye += 1
            elif kutle_3 == kutle_1:
                ortak_k = kutle_1
                farkli_kutle = kutle_2
                farkli_bilye += 1
            else:
                farkli_bilye = 2

        else:  # Ortak değer bulunduktan sonra onun sayesinde diğer bilyeleri kontrol ediyoruz.
            if kutle != ortak_k:
                farkli_kutle = kutle
                farkli_bilye += 1
            # Artık iki farklı bilyemiz olduğu an program durur.
        if farkli_bilye == 2:
            bilye -= 1  # En son bilyede ise iki hatalı bilye bulunduğunda bilyeler bastırılmasının önlemini alıyoruz.
            hatali_kutu += 1
            iade_bilye += bilye_sayi
            print("Kutunuz hatalıdır.")

        # En sonda hatasız olarak gördüğümüz kutuların bilgi aşaması yer alıyor.
        if bilye == bilye_sayi:
            # Eğer farklı bilye yoksa onu tüm bilyelerin kütleleri eşit olan kutu olarak sayıyoruz.
            if farkli_bilye == 0:
                hepsi_ayni_kutu += 1
                # Kütleleri aynı olan kutulardan en çok bilyesi olanı bulmak için.
                if hepsi_ayni_kutu_bilye_say < bilye_sayi:
                    hepsi_ayni_kutu_bilye_say = bilye_sayi
                    hepsi_ayni_kutu_bilye_kutle = ortak_k
                # Kütleleri aynı olan kutulardan ortak kütlesi en çok olanı bulmak için.
                if hepsi_ayni_kutu_agir_bilye_kutle < ortak_k:
                    hepsi_ayni_kutu_agir_bilye_say = bilye_sayi
                    hepsi_ayni_kutu_agir_bilye_kutle = ortak_k
                print("Kutudaki tüm bilyelerin kütlesi eşit.")
            else:
                # Burada ise kutudaki bir farklı bilyenin ağır olması durumunda basılacak bilgiler yer alıyor.
                if farkli_kutle > ortak_k:
                    deger_farki = abs(farkli_kutle - ortak_k)
                    deger_yuzdesi = abs((deger_farki / ortak_k) * 100)

                    print("Farklı olan bilye diğer bilyelerden ağır.")
                    print(f"Ağırlık farkı: {abs(deger_farki):.2f} miligram.")
                    print(f"Ağırlık farkı yüzdesi: %{deger_yuzdesi:.2f}.")

                    toplam_ag_farki_deger_AK += deger_farki
                    toplam_ag_farki_yuzde_AK += deger_yuzdesi
                    agir_kutu += 1
                    # Burada ise daha ağır bilyesi olan kutularda min deger yuzdesini bulmaya yönelik bir algorimamız bulunmakta.
                    if ag_farki_var == 0:  # Girilen ilk daha ağır bilyesi olan kutunun değerlerini min değer olarak atıyor.
                        ag_min_yuzde = deger_yuzdesi
                        ag_min_fark = deger_farki
                        ag_farki_var += 1
                    else:  # Sonrasında ise diğerlerini onunla kıyaslıyor.
                        if deger_yuzdesi < ag_min_yuzde:
                            ag_min_fark = deger_farki
                            ag_min_yuzde = deger_yuzdesi

                    # Burada ise max değeri bulmak için algoritma var.
                    if deger_farki > ag_max_fark:
                        ag_max_fark = deger_farki
                        ag_max_yuzde = deger_yuzdesi

                else:  # Burada ise kutudaki bir farklı bilyenin hafif olması durumunda basılacak bilgiler yer alıyor.

                    deger_farki = abs(ortak_k - farkli_kutle)
                    deger_yuzdesi = abs((deger_farki / ortak_k) * 100)

                    print("Farklı olan bilye diğer bilyelerden hafif.")
                    print(f"Hafiflik farkı: {deger_farki:.2f} miligram.")
                    print(f"Hafiflik farkı yüzdesi: %{deger_yuzdesi:.2f}.")

                    toplam_haf_farki_deger_HK += deger_farki
                    toplam_haf_farki_yuzde_HK += deger_yuzdesi
                    hafif_kutu += 1
                    # Burada ise daha hafif bilyesi olan kutularda min deger yuzdesini bulmaya yönelik bir algorimamız bulunmakta.
                    if haf_farki_var == 0:  # Girilen ilk daha hafif bilyesi olan kutunun değerlerini min değer olarak atıyor.
                        haf_min_yuzde = deger_yuzdesi
                        haf_min_fark = deger_farki
                        haf_farki_var += 1
                    else:  # Sonrasında ise diğerlerini onunla kıyaslıyor.
                        if deger_yuzdesi < haf_min_yuzde:
                            haf_min_fark = deger_farki
                            haf_min_yuzde = deger_yuzdesi
                    # Burada ise max değeri bulmak için algoritma var.
                    if deger_farki > haf_max_fark:
                        haf_max_fark = deger_farki
                        haf_max_yuzde = deger_yuzdesi

            print("Kutunuz hatasızdır.")

        bilye += 1

    kutu_sayi += 1
    karar = input("Devam etmek ister misiniz? (e/E/h/H): ")
    while not karar in ['e', 'E', 'h', 'H']:
        print("Lütfen (e/E/h/H) bunlardan birini giriniz!")
        karar = input("Devam etmek ister misiniz? (e/E/h/H): ")
    if karar == 'h' or karar == 'H':
        print("Üretim hatası tespit programından çıkılıyor...")

ag_fark_deger_orta = toplam_ag_farki_deger_AK / agir_kutu
ag_fark_yuzde_orta = toplam_ag_farki_yuzde_AK / agir_kutu

haf_fark_deger_orta = toplam_haf_farki_deger_HK / hafif_kutu
haf_fark_yuzde_orta = toplam_haf_farki_yuzde_HK / hafif_kutu

print(f"Üretim hatası olan kutu sayısı: {hatali_kutu} ve tüm kutular içindeki oranı: %{hatali_kutu / kutu_sayi * 100:.2f}.")

print(f"İade edilen toplam bilye sayısı: {iade_bilye} ve kabul edilen toplam bilye sayısı: {toplam_bilye - iade_bilye}.")

print(
    f"Aynı olan kutu sayısı: {hepsi_ayni_kutu} ve yüzdesi: %{hepsi_ayni_kutu / (kutu_sayi - hatali_kutu) * 100:.2f}.\n"
    f"Ağır olan kutu sayısı: {agir_kutu} ve yüzdesi: %{agir_kutu / (kutu_sayi - hatali_kutu) * 100:.2f}.\n"
    f"Hafif olan kutu sayısı: {hafif_kutu} ve yüzdesi: %{hafif_kutu / (kutu_sayi - hatali_kutu) * 100:.2f}.")

print(
    f"1 bilyenin diğerlerinden daha ağır olduğu kutulardaki ağır olan bilyelerin ağırlık farkı değerlerinin ortalaması: {ag_fark_deger_orta:.2f} ve "
    f"ağırlık farkı yüzdelerinin ortalaması: %{ag_fark_yuzde_orta:.2f}.")
print(
    f"1 bilyenin diğerlerinden daha hafif olduğu kutulardaki hafif olan bilyelerin ağırlık farkı değerlerinin ortalaması: {haf_fark_deger_orta:.2f} ve "
    f"ağırlık farkı yüzdelerinin ortalaması: %{haf_fark_yuzde_orta:.2f}.")
print(
    f"Aynı kütledeki kutunun en fazla bilye sayısı: {hepsi_ayni_kutu_bilye_say} ve o bilyelerin ağırlığı: {hepsi_ayni_kutu_bilye_kutle:.2f} miligram.")
print(
    f"Aynı kütledeki kutunun en ağır bilye sayısı: {hepsi_ayni_kutu_agir_bilye_say} ve o bilyelerin ağırlığı: {hepsi_ayni_kutu_agir_bilye_kutle:.2f} miligram.")

if ag_max_fark > haf_max_fark:
    print(
        f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının değeri: {ag_max_fark:.2f}, "
        f"Yüzdesi: %{ag_max_yuzde:.2f} ve İşareti: Ağır.")
elif ag_max_fark < haf_max_fark:
    print(
        f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki farkın değerinin en büyük olduğu ağırlık farkının değeri: {haf_max_fark:.2f}, "
        f"Yüzdesi: %{haf_max_yuzde:.2f} ve İşareti: Hafif.")

if ag_min_fark > haf_min_fark:
    print(
        f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki yüzdesinin değerinin en küçük olduğu ağırlık farkının değeri: {haf_min_fark:.2f}, "
        f"Yüzdesi: %{haf_min_yuzde:.2f} ve İşareti: Hafif.")
else:
    print(
        f"Farklı olan bilyenin ağırlığının kutudaki diğer bilyelerin ağırlığıyla arasındaki yüzdesinin değerinin en küçük olduğu ağırlık farkının değeri: {ag_min_fark:.2f}, "
        f"Yüzdesi: %{ag_min_yuzde:.2f} ve İşareti: Ağır.")
