# Tehtävä 2
#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.
import math
r = float(input("Mikä on ympyrän säde? (m): "))
area = math.pi * r * r
print(f"Ympyrän säde on {r} ja pinta-ala on {area:1f} neliömetriä.")
