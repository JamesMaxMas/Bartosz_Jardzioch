import time
n = int(input())
T=[]
wynik = []
#dzien_roz = 0
# numer_1 = 0
# zajety_czas =0
#
# max_czas_wykononia=0
# # print(range(n))
# start = time.time()
for i in range(n):
    a, b = input().split(" ")
    a=int(a)
    b= int(b)
    T.append([i+1, a, b, b-a])
    # print("b-a+1")
    # print(b-a+1)
    # print("dzien_roz")
    # print(dzien_roz)
    # if (b-a+1) > dzien_roz :
    #     # print(";)")
    #     dzien_roz = b-a+1
    #     numer_1 = i+1
    #     zajety_czas = 1
    # elif (b-a+1) == dzien_roz and max_czas_wykononia < a:
    #     # print(";)")
    #     max_czas_wykononia = a
    #     dzien_roz = b - a + 1
    #     numer_1 = i + 1
    #     zajety_czas = 1
# print(T)
# print(wynik)
# print([numer_1, dzien_roz])
# wynik.append([numer_1, dzien_roz])
# T.remove(T[numer_1-1])
# end = time.time()
# print(end - start)


def rev(a):
    return (-1)*a


# start = time.time()
T.sort(key =lambda a:rev(a[3]))
# print(T)
akt_rezerwa = T[0][3]
wynik.append([T[0][0], akt_rezerwa+1])
T.remove(T[0])
for i in T:
    if i[1] > akt_rezerwa:
        continue

    else:
        if i[2]> akt_rezerwa:
            akt_rezerwa = akt_rezerwa - i[1]
            wynik.append([i[0], akt_rezerwa + 1])
        else:
            akt_rezerwa = i[3]
            wynik.append([i[0], akt_rezerwa + 1])

    # elif i[2] >= dzien_roz-zajety_czas:
#         # print(index)
#         # print("2TAK")
#         znalazlem, numer_1, ten_index, min_czas  = True, i[0], index, i[1]
#         zajety_czas += min_czas
#         wynik.append([numer_1, dzien_roz - zajety_czas + 1])
#         T.remove(T[ten_index])
#         break
#     index +=1
#     if (not znalazlem or len(T)<1):
#         koniec =True
#         break
# end = time.time()
# print(end - start)
# start = time.time()
# koniec = False
# while (not koniec):
#     # li +=1
#     # print(li)
#     # print("----------------")
#     # print("wynik")
#     # print(wynik)
#     # print("zajety_czas")
#     # print(zajety_czas)
#     # print(koniec)
#     numer_1 = 0
#     min_czas = T[0][1]
#     index =0
#     ten_index = 0
#     znalazlem=False
#     for i in T:
#         if i[1] > dzien_roz - zajety_czas:
#             koniec = True
#             break
#         elif i[2] >= dzien_roz-zajety_czas:
#             # print(index)
#             # print("2TAK")
#             znalazlem, numer_1, ten_index, min_czas  = True, i[0], index, i[1]
#             zajety_czas += min_czas
#             wynik.append([numer_1, dzien_roz - zajety_czas + 1])
#             T.remove(T[ten_index])
#             break
#         index +=1
#     if (not znalazlem or len(T)<1):
#         koniec =True
#         break
print(len(wynik))
for i in wynik:
    print(i[0], i[1])
# end = time.time()
# print(end - start)