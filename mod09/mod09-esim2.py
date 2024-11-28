
#Harjoitus opettajan kanssa: 9. Luokka, olio, alustaja ja 10 myös.

import random

class Autotalli:
    def __init__(self):
        self.autot = []

    def auto_sisaan(self, auto):
        # Tarkistetaan, ettei auto ole jo tallissa
        #parempi tapa olisi muuttaa lista joukoksi, jolloin duplikaatteja ei sallita
        for a in self.autot:
            if a == auto: #=>  True, jos  viitattavat
                return
        self.autot.append(auto)

    def auto_ulos(self, auto):
        self.autot.remove(auto)

    def tulosta_inventaario(self):
        print("Auto tallissa:")
        for auto in self.autot:
            auto.tulosta_ominaisuudet()


class Kuljettaja:
    def __init__(self, nimi, ika, auto):
        self.nimi = nimi
        self.ika = ika
        self.auto = auto

    def aja(self):
        print(f"Olen {self.nimi}, {self.ika} ja ajan autoa {self.auto.rek_nro}")
        self.auto.kiihdyta(40)
        print(self.auto.nopeus)
        self.auto.kulje(1)
        self.auto.kiihdyta(140)
        print(self.auto.nopeus)
        self.auto.kulje(0.1)
        self.auto.kiihdyta(-250)
        self.auto.tulosta_ominaisuudet()

class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.matka = 0
        self.huippunopeus = huippunopeus
        self.kuljettaja = "Räikkönen"
        print(f"Auto luoto {rek_nro}, huiput: {huippunopeus}")


    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Nopeus: {self.nopeus}, matkamittari: {self.matka}")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        # rajoitetaan kiihdytykseen tulos huippunopeuteen.
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        # auto pysähtyy, jos nopeus alle o
        if self.nopeus < 0:
            self.nopeus = 0


    def kulje(self, aika):
        # aika tunneissa
      self.matka += aika * self.nopeus

# Luodaan oliot ja sijoitetaan viittaukseen niihin muuttuujiin
a1 = Auto("ABC-123", 142) ## 'a1' on olio, joka kuuluu luokkaan 'Auto'
a2 = Auto("ZYX-789", 250)
kuski = Kuljettaja("Räikkönen", 44, a1)

kuski.aja()
#vaihdetaan kuljettajan autoa ja ajetaan uudestaan
kuski.auto = a2
kuski.aja()

# Luodaan Autotalli-tyyppinen olio ja sijoitetaan auto sinne
talli = Autotalli()
talli.auto_sisaan(a1)
talli.tulosta_inventaario()
talli.auto_sisaan(a2)
#talli.auto_sisaan(a2)
#talli.auto_ulos(a1)

talli.tulosta_inventaario()

#Luodaan 10 erilaista auto-oliota autotalliin
for i in range(10):
    uusi_auto = Auto(f"ABC-{i+1}", random.randint(100, 200))
    talli.auto_sisaan(uusi_auto)
#talli.tulosta_inventaario()


#a2.kiihdytä(5)
#print(a2.nopeus)
#a2.kiihdytä(300)
#a1.kiihdytä(-50)
#a2.kiihdytä(-200)
#a1.tulosta_ominaisuudet()
#a2.tulosta_ominaisuudet()

# mod09 harjoitus 1 esimerkkiratkaisu


#a1 = a2
#a1.tulosta_rekkari()

#a1.rek.nro = "0"
#a2.tulosta_rekkari()
