import random
#Monikko()

print('/ nmonikko()/n')

# Monikko (tuple) on "kuin lista jota ei voi muokata"

minun_lista = [1, 2, 3, 4, 5, 6]
print(minun_lista)

minun_monikko = (1, 2, 3, 4, 5, 6)
#minun_monikko = 1, 2, 3, 4, 5, 6
print(minun_monikko)

minun_monikko2 = (1, 2, (3, 4), 5, 'kuusi')
print(minun_monikko2)

#luetaan ensimmäinen alkio
print(minun_lista[0])
print(minun_monikko2[0])

# yritetään nyt muokata eka alkio numeroksi 0 ja lisätä loppuun 7
# Listaan sisältää voi muokata, mutable
minun_lista[0] = 0
minun_lista. append(7)
print(f"Muokattu lista {minun_lista}")


# Monikon sisältöä EI voi muokata, imutable
#minun_monikko[0] = 0

# monikko on tarkoituksenmukaista käyttä tilanteissa, jossa alkioden jono on luonteeltaan staattinen.
# tiedetään, että muutoksille ei ole tarvetta ohjelman suorituksen aikana.

# Koodiesimerkki materiaalista
viikonpäivät = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
järjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
print(viikonpäivät[1])
viikonpäivä = viikonpäivät[järjestysnumero-1]
print (f"{järjestysnumero}. viikonpäivä on {viikonpäivä}.")


# monikon läpikäynti kuten listan
#minun_monikko = (1, 2, 3, 4, 5, 6)
minun_monikko3 = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')
for i in minun_monikko3:
    print(i)
    if i == 'kolmas':
        print('kolmas löytyy')
print(minun_monikko3)

# Monikon arvojen purku muuttujiin
hedelmät = ('Lime', 'Sitruna', 'Appelsiini')
#(eka, toka, kolmas) = ('Lime', 'Sitruna', 'Appelsiini')
(eka, toka, kolmas) = hedelmät
print(eka)
print(toka)

print('/nMonikon voi antaa funktiolle parametrina:\n ')

sanalista = ('eka', 'toka', 'kolmas', 'neljäs', 'viides')

print('Terve')
def tulosta_monikko(sanalista):
    for i in sanalista:
        print(i)


tulosta_monikko(sanalista)
tulosta_monikko(hedelmät)


#perinteinen print  ilman paluuarvoa
def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f"Nopista tuli {eka} ja {toka}.")

heitä()

#Monikkp funktion paluuarvona
def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka

#(noppa1, noppa2) = (eka, toka)
noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")


#Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.

#Joukko (set) on järjestämätön tietorakenne, eli sen alkiot voivat olla missä tahansa järjestyksessä.

#Toisin kuin listassa tai monikossa, sama alkio voi esiintyä joukossa vain kertaalleen, eli joukossa ei voi olla kahta samansisältöistä alkiota.


# Joukko eli set {}
joukko = {1, 2, 3, 4, 5, 6}
# joukko merkitään altosulkeilla
print(joukko)

print(f"Numero 6 voi olla esiintyä listassa useasti:")
minun_lista = [6, 2, 3, 4, 5, 6]
print(minun_lista)

print(f"Numero 6 voi olla esiintyä listassa useasti:")
minun_monikko = (6, 2, 3, 4, 5, 6)
print(minun_monikko)

print(f"Numero 6 EI voi olla esiintyä listassa useasti:")
minun_joukko = {6, 2, 3, 4, 5, 6}
print(minun_joukko)

# yllä oleva ei sinänsä tuota virhettä, kute ei add-metodi
minun_joukko.add(6) # ei onnistu mutta ei tuota virhettä
minun_joukko.add(7)
print(minun_joukko)
minun_joukko.remove(7)
print(minun_joukko)

# Koodiesimerkki, järjestys voi muuttaa printatessa
pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

