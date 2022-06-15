n, m = input().split()
n= int(n)
m= int(m)
T = [None]*n
litery = {}
for i in range(n):
    T[i] = str(input())
    for j in T[i]:
        litery[j]=True
stempel =""
stempel+=T[0][0]
ostatnia_litera_stempla = T[n-1][m-1]
pierwsza_litera_stempla = T[0][0]
litery_stempel ={T[0][0]:True}
wynik_poziomo = []
mozliwa_litera_nie_w_stemplu = T[0][0]
for i in range(1,m):
    stempel += T[0][i]
    litery_stempel[T[0][i]] = True
    if litery.keys() == litery_stempel.keys() and T[0][i] == ostatnia_litera_stempla:
        wynik_poziomo.append(stempel)
        # print("stempel")
        # print(stempel)
        for j in range(len(stempel)-1):
            # print("j")
            # print(j)
            # print("stempel[j]")
            # print(stempel[j])
            # print("pierwsza_litera_stempla")
            # print(pierwsza_litera_stempla)
            # print("stempel[j:(len(stempel)-1)]")
            # print(stempel[j+1:(len(stempel))])
            if stempel[j] == pierwsza_litera_stempla and stempel[j+1] == pierwsza_litera_stempla :
                wynik_poziomo.append(stempel[j+1:(len(stempel))])
            else:
                break
#--------------------------------------------
print(1)
stempel =""
# stempel+=T[0][0]
litery_stempel ={}
wynik_poziomo_dol = []
for i in range(0,m):
    stempel += T[n-1][i]
    litery_stempel[T[n-1][i]] = True
    if litery.keys() == litery_stempel.keys() and T[n-1][i] == ostatnia_litera_stempla:
        wynik_poziomo_dol.append(stempel)
        # print("stempel")
        # print(stempel)
        for j in range(len(stempel)-1):
            # print("j")
            # print(j)
            # print("stempel[j]")
            # print(stempel[j])
            # print("pierwsza_litera_stempla")
            # print(pierwsza_litera_stempla)
            # print("stempel[j:(len(stempel)-1)]")
            # print(stempel[j+1:(len(stempel))])
            if stempel[j] == ostatnia_litera_stempla and stempel[j+1] == pierwsza_litera_stempla :
                wynik_poziomo_dol.append(stempel[j+1:(len(stempel))])
            else:
                break
#==========================================
print(2)
stempel = ""
stempel+=T[0][0]
litery_stempel ={T[0][0]:True}
wynik_pionowo = []
for i in range(1,n):
    stempel += T[i][0]
    litery_stempel[T[i][0]] = True
    if litery.keys() == litery_stempel.keys() and T[i][0] == ostatnia_litera_stempla:
        # print(True)
        wynik_pionowo.append(stempel)
        for j in range(len(stempel)-1):
            # print("j")
            # print(j)
            # print("stempel[j]")
            # print(stempel[j])
            # print("pierwsza_litera_stempla")
            # print(pierwsza_litera_stempla)
            # print("stempel[j:(len(stempel)-1)]")
            # print(stempel[j+1:(len(stempel))])
            if stempel[j] == pierwsza_litera_stempla and stempel[j+1] == pierwsza_litera_stempla :
                wynik_pionowo.append(stempel[j+1:(len(stempel))])
            else:
                break
#-------------------------------------------
print(3)
stempel = ""
# stempel+=T[0][0]
litery_stempel ={}
wynik_pionowo_prawo = []
for i in range(0,n):
    stempel += T[i][m-1]
    litery_stempel[T[i][m-1]] = True
    if litery.keys() == litery_stempel.keys() and T[i][m-1] == ostatnia_litera_stempla:
        # print(True)
        wynik_pionowo_prawo.append(stempel)
        for j in range(len(stempel)-1):
            # print("j")
            # print(j)
            # print("stempel[j]")
            # print(stempel[j])
            # print("pierwsza_litera_stempla")
            # print(pierwsza_litera_stempla)
            # print("stempel[j:(len(stempel)-1)]")
            # print(stempel[j+1:(len(stempel))])
            if stempel[j] == ostatnia_litera_stempla and stempel[j+1] == pierwsza_litera_stempla :
                wynik_pionowo_prawo.append(stempel[j+1:(len(stempel))])
            else:
                break
print(4)
# print(wynik_poziomo)
# print(wynik_poziomo_dol)
# print(wynik_pionowo)
# print(wynik_pionowo_prawo)
# if len(wynik_poziomo) !=0 and len(wynik_pionowo)!=0:
#     if len(wynik_poziomo)>len(wynik_pionowo):
#         for i in wynik_pionowo:
#             if i in wynik_poziomo:
#                 wynik.append(i)
#     else:
#         for i in wynik_poziomo:
#             if i in wynik_pionowo:
#                 wynik.append(i)
# else:
#     if len(wynik_poziomo) ==0:
#         wynik = wynik_pionowo
#     else:
#         wynik = wynik_poziomo

