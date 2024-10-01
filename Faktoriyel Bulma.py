print("""
*************************
   Faktöriyel Bulma
(Çıkak için q'ya basın)
*************************
""")

while True:
    sayı = input("Sayı:")

    if (sayı == "q"):
        print("Sonlandırılıyor...")
        break

    sayı = int(sayı)
    fakto = 1
    for a in range(2,sayı+1):
        fakto *= a
    print("{}{} = {}".format(sayı,"!",fakto))
