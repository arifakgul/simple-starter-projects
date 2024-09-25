print('''
****************************************************************
Asal Sayı Bulma
Asal Sayı: 1 ve kendinden başka sayıya bölünmeyen sayılardır.
****************************************************************
''')


def asal_mi(sayı):
    if (sayı == 1):
        return False
    elif (sayı == 2):
        return True
    else:
        for a in range(2,sayı):
            if (sayı % a == 0):
                return False
        return True

while True:
    sayı = input("sayı:")
    if (sayı == "q"):
        break
    else:
        sayı =int(sayı)
        if (asal_mi(sayı)):
            print("Sayı Asal Bir Sayıdır.")
        else:
            print("Sayı Asal Bir Sayı Değildir.")