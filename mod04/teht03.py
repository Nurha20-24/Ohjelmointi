#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman

luku = input("Syötä luku: ")
if luku != "":
    max_num = min_num = int(luku)
while luku != "":
    luku = input("Syötä luku: ")
    if luku == "":
        break
    number = int(luku)
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number

print(f"Pienin numero: {min_num} ja suurin numero: {max_num}")

