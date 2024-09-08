
# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta).
# Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pizzan_yksikkohinta(halkaisija, hinta):
    halkaisija_metri = halkaisija / 100
    sade = halkaisija_metri / 2
    pinta_ala = math.pi * sade ** 2
    yksikköhinta = pinta_ala / hinta
    return yksikköhinta

def pääohjelma():
    halkaisija1 = float(input("Anna ensimmäinen pizzan halkaisijat (cm): "))
    hinta1 = float(input("Anna ensimmäisen pizzan hinta (€): "))

    halkaisija2 = float(input("Anna toisen pizzan halkaisijat (cm): "))
    hinta2 = float(input("Anna toisen pizzan hintaa (€): "))

    yksikköhinta1 = pizzan_yksikkohinta(halkaisija1, hinta1)
    yksikköhinta2 = pizzan_yksikkohinta(halkaisija2, hinta2)

    print(f"Ensimmäinen pizzan yksikköhinta on {yksikköhinta1}")
    print(f"Toisen pizzan yksikköhinta on {yksikköhinta2}")

    if yksikköhinta1 < yksikköhinta2: print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    elif yksikköhinta1 > yksikköhinta2: print("Toinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Molemmat pizza antaa yhtä hyvä vastine rahalle")

pääohjelma()




