#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan.
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen.
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
# Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty.
# (Oikea käyttäjätunnus on python ja salasana rules).


oikea_käyttäjätunnus = 'python'
oikea_salasana = 'rules'

yritys = 0
maksimi_yritys = 5

while yritys < maksimi_yritys:
    käyttäjätunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    if käyttäjätunnus == oikea_käyttäjätunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break
    else:
        yritys += 1

if yritys == maksimi_yritys:
    print("Pääsy evätty")



