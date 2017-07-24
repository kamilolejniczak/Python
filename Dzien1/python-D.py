# -*- coding: utf-8 -*-

#komentarz jednowierszowy
zmienna1 = 5
zmienna2 = 5.3
'''
poczatek komentarza blokowego
text = "to jest moj tekst"
text2 = 'to jest inny tekst'
literki = "A"
literki = 'a'
koniec komentarza blokowego

witaj = "i'm kamil"
zmienna3 = 2 + 5
Zmienna3 = 'liczba'
nowa_zmienna = zmienna3 + 5

print(zmienna1)
print(zmienna1, zmienna2)
print(witaj)
print(zmienna3, Zmienna3)
print(nowa_zmienna)
print("Hi, "+ witaj + "." + " ", zmienna3)
print("przed zmiana", Zmienna3)
Zmienna3 = 3.14
print("po zmianie:", Zmienna3)
del zmienna1
#print(zmienna1)
'''
#P1
'''
zmienna_a = 1
zmienna_b = 2.4
zmienna_c = "w1"
print(zmienna_a,zmienna_b,zmienna_c)
#P2
zmienna_a = 2.1
zmienna_b = "abc"
zmienna_c = 0
print(zmienna_a,zmienna_b,zmienna_c)
#P3
imie = 'kamil'
nazwisko = 'o'
rok_urodzenia = '1999-01-01'
stanowisko = 'inspektor'
placa = '10k'
print(imie,nazwisko,rok_urodzenia,stanowisko,placa)
'''
#P4
'''
pi = 3.14
#int() - rzutuje na integer
#input() - czyta wartość z klawiatury - string!
promien = int(input("podaj liczbę "))
pole_kola = pi*promien*promien
#podstawa ** wykladnik
print(pole_kola, pi*(promien**2))
'''
#P5
'''
imie = input('podaj imie ')
nazwisko = input('podaj nazwisko ')
rok_urodzenia = input('podaj datę urodzenia ')
stanowisko = input('podaj stanowisko ')
placa = input('podaj płacę ')
print(imie,nazwisko,rok_urodzenia,stanowisko,placa)
'''
#type() - zwraca typ wartości zmiennej
'''
print(type(pole_kola))
print(type(21j))

dluga = 3147483647
print(type(dluga))
dluga2 = 32
print(type(dluga2))
#// podwójny slash odrzuca resztę
print(3/2, 3//2)
print(round(1.3),round(1.5),round(1.8),round(-1.8))
print(int(1.3),int(1.5),int(1.9))
'''
#P6
'''
kwota_netto = float(input("podaj kwotę netto: "))
print(kwota_netto, "zł")
vat = int(input("Podaj stawkę vat (3%, 7%, 23%): "))
kwota_brutto = kwota_netto + (kwota_netto*(vat/100))
print("Twoja kwota brutto przy stawce "+str(vat)+" vat wynosi: "+str(kwota_brutto))
'''
#P7
'''
nazwa1 = 'chleb'
nazwa2 = 'mleko'
nazwa3 = 'cukierki'

cena_p1 = 1.99
cena_p2 = 4.15
cena_p3 = 15.99

zamowienie_p1 = int(input("liczba chlebów: "))
zamowienie_p2 = float(input("litry mleka: "))
zamowienie_p3 = float(input("waga cukierków (g): "))
suma = (cena_p1 * zamowienie_p1) + (cena_p2 * zamowienie_p2) + (cena_p3/1000 * zamowienie_p3)

print("Twoje zamówienie")
print("================")
print("Liczba chlebów: ", zamowienie_p1, "szt.")
print("Ilość mleka: ", zamowienie_p2, "l.")
print("Waga cukierków: ", zamowienie_p3, "g.")
print("================")
print("Do zapłaty: ")
print("================")
print(round(suma, 2), "zł")
'''
#P
'''
print((1+1j)+(1+1j))
a = 12
b = 1+(-1j)
print(a*b)
log1 = True
print(type(log1))

print(bool(""), bool(0), bool("Ala"))

a = """
autor:
data:
wersja:
"""
print(a)
#\n - znak przejścia do nowej linii
b = "autor:\ndata:\nwersja:"
print(b)
'''
#P
'''
txt = "napis "
print(txt*3)

imie = input("Podaj imie: ")
imie_1 = imie + ", "
imie_2 = imie + "."
n = int(input("Podaj ile razy mam wpisać imię: "))

print((imie_1 * (n-1)) + imie_2)


imie = input('podaj imie ')
nazwisko = input('podaj nazwisko ')
wiek = int(input('podaj wiek '))
stanowisko = input('podaj stanowisko ')
pensja = int(input('podaj pensję '))
print("pan " + imie + " " + nazwisko + " " + "w wieku " + str(wiek) + " lat " + "objął stanowisko " + stanowisko + " z pensją " + str(pensja))

a = 1
print(type(a))
napis = str(a)
#bool(), float(), int(), str()
print(type(napis))
'''

#P
'''
kwota_netto_h = 5500/168
print("Kwota netto / H", round(kwota_netto_h,2), "zł")
print("Kwota brutto / H", round(kwota_netto_h * 1.23,2), "zł")
'''
#P
'''
p = False
q = False
dM1 = not (p and q)
dM2 = (not p) or (not q)
print(dM1, dM2)
#==porównanie wartości
print(dM1 == dM2)
'''
#P
'''
a = False
b = False
c = True

p1 = (not a) and (not b) and (not c)
p2 = (not a) and (not b) and c
p3 = (not a) and b and (not c)
p4 = a and (not b) and (not c)
print(p1,p2,p3,p4)
res = p1 or p2 or p3 or p4
print(res)

print('ala' == 'ala')
print('ala' < 'alan')
'''

#P
'''
liczba = round(17**(1/2),2)
uroj = 1j
res = str(liczba * uroj)
print("liczba zespolona: 0 + "+res)

Z = 17 % 7
print(Z**2 + 3*Z)

print((str(1.2e+3+34.5) + ";") * 20)
'''
#P
'''
napis1 = input("Podaj napis1 ")
napis2 = input("Podaj napis2 ")
print("napis 1 jest większy leksykograficznie", napis1 > napis2)
print("napisy są takie same", napis1 == napis2)
print("napis 2 jest większy leksykograficznie", napis1 < napis2)
'''
#P
'''
print("imie\t"+"nazwisko\t"+"stanowisko")
#P
N = int(input("Stan konta za x lat "))
SPK = int(input("Stan konta "))
P = float(input("Stopa procentowa "))
res = round(SPK*(1+P/100)**N,2)
print("Kwota po "+str(N)+" latach wynosi: "+str(res) +"zł.")
'''


