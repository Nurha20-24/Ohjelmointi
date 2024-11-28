#Tehtävä 2
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print(f"Kohdekerros {kohdekerros} on virheellinen. Siirry kerrokseen {self.alin_kerros}-{self.ylin_kerros} välillä.")
            return

        while kohdekerros > self.kerros:
            self.kerros_ylös()

        while kohdekerros < self.kerros:
            self.kerros_alas()
        print(f"Hissi on nyt kerroksessa {self.kerros}")

    def kerros_ylös(self):
       if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi siirtyy kerrokseen {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi siirtyy kerrokseen {self.kerros}")

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissit = [Hissi(alin_kerros, ylin_kerros) for _ in range(hissien_lkm)]

    def aja_hissia(self, hissi_numero, kohdekerros):
        if 0 <= hissi_numero < len(self.hissit):
            self.hissit[hissi_numero].siirry_kerrokseen(kohdekerros)
            print(f"Hissi numero {hissi_numero} on {kohdekerros} kerroksessa. ")
        else:
            print(f"Hissi numero {hissi_numero} ei ole olemassa.")

talo = Talo(2,10, 3)
talo.aja_hissia(1, 3)
talo.aja_hissia(2, 12)
talo.aja_hissia(1, 5)
talo.aja_hissia(2, 10)