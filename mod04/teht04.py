#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.


import random
luku = random.randint(1, 10)

while True:
    arvaus = int(input("Arvaa luku väliltä 1..10: "))
    if arvaus > luku:
        print("Liian suuri arvaus")
    elif arvaus < luku:
        print("Liian pieni arvaus")
    else:
        print("Oikein arvasit!")
        break
