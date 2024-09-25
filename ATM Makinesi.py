print('''
******************************
ATM'ye Hoşgeldiniz.
#Bakiye sorgulamak için 1'e
#Para yatırma için 2'ye
#Para çekme için 3'e
#Çıkmak için 'çıkış' yazın.
''')
bakiye = 1250
while True:
    işlem=input("Yapmak istediniz işlem:")
    if (işlem == "çıkış"):
        print("Hoşça Kalın.☺")
    elif (işlem == "1"):
        print("Bakiyeniz:",bakiye)
    elif (işlem == "2"):
        b = int(input("Yatırılacak Miktar:"))
        bakiye+=b
        print("Başarıyla Eklendi.")
    elif (işlem == "3"):
        c = int(input("İstenen Miktar:"))
        if (c>bakiye):
            print("O kadar paran yok doru tutar gir.")
            continue
        print("Başarıyla Çekildi.")
        bakiye -= c
    else:
        print("Geçersiz İşlem.")

