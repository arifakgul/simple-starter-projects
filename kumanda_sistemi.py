import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi = ["TRT"],kanal = "TRT"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal

    def tv_aç(self):
        if (self.tv_durum == "Açık"):
            print("TV zaten açık.")
        else:
            print("Televizyon Açılıyor...")
            time.sleep(2)
            self.tv_durum = "Açık"
            print("TV Açıldı.")

    def tv_kapa(self):
        if (self.tv_durum == "Kapalı"):
            print("TV zaten kapalı.")
        else:
            print("Televizyon Kapanıyor...")
            time.sleep(2)
            self.tv_durum = "Kapalı"
            print("TV Kapatıldı.")

    def ses_ayarları(self):
        while True:
            istek = input("Sesi Azalt: '-'\tSesi Yükselt: '+'\tÇıkış: 'q'\n:")
            if (istek == "-"):
                if (self.tv_ses != 0):
                    self.tv_ses -= 1
                    print("Ses:",self.tv_ses)

            elif (istek == "+"):
                if (self.tv_ses != 30):
                    self.tv_ses += 1
                    print("Ses:",self.tv_ses)

            else:
                print("Ses Güncellendi:",self.tv_ses)
                break

    def kanal_ekle(self,new_kanal):
        print("Kanal Ekleniyor...")
        time.sleep(2)
        self.kanal_listesi.append(new_kanal)
        print("Kanal Eklendi.")

    def rasgele_kanal(self):
        rasgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rasgele]

    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "TV Durumu: {}\nTV Ses: {}\nKanal Listesi: {}\nŞu Anki Kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

deneme = Kumanda()

print("""
\t Televizyon Uygulaması \t
1.Tv Aç

2.Tv Kapat

3.Ses Ayarları

4.Kanal Ekle

5.Kanal Sayısı Öğrenme

6.Rastgele Kanala Geçme

7.Televizyon Bilgileri
Çıkmak İçin: 'p'
""")

while True:
    işlem = input("İşlem Seçiniz:")

    if (işlem == "p"):
        print("Program Sonlandırılıyor...")
        time.sleep(1)
        break
    elif (işlem == "1"):
        deneme.tv_aç()
    elif (işlem == "2"):
        deneme.tv_kapa()
    elif (işlem == "3"):
        if (deneme.tv_durum == "Açık"):
            deneme.ses_ayarları()
        else:
            print("Lütfen Televizyonu Açın.")
    elif (işlem == "4"):
        if (deneme.tv_durum == "Açık"):
            kanal_isimleri = input("Kanal isimleri ',' ile girin\n:")
            kanal_listesi = kanal_isimleri.split(",")

            for eklenecekler in kanal_listesi:
                deneme.kanal_ekle(eklenecekler)
        else:
            print("Lütfen Televizyonu Açın.")
    elif (işlem == "5"):
        print("Kanal Sayısı:",len(deneme))
    elif (işlem == "6"):
        deneme.rasgele_kanal()
        print("Kanal",deneme.kanal)
    elif (işlem == "7"):
        print(deneme)
    else:
        print("Geçersiz İşlem..........")