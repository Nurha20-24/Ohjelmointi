#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman, hakea jo syötetyn lentoaseman tiedot vai lopettaa.
# Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen.
# Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen.
# Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy.
# Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa.
# (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK.
# Löydät koodeja helposti selaimen avulla.)

lentoasemat = {}

while True:
    print("Valitse toiminto: ")
    print("1 - Haluatko syötä uuden lentoaseman")
    print("2 - Haluatko hakea syötetyn lentoaseman tiedot")
    print("3 - Lopeta ohjelma")
    valinta = input("Syötä valintasi (1, 2 tai 3): ")
    if valinta == "1":
       icao = input("Syötä lentoaseman ICAO-koodi: ").upper()
       nimi = input("Syötä lentoaseman nimi: ")
       lentoasemat[icao] = nimi
       print(f"Lentoaseman {nimi} ja (ICAO: {icao}) lisätty.")
    elif valinta == "2":
        icao = input("Syötä haettavan lentoaseman ICAO-koodi: ").upper()
        if icao in lentoasemat:
            print(f"{lentoasemat[icao]} lentoaseman ICAO koodi on {icao}")
        else:
            print("Lentoasema ei löytdy,")
    elif valinta == "3":
        print("Ohjelma lopetetaan.")
        break
    else:
        print("Virheellinen valinta. Yritä uudelleen.")