# Alkiot voidaan iteroida for/in rakenteella
for p in pelit:
    print(p)
    # Löytyykö Cluedo, jos löytyy printtaa jotain
    if p =="Cluedo":
        print("Cluedo löytyi!!!")

# if/in haku toimii kuten listoissa
if "Monopoli" in pelit:
    print("Monopoli löytyi")


# Tyhjän joukko luodaan edellä esitetystä poiketen set-funktion avulla.

autolista = []
autolista.append('Audi')
print(autolista)

# Tästä tuleekin sanakirja eli dictionary
autojoukko = {}
print(type(autojoukko))

autojoukko = set()
autojoukko.add('Audi')
print(type(autojoukko)) # tämä on <class 'set'>
print(autojoukko)

# Sanakirja {}
################

# Sanakirja (dictionary) on Pythonin käytetympiä tietorakenteitä
# Sanakirjan voidaan tallentaa avain-arvopareja.
# Kun sanakirja alustetaan arvot luettelemalla annan kunkin avainarvopari

print('/nSanakirja{}\n')
oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 11, 'Daniel': 33, 'Emma': 22}
print(oppilaat)

# Mitä ovat tietueet / items
print(oppilaat.items())

# Mitä ovat avaimet sanakirjassa?
print(oppilaat.keys())

# Mitä ovat arvoja sanakirjassa?
print(oppilaat.values())

# Kun sanakirjaa käydään läpi for/in rakenteella:

# Tietuet  eli avain -arvoparit

for i in oppilaat.items():
    print(i)

#Kun sanakirja läpikäydään for/in-rakennetta käyttäen,
#saa kierrosmuuttuja arvokseen vuoron perään kunkin sanakirjassa esiintyvän avaimen.
for i in oppilaat:
    print(i)

#oppilaat = {'Aapeli': 25, 'Bertta': 45, 'Cecilia': 11, 'Daniel': 33, 'Emma': 22}
#Yksittäisen arvon haku  avaimen avulla.
avain = 'Aapeli'
#print(oppilaat[Aapeli])
print(oppilaat[avain]) # Etsi avaimella Aapeli sen arvoa joka on 25

# Etsi kaikki arvot
for i in oppilaat:
    print(oppilaat[i])

# if/in rakenteela voidaan myös hakea sanakirjasta tietoa
nimi = input('Anna nimi, niin etsin sen sanakirjasta jos löytyy: ')
if nimi in oppilaat:
    print(f'Löytyi oppilas {nimi} ikä hänellä on {oppilaat[nimi]}')

#Kun olemassa olevaan sanakirjaan lisätään arvo,
# käytetään notaatiota sanakirja[avain] = arvo

# Lisätään uusi oppilas mikäli ei löydy
# Jos avain löytyy se muokkaa olemassaoleva, muuten luodaan uusi.

oppilaat['Bertta'] = 22
print(oppilaat)

oppilaat[('Maisaa')] = 13
print(oppilaat)



#Toinen tunti

nimet = ["Viivi", "Ahmed"]
numerot = ["050-1234567", "040-11122223"]

print(f"{nimet[0]}, {numerot[0]}")

yhteistiedot = {"Viivi": "050-1234567", "Ahmed": "040-11122223"}
#print(f")Viivin numero:{yhteiystiedot['Viivi']}")
hakusana = input("Puhelinnumero haku, anna nimi: ")
# listojen avulla, selvitetään ensin oikea indeksi
index = nimet.index(hakusana)
print(f"{hakusana}, numero: {numerot[index]}")
# sanakirjalla, hyödynnetään avainta
print(f"{hakusana}, numero: {yhteistiedot[hakusana]}")


# extra moniulotteinen sanakirja
yhteistiedot ={
    "Viivi": {"puh": "050-1234567", "osoite": "pilkutie 15"},
    "Ahmed": {"puh": "040-11122223", "osoite": "isotie 1"}
    }
print(f"Viivin osoite: { yhteistiedot['Viivi']['osoite'] }")
