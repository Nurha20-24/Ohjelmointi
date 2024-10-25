#Tehtävä 4

import random
from tabulate import tabulate

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

autot = []
for i in range(10):
    rekisteritunnus = f"ABC-{i+1}"
    huippunopeus = random.randint(100, 200)
    uusi_auto = Auto(rekisteritunnus, huippunopeus)
    autot.append(uusi_auto)

tunti = 0
while True:
    for auto in autot:
        nopeuden_muutos = random.randint(-10, 15)
        auto.kiihdyta(nopeuden_muutos)
        auto.kulje(1)

    if any(auto.kuljettu_matka >= 10000 for auto in autot):
        break
    tunti += 1

header = ["Rekistertunnus", "Huippunopeus (km/h)", "Nopeus (km/h)", "Kuljettu matka (km)"]
table = [auto.auton_ominaisuudet() for auto in autot]
print("\nKilpailun tulokset:")
print(tabulate(table, headers=header, tablefmt ="grid"))


