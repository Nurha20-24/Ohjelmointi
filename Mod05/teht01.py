# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan. Käytä for-toistorakennetta.


import random
total = 0
dice_count = int(input("Montas nappaa laitettaan: "))
for i in range(dice_count):
     total = total + random.randint(1,6)
print(f"Noppien silmälukujen summa on {total}")


