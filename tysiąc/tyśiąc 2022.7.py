import random
# import pyttsx3
from tkinter import *
from PIL import Image, ImageTk
# engine = pyttsx3.init()
# engine.setProperty('rate', 110)     # setting up new voice rate
root = Tk()
root.title("Tysiąc 2022.7")
bok = 1000
root.geometry(str(bok) +"x"+str(bok))


wartosc = {"9": 0, "J": 2, "Q": 3, "K": 4, "10": 10, "A": 11}
stol = [" ", " ", " "]


def karta_jest_bioraca(karta, karty, karty_ktore_poszly):
    # pomdic = {"A": 6, "10":5, "K":4, "Q":3, "J":2, "9":1}
    wszystkie_karty = ["A", "10", "K", "Q", "J", "9"]
    liczba_posiadanych_kart = 0
    for i in wszystkie_karty:
        # print(liczba)
        if (karta[0] + i) in karty or (karta[0] + i) in karty_ktore_poszly:
            liczba_posiadanych_kart += 1
    if karta[1::] == "A":
        return True
    elif (karta[0] + "A") in karty or (karta[0] + "A") in karty_ktore_poszly:
        if karta[1::] == "10":
            return True
        elif liczba_posiadanych_kart >= 5:
            return True
        elif (karta[0] + "10") in karty or (karta[0] + "10") in karty_ktore_poszly:
            if karta[1::] == "K":
                return True
            elif liczba_posiadanych_kart >= 4:
                return True
            elif (karta[0] + "K") in karty or (karta[0] + "K") in karty_ktore_poszly:
                if karta[1::] == "Q":
                    return True
                elif liczba_posiadanych_kart >= 3:
                    return True
    return False


def wartosc_do_dorzucenia(karta, kolor, atut, karty, karty_ktore_poszly):
    wynik = wartosc[karta[1::]]
    ####################
    # sprawdzanie 10
    czy_jest_10 = False
    liczba_w_kolorze = 0
    for i in karty:
        if i[0] == karta[0]:
            liczba_w_kolorze += 1
            if i[1::] == "10" and i != karta and not karta_jest_bioraca(i, karty, karty_ktore_poszly):
                czy_jest_10 = True
    if liczba_w_kolorze == 2 and czy_jest_10:
        wynik += 5
    ####################
    if karta[0] == atut:
        wynik += 5
    ####################
    if karta_jest_bioraca(karta, karty, karty_ktore_poszly):
        wynik += 15
    else:
        wynik-=5
    ####################
    if karta[1::] == "K":
        if (karta[0] + "Q") in karty and not karta_jest_bioraca((karta[0] + "Q"), karty, karty_ktore_poszly):
            wynik += 6.1
    if karta[1::] == "Q":
        if (karta[0] + "K") in karty and not karta_jest_bioraca((karta[0] + "K"), karty, karty_ktore_poszly):
            wynik += 7.2
    ####################

    # print(karta, wynik)

    return wynik


