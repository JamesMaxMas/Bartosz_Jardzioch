import math
import time
liczba = int(input())
# T = [0] * (liczba+1)
T=[]
# T=[0, 0, 0]
s = str(input())
index = 0
# for i in s:
#     if i != " ":
#         T[index] = [int(i), 0, 0]
#         index += 1


# for i in s:
#     if i != " ":
#         print(T[index])
#         index += 1
class krasnale:
    def __init__(self,numer, inf):
        self.inf = int(inf)
        self.numer = int(numer)
    numer = 0
    inf = 0
    inf_lewo = None
    inf_prawo = None
    na_pewno = 0
s=s.split(" ")
for i in s:
    if i != " ":
        # T[index] = krasnale(index,i)
        T.append(krasnale(index,i))
        index += 1

index = 0
# for i in range(liczba):
#     a = T[i].inf
#     if i != 0:
#         if T[i - 1]. != 0:
#             T[i - 1][2] = a
#         else:
#             T[i - 1][1] = a
#     if i != liczba - 1:
#         if T[i + 1][1] != 0:
#             T[i + 1][2] = a
#         else:
#             T[i + 1][1] = a
mozliwosci = []
mozliwosci_dic = {}
for i in range(1, liczba + 1):
    mozliwosci.append(i)
for i in range(liczba):
    a = T[i].inf
    mozliwosci_dic[a]=True
    if i != 0:
        T[i - 1].inf_prawo = a
    # else:
    #     T[i].inf_lewo = None
    if i != liczba - 1:
        T[i + 1].inf_lewo = a

# for krasnal in T:
#     a = krasnal.inf
#     if krasnal.numer != 0:
#
# mozliwosci = list(range(1, liczba + 1))


# print(mozliwosci)
# for i in range(liczba):
#     if T[i][1] == T[i][2]:
#         mozliwosci.remove(T[i][1])
# print(mozliwosci)
sprzecznosc = False
start = time.time()

T[1].na_pewno = T[1].inf_lewo
if T[1].na_pewno in mozliwosci:
    mozliwosci.remove(T[1].na_pewno)

T[liczba-2].na_pewno = T[liczba-2].inf_prawo
if T[liczba-2].na_pewno in mozliwosci:
    mozliwosci.remove(T[liczba-2].na_pewno)
# for i in T:
#     print(i.na_pewno)
print("-----------------------")
for i in range(0,liczba):
    # print(i)
    if T[i].na_pewno==0:
        if T[i].inf_prawo == T[i].inf_lewo:
            T[i].na_pewno = T[i].inf_prawo
            if T[i].na_pewno in mozliwosci:
                mozliwosci.remove(T[i].na_pewno)
    if T[i].inf_prawo != T[i].inf_lewo:
        if T[i].na_pewno == T[i].inf_prawo and i>1:
            if T[i - 2].na_pewno == 0 or T[i - 2].na_pewno == T[i].inf_lewo:
                T[i - 2].na_pewno = T[i].inf_lewo
                # print("i-2")
                # print(i - 2)
                # print("T[i].inf_lewo")
                # print(T[i].inf_lewo)
                if T[i - 2].na_pewno in mozliwosci:
                    mozliwosci.remove(T[i - 2].na_pewno)
            else:
                sprzecznosc = True
                break
        if T[i].na_pewno == T[i].inf_lewo and i < liczba -2 :
            if T[i + 2].na_pewno == 0 or T[i + 2].na_pewno == T[i].inf_prawo:
                T[i + 2].na_pewno = T[i].inf_prawo
                # print("i+2")
                # print(i + 2)
                # print("T[i].inf_lewo")
                # print(T[i].inf_prawo)
                if T[i + 2].na_pewno in mozliwosci:
                    mozliwosci.remove(T[i + 2].na_pewno)
            else:
                sprzecznosc = True
                break
for i in range(liczba-1,-1,-1):
    # print(i)
    if T[i].na_pewno==0:
        if T[i].inf_prawo == T[i].inf_lewo:
            T[i].na_pewno = T[i].inf_prawo
            if T[i].na_pewno in mozliwosci:
                mozliwosci.remove(T[i].na_pewno)
    if T[i].inf_prawo != T[i].inf_lewo:
        if T[i].na_pewno == T[i].inf_prawo and i>1:
            if T[i - 2].na_pewno == 0 or T[i - 2].na_pewno == T[i].inf_lewo:
                T[i - 2].na_pewno = T[i].inf_lewo
                # print("i-2")
                # print(i - 2)
                # print("T[i].inf_lewo")
                # print(T[i].inf_lewo)
                if T[i - 2].na_pewno in mozliwosci:
                    mozliwosci.remove(T[i - 2].na_pewno)
            else:
                sprzecznosc = True
                break
        if T[i].na_pewno == T[i].inf_lewo and i < liczba -2 :
            if T[i + 2].na_pewno == 0 or T[i + 2].na_pewno == T[i].inf_prawo:
                T[i + 2].na_pewno = T[i].inf_prawo
                # print("i+2")
                # print(i + 2)
                # print("T[i].inf_lewo")
                # print(T[i].inf_prawo)
                if T[i + 2].na_pewno in mozliwosci:
                    mozliwosci.remove(T[i + 2].na_pewno)
            else:
                sprzecznosc = True
                break
end = time.time()
print(end-start)
# for i in T:
#     print(i.na_pewno)
print(list(mozliwosci_dic.keys()))
# end = time.time()
# print(end-start)
#     print(i.numer)
#     print(i.inf)
#     print(i.inf_prawo)
#     print(i.inf_lewo)
#     print(i.na_pewno)
#     print("------------------------")
licznik_wystepujacych = 0
licznik_nie_wystepujacych = 0
for i in mozliwosci:
    if i in list(mozliwosci_dic.keys()):
        licznik_wystepujacych+=1
    else:
        licznik_nie_wystepujacych+=1
if sprzecznosc:
    print(0)
else:

    print(mozliwosci)
    print(math.factorial(len(mozliwosci))%1000000007)
# print(math.factorial(len(mozliwosci))%1000000007)
#NIE BIERZE POD UWAGĘ, ŻE KAŻDY KRASNAL MÓWI PRAWDĘ
# print(type(T[1].na_pewno))
# print(type(mozliwosci[2]))
# # mozliwosci.remove(T[1].na_pewno)
# print(T[1].na_pewno in mozliwosci)
# print(3 in [3,1])