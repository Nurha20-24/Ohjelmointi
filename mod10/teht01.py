# Tehtävä 1
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros

    def siirry_kerrokseen(self, kohdekerros):
        if kohdekerros < self.alin_kerros or kohdekerros > self.ylin_kerros:
            print(f"Kerros {kohdekerros} on virheellinen. Siirry kerrokseen {self.alin_kerros}-{self.ylin_kerros} välillä.")
            return

        elif kohdekerros > self.kerros:
            while kohdekerros > self.kerros:
                self.kerros_ylös()
        elif kohdekerros < self.kerros:
            while kohdekerros < self.kerros:
                self.kerros_alas()

        print(f"Hissi on nyt kerroksessa {kohdekerros}")

    def kerros_ylös(self):
       if self.kerros < self.ylin_kerros:
            self.kerros += 1
            print(f"Hissi siirtyy kerrokseen {self.kerros}")

    def kerros_alas(self):
        if self.kerros > self.alin_kerros:
            self.kerros -= 1
            print(f"Hissi siirtyy kerrokseen {self.kerros}")

h = Hissi(2,10)

h.siirry_kerrokseen(10)
h.siirry_kerrokseen(11)
h.siirry_kerrokseen(2)
