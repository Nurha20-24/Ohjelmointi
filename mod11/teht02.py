# Tehtävä 2
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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, akkukapasiteetti):
        super().__init__(rekisteritunnus, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti
        self.nopeus = 100

    def matkamittarilukemat(self):
        print("Sähköauto:")
        print(f"Rekisteritunnus: {self.rekisteritunnus},  Akkukapasiteetti: {self.akkukapasiteetti} kWh,  Huippunopeus: {self.huippunopeus} km/h,  Nopeus: {self.nopeus} km/h,  Kuljettu matka: {self.kuljettu_matka} km\n")

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, bensatanki ):
        super().__init__(rekisteritunnus, huippunopeus)
        self.bensatanki = bensatanki
        self.nopeus = 110

    def matkamittarilukemat(self):
        print("Polttomoottoriauto: ")
        print(f"Rekisteritunnus: {self.rekisteritunnus},  Bensatanki:  {self.bensatanki} l,  Huippunopeus: {self.huippunopeus} km/h,  Nopeus: {self.nopeus} km/h,  Kuljettu matka: {self.kuljettu_matka} km.")

s_auto = Sähköauto("ABC-15", 180, 52.5)
p_auto = Polttomoottoriauto("ACD-123", 165, 32.3)

for tunti in range(3):
    s_auto.kulje(1)
    p_auto.kulje(1)

print("Autojen mittarilukemat 3 tunnin ajaamiseen jälkeen: ")
print("_" * 55)
s_auto.matkamittarilukemat()
p_auto.matkamittarilukemat()




