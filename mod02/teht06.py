#Tehtävä 6
#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

import random
print("Arpoo ja tulostaa kolmenumeroisen koodin väliltä 0-9")
for i in range(3):
    randum_number = random.randint(0, 9)
    print(randum_number)
print("Arpo ja tulostaa nelinumeroisen koodin väliltä 1-6")
for i in range(4):
    randum_number = random.randint(0, 6)
    print(randum_number)