class Gracz_czlowiek:
    def __init__(self, nr):
        self.nr = nr
        self.karty = []
        self.meldunki = []
        self.zebrane_punkty = 0
        self.karty_ktore_poszly = []
        self.wynik = 0
        self.obrazy_kart = []
        self.czlowiek = True
    def wyswietl_karty(self):
        for obraz in self.obrazy_kart:
            obraz.destroy()
        liczba_kart = len(self.karty)
        for i in range(liczba_kart):
            image = Image.open('./karty/' + self.karty[i] + '.png')
            image = image.resize((70, 120))
            photo = ImageTk.PhotoImage(image)
            # print(i)
            karta = Button(root, image=photo, height=120, width=70, command = lambda x = i : f_karta(x))
            karta.indeks = i
            karta.image = photo
            karta.place(x=70 * (i)+250, y=700)

            self.obrazy_kart.append(karta)
    def zmien_kolejnosc_kart(self, i, j):
        if i>len(self.karty) or j>len(self.karty):
            print("Błąd")
        else:
            buf = self.karty[i]
            self.karty[i] = self.karty[j]
            self.karty[j] = buf
            self.wyswietl_karty()
    def przypisz_karty(self, karty):
        self.karty = karty
        self.meldunki = []
        # print(self.meldunki)
        self.karty_ktore_poszly = []
        self.zebrane_punkty = 0
        print("Oto twoje karty", self.karty)
        # self.wyswietl_karty()
        # input("Ok?")
    def czy_po_60(self):
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        czy = input("Czy dajesz po 60? Y/N")
        if czy == "Y":
            print("gracz nr %s daje po 60" % self.nr)
            return True
        else:
            print("gracz nr %s nie daje po 60" % self.nr)
            return False
    def ile_moge_grac(self):
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        ile = int(input("Ile mozesz grac?"))
        return ile
    def uloz_karty(self):
        print("Oto twoje karty", self.karty)
        # self.wyswietl_karty()
    def wyrzuc_karte_na(self, stol):
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        karta = input("Ktora karte chesz wyrzucic na stol?")
        stol[self.nr - 1] = karta
        # print(self.karty)
        self.karty.remove(karta)
        print("gracz nr %s wychodzi karta %s" % (self.nr, karta))

    def dorzuc_karte(self, stol, kolor, najwyzsza_karta_na_stole, atut):
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        karta = input("Ktora karte chesz dorzucic na stol?")
        stol[self.nr - 1] = karta
        # print(self.karty)
        self.karty.remove(karta)
        print("gracz nr %s wychodzi karta %s" % (self.nr, karta))
    def oddaj_karty(self, gracz_do_oddania1, gracz_do_oddania2):
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        karta = input("Ktora karte chesz oddac?")
        self.karty.remove(karta)
        gracz_do_oddania1.karty.append(karta)
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        karta = input("Ktora karte chesz oddac?")
        self.karty.remove(karta)
        gracz_do_oddania2.karty.append(karta)
    def licytuj_1(self, ile, stawka):
        print("Oto twoje karty", self.karty)
        print(ile)
        self.wyswietl_karty()
        global stawki_kolejnosc
        global najwyzsza_stawka
        if ile == "pass":
            stawki_kolejnosc[0] = "pass"
            self.tekst_licytacji.set("pass")
            root.update_idletasks()
            # return int(ile)
        else:
            self.tekst_licytacji.set(stawka + 10)
            root.update_idletasks()
            najwyzsza_stawka = najwyzsza_stawka + 10
            stawki_kolejnosc[0] = stawka +10
            # return ile
    def licytuj(self, stawka):
        print("Oto twoje karty", self.karty)
        self.wyswietl_karty()
        ile = input("Co mówisz?")
        if ile != "pass":
            return int(ile)
        else:
            return ile


