
class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros = alin_kerros #nykyinen kerros

    def sirry_kerrokseen(self, kohdekerros):
        if kohdekerros > self.kerros:
            #olion omia metodeita kutsuttuaessa käytetään self.
            while kohde > self.kerros:
                self.kerros_ylos()
        #TODO: toteuta elif-haara alaspäin liikkumiselle
    def kerros_ylos(self):
        self.kerros += 1

    def kerros_alas(self):
    # TODO: toteuta  toiminto
        return


h = Hissi(2, 10)
h.sirry_kerrokseen(4)
print(h.kerros)
h.sirry_kerrokseen(1) # ei toimi vielä
print(h.kerros)



