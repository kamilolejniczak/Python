# -*- coding: utf-8 -*-
'''
class PierwszaKlasa:
    a = 1
    b = "witaj w klasie"
    
    
    def witaj(self):
        print("Witaj w metodzie klasie")
    def dodaj(self, x, y):
        print("dodawanie")
        self.x = x
        self.y = y
        return self.x + self.y
    def odejmowanie(self):
        print("odejmowanie")
        return self.x - self.y

obiekt1 = PierwszaKlasa()
obiekt1.witaj()
print(obiekt1.dodaj(4,5))
print(obiekt1.odejmowanie())
obiekt2 = PierwszaKlasa()
obiekt2.witaj()
print(obiekt2.dodaj(2,3))
'''
#
'''
class PierwszaKlasa:
   def __init__(self, x, y):
      self.x = x
      self.y = y
      self.dodaj()
      self.odejmowanie()
   def dodaj(self):
      self.wynik_d = self.x + self.y
   def odejmowanie(self):
      self.wynik_o = self.x - self.y
      return self.wynik_o
   def __str__(self):
      return "Wynik dodawania wynosi: "+str(self.wynik_d)+", a odejmowania wynosi: " + str(self.wynik_o)
   def __add__(self,other):
      return self.x + other.x, self.y + other.y
   def __ge__(self,other):
      return self.wynik_d >= other.wynik_d, self.wynik_o >= other.wynik_o
      

obiekt1 = PierwszaKlasa(5,6)
obiekt2 = PierwszaKlasa(1,2)
print(obiekt1)
#rzutowanie z ___str__
print(obiekt2)
#rzutowanie z __add__
print(obiekt1 + obiekt2)
#rzutowanie na operacje >=
print(obiekt1 >= obiekt2)
print(obiekt1.wynik_d >= obiekt2.wynik_d)

'''
#75
'''
class BMI:
    def __init__(self, imie, nazwisko, waga, wzrost):
        self.imie = imie
        self.nazwisko = nazwisko
        self.waga = waga
        self.wzrost = wzrost
        self.obliczBMI()
    def obliczBMI(self):
        self.BMI = round(self.waga / ((self.wzrost/100)**2))
    def __str__(self):
        return "BMI dla "+self.imie+ " " +self.nazwisko+" wynosi: "+str(self.BMI)
    
z1 = BMI("Kamil","O.", 73, 176)
print(z1)
        
'''
# sample - bez zwracania - lotto losowanie
import random
'''
class Lotto:
    def __init__(self):
        self.L = range(1,50)
        self.Tab = random.sample(self.L,6)
        self.sort()
    def sort(self):
        self.Tab_s = sorted(self.Tab)
    def __str__(self):
        self.res = ""
        for i, v in enumerate(self.Tab_s):
            if(i == len(self.Tab_s)-1):
                self.res += str(v)
            else:
                self.res += str(v) + ", "
        return "Wynik losowania: " + self.res
        
los1 = Lotto()
print(los1)
los2 = Lotto()
print(los2)
los3 = Lotto()
los4 = Lotto()
los5 = Lotto()
los6 = Lotto()
'''
#dziedziczenie
'''
class Szkolenia:
    def __init__(self, nazwa, termin, cena_n, ilosc):
        self.nazwa = nazwa
        self.termin = termin
        self.cena_n = cena_n
        self.ilosc = ilosc
    def obliczCalk(self):
        self.suma_b = (self.cena_n*self.ilosc)*1.23
        return self.suma_b
    
class Technologie(Szkolenia):
    def __init__(self, nazwa, termin, cena_n, ilosc, technologia, poziom):
        super().__init__(nazwa, termin, cena_n, ilosc)
        self.technologia = technologia
        self.poziom = poziom

class Trenerzy(Technologie):
    def __init__(self, nazwa, termin, cena_n, ilosc, technologia, poziom, imie, nazwisko, pensja):
        super().__init__(nazwa, termin, cena_n, ilosc, technologia, poziom)
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja
    def obliczCalkTrener(self):
        return self.obliczCalk() - (self.pensja*1.23)

s1 = Technologie("Kurs Python dla dzieci", '2000-02-20', 2000, 20, "Python3.6", 'python')
s2 = Trenerzy("Kurs Python dla dzieci", '2000-02-20', 2000, 20, "Python3.6", 'python', "Michał", "Kruczkowski", 1000)
print(s2.obliczCalkTrener())
'''
#P80
'''
class Produkt:
    def __init__(self, nazwa, cena):
        self.nazwa = nazwa
        self.cena = cena
    def __str__(self):
        return "Produkt: "+self.nazwa +" "+str(self.cena)

class Oprogramowanie(Produkt):
    def __init__(self, nazwa, cena, jezyk, system):
        super().__init__(nazwa, cena)
        self.jezyk = jezyk
        self.system = system
    def __str__(self):
        return "Produkt: "+self.nazwa+" "+str(self.cena)+" "+self.jezyk+self.system

class Szkolenia(Oprogramowanie):
    def __init__(self, nazwa, cena, jezyk, system, termin):
        super().__init__(nazwa, cena, jezyk, system)
        self.termin = termin
    def __str__(self):
        return "Produkt: "+self.nazwa+" "+str(self.cena)+" "+self.jezyk+" "+self.system+" "+self.termin

sk1 = Szkolenia("Witaj Python", 1000, "Python2.8", "MacOS", "2012-02-20")
print(sk1)
'''
#
'''
class Kolory:
    def __init__(self, kolor_r, kolor_g, kolor_b):
        self.kolor_r = kolor_r
        self.kolor_g = kolor_g
        self.kolor_b = kolor_b
    def __str__(self):
        return "Twój kolor: ["+str(self.kolor_r)+" ' "+str(self.kolor_g)+" ' "+str(self.kolor_b)+"]"
    def __add__(self,other):
        return (self.kolor_r + other.kolor_r)/2, (self.kolor_g + other.kolor_g)/2, (self.kolor_b + other.kolor_b)/2  

kolor1 = Kolory(100,100,100)
print(kolor1)
kolor2 = Kolory(100,150,50)
print(kolor2)
kolor3 = kolor1 + kolor2
print(kolor3)
'''
#

class Pracownik:
    def __init__(self, imie, nazwisko, etat="staz", pensja=500):
        self.imie = imie
        self.nazwisko = nazwisko
        self.etat = etat
        self.pensja = pensja
    def przelicz(self):
        self.pensja_b = self.pensja*1.23
        return self.pensja_b, self.pensja


class Kontrakt(Pracownik):
    def __init__(self,  imie, nazwisko, etat="staz", pensja=500):
        super().__init__(imie, nazwisko, etat, pensja)
    def zmienKontrakt(self, etat, pensja):
        self.etat = etat
        self.pensja = pensja
    def dodajNadgodziny(self, liczba):
        self.liczba = liczba
        self.pensja = self.pensja +((self.pensja / (20 * 8)) * self.liczba)
    def __str__(self):
        return "Pensja pracownika: "+self.imie+" "+self.nazwisko+" z nadgodzinami: " + str(self.pensja*1.23)+" zł brutto"
    
p1 = Kontrakt("Adam","Kowalski")
print(p1.przelicz())
p1.zmienKontrakt("Dev",5000)
print(p1.przelicz())
p1.dodajNadgodziny(50)
print(p1.przelicz())