class Gracz:
    def __init__(self, nr):
        self.nr = nr
        self.karty = []
        self.meldunki = []
        self.zebrane_punkty = 0
        self.karty_ktore_poszly = []
        self.wynik = 0

    def przypisz_karty(self, karty):
        self.karty = karty
        self.meldunki = []
        # print(self.meldunki)
        self.karty_ktore_poszly = []
        self.zebrane_punkty = 0

    def czy_po_60(self):
        if self.ile_moge_grac()>=100:
            # print(self.karty, self.meldunki)
            print("gracz nr %s nie daje po 60" % self.nr)
            return False
        else:
            # print(self.karty, self.meldunki)
            print("gracz nr %s  daje po 60" % self.nr)
            return True

    def ile_moge_grac(self):
        self.uloz_karty()
        # liczba_kart = len(self.karty)
        liczba_bioracych_lew = 0
        pewne_meldunki = 0
        for i in self.karty:
            if karta_jest_bioraca(i, self.karty, []):
                liczba_bioracych_lew += 1
        oddane_lewy = 8-liczba_bioracych_lew
        wartosc_meldunkow = {"1": 100, "2": 80, "3": 60, "4": 40}
        punkty_za_oddale_lewy = {0: 120, 1:90, 2:70, 3:50, 4:40, 5:30, 6:20, 7:10, 8:0}
        if len(self.meldunki) == 1:
            pewne_meldunki = wartosc_meldunkow[self.meldunki[0]]
        elif len(self.meldunki) >1:
            pewne_meldunki = wartosc_meldunkow[max(self.meldunki, key= lambda x : wartosc_meldunkow[x])]
        # print("tyle moge grac" , punkty_za_oddale_lewy[oddane_lewy]+pewne_meldunki, "z takimi kartami", self.karty)
        return punkty_za_oddale_lewy[oddane_lewy]+pewne_meldunki+100

    def uloz_karty(self):
        self.meldunki = []
        if "1K" in self.karty and "1Q" in self.karty:
            self.meldunki.append("1")
        if "2K" in self.karty and "2Q" in self.karty:
            self.meldunki.append("2")
        if "3K" in self.karty and "3Q" in self.karty:
            self.meldunki.append("3")
        if "4K" in self.karty and "4Q" in self.karty:
            self.meldunki.append("4")

    def wyrzuc_karte_na(self, stol):
        # a = random.choice(self.karty)
        self.karty = sorted(self.karty,
                            key=lambda x: wartosc_do_dorzucenia(x, "5", "5", self.karty, self.karty_ktore_poszly),
                            reverse=True)
        najwyzsza_karta = self.karty[0]
        stol[self.nr - 1] = najwyzsza_karta
        # print(self.karty)
        self.karty.remove(najwyzsza_karta)
        print("gracz nr %s wychodzi karta %s" % (self.nr, najwyzsza_karta))

    def dorzuc_karte(self, stol, kolor, najwyzsza_karta_na_stole, atut):
        # print(self.karty)
        karta_do_dorzucenia = ""
        self.karty = sorted(self.karty,
                            key=lambda x: wartosc_do_dorzucenia(x, kolor, atut, self.karty, self.karty_ktore_poszly),
                            reverse=True)
        # print(self.karty)
        for i in self.karty:
            if i[0] == kolor:
                karta_do_dorzucenia = i
                if wartosc[i[1::]] > wartosc[najwyzsza_karta_na_stole[1::]]:
                    break
        if karta_do_dorzucenia == "":
            karta_do_dorzucenia = self.karty[-1]
        stol[self.nr - 1] = karta_do_dorzucenia
        print("gracz nr %s dorzuca karta %s" % (self.nr, karta_do_dorzucenia))
        # engine.say("gracz nr %s dorzuca karta %s" % (self.nr, karta_do_dorzucenia))
        # engine.runAndWait()
        self.karty.remove(karta_do_dorzucenia)

    def oddaj_karty(self, gracz_do_oddania1, gracz_do_oddania2):
        self.karty = sorted(self.karty,
                            key=lambda x: wartosc_do_dorzucenia(x, "5", "5", self.karty, self.karty_ktore_poszly),
                            reverse=True)
        najnizsza_karta1 = self.karty[-1]
        najnizsza_karta2 = self.karty[-2]
        self.karty.remove(najnizsza_karta1)
        gracz_do_oddania1.karty.append(najnizsza_karta1)
        self.karty.remove(najnizsza_karta2)
        gracz_do_oddania2.karty.append(najnizsza_karta2)


    def licytuj(self, stawka):
        if self.ile_moge_grac() > stawka:
            print("gracz nr %s, mówi %s" % (self.nr, stawka + 10))
            self.tekst_licytacji.set(stawka+10)
            root.update_idletasks()
            return stawka+10
        else:
            print("gracz nr %s, mówi %s" % (self.nr, "pass"))
            self.tekst_licytacji.set("pass")
            root.update_idletasks()
            return "pass"


def rozdawanie(wszystkie_karty, karty1, karty2, karty3, musik):
    a = 0
    while a < 7:
        b = random.choice(wszystkie_karty)
        wszystkie_karty.remove(b)
        karty1.append(b)
        c = random.choice(wszystkie_karty)
        wszystkie_karty.remove(c)
        karty2.append(c)
        d = random.choice(wszystkie_karty)
        wszystkie_karty.remove(d)
        karty3.append(d)
        a = a + 1
    for i in range(len(wszystkie_karty)):
        musik.append(wszystkie_karty[i])
