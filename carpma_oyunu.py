import random as rd
import os
"""

bu programda random modülü'nün 
randint fonksiyonunu kullanarak daha kısa bir kod yazılabilirdi fakat
algoritmamı geliştirmek istediğim için bu fonksiyonu kullanmadım

"""

class oyun():
    puan = 10
    def __init__(self):
        self.sayilar_liste = [] #islem yapilacak sayilarin tutuldugu yer
        self.sayi_adet = 2 # kac sayi ile islem yapilacagini belirleyen yer
        self.sayilar = "1234567890" 
        self.sayi_eleman = [] # sayilarin basamaklarinin bulundugu yer
        self.sayi_basamak = 1 # sayinin basamak sayisi
    def zorluk_sec():
        zorluklar = ["basit","zor","imkansiz"]
        sayi = 1
        for u in zorluklar:
            print(f"[{sayi}] {u}")
            sayi += 1
        zorluk = int(input("hangi zorlugu istersiniz = "))
        if zorluk == 1:
            return "basit"
        if zorluk == 2:
            return "orta"
        if zorluk == 3:
            return "zor" 
    def kontrol(sayilar = list): 
        # icine girilen (self.sayilar_liste) adli listedeki sayilari
        # carpip bizim cevabimiz ile karsilastiran fonksiyon
        os.system("cls")
        sonuc = 1
        for u in sayilar:
            sonuc = sonuc * u 
        if cevap == sonuc:
            print("dogru cevap")
            if oyun.puan + 5 >= 60 : # puan 60 oldugu anda sona erer
                print("kazandiniz")
                return True
            else:
                oyun.puan += 5
        else:
            print("yanlis cevap")
            if oyun.puan - 5 <= 0 :#0 oldugunda oyun biter
                print("kaybettiniz")
                return True
            else:
                oyun.puan -= 5
    def oyun_modu(self,zorluk_kontrol):
        os.system("cls")
        dene = 2 # sayi adeti icin olusturulan bir degisken
        if zorluk_kontrol == "basit":
            self.sayi_basamak = 1
        if zorluk_kontrol == "orta":
            self.sayi_basamak = 2
        if zorluk_kontrol == "zor":
            self.sayi_basamak = 2
            self.sayi_adet = 3
            dene = 3
        while True:
            global cevap
            print("PUANINIZ = {}".format(oyun.puan))
            basamak_sayisi_belirle = 0 
            #basamak adedinin while dongusunu saglamak icin 
            sayi_adet_belirle = 0
            #sayi adedinin while dongusunu saglamak icin
            while sayi_adet_belirle < self.sayi_adet:
                self.sayi_eleman.clear()
                while basamak_sayisi_belirle < self.sayi_basamak:
                    sayi_basamaklari = rd.choice(self.sayilar)
                    self.sayi_eleman.append(sayi_basamaklari)
                    basamak_sayisi_belirle += 1
                if dene == 3:
                    basamak_sayisi_belirle = 0
                else:
                    basamak_sayisi_belirle = 0
                sayi = "".join(self.sayi_eleman)
                sayi = int(sayi)
                self.sayilar_liste.append(sayi)
                sayi_adet_belirle += 1
            if dene == 3:
                #dene 3 iken 3 elemanli bir carpma islemi yazar
                print(f"{self.sayilar_liste[0]} * {self.sayilar_liste[1]} * {self.sayilar_liste[2]} = ?") 
            else:
                print(f"{self.sayilar_liste[0]} * {self.sayilar_liste[1]} = ?")
            cevap = int(input("cevabiniz nedir = "))
            kontrol_et = oyun.kontrol(self.sayilar_liste)
            self.sayilar_liste.clear()
            if kontrol_et == True:
                break

zorluk = oyun.zorluk_sec()
oyun().oyun_modu(zorluk)