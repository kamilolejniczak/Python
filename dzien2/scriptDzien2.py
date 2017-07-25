# -*- coding: utf-8 -*-
import random

#Dzień 2
'''
literki = {'a' : 'A', 'b' : 'B', 'c' : 'C'}
print(literki)
print(len(literki))
print(literki['a'], literki['b'])
literki['c'] = "napis"
print(literki['c'])
print(literki.keys(), literki.values())
literki['d'] = 'D'
del literki['c']
print(literki)
literki[2] = 'abc'
print(literki[2])
to_str = str(literki)
print(to_str[0], to_str[1])
'''
#P
'''
key1 = input('Podaj liczę (1-5) zapisaną słownie: ')
to_dec = {'jeden' : 1, 'dwa' : 2, 'trzy' : 3, 'cztery' : 4, 'pięć' : 5, 'piec' : 5}
to_rom = {1 : 'I', 2 : 'II', 3 : 'III', 4 : 'IV', 5 : 'V'}
print(key1.capitalize()+" w postaci liczby dziesiętnej to: "
      +str(to_dec[key1])+", a w postaci rzymskiej: " 
      +str(to_rom[to_dec[key1]]))
'''
#P
'''
nazwa = input("Jaki produkt chcesz zamówić? (chleb, bagietka, bułki): ")
ilosc = int(input("Podaj ilość wybranoego produktu: "))
nazwa_t = {"chleb" : '1x1', 'bułki' : '2x2', 'bagietka' : '3x3'}
cena = {'1x1' : 1.99, '2x2' : 3.99, '3x3' : 5.99}
print("Do zapłaty: "
      +str(cena[nazwa_t[nazwa]]*ilosc) 
      + "zł ("
      +str(round((cena[nazwa_t[nazwa]]*ilosc)*1.23,2))
      +"zł brutto.)")
'''
#P
'''
ksztalty = set(['kolo', 'kwadrat', 'trójkąt'])
ksztalty.add('okrąg')
ksztalty.discard('kolo')
print(ksztalty)
okragle = set(['okrąg'])
print(len(ksztalty), len(okragle))
print(ksztalty.issubset(okragle))
print(ksztalty.issuperset(okragle))

#P operacje na zbiorach
print(ksztalty)
print(okragle)
print(ksztalty | okragle)
print(ksztalty & okragle)
print(ksztalty - okragle)
print(ksztalty ^ okragle )
'''
#P
'''
los1 = random.randint(1,49)
los2 = random.randint(1,49)
los3 = random.randint(1,49)
los4 = random.randint(1,49)
los5 = random.randint(1,49)
los6 = random.randint(1,49)
print(los1, los2,los3,los4,los5,los6)
'''
#
'''
S = set()
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
S.add(random.randint(1,49))
L = list(S)
print(L[:6])
'''
#instrukcja if
'''
a = int(input("Podaj liczbę: "))

if(a%2 == 0):
    print("Liczba "+str(a)+' jest parzysta')
    if(a>=10):
        print("Liczba "+str(a)+' jest parzysta i większa równa od 10')
    else:
        print("Liczba "+str(a)+' jest parzysta i mniejsza od 10')
else:
    print("Liczba "+str(a)+' jest nieparzysta')
print('jestem już za instrukcją if')
'''
#
'''
a = int(input("Podaj liczbę: "))

if(a%2 == 0 and a >= 10):
    print("Liczba "+str(a)+' jest parzysta i większa równa od 10')
elif(a%2 == 0 and a < 10):
    print("Liczba "+str(a)+' jest parzysta i mniejsza od 10')
else:
    print("Liczba "+str(a)+' jest nieparzysta')
'''
#
'''
if(bool(0)):
    print(bool(0))
if(bool(1)):
    print(bool(1))
if(bool(2)):
    print(bool(2))
if(bool(3)):
    print(bool(3))   
if(bool(4)):
    print(bool(4))
'''
#
'''
lista = [1,2,3,4,5,6,7,8,9]
index = int(input("Podaj któRy element chcesz wyświetlić: "))
if(index >= 0 and index <= (len(lista)-1)):
    print("Index is ok")
    print(lista[index])
else:
    print('out of range')
'''
#
'''
lista = [1,2,3,4,5,6,7,8,9]
if(lista[0]>0 and lista[1]>0):
    print('oba elementy większe od zera')
elif(lista[0]>0 and lista[1]<0):
    print('Pierwszy element wiekszy od zera a drugi mniejszy od zera')
elif(lista[0]<0 and lista[1]>0):
    print('pierwszy element mniejszy od zera a drugi wiekszy od zera')
else:
    print('Oba elementy są mniejsze od zera')
'''
#zbiory
'''
A = set([1,2,3,4,5,])
B = set([1,2,3,5])
if(A == B):
    print('zbiory równe')
elif(A.issuperset(B)):
    print('A jest nadzbiorem B')
else:
    print('B jest nadzbiorem A')
'''
#
'''
lista = [1,2,3,4,5,6,7,8,9]
i = 0
while(i <=(len(lista)-1)):
    print("Index: "+str(i)+"\t wartość: "+str(lista[i]))
    i += 1
print('poza pętlą')
'''
#
'''
lista = [1,2,3,4,5,6,7,8,9]
i = len(lista)-1
print('parzyste')
while(i >= 0):
    if(lista[i]%2 == 0):
        print("Index: "+str(i)+"\t wartość: "+str(lista[i]))
    i -= 1
else:
    print('jestem w else')
print('jestem poza')
'''
#któRa z liczb jest większa i o ile? wyrażenie trójargumentowe
'''
a = 14
b = 15

print("a jest wieksze od b o: "+str(a-b)) if(a>=b) else print("a jest mniejsze od b o: "+str(b-a))
'''
#
'''
lista = [1,2,3,4,5,6,7,8,9]
for var in lista:
    print("Wartość: "+str(var))
lista.append(15)
for index,var in enumerate(lista):
    print("Index: "+str(index)+"\tWartość: "+str(var))

SL = {'a' : 1, 'b' : 2, 'c' : 3}
for k in SL:
    print(k, SL[k])
for k in SL:
    if(SL[k]>=2):
        print(k,SL[k])
'''
#
'''
sl = range(100)
print(sl)
for i in sl:
    print(i)
for j in range(15,25):
    print(j)
for k in range(0,10):
    print(k**4,k,k**2,k**3)
for l in range(0,100):
    print("wynik: %4i%6i%8i" % (l,l**2,l**3))
for m in range(5,100,10):
    print("pierwiastek kwadratowy z %4i wynosi: %6.2f" % (m,m**0.5))
'''
#57
'''
sklep_produkty = {"monitor" : 1, "klawiatura logitech" : 2, "mysz" : 3}
produkty_cena = {1:1500,2:400,3:200}
produkty_dostepnosc = {1:5,2:5,3:15}
suma = 0
i = "t"
while(i == "t"):
    zamowienie = input("Wybierz towar: ")
    zamowienie_ilosc = int(input("podaj ilość: "))
    for k in sklep_produkty:
        if(zamowienie in sklep_produkty.keys()):
            if(zamowienie == k and produkty_dostepnosc[sklep_produkty[k]]>= zamowienie_ilosc):
                print("Produkt dostępny: " + k)
                print("Zamawiasz: " + str(zamowienie_ilosc)+' szt')
                suma += zamowienie_ilosc*produkty_cena[sklep_produkty[k]]
            elif(zamowienie == k and produkty_dostepnosc[sklep_produkty[k]]< zamowienie_ilosc):
                print("Produkt dostępny: "+k)
                print("Jest dostępne tylko: "+str(produkty_dostepnosc[sklep_produkty[k]])+ ' szt')
        else:
            print("Brak produktu w sklepie")
    i = input("Czy chcesz zamawiać dalej? (t/n)")
print("Do zapłaty: "+str(suma))
'''
#P
'''
i = "t"
res = []
to_dec = {'1' : 'jeden', '2' : 'dwa', '3' : 'trzy',
          '4' : 'cztery', '5' : 'pięć', '6' : 'sześć',
          '7' : 'siedem', '8' : 'osiem', '9' : 'dziewięć'} 
while(i == 't'):
    dig = input("Wprowadź cyfrę: ")
    if(dig.isdigit()):
        res.append(to_dec[dig])
    else:
        print('podana wartość nie jest cyfrą')
    i = input("czy chcesz wprowadzać dalej? (t/n)")
print(res)
for i in res:
    print(i,end="<<<===d(*_*)b===")
'''
#P61
'''
line = range(1,6)
n = 1
print("    %3i%3i%3i%3i%3i" % (1,2,3,4,5))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
while(n<=5):
    print(str(n)+" (*..*)",end="")
    print("%3i%3i%3i%3i%3i" % (n*line[0], n*line[1], n*line[2], n*line[3], n*line[4]))
    n += 1
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
'''
#P3
print("Kwadraty Liczb Nieparzystych")
np = range(1,10,2)
i = len(np) - 1
while(i>=0):
    if(i == 0):
        print(np[i]**2)
    else:
        print(np[i]**2, end=", ")
    i -= 1

        
    