def rozdawanie_2_osoby(wszystkie_karty, karty1, karty2, musik):# jedna okoba ma już karty, z licytacją
    a = 0
    while a < 7:
        b = random.choice(wszystkie_karty)
        wszystkie_karty.remove(b)
        karty1.append(b)
        c = random.choice(wszystkie_karty)
        wszystkie_karty.remove(c)
        karty2.append(c)
        a = a + 1
    for i in range(len(wszystkie_karty)):
        musik.append(wszystkie_karty[i])
def rozdawanie_2_osoby_po_musiku(wszystkie_karty, karty1, karty2):# jedna okoba ma już karty, z licytacją
    a = 0
    while a < 8:
        b = random.choice(wszystkie_karty)
        wszystkie_karty.remove(b)
        karty1.append(b)
        c = random.choice(wszystkie_karty)
        wszystkie_karty.remove(c)
        karty2.append(c)
        a = a + 1



def gra(kolejnosc, stawka):
    # kolejnosc = [gracz1, gracz2, gracz3]
    # print("######",gracz1.karty, gracz2.karty, gracz3.karty, "######")
    # print("######", gracz1.zebrane_punkty, gracz2.zebrane_punkty, gracz3.zebrane_punkty, "######")
    print("gracz nr %s, gra %s" % (kolejnosc[0].nr, stawka))
    a = 0
    ten_kto_gra = kolejnosc[0]
    ten_kto_nie_gra1 = kolejnosc[1]
    ten_kto_nie_gra2 = kolejnosc[2]
    atut = "5"  # bez atu
    while a < 8:
        print("---------kolejka nr %s ------------" % str(a + 1))

        kolejnosc[0].wyrzuc_karte_na(stol)

        najwyzsza_karta_na_stole = stol[kolejnosc[0].nr - 1]
        if (stol[kolejnosc[0].nr - 1][1::] == "Q" and (stol[kolejnosc[0].nr - 1][0] + "K") in kolejnosc[0].karty) or (stol[kolejnosc[0].nr - 1][1::] == "K" and (stol[kolejnosc[0].nr - 1][0] + "Q") in kolejnosc[0].karty):
            if stol[kolejnosc[0].nr - 1][0] == "1":
                atut = "1"
                if kolejnosc[0].zebrane_punkty > 0:
                    kolejnosc[0].zebrane_punkty += 100
                    print("gracz nr ", kolejnosc[0].nr, " melduje 100")
            elif stol[kolejnosc[0].nr - 1][0] == "2":
                atut = "2"
                if kolejnosc[0].zebrane_punkty > 0:
                    kolejnosc[0].zebrane_punkty += 80
                    print("gracz nr ", kolejnosc[0].nr, " melduje 80")
            elif stol[kolejnosc[0].nr - 1][0] == "3":
                atut = "3"
                if kolejnosc[0].zebrane_punkty > 0:
                    kolejnosc[0].zebrane_punkty += 60
                    print("gracz nr ", kolejnosc[0].nr, " melduje 60")
            elif stol[kolejnosc[0].nr - 1][0] == "4":
                atut = "4"
                if kolejnosc[0].zebrane_punkty > 0:
                    kolejnosc[0].zebrane_punkty += 40
                    print("gracz nr ", kolejnosc[0].nr, " melduje 40")

        kolejnosc[1].dorzuc_karte(stol, stol[kolejnosc[0].nr - 1][0], najwyzsza_karta_na_stole, atut)

        if stol[kolejnosc[0].nr - 1][0] == stol[kolejnosc[1].nr - 1][0] and wartosc[stol[kolejnosc[0].nr - 1][1::]] < \
                wartosc[stol[kolejnosc[1].nr - 1][1::]]:
            najwyzsza_karta_na_stole = stol[kolejnosc[0].nr - 1]

        kolejnosc[2].dorzuc_karte(stol, stol[kolejnosc[0].nr - 1][0], najwyzsza_karta_na_stole, atut)

        # print(gracz1.karty, gracz2.karty, gracz3.karty, stol)
        # print(stol)
        kolor_glowny = stol[kolejnosc[0].nr - 1][0]
        zwyciezca, punkty = sedzia(stol, kolor_glowny, atut)
        for i in stol:
            gracz1.karty_ktore_poszly.append(i)
            gracz2.karty_ktore_poszly.append(i)
            gracz3.karty_ktore_poszly.append(i)
        # print("zwyciezca ma nr %s " % zwyciezca)
        if zwyciezca == 1:
            gracz1.zebrane_punkty += punkty
            kolejnosc = [gracz1, gracz2, gracz3]
        elif zwyciezca == 2:
            gracz2.zebrane_punkty += punkty
            kolejnosc = [gracz2, gracz3, gracz1]
        else:
            gracz3.zebrane_punkty += punkty
            kolejnosc = [gracz3, gracz1, gracz2]
        print("wynik gry", gracz1.zebrane_punkty, gracz2.zebrane_punkty, gracz3.zebrane_punkty, "suma",
              gracz1.zebrane_punkty + gracz2.zebrane_punkty + gracz3.zebrane_punkty)
        a += 1

    if ten_kto_gra.zebrane_punkty >= stawka:
        ten_kto_gra.wynik += stawka
    else:
        ten_kto_gra.wynik -= stawka
    ten_kto_nie_gra1.wynik += int(ten_kto_nie_gra1.zebrane_punkty / 10 + 0.5) * 10
    ten_kto_nie_gra2.wynik += int(ten_kto_nie_gra2.zebrane_punkty / 10 + 0.5) * 10
    print("wynik gry: gracz nr %s ugral %s ,a mial ugrac %s, gracz nr %s ugral %s, gracz nr %s ugral %s" % (
        ten_kto_gra.nr, ten_kto_gra.zebrane_punkty, stawka, ten_kto_nie_gra1.nr,
        int(ten_kto_nie_gra1.zebrane_punkty / 10 + 0.5) * 10, ten_kto_nie_gra2.nr,
        int(ten_kto_nie_gra2.zebrane_punkty / 10 + 0.5) * 10))
    # print("----", gracz1.zebrane_punkty+gracz2.zebrane_punkty+gracz3.zebrane_punkty, "----")
    print("wynik partii", gracz1.wynik, gracz2.wynik, gracz3.wynik)


