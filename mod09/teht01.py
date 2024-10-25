# Tehtävä 1

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka
        
    def auton_tiedot(self):
        print(f"Auton rekisteritunnus on {self.rekisteritunnus}, huippunopeus on {self.huippunopeus}, "
              f"nopeus on {self.nopeus} km/h, ja kuljettu matka on {self.kuljettu_matka} km.")

auto = Auto("ABC-123", "142 km/h")
auto.auton_tiedot()
