# 1.Kirjoita ohjelma, joka kysyy kalastajalta kuhan pituuden senttimetreinä.
# Jos kuha on alamittainen, ohjelma käskee laskea kuhan takaisin järveen ilmoittaen samalla käyttäjälle,
# montako senttiä alimmasta sallitusta pyyntimitasta puuttuu.
# Kuha on alamittainen, jos sen pituus on alle 37 cm..

kuha = float(input("Mikä on kuhan pituus cm: "))
if kuha < 37:
    print("Kuha on alimittainen, laskee kuhan takaisin järven.")
    paino = 37 - kuha
    print(f"Alimmasta sallitusta pyyntimitasta puuttuu {paino} cm ")
else:
    print("Kuha on sallittu pyyntimittainen")