def sedzia(stol, kolor, atut):
    karta1 = wartosc[stol[0][1::]]
    kolor1 = stol[0][0]

    karta2 = wartosc[stol[1][1::]]
    kolor2 = stol[1][0]

    karta3 = wartosc[stol[2][1::]]
    kolor3 = stol[2][0]
    suma_stolu = karta1 + karta2 + karta3
    if kolor1 == atut:
        karta1 = karta1 + 20
    elif kolor1 != kolor:
        karta1 = -1
    if kolor2 == atut:
        karta2 = karta2 + 20
    elif kolor2 != kolor:
        karta2 = -1
    if kolor3 == atut:
        karta3 = karta3 + 20
    elif kolor3 != kolor:
        karta3 = -1
    # print(kolor1, kolor2, kolor3, kolor)
    # print(karta1, karta2 , karta3)
    if (karta1 > karta2) and (karta1 > karta3):
        zwyciezca = 1
    elif (karta2 > karta1) and (karta2 > karta3):
        zwyciezca = 2
    else:
        zwyciezca = 3
    # print("zwyciezca", zwyciezca, suma_stolu)

    # print("wynik gry", gracz1.zebrane_punkty, gracz2.zebrane_punkty, gracz3.zebrane_punkty, "suma", gracz1.zebrane_punkty +gracz2.zebrane_punkty+gracz3.zebrane_punkty)
    return (zwyciezca, suma_stolu)


def koniec_licytacji(najwyzsza_stawka, zwyciezca, nie_zwyciezca1, nie_zwyciezca2, musik):
    for i in musik:
        zwyciezca.karty.append(i)
    zwyciezca.uloz_karty()
    zwyciezca.oddaj_karty(nie_zwyciezca1, nie_zwyciezca2)
    nie_zwyciezca1.uloz_karty()
    nie_zwyciezca2.uloz_karty()
    czy_po_60 = False
    if najwyzsza_stawka == 100:
        czy_po_60 = zwyciezca.czy_po_60()
    if czy_po_60:
        nie_zwyciezca1.wynik += 60
        nie_zwyciezca2.wynik += 60
        print("wynik partii", gracz1.wynik, gracz2.wynik, gracz3.wynik)
    else:
        nowa_stawka = zwyciezca.ile_moge_grac()
        if nowa_stawka > najwyzsza_stawka:
            najwyzsza_stawka = nowa_stawka
        gra([zwyciezca, nie_zwyciezca1, nie_zwyciezca2], najwyzsza_stawka)


