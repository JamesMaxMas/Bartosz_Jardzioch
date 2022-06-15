import math
# import time
def fib2(x):
    x=x+1
    return int((1/math.sqrt(5))*(pow((1+math.sqrt(5))/2,x)-pow((1-math.sqrt(5))/2,x)))
def odw_fib(y):
    a= (1/math.sqrt(5))
    b=(1+math.sqrt(5))/2
    c=(1-math.sqrt(5))/2
def fibonacci(x):
    if x==1:
        return 1
    if x==2:
        return 2
    return fibonacci(x-1)+fibonacci((x-2))
def sprawdzanie(x):
    wynik = 1
    while x>1:
        x=x/1.618
        wynik +=1
    return wynik
m=int(input())
# print(sprawdzanie(m))
# print(fib2(sprawdzanie(m)))
# if fibonacci(m)==(1/math.sqrt(5))*(pow((1+math.sqrt(5))/2,m)-pow((1-math.sqrt(5))/2,m)):
#     print("Tak")
# print(fibonacci(m))
# print((1/math.sqrt(5))*(pow((1+math.sqrt(5))/2,m+1)-pow((1-math.sqrt(5))/2,m+1)))
# print(fib2(m))
#LICZBA M MUSI BYĆ MOŻLIWA DO ZAPISANIA JAKO ILORAZ WYRAZÓW CIĄGU FIBONACCIEGO
# koniec = 1
# wynik = 0
# liczba = m
# start = time.time()
# while koniec !=0:
#     for i in range(1,pow(10,2)):
#         a = fib2(i)
#         # print("NIE")
#
#         if liczba==1:
#             koniec = 0
#         elif a==liczba:
#             # print(i)
#             liczba = liczba/a
#             wynik+=(i)
#             koniec =0
#             break
#         elif liczba%a==0 and a != 1:
#             liczba=liczba/a
#             wynik+=(i+1)
#             break
#         elif a >m:
#             # print("NIE")
#             koniec = 0
#             break
#     else:
#         # print("NIE")
#         koniec = 0
# if liczba==1:
#     print(wynik)
# else:
#     print("NIE")
# end = time.time()
# print(end-start)
koniec = 1
wynik = 0
liczba = m
# start = time.time()
while koniec !=0:
    for i in range(sprawdzanie(liczba),1, -1):
        a = fib2(i)
        # print("i")
        # print(i)
        # print("a")
        # print(a)
        if liczba==1:
            koniec = 0
        elif a==liczba:
            # print(i)
            liczba = liczba/a
            wynik+=(i)
            koniec =0
            break
        elif liczba%a==0 and a != 1:
            liczba=liczba/a
            wynik+=(i+1)
            break
        # elif a >m:
        #     # print("NIE")
        #     koniec = 0
        #     break
    else:
        # print("NIE")
        koniec = 0
if liczba==1:
    print(wynik)
else:
    print("NIE")
# end = time.time()
# print(end - start)
#PRZY 144 ZNAJDUJE JEDEN Z WYNIKÓW ->19 A NIE NAJLEPSZY->11
# print(fib2(9999))