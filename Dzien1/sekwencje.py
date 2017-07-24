# -*- coding: utf-8 -*-
'''
napis = "zawartość"
print(napis.capitalize())
print(napis.count("aw"))
print(napis.islower())
print(napis.index("a"))
print(napis.replace("zawa","otwa"))
'''
#P
'''
Tab = []
Tab.append(1)
Tab.append("abc")
Tab.append('A')

print(Tab[0],Tab[1],Tab[2])
'''
#deklaracja i przypisanie wartości
oceny = []
'''
a = input("Podaj ocenę")
oceny.append(a)
oceny.append(input("Podaj ocenę"))
print(oceny[0], oceny[1])
oceny[0] = '5'
print(oceny[0], oceny[1])

oceny2 = [3,4,5]
'''
#P
'''
ListList = [[1, 2, 3], ["Nocny", [0,1,2]]]
print(ListList[1][0])
oceny2 = [3,4,5,6,7,8,9,10]
print(oceny2[3::2])
print(len(oceny2))

text = 'napis'
lista = list(text)
print(lista)
lista[2] = "w"
print(lista)
print(lista.pop(2), len(lista))
print(lista)
print(lista[2], len(lista))
'''
#
'''
artykuly = [["mleko","chleb","cukierki"],[1.99,3.15,13.55]]
print(artykuly)
print("nazwa\t\tcena")
print(artykuly[0][0] +"\t\t"+ str(artykuly[1][0]))
print(artykuly[0][1] +"\t\t"+ str(artykuly[1][1]))
print(artykuly[0][2] +"\t"+ str(artykuly[1][2]))
'''
#
'''
krotka = ("a",2,13.5)
krotka2 = "a","b","c"
print(krotka)
print(krotka2)
'''
#P
'''
krotka = "dzien","miesiac","rok"
print(krotka)

data = (("mleko","chleb","cukierki"),("01-01-2019","01-01-2020","01-01-2021"))
print(data)
print(data[0][0] +"\t\t"+ str(data[1][0]))
print(data[0][1] +"\t\t"+ str(data[1][1]))
print(data[0][2] +"\t"+ str(data[1][2]))
'''
#P
tabelka = [("Kowal",("Nowak","-Cos")),("1987-02-15","1985-02-14"),["dev","dev"]]
tabelka[2][0] = "admin"
print(tabelka[0][0], tabelka[1][0], tabelka[2][0])
print(tabelka[0][1][0]+tabelka[0][1][1], tabelka[1][1], tabelka[2][1])