def licytacja(kolejnosc, musik):
    # kolejnosc = [gracz1, gracz2, gracz3] #musik ->gracz nr 1
    stawki_kolejnosc = [100, "", ""]
    najwyzsza_stawka = 100
    gracz1.zebrane_punkty = 0
    gracz2.zebrane_punkty = 0
    gracz3.zebrane_punkty = 0
    # print(stawki)
    a = 0
    while a < 5:
        if stawki_kolejnosc[1] != "pass":
            if stawki_kolejnosc[1] != najwyzsza_stawka:
                stawki_kolejnosc[1] = kolejnosc[1].licytuj(najwyzsza_stawka)
                if stawki_kolejnosc[1] != "pass":
                    najwyzsza_stawka = stawki_kolejnosc[1]
            else:
                koniec_licytacji(najwyzsza_stawka, kolejnosc[1], kolejnosc[2], kolejnosc[0], musik)
                break
        if stawki_kolejnosc[2] != "pass":
            if stawki_kolejnosc[2] != najwyzsza_stawka:
                stawki_kolejnosc[2] = kolejnosc[2].licytuj(najwyzsza_stawka)
                if stawki_kolejnosc[2] != "pass":
                    najwyzsza_stawka = stawki_kolejnosc[2]
            else:
                koniec_licytacji(najwyzsza_stawka, kolejnosc[2], kolejnosc[0], kolejnosc[1], musik)
                break
        if stawki_kolejnosc[0] != "pass":
            if stawki_kolejnosc[0] != najwyzsza_stawka:
                stawki_kolejnosc[0] = kolejnosc[0].licytuj(najwyzsza_stawka)
                if stawki_kolejnosc[0] != "pass":
                    najwyzsza_stawka = stawki_kolejnosc[0]
            else:
                koniec_licytacji(najwyzsza_stawka, kolejnosc[0], kolejnosc[1], kolejnosc[2], musik)
                break
        a += 1

    # kolejnosc_gry = kolejnosc
    # gra(kolejnosc_gry, najwyzsza_stawka)

# root.mainloop()



def partia():
    # start.destroy()
    # var = IntVar()
    # exit = Button(root, text="EXIT", command=lambda: root.destroy())
    # exit.place(x=0, y=0)
    # root.update_idletasks()
    licznik = 0
    # print("s")

    kolejnosc = [gracz1, gracz2, gracz3]
    while gracz1.wynik < 100 and gracz2.wynik < 100 and gracz3.wynik < 100:
        wszystkie_karty = ["1A", "110", "1K", "1Q", "1J", "19", "2A", "210", "2K", "2Q", "2J", "29", "3A", "3K", "3Q", "3J",
                           "310", "39", "4A", "410", "4K", "4Q", "4J", "49"]
        karty1, karty2, karty3, musik = [], [], [], []
        rozdawanie(wszystkie_karty, karty1, karty2, karty3, musik)
        licznik += 1
        gracz1.przypisz_karty(karty1)
        gracz2.przypisz_karty(karty2)
        gracz3.przypisz_karty(karty3)
        gracz1.uloz_karty()
        gracz2.uloz_karty()
        gracz3.uloz_karty()
        licytacja(kolejnosc, musik)
        kolejnosc = [kolejnosc[1], kolejnosc[2], kolejnosc[0]]

    # print(licznik)

gracz1 = Gracz_czlowiek(1)
gracz2 = Gracz(2)
gracz3 = Gracz(3)
etap = 1
etap_licytacji = 1
zamienianie_kart = False
kolejnosc = [gracz1, gracz2, gracz3]
musik = []

