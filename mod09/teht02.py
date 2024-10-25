#Tehtävä 2

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka= 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def auton_ominaisuudet(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus},huippunopeus on {self.huippunopeus} km/h, "
              f"nopeus on {self.nopeus} km/h, ja kuljettu matka on {self.kuljettu_matka} km.")

    def kiihdyta(self, nopeuden_muutos):
        self.nopeus = self.nopeus + nopeuden_muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0


auto = Auto("ABC-123", 142)
auto.auton_ominaisuudet()

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
auto.auton_ominaisuudet()

auto.kiihdyta(-200)
auto.auton_ominaisuudet()


