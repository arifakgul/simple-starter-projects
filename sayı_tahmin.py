from random import randint
from time import sleep
print("""
*********************************
Sayı Tahmin Oyunu
1 ile 1000 Arasındaki Sayıyı Bul
(Çıkmak için q'ya basın.)
*********************************
""")
rasgele_sayı = randint(1,1000)
tahmin_hakkı = 10
while True:
    tahmin = input("Tahmininiz:")

    if (tahmin == "q"):
        print("Oyun Sonlandırılıyor...")
        break
    tahmin = int(tahmin)
    if (tahmin < rasgele_sayı):
        tahmin
        print("Tahmin Sorgulanıyor...")
        sleep(2)

        print("Daha yüksek bir sayı söyleyin.")
        tahmin_hakkı -= 1
        print("Kalan Hak =",tahmin_hakkı)

    elif (tahmin > rasgele_sayı):
        print("Tahmin Sorgulanıyor...")
        sleep(2)

        print("Daha düşük bir sayı söyleyin.")
        tahmin_hakkı -= 1
        print("Kalan Hak =", tahmin_hakkı)


    else:

        print("Bilgiler Sorgulanıyor....")

        sleep(1)

        print("Tebrikler! Sayımız", rasgele_sayı)

        break

    if (tahmin_hakkı == 0):
        print("Tahmin Hakkınız Bitti...")

        print("Sayımız:", rasgele_sayı)

        break











