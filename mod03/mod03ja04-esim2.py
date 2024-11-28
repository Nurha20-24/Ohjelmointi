# mod 3 ja 4
# 3,4. Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi. Vuosi on karkausvuosi, jos se on jaollinen neljällä. Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

"""
year = int(input("anna vuosiluku: "))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("On karkausvuosi. ")
else:

    print("Ei ole karkausvuosi ")

#Bonus: Tulostaa kaikki karkausvuodetannettuun vuosilukuun asti.

iterator = 0
while iterator < year:
    iterator += 4
    if iterator % 400 == 0 or iterator % 100 != 0:
        print(f"{iterator} on karkausvuosi. ")

"""
from operator import truediv

#4,3
input_string = input("Syötä luku: ")
if input_string != "":
    max_num = min_num = int(input_string)

while input_string != "":
   input_string = input("Syötä luku: ")
   if input_string == "":
        break
   number = int(input_string)
   if number > max_num:
       max_num = number
   if number < min_num:
        min_num = number

print("Ei lukuja syötetty. ")
print (f"Pienin numero: {min_num}, suurin numero: {max_num}")

#4,6.   π = 4n/N, jossa N on kaikkien pisteiden lukumäärä ja
# n yksikköympyrän sisälle osuvien pisteiden määrä
# jos, pisteen koordinaatit toteuttavat epäyhtälön x^2+y^2<1, piste on ympyrässä

import random

#TODO: kysy N arvo käyttäjältä
N = 100 #Pisteiden kokonaismäärä
n = 0 #ympyrän osuvien pisteiden lukumäärä
iterator = 0
while iterator < N:
    iterator += 1
    #arvotaan yksi piste
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f"2Arvottu piste: {x}, {y}")
    print(x**2 + y**2 < 1)
    if x**2 + y**2 < 1:
        print("Piste on yksikköympyrässä. ")
        #TODO: Lisää n arvoon 1
#TODO: Tulosta kaavan mukaan laskettu piin likiarvoa





