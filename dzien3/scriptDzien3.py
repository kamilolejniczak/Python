# -*- coding: utf-8 -*-
'''
x = int(input("x: "))
y = int(input("Podaj do której potęgi podnieść wartość y: "))
res = 1
i = 1
while(i <= y):
    res *= x
    i += 1
print(res)
'''
#P
'''
n = int(input("n: "))
a1 = float(input("a1: "))
q = float(input("q: "))
i = 0
S = 0
L = []
while(i < n):
    S += a1*(q**i)
    L.append(a1*(q**i))
    i += 1
#odstępy Modulo %, 15.2f = 12znakow+kropka+2miejsca po przecinku
print("%10s %15.2f" % ("Suma: ",S))
print("%10s " % ("Składowe: "), end = "")
#indeksy i wartości i,v
for i,v in enumerate(L):
    if(i == 0):
        print("%15.2f" % (v), end = " ")
    else:
        print("%5.2f" % (v), end = " ")
'''
#
'''
n = int(input("n: "))
a1 = float(input("a1: "))
q = float(input("q: "))
i = 0
S = 0
L = []
while(i < n):
    S += a1*(q**i)
    L.append(a1*(q**i))
    i += 1
#odstępy Modulo %, 15.2f = 12znakow+kropka+2miejsca po przecinku
print("%10s %15.2f" % ("Suma: ",S))
print("%10s %10s" % ("Składowe: ",""), end = "")
#indeksy i wartości i,v
for v in L:
    print("%5.2f" % (v), end = " ")
'''
#
'''
napis = input("ciag znakow: ")
s = input("szukane: ")
i = 0
licznik = 0
while(i <= len(napis)-1):
    if(napis[i] == s):
        print("znaleziono", s, "na pozycji", i+1)
        licznik += 1
    i += 1
print("szukaną frazę znaleziono", licznik, "razy")
'''
#
'''
napis = input("ciag znakow: ")
s = input("szukane: ")
i = 0
licznik = 0
while(i < len(napis)):
    tab = napis[i:i+len(s)]
    if(tab == s):
        print("znaleziono", s, "na pozycji", i+1)
        licznik += 1
        i = i + len(s)
    else:
        i += 1
print("szukaną frazę znaleziono", licznik, "razy")
'''
#P67
#farenheit F=(C+1.8) + 32
#F = (C+1.8)+32
'''
C = range(-20,45,5)
print(C)
i = len(C) - 1
print("%5s | %3s" % ("C", "F"))
while(i >= 0):
    print("%+5i | %6.2f" % (C[i], (C[i]*1.8)+32))
    i -= 1
'''
#
'''
start = int(input("start: "))
stop = int(input("stop: "))
step = int(input("step: "))
if((stop - start) % step == 0):
    C = range(start, stop+step,step)
else:
    C = range(start,stop,step)
i = len(C) - 1
print("%5s | %3s" % ("C", "F"))
while(i >= 0):
    if(C[i] == 0):
        print("-------------------------")
        print("%5i | %6.2f" % (C[i], (C[i]*1.8)+32))
        print("-------------------------")
    else:
        print("%+5i | %+6.2f" % (C[i], (C[i]*1.8)+32))
    i -= 1
'''
#P68
'''
Dop = ['3','3.5','4','4.5','5']
oceny = 'x'
O = []
while(oceny != ''):
    oceny = input("wprowadź ocenę: ")
    if(oceny in Dop):
        O.append(float(oceny))
    elif(oceny == ""):
        print("wprowadzanie ocen zakonczone")
    else:
        print("ocena niepoprawna")
sr = 0
for oceny in O:
    sr += oceny
print("srednia ocen", round(sr/len(O),2))
'''

# FUNKCJE
#=========================================================================

