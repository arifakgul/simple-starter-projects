print('''
***************************
Bir Sayının Tam Bölenleri
(Çıkmak için q'ya basın)
***************************
''')

def tam_bölenleri(sayı):
    tam_bölenler = []
    for a in range(1,sayı):
        if (sayı % a == 0):
            tam_bölenler.append(a)
    return tam_bölenler

while True:
    sayı = input("sayı:")
    if (sayı == "q"):
        print("Program Sonlandırılıyor...")
        break
    else:
        sayı = int(sayı)
        print("Tam Bölenler:",tam_bölenleri(sayı))