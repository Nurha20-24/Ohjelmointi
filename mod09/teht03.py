#Tehtävä 3

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus=0, kuljettu_matka=2000):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def auton_ominaisuudet(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus},huippunopeus on {self.huippunopeus} km/h," 
              f"tämänhetkinen nopeus on {self.nopeus} km/h, kuljettu matka on {self.kuljettu_matka:.1f} km.")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimaara):
        self.kuljettu_matka += tuntimaara * self.nopeus

auto = Auto("ABC-123", 142)
auto.auton_ominaisuudet()

auto.kiihdyta(60)
auto.auton_ominaisuudet()

auto.kulje(1.5)
auto.auton_ominaisuudet()