
class Työntekijä:

    työntekijöiden_lukumäärä = 0

    def __init__(self, etunimi, sukunimi):
        Työntekijä.työntekijöiden_lukumäärä = Työntekijä.työntekijöiden_lukumäärä + 1
        self.työntekijänumero = Työntekijä.työntekijöiden_lukumäärä
        self.etunimi = etunimi
        self.sukunimi = sukunimi


    def tulosta_tiedot(self):
        print(f"{self.työntekijänumero}: {self.etunimi} {self.sukunimi}")

class Tuntipalkkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi,tuntipalkka):
        self.tuntipalkka = tuntipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        #print(f"{self.työntekijänumero}: {self.etunimi}: {self.sukunimi}")
        print(f"Tuntipalkka: {self.tuntipalkka}")

class Kuukausipalkainen(Työntekijä):
    def __init__(self, etunimi, sukunimi, kuukausipalkka):
        self.kuukausipalkka = kuukausipalkka
        super().__init__(etunimi, sukunimi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"Kuukausipalka: {self.kuukausipalkka}")


työntekijät = []
työntekijät.append(Työntekijä("Viivi", "Virta"))
työntekijät.append(Työntekijä("Ahmed", "Habib"))
työntekijät.append(Tuntipalkkainen("Olga", "Glebova", 14.92))
työntekijät.append(Kuukausipalkainen("Nur", "Hana", 2500))

for t in työntekijät:
    t.tulosta_tiedot()


class Kulkuneuvo:
    def __init__(self, nopeus):
        self.nopeus = nopeus

class Urheiluväline:
    def __init__(self, paino):
        self.paino = paino

class Polkopyörä(Kulkuneuvo, Urheiluväline):
    def __init__(self, nopeus, paino, vaiheet):
        Kulkuneuvo.__init__(self, nopeus)
        Urheiluväline.__init__(self, paino)

        self.vaiheet = vaiheet
p = Polkopyörä(22, 22, 3)

print(p.vaiheet)
print(p.nopeus)
print(p.paino)


class Julkaisu:
    def __init__(self, nimi, julkaisuvuosi):
        self.nimi = nimi
        self.julkaisuvuosi = julkaisuvuosi

    def tulosta_tiedot(self):
        print(f"Julkaisun nimi: {self.nimi} julkaisuvuosi: {self.julkaisuvuosi}")


class Kirja(Julkaisu):
    def __init__(self, nimi, julkaisuvuosi, kirjoittaja, sivumäärä ):
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä
        super().__init__(nimi, julkaisuvuosi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"kirjoittaja: {self.kirjoittaja}, sivumäärä: {self.sivumäärä}")

class Lehti(Julkaisu):
    def __init__(self, julkaisuvuosi, nimi, päätoimittaja):
        self.päätoimittaja = päätoimittaja
        super().__init__(nimi, julkaisuvuosi)

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f"päätoimittja {self.päätoimittaja}")

j = Julkaisu("Aku Ankka", 2020)

kirja = Kirja("Hytti n:o 6",2022,"Rosa Liksom", 200)
print(kirja.kirjoittaja)
lehti = Lehti(2021, "Aku Ankka", "Aki Hyyppä")
print(lehti.päätoimittaja)
j.tulosta_tiedot()
lehti.tulosta_tiedot()
kirja.tulosta_tiedot()