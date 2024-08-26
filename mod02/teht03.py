# Tehtävä 3
#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan.

import math
kanta = float(input("Mikä on suorakulmion kanta?: "))
korkeus = float(input("Mikä on suorakulmion korkeus?: "))

piiri = kanta * 2 + korkeus * 2
area = kanta * korkeus
print(f"Suorakulmion piiri on {piiri}")
print(f"suorakulmion pinta-ala on {area}")