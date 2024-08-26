# Tehtävä 1
from random import random

Nimi = input("Mikä on nimesi?: ")
print("Terve, " + Nimi + "!")


# Tehtävä 2
import math
r = float(input("Mikä on ympyrän säde? (m): "))
area = math.pi * r * r
print(f"Ympyrän säde on {r} ja pinta-ala on {area:1f} neliömetriä.")


# Tehtävä 3
import math
kanta = float(input("Mikä on suorakulmion kanta?: "))
korkeus = float(input("Mikä on suorakulmion korkeus?: "))
piiri = 5 + 5 + 5 + 5
area = 5 * 5
print(f"Suorakulmion piiri on {piiri}")
print(f"suorakulmion pinta-ala on {area}")


#Tehtävä 4
luku1 = int(input("Kerro ensimmäinen luku: "))
luku2 = int(input("Kerro toinen luku: "))
luku3 = int(input("Kerro kolmas luku: "))
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3
print(f"Lukujen summa on: {summa}")
print(f"Lukujen tulo on: {tulo}")
print(f"Lukujen keskiarvo on: {keskiarvo:.1f}")


#Tehtävä 5
leiviskät = print(input("Anna leiviskät: "))
naulat = print(input("Anna naulat: "))
luodit = print(input("Anna luodit: "))
gramma = 13.3 + 425.6 + 8512
kilogramma = 13.3 + 425.6 + 8512 / 1000
print(f"Massa nykymittojen mukaan: {kilogramma:.0f} kilogrammaa ja {gramma:.2f} grammaa.")


#Tehtävä 6
import random
print("Arpoo ja tulostaa kolmenumeroisen koodin väliltä 0-9")
for i in range(3):
    randum_number = random.randint(0, 9)
    print(randum_number)
print("Arpo ja tulostaa nelinumeroisen koodin väliltä 1-6")
for i in range(4):
    randum_number = random.randint(0, 6)
    print(randum_number)


