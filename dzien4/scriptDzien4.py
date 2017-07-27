# -*- coding: utf-8 -*-
import random
'''
def suma(*arg):
    suma = 0
    ave = 0
    for v in arg:
        suma += v
        ave = suma/len(arg)
    return ave
print(suma(2,3,4))
print(suma())
'''
#P74
'''
def wykres(d, znak = "*", ilosc = 100):
    i = 0
    Wartosci = []
    if(d == "M"):
        while(i < ilosc):
            var = int(input("Podaj kolejną wartość: "))
            while(var < 0 or var > 9):
                print("Podaj wartość z przedziału (0-9)")
                var = int(input("Podaj kolejną wartość: "))
            Wartosci.append(var)
            i += 1
    elif (d == "A"):
        while(i < ilosc):
            Wartosci.append(random.randint(0,9))
            i += 1
    for v in Wartosci:
        print(znak * v)
def menu():
    znak_menu = input("podaj znak: ")
    ilosc_menu = input("podaj ilosc: ")
    decyzja = input("Wybierz opcję: (A)-auto, (M)-manual ")
    while(decyzja != "A" and decyzja != "M"):
        decyzja = input("Błąd!!! Wybierz opcję: (A)-auto, (M)-manual ")
    if (znak_menu == "" and ilosc != ""):
        wykres(d=decyzja, ilosc = int(ilosc_menu))
    elif(znak_menu != "" and ilosc_menu == ""):
        wykres(d=decyzja, znak = znak_menu)
    elif (znak_menu != "" and ilosc_menu != ""):
        wykres(decyzja,znak_menu,int(ilosc_menu))
    else:
        wykres(d=decyzja)
menu()
'''
#P74
'''
def HTML_export(napis, color ="black", size = "12px", weight = "5"):
    return '<span style="color: '+color+'; font-size: '+size+'; font-weight: '+weight+'">'+napis+'</span>'
print(HTML_export("Witaj w HTML"))
'''
#P
'''
kolor = "blue"
licznik = 0
licznik_b = 0
licznik_r = 0
def naprzemian():
    global kolor
    global licznik, licznik_r, licznik_b
    licznik += 1
    if(kolor == "blue"):
        kolor = "red"
        licznik_r += 1
    elif(kolor == "red"):
        kolor = "blue"
        licznik_b += 1
    return kolor
print(naprzemian())
print(naprzemian())
print(naprzemian())
print(licznik, licznik_r, licznik_b)
'''
#P
'''
def dodawanie(a,b):
    return a+b
def odejmowanie(x,y):
    return x-y
def menu2():  
    dec = ""
    while (dec != "Q"):
        dec = input("Co robimy (+)-dodawanie, (-)-odejmowanie, (Q)-wyjście ")
        if(dec == "+"):
            print("wynik= ", dodawanie(int(input("a=")), int(input("b="))))
        elif(dec == "-"):
            print("wynik= ", odejmowanie(int(input("x=")), int(input("y="))))
        elif(dec != "+" and dec != "-" and dec != "Q"):
            print("Zły wybór!!!")
menu2()
'''
#P

def wprowadz():
    Tab = []
    i = "t"
    print("Wprowadź elementy (enter) - koniec wprowadzania: ")
    while(i != ""):
        i = input(" ")
        if(i != ""):
            while True:
                try:
                    i = float(i)
                    break
                except ValueError:
                    print("Błąd!! Podaj liczbę")
                    i = input(" ")
            Tab.append(float(i))
        elif(i == ""):
            print("Wprowadzanie zakończone")
            print(Tab)
            return Tab
def wypisz5(limit,lista):
    print("filtruje elementy większe od " +str(limit))
    suma = 0
    for v in lista:
        if(v >= limit):
            print(v, end=" ")
            suma += v
    print("Suma: ", suma)
wypisz5(int(input("Podaj limit odcięcia: ")),wprowadz())