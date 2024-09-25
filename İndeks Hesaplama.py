print("----------Boy,Kilo İndeksi Hesaplama----------")
a=float(input("Kilonuz(kg):"))
b=float(input("Boyunuz(m):"))
indeks= a / (b * b)

if (indeks<18.5):
    print("İndeksiniz: {}".format(indeks),"-------> Çok Zayıfsınız.")

elif (18.5<indeks<25):
    print("İndeksiniz: {}".format(indeks),"-------> İdeal kilonuzdasınız.")

elif (25<indeks<30):
    print("İndeksiniz: {}".format(indeks),"------->  Fazla kilolusunuz.")

elif (indeks>30):
    print("İndeksiniz: {}".format(indeks),"-------> Uyarı!! Bir diyet doktoru ile görüşün.")
