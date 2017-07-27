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
class Lotto:
    def __init__(self):
        print(random.sample(range(1,50),6))
        
los1 = Lotto()
los2 = Lotto()
los3 = Lotto()
los4 = Lotto()
los5 = Lotto()
los6 = Lotto()