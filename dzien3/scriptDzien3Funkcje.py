# -*- coding: utf-8 -*-
import random
#FUNKCJE
'''
def powitanie(imie):
    witaj = "Witaj " + imie
    return witaj

a = powitanie("Kamil")
b = powitanie("Ania")
c = powitanie("Agata")
print(a,b,c)
'''
#
'''
def powitanie(imie):
    witaj = "Witaj " + imie
    return witaj
L = []
for i in range(1,4):
    L.append(powitanie(input("Podaj imie: ")))
print(L)
'''
#
'''
def dodawanie(a,b,imie='Anonim',nazwisko='Anonim'):
    wynik = a+b
    print(a,b)
    print(imie,nazwisko)
    return wynik

res = dodawanie(a=14,b=25,nazwisko='olej')
print(res)
'''
#69
'''

def silnia(n):
    res = 1
    L = []
    i = 1
    while(i <= n):
        res *= i
        L.append(res)
        i += 1
    return L

#--------------------------
def wyswietl(lista):
    for i in lista:
        print(i, end=' ')
#--------------------------------

wyswietl(silnia(7))
'''
#P70
'''
def fibo(n):
    tablica = [0,1]
    suma = 0
    i = 2
    a = 0
    while(i < n):
        a = (tablica[i-2] + tablica[i-1])
        tablica.append(a)
        i += 1
    for i in tablica:
        suma = suma + i
    return tablica[len(tablica)-1], suma, tablica

Fib = fibo(6)
print("(Element, Suma, Kolejne elementy)",Fib)
'''
#71
'''
def zdania(a=5):
    wyrazy = ["ciąg", "Fibonacciego", "ciąg", "liczb", "naturalnych", "sposób", "następujący"]
    i = 0
    zdanie = []
    while(i < a):
        zdanie.append(wyrazy[random.randint(0,len(wyrazy)-1)])
        i += 1
    return zdanie
def format(zdanie):
    for i,v in enumerate(zdanie):
        if(i == 0):
            print(v.capitalize(), end=" ")
        elif(i == len(zdanie)-1):
            print(v, end = ".")
        else:
            print(v, end = " ")
            
           
format(zdania(6))
'''
#72 wzor na odleglosc
from math import sqrt
'''
def dist(x1,y1,x2,y2):
    d = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return round(d,2)
print(dist(1,1,5,5))
'''
#

def dist(x1,y1,x2,y2):
    d = sqrt(((x2-x1)**2)+((y2-y1)**2))
    return round(d,2)

i = 0
x = []
y = []
print("podaj polozenie poczatkowe: ")
while(i < 2):
    if (i == 1):
        print("podaj polozenie koncowe: ")
    else:
        u1 = int(input(" "))
    u2 = int(input(" "))
    x.append(u1)
    y.append(u2)
    i = i + 1
    
print("dystans: ", dist(x[0],x[1],y[0],y[1]))    
    