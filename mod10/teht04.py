# Tehtävä 4
import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def auton_ominaisuudet(self):
        return [self.rekisteritunnus, self.huippunopeus, self.nopeus, self.kuljettu_matka]

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += tuntimaara * self.nopeus

class Kilpailu:
    def __init__(self, nimi, kilometrimäärä, autolista):
        self.nimi = nimi
        self.kilometrimäärä= kilometrimäärä
        self.autolista= autolista

    def tunti_kuluu(self):
        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdyta(nopeuden_muutos)
            auto.kulje(1)

    def tulosta_tilanne(self):
        print(f"\nKilpailu {self.nimi} - {self.kilometrimäärä} km\n")
        print("Rekisteritunnus |  Huippunopeus | Nopeus | Kuljettu matka  |")
        for auto in self.autolista:
            print("-" * 60)
            print(f"{auto.rekisteritunnus:<17}| {auto.huippunopeus:<12} | {auto.nopeus: <6} | {auto.kuljettu_matka:<14.0f}  |")
        print("-" * 60)

    def kilpailu_ohi(self):
            for auto in self.autolista:
                if auto.kuljettu_matka >= self.kilometrimäärä:
                    return True
            return False

autot = []
for i in range(10):
    rekisteritunnus = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

tunti = 0
while not kilpailu.kilpailu_ohi():
    kilpailu.tunti_kuluu()
    tunti += 1

    if tunti % 10 == 0:
        kilpailu.tulosta_tilanne()

print("\nKilpailu on ohi! \n")
kilpailu.tulosta_tilanne()

