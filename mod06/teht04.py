
#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja. Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.


def lista(kokonaisluvut):
    summa = 0
    for luku in kokonaisluvut:
        summa += luku
    return summa
kokonaisluvut = [2, 4, 7, 8, 19, 21]
print(lista(kokonaisluvut))






