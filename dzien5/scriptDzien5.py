# -*- coding: utf-8 -*-

import pymysql

class MySQLConnector:
    def __init__(self,passwd):
        self.passwd = passwd
        self.conn = pymysql.connect("localhost", "root", self.passwd, "skoczkowie")
        self.c = self.conn.cursor()
        print("Połączenie ustanowione")
        nav = ''
        while(nav != "Q"):
            nav = input("Co chcesz zrobić? (S)-Select, (I)-Insert, (U)-Update, (Q)-wyjście: ")
            if(nav == "S"):
                self.select()
            elif(nav == "I"):
                self.insert()
            elif(nav == "U"):
                self.update()
        print("Połączenie zakończone")
        self.conn.close()
    def select(self):
        self.c.execute("SELECT id_skoczka, imie, nazwisko, kraj from zawodnicy order by id_skoczka;")
        res = self.c.fetchall()
        for v in res:
            id_s = v[0]
            imie = v[1]
            nazwisko = v[2]
            kraj = v[3]
            print("%3s %10s %15s %3s" % (id_s, imie, nazwisko, kraj))
    def insert(self):
        self.c.execute("insert into zawodnicy values (25, 'xxx', 'xxx', 'GER', '1981-02-24', 187, 68);")
        self.conn.commit()
        print("dane wprowadzono")
    def update(self):
        self.c.execute("Update zawodnicy Set imie = 'yyy' where id_skoczka = 25;")
        self.conn.commit()
        print("Dane zaktualizowane")
        

c1 = MySQLConnector("kamil2017")



