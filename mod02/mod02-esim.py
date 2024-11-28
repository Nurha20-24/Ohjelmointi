import math
# Syötteen lukeminen
name = input("Anna nimesi: ")
# name = "Matti"
print("Moi " + name)

age = "7"
print("Ikäsi on "+ age)
#Muutetaan merkkijono (str) kokonaisluvuksi (int) ja lisätään
age = int(age) + 1 # "7" - # 7 + 1 - 8

# esitellään uusi muuttuja , johon sijoitetaan numeroarvo merkki
age_string = str(age) # Muutetaan int - string, esim. 8 - "8"
print("Ikäsi on vuoden päästä " + age_string)
age = int(age) + 1
# Toinen tapa, tehdään tyyppi muunnos vain tarvittavaan kohtaan
print("Ikäsi on kahden vuoden päästä " + str(age))
age = int(age) + 1
print("Ikäsi on kolmen vuoden päästä " + str(age))

#käyttäjän pituus metreinä, liukuluku (float)
height = 1.8
# Kysytään pituus käyttäjältä ja muutetaan samantien liukuluvut
height = float(input("Anna pituus (m): "))
height = input("Anna pituus: ")
height = float(height)
#kasvatetaan käyttäjään 10 cm
height = height + 0.1
# Tulos f-string muodossa, ei tarvita str()-funktiota
print(f"Nimi: {name}, Ikä: {age} Pituus: {height:.2f} metriä.")

# luetaan piin likiarvon math-paketista (import-lauseet aina tiedoston alkuun)
#print(math.pi)
import random
# Satunnaisen kokonaisluvun arpominen väliltä 1-6
random_number = random.randint(1, 6)


print(f"satunnainen luku 1-6: {random_number}")
random.randint


  #Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan
  #pii*r^2




r = float(input("Anna ympyrän säde (m): "))
area = math.pi * r * r
print(f"Ympyrän, jonka säde on {r}, pinta-ala on {area:1f} neliömetriä.")