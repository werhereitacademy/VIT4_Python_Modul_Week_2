#  week 2 Soru1: Öğrenci Notları İşleme

""" input ile
ogrenciler = {}

for i in range(1, 11):
    print(f"Öğrenci {i} Bilgileri:")
    ad = input("Adınız: ")
    soyad = input("Soyadınız: ")
    vize_notu = float(input("Vize Notunuz: "))
    final_notu = float(input("Final Notunuz: "))
    sozlu_notu = float(input("Sözlü Notunuz: "))

    ogrenciler[f"{ad} {soyad}"] = [vize_notu, final_notu, sozlu_notu]

# Sözlüğü ekrana yazdırmadan önce kontrol amaçlı
print("Girilen Öğrenci Bilgileri (Sözlük Hali):")
print(ogrenciler)

"""

#  hazir liste ile
ogrenciler = {
    "Ahmet Yılmaz": [85, 90, 75],
    "Ayşe Demir": [70, 80, 85],
    "Mehmet Kaya": [75, 95, 70],
    "Fatma Yıldız": [45, 55, 70],
    "Emre Öz": [80, 75, 90],
    "Zeynep Şahin": [85, 70, 65],
    "Ali Kocabaş": [75, 25, 55],
    "Aylin Yılmaz": [95, 90, 80],
    "Ahmet Çelik": [85, 75, 85],
    "Nazlı Kurt": [80, 85, 90]
}
# sozlukte not ortalamalari
not_ortalamalari = {}

for i, j in ogrenciler.items():
    not_ortalamasi = sum(j) / len(j)
    not_ortalamalari[i] = not_ortalamasi
print(not_ortalamalari)


## en yuksek not ve isim
en_yuksek_not_ortalamasi = max(not_ortalamalari.values())

for x, y in not_ortalamalari.items():
    if y == en_yuksek_not_ortalamasi:
        en_yuksek_ogrenci = x
        break
print(f"En yüksek not ortalamasına sahip öğrenci: {en_yuksek_ogrenci}, Not Ortalaması: {en_yuksek_not_ortalamasi}")


#  öğrencinin adını soyadından ayır ayrı bir tuple içinde  ve bunları bir listeye ekleyin.
ogrenci_adlari = []

for isim in ogrenciler.keys():
    ad, soyad = isim.split(" ")
    ogrenci_adlari.append((ad, soyad))
print(ogrenci_adlari)

#Adları alfabetik sıraya göre sıralayın ve sıralanmış listeyi ekrana yazdırın.

ogrenci_adlari_sirali = sorted(ogrenci_adlari)
print("Öğrenci Adları Alfabetik Sıraya Göre Sıralanmış Liste:")
print([f"{ad} {soyad}" for ad, soyad in ogrenci_adlari_sirali])


#
not_70_alti_ogrenciler = set()

for isim, notlar in ogrenciler.items():
    not_ortalamasi = sum(notlar) / len(notlar)
    if not_ortalamasi < 70:
        not_70_alti_ogrenciler.add(isim)
print("Not Ortalaması 70'in Altında Olan Öğrenciler:")
print(not_70_alti_ogrenciler)
