# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen..
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True. """


lista = []
while True:
    annettu_luvut = input("Kerro luku: ")
    if annettu_luvut != "":
        lista.append(int(annettu_luvut))

    if annettu_luvut == "":
        break

lista.sort(reverse=True)

for numero in lista[0:5]:
    print(numero)

