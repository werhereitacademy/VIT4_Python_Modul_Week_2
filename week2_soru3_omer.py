musteriler = {}
# Yeni müşteri eklemek
def yeni_musteri_ekle():
    musteri_id = input("Müşteri Kimliği (ID) girin: ")
    ad = input("Adinizi girin: ")
    soyad = input("Soyadinizi girin: ")
    email = input("E-posta adresinizi girin: ")
    telefon = input("Telefon numaranizi girin: ")

    musteri = {
        'Ad': ad,
        'Soyad': soyad,
        'E-posta': email,
        'Telefon': telefon
    }

    musteriler[musteri_id] = musteri
    print(f"{ad} {soyad} müşterisi eklenmiştir.")

# Müşteri bilgilerini güncellemek
def musteri_guncelle():
    musteri_id = input("Güncellemek istediğiniz müşterinin kimliğini (ID) girin: ")

    if musteri_id in musteriler:
        print(f"{musteri_id} müşterisinin mevcut bilgileri:")
        mevcut_musteri = musteriler[musteri_id]
        for anahtar, deger in mevcut_musteri.items():
            print(f"{anahtar}: {deger}")

        ad = input("Yeni adi girin (değiştirmek istemiyorsaniz boş birakin): ")
        soyad = input("Yeni soyadi girin (değiştirmek istemiyorsaniz boş birakin): ")
        email = input("Yeni e-postayi girin (değiştirmek istemiyorsaniz boş birakin): ")
        telefon = input("Yeni telefon numarasini girin (değiştirmek istemiyorsaniz boş birakin): ")

        if ad:
            mevcut_musteri['Ad'] = ad
        if soyad:
            mevcut_musteri['Soyad'] = soyad
        if email:
            mevcut_musteri['E-posta'] = email
        if telefon:
            mevcut_musteri['Telefon'] = telefon

        musteriler[musteri_id] = mevcut_musteri
        print(f"{musteri_id} müşteri bilgileri güncellendi.")
    else:
        print(f"{musteri_id} müşterisi bulunamadi.")

# Müşteri silmek
def musteri_sil():
    musteri_id = input("Silmek istediğiniz müşterinin kimliğini (ID) girin: ")

    if musteri_id in musteriler:
        silinen_musteri = musteriler.pop(musteri_id)
        print(f"{silinen_musteri['Ad']} {silinen_musteri['Soyad']} müşterisi silinmiştir.")
    else:
        print(f"{musteri_id} müşterisi bulunamadi.")

# Tüm müşterileri listeleme
def musterileri_listele():
    if len(musteriler) == 0:
        print("Henüz müşteri kaydi yok.")
    else:
        print("\nTüm Müşteriler:")
        for musteri_id, musteri in musteriler.items():
            print(f"Müşteri Kimliği (ID): {musteri_id}")
            for anahtar, deger in musteri.items():
                print(f"{anahtar}: {deger}")
            print("-" * 30)

# Ana program döngüsü
while True:
    print("\nMüşteri Yönetim Sistemi")
    print("1. Yeni Müşteri Ekle")
    print("2. Müşteri Bilgilerini Güncelle")
    print("3. Müşteri Sil")
    print("4. Tüm Müşterileri Listele")
    print("5. Çikiş")

    secim = input("Yapmak istediğiniz işlemi seçin: ")

    if secim == '1':
        yeni_musteri_ekle()
    elif secim == '2':
        musteri_guncelle()
    elif secim == '3':
        musteri_sil()
    elif secim == '4':
        musterileri_listele()
    elif secim == '5':
        print("Programdan çikiliyor...")
        break
    else:
        print("Geçersiz seçenek! Lütfen tekrar deneyin.")