def tryb_zamieniania():
    global zamienianie_kart
    if zamienianie_kart == False:
        zamienianie_B.configure(bg = "blue")
        zamienianie_kart = True
    else:
        zamienianie_B.configure(bg = "white")
        zamienianie_kart = False

def dalej():
    global etap
    global etap_licytacji
    global kolejnosc
    global musik
    global stawki_kolejnosc
    global najwyzsza_stawka
    print(etap)
    print("----------------------")
    if etap == 1:# rozdawanie kart i układanie kart
        wszystkie_karty = ["1A", "110", "1K", "1Q", "1J", "19", "2A", "210", "2K", "2Q", "2J", "29", "3A", "3K", "3Q",
                           "3J",
                           "310", "39", "4A", "410", "4K", "4Q", "4J", "49"]
        karty1, karty2, karty3 = [], [], []
        rozdawanie(wszystkie_karty, karty1, karty2, karty3, musik)
        gracz1.przypisz_karty(karty1)
        gracz2.przypisz_karty(karty2)
        gracz3.przypisz_karty(karty3)
        gracz1.wyswietl_karty()
        zamienianie_B["state"]="normal"
        stawki_kolejnosc = [100, "", ""]
        najwyzsza_stawka = 100
        etap += 1
    elif etap == 2:#licytacja
        pass_B["state"] = "normal"
        podbij_B["state"] = "normal"
        # gracz1.zebrane_punkty = 0
        # gracz2.zebrane_punkty = 0
        # gracz3.zebrane_punkty = 0

        if stawki_kolejnosc[1] != "pass":
            if stawki_kolejnosc[1] != najwyzsza_stawka:
                stawki_kolejnosc[1] = kolejnosc[1].licytuj(najwyzsza_stawka)
                if stawki_kolejnosc[1] != "pass":
                    najwyzsza_stawka = stawki_kolejnosc[1]
            else:
                etap+=1
                print("gra gracz nr", kolejnosc[1].nr, " ", najwyzsza_stawka)
                kolejnosc = [kolejnosc[1], kolejnosc[2], kolejnosc[0]]
                return
                # koniec_licytacji(najwyzsza_stawka, kolejnosc[1], kolejnosc[2], kolejnosc[0], musik)
                # break
        if stawki_kolejnosc[2] != "pass":
            if stawki_kolejnosc[2] != najwyzsza_stawka:
                stawki_kolejnosc[2] = kolejnosc[2].licytuj(najwyzsza_stawka)
                if stawki_kolejnosc[2] != "pass":
                    najwyzsza_stawka = stawki_kolejnosc[2]
            else:
                etap+=1
                print("gra gracz nr", kolejnosc[2].nr, " ", najwyzsza_stawka)
                kolejnosc = [kolejnosc[2], kolejnosc[0], kolejnosc[1]]
                return
                # koniec_licytacji(najwyzsza_stawka, kolejnosc[2], kolejnosc[0], kolejnosc[1], musik)
                # break
        if stawki_kolejnosc[0] != "pass":
            if stawki_kolejnosc[0] != najwyzsza_stawka:
                # stawki_kolejnosc[0] = kolejnosc[0].licytuj(najwyzsza_stawka)
                kolejnosc[0].tekst_licytacji.set("czekamy")
                # if stawki_kolejnosc[0] != "pass":
                #     najwyzsza_stawka = stawki_kolejnosc[0]
            else:
                etap+=1
                print("gra gracz nr", kolejnosc[0].nr, " ", najwyzsza_stawka)
                return
                # koniec_licytacji(najwyzsza_stawka, kolejnosc[0], kolejnosc[1], kolejnosc[2], musik)
                # break
        # a += 1
    # etap +=1
    # print(etap)




# display_text = StringVar()
# display = Label(root, textvariable=display_text)
# display.place(x=800, y=100)
# display_text.set('')
# image = Image.open('./karty/' + self.karty[i] + '.png')
image1 = Image.open('gracz.png')
test = ImageTk.PhotoImage(image1)
label1 = Label(image=test , width = 200, height= 200)
label1.image = test
label1.place(x=50, y=100)

label2 = Label(image=test , width = 200, height= 200)
label2.image = test
label2.place(x=600, y=100)

