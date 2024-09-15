#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron,
# jonka jälkeen ohjelma tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi).
# Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen.
# Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten,
# että joulukuu on ensimmäinen talvikuukausi.

#kuukaudet = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
kuukaudet = ('Tammikuu', 'Helmikuu', 'Maaliskuu', 'Huuhtikuu', 'Toukokuu', 'Kesäkuu', 'Huuhtikuu', 'Elokuu', 'Syyskuu', 'Lokakuu', 'Marraskuu', 'Joulukuu')
vuodenajat = ('Talvi', 'Kevät', 'Kesä', 'Syksy' )

kuukausi_numero = int(input("Anna kaukauden numero (1-12): "))

vuodenaika = (kuukausi_numero % 12) // 3
print(kuukaudet[kuukausi_numero - 1], "on", vuodenajat[vuodenaika])