a=len(wynik_pionowo)
b=len(wynik_pionowo_prawo)
c=len(wynik_poziomo)
d=len(wynik_poziomo_dol)
# g = [a, b, c, d]
# g.sort(reverse=True)
# for i in g:
#     if i == 0:
#
if a!=0 and b!=0 and c!=0 and c!= 0:
    wynik = list(set(wynik_pionowo).intersection(set(wynik_pionowo_prawo), set(wynik_poziomo), set(wynik_poziomo_dol)))
if a ==0:
    if b == 0:
        wynik = list(set(wynik_poziomo).intersection( set(wynik_poziomo_dol)))
    else:
        wynik = list(set(wynik_pionowo_prawo).intersection(set(wynik_poziomo), set(wynik_poziomo_dol)))
elif b ==0:
    wynik = list(set(wynik_pionowo).intersection(set(wynik_poziomo), set(wynik_poziomo_dol)))
elif c ==0:
    if d == 0:
        wynik = list(set(wynik_pionowo).intersection(set(wynik_pionowo_prawo)))
    else:
        wynik = list(set(wynik_pionowo).intersection(set(wynik_pionowo_prawo), set(wynik_poziomo_dol)))
elif d ==0:
    wynik = list(set(wynik_pionowo).intersection(set(wynik_pionowo_prawo), set(wynik_poziomo)))
else:
    wynik = list(set(wynik_pionowo).intersection(set(wynik_pionowo_prawo), set(wynik_poziomo), set(wynik_poziomo_dol)))
print(wynik)
T1 = []
for i in range(n):
    T1.append([])
    for j in range(m):
        T1[i].append(False)
poczatek = False
# for stempel in wynik:
#     l = len(stempel)
#     for i in T:
#         for j in i:
#             if j == stempel[0]:
#                 poczatek=True
#             if poczatek:
#                 T1[i][j]=True
ostateczny_wynik = []
for stempel in wynik:
    print(5)
    l = len(stempel)
    T1 = []
    for i in range(n):
        T1.append([])
        for j in range(m):
            T1[i].append(False)
    # T1 = [[False]*m]*n
    # T1 =[ [False,False, False ,False, False, False, False, False], [False,False, False ,False, False, False, False, False], [False,False, False ,False, False, False, False, False], [False,False, False ,False, False, False, False, False], [False,False, False ,False, False, False, False, False]]
    # print("stempel")
    # print(stempel)
    # print("l")
    # print(l)
    for i in range(n):
        # print("i")
        # print(i)
        for j in range(m):
            # print("j")
            # print(j)
            if T1[i][j]!=True:
                # print("m-j")
                # print(m - j)
                if m-j >= l:
                    for k in range(l):
                        # print("T[i][j+k]")
                        # print(T[i][j+k])
                        # print("stempel[k]")
                        # print(stempel[k])
                        if T[i][j+k]==stempel[k]:
                            # print(1)
                            continue
                        else:
                            # print(2)
                            break
                    else:
                        # print(3)
                        for k in range(l):
                            # print("T1[i][j + k]")
                            # print(T1[i][j + k])
                            # print("i")
                            # print(i)
                            # print("j+k")
                            # print(j+k)
                            T1[i][j + k] = True
                else:
                    break
    for i in range(m):
        # print("i")
        # print(i)
        for j in range(n):
            # print("j")
            # print(j)
            if T1[j][i]!=True:
                # print("m-j")
                # print(m - j)
                if n-j >= l:
                    for k in range(l):
                        # print("T[i][j+k]")
                        # print(T[i][j+k])
                        # print("stempel[k]")
                        # print(stempel[k])
                        if T[j+k][i]==stempel[k]:
                            # print(1)
                            continue
                        else:
                            # print(2)
                            break
                    else:
                        # print(3)
                        for k in range(l):
                            # print("T1[i][j + k]")
                            # print(T1[i][j + k])
                            # print("i")
                            # print(i)
                            # print("j+k")
                            # print(j+k)
                            T1[j+k][i] = True
                else:
                    break
    # print(T1)
    for i in range(n):
        # print("i")
        # print(i)
        for j in range(m):
            if T1[i][j]==False:
                break
        else:
            continue
        break
    else:
        # print(stempel)
        ostateczny_wynik.append(stempel)
# print(ostateczny_wynik)
print(len(ostateczny_wynik))
dlugosci = ""
ostateczny_wynik.sort()
for i in ostateczny_wynik:
    dlugosci+=(str(len(i)))
    dlugosci+=" "
print(dlugosci)