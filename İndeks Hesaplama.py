print("----------Boy,Kilo İndeksi Hesaplama----------")
a=float(input("Kilonuz(kg):"))
b=float(input("Boyunuz(m):"))
indeks= a / (b * b)

if (indeks<18.5):
    print("İndeksiniz: {}".format(indeks),"-------> Zargana burayı terket☺")

elif (18.5<indeks<25):
    print("İndeksiniz: {}".format(indeks),"-------> Normalsin aferin ula")

elif (25<indeks<30):
    print("İndeksiniz: {}".format(indeks),"------->  Az ye az lan")

elif (indeks>30):
    print("İndeksiniz: {}".format(indeks),"-------> Öküz!")
