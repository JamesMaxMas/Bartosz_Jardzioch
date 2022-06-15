# liczba ,modulo = input().split()
liczba = input()
liczba = int(liczba)
# modulo = int(modulo)
# krok = 1
wynik = 0
# krok +=1
liczba_mozliwych_poziomow = (liczba-1)+liczba-2
maksymalna_suma = liczba_mozliwych_poziomow*(liczba-1)-1
# def f(do_dodania):
#     global wynik
#     global krok
#     # print(krok)
#     for i in range(1, (liczba)):
#         if krok == liczba and i ==liczba-1:
#             # print("----1")
#             continue
#         print((i))
#         # print("krok")
#         # print(krok)
#         wynik +=(i+do_dodania)
#         if krok == ((liczba-1)+liczba-2):
#             # print("----2")
#             return 0
#         # elif i == 1:
#         #     print("----3")
#         #     continue
#
#         elif i==liczba-1:
#             # print("----4")
#             krok += 1
#             f(do_dodania+i)
#         # elif i == 2 :
#         #     for j in range(1,liczba):
#         #         print((j))
#         #         wynik +=(do_dodania+i+j)
#         else:
#             # print("----5")
#             koniec(i+do_dodania, i)
# def koniec(do_dodania,liczba_mozliwych_poziomow):
#     global wynik
#     # print("zaczynam")
#     # print(liczba_mozliwych_poziomow)
#     if(liczba_mozliwych_poziomow!=1):
#         # print("TAK")
#         wynik += (do_dodania + 1)
#         print(1)
#         for i in range(2, liczba):
#             print(i)
#             wynik +=(do_dodania+i)
#             koniec(do_dodania+i,liczba_mozliwych_poziomow-1)
#
#
# f(0)
def suma_n_kolejnych_liczb_od_m(n, m):
    wynik = 0
    for i in range(1,n+1):
        # print(i)
        wynik +=i
    return wynik+(m-1)*(n)

# print(wynik%modulo)
# print(suma_n_kolejnych_liczb_od_m(4, 2))
# wynik+=suma_n_kolejnych_liczb_od_m(liczba, 1)
skok = liczba-1
# print(maksymalna_suma-(liczba-2))
# print(range(3,maksymalna_suma-(liczba-1), +skok))
# for i in range(3,maksymalna_suma-(liczba-2)+1, +1):
#     print(i)
for h in range(0, liczba-3):
    print("Raz")
    koniec = False
    poczatek = 1+h*3
    wynik += suma_n_kolejnych_liczb_od_m(liczba-1, poczatek)
    krok = 1
    while not koniec:
        # print(wynik)
        if liczba_mozliwych_poziomow<=1:
            koniec = True
        poczatek +=2
        krok +=1
        koniec_przedzialu = poczatek+(liczba -2)
        poczatek_przedzialu = poczatek
        for i in range(poczatek, poczatek+(liczba -2)):
            # print("krok")
            # print(krok)
            # print("--")
            # print(poczatek+(liczba -2)-1)
            # print(i)
            # print("--")
            if krok==liczba+1 and koniec_przedzialu-1 ==i:
                continue
            # elif i!= poczatek_przedzialu:
            #     pass
            print("i")
            print(i)
            poczatek+=1
            wynik += suma_n_kolejnych_liczb_od_m(liczba-1, i)
            # print(wynik)
        poczatek -=1
        if krok == liczba_mozliwych_poziomow-h:
            koniec=True
print("----------------------------")
wynik -=(liczba)*(liczba-1)
print(wynik%1000)
print(wynik%modulo)