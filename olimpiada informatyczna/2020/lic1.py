dlugosc_wyswietlacza, liczba_operacji = input().split(" ")
dlugosc_wyswietlacza = int(dlugosc_wyswietlacza)
liczba_operacji = int(liczba_operacji)
dlug_1 = input()
dlug_2 = input()

wyswietlacz = [0]* dlugosc_wyswietlacza
# print("dlugosc:")
# print(dlugosc_wyswietlacza)
# print("liczba operacji:")
# print(liczba_operacji)
# print("wyswietlacz:")
# print(wyswietlacz)
# wyswietlacz[1] = 5
# print("wyswietlacz:")
# print(wyswietlacz)
while liczba_operacji>0:
    string = input()
    if string[0] == "W":
        # numer_liczby = int(string[2])
        # nowa_liczba = string[4]
        a , numer_liczby, nowa_liczba = string.split(" ")
        numer_liczby = int(numer_liczby)
        dlug_1 = dlug_1[0:dlugosc_wyswietlacza - numer_liczby-1] +nowa_liczba+dlug_1[dlugosc_wyswietlacza - numer_liczby:dlugosc_wyswietlacza]
        # print(dlug_1)
    if string[0] == "Z":
        # numer_liczby = int(string[2])
        # nowa_liczba = string[4]
        a, numer_liczby, nowa_liczba = string.split(" ")
        numer_liczby = int(numer_liczby)
        dlug_2 = dlug_2[0:dlugosc_wyswietlacza - numer_liczby-1]+nowa_liczba+dlug_2[dlugosc_wyswietlacza - numer_liczby:dlugosc_wyswietlacza-1]
        # print(dlug_2)
    if string[0]=="S":
        # numer_liczby = int(string[2:])
        a, numer_liczby = string.split(" ")
        numer_liczby = int(numer_liczby)
        przeniesione = 0
        # print("numer")
        # print(numer_liczby)
        for i in range((dlugosc_wyswietlacza-2),-1, -1):

            a = int(dlug_1[i])+int(dlug_2[i])
            a += przeniesione

            b = a %10
            if a > 9:
                przeniesione = 1
            else:
                przeniesione = 0
            # print("i")
            # print(i)
            # print("a")
            # print(a)
            # print("b")
            # print(b)
            # print("przeniesione")
            # print(przeniesione)
            if i == dlugosc_wyswietlacza -numer_liczby-1 :
                # print(i)
                # print(dlugosc_wyswietlacza -numer_liczby-1)
                print(b)
                break
            elif i == 0 and numer_liczby == dlugosc_wyswietlacza:
                # print("jestem tu")
                print(przeniesione)
    liczba_operacji -=1