label2 = Label(image=test , width = 200, height= 200)
label2.image = test
label2.place(x=50, y=700)

display_text = StringVar()
display = Label(root, textvariable=display_text)
# display.place(x=800, y=100)
display_text.set('')

gracz1.tekst_licytacji = StringVar()
gracz2.tekst_licytacji = StringVar()
gracz3.tekst_licytacji = StringVar()
gracz1.tekst_licytacji_L = Label(root, textvariable=gracz1.tekst_licytacji, font=("Arial", 25))
gracz2.tekst_licytacji_L = Label(root, textvariable=gracz2.tekst_licytacji, font=("Arial", 25))
gracz3.tekst_licytacji_L = Label(root, textvariable=gracz3.tekst_licytacji, font=("Arial", 25))
gracz1.tekst_licytacji.set('')
gracz2.tekst_licytacji.set('')
gracz3.tekst_licytacji.set('')
gracz2.tekst_licytacji_L.place(x=50, y=100)
gracz3.tekst_licytacji_L.place(x=600, y=100)
gracz1.tekst_licytacji_L.place(x=50, y=700)
def zbieraj_indeks_do_zamiany(i):
    s = display_text.get()
    # print(i.indeks)
    if len(s)==0:
        s += str(i)
        display_text.set(s)
    else:
        gracz1.zmien_kolejnosc_kart(int(s[0]), i)
        gracz1.wyswietl_karty()
        s = ''
        display_text.set(s)
    # print("jestem tu "+s)
    root.update_idletasks()
T_kart_do_zamiany = []
# gracz1 = Gracz(1)

def f_karta(i):
    global zamienianie_kart
    if zamienianie_kart:
        zbieraj_indeks_do_zamiany(i)

start = Button(root, text = "Dalej", command = lambda : dalej())
start.place(x=0, y=0)

zamienianie_B = Button(root, text = "Zmien kolojnosc kart", command = lambda : tryb_zamieniania())
zamienianie_B.place(x=100, y=650)
zamienianie_B["state"]="disabled"

pass_B = Button(root, text = "pass", command = lambda : gracz1.licytuj_1("pass", najwyzsza_stawka))
pass_B.place(x=300, y=650)
pass_B["state"]="disabled"

podbij_B = Button(root, text = "podbij", command = lambda : gracz1.licytuj_1("+", najwyzsza_stawka))
podbij_B.place(x=400, y=650)
podbij_B["state"]="disabled"


# image = Image.open('./karty/1A.png')
# image = image.resize((40, 80))
# # photo = PhotoImage(file = r"C:\Users\admin\Desktop\py\tysiąc\tysiąc 2022\karty\1A.png")
# photo = ImageTk.PhotoImage(image)
# karta = Button(root, image = photo, height = 80, width = 40)
# karta.place(x=100, y=100)
# cos()

root.mainloop()
# wygrane = 0
# for i in range(1000):
#     wszystkie_karty = [ "1K", "1J", "19", "2Q", "2J", "29", "3K", "3Q", "3J",
#                                 "39", "4A", "410", "4K", "4Q", "4J", "49"]
#     karty1, karty2, karty3, musik = [], [], ["1A", "110", "1Q", "2A", "210", "2K", "3A","310"], []
#     rozdawanie_2_osoby_po_musiku(wszystkie_karty, karty1, karty2)
#     gracz1.przypisz_karty(karty1)
#     gracz2.przypisz_karty(karty2)
#     gracz3.przypisz_karty(karty3)
#     gracz1.uloz_karty()
#     gracz2.uloz_karty()
#     gracz3.uloz_karty()
#     kolejnosc = [gracz3, gracz1, gracz2]
#     # print("######",gracz1.karty, gracz2.karty, gracz3.karty, "######")
#     gra(kolejnosc, 120)
#     print("---------------------------------------", gracz3.zebrane_punkty)
#     if gracz3.zebrane_punkty ==120:
#         wygrane +=1
#
# print(wygrane)

    # print("######", gracz1.zebrane_punkty, gracz2.zebrane_punkty, gracz3.zebrane_punkty, "######")
