
# Alustus ehtolauseilla



 rahat = float(input("Anna rahamäärä: "))

if rahat >= 5:
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa")

print("Jatketaan pääohjelma")

# Sama kuin:
rahat = float(input("Anna rahamäärä: "))
ehto = (rahat >= 5)
print(ehto)
if ehto:
    # Tämä osa on lohko ja suoritetaan jos ehto on totta
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa")

#
suutari = input("Anna suutarin nimi: ")
räätäli = input("Anna räätälin nimi: ")

if suutari==räätäli:
    print("Hyvänen aika! Suutari ja räätäli ovat kaimoja!")

# Luo ohjelma, joka pyytä käyttäjän numero ja tulosta onko luku pos, neg vai nolla

luku = int(input("Anna luku: "))
if luku > 5:
    print("numero on pos")
elif luku < 4:
    print("numero on neg")
#
else:
    print("Numero on viisi")



# Kaksi toisensa poissulkeva vaihtoehtoa

rahat = float(input("Anna rahamäärä: "))
if rahat >= 5:
    print("Voit ostaa latten, sinulla on tarpeeksi rahaa")
else:
    print("Sinulla ei välitettavasti ole tarpeeksi rahaa latteen")

# Monta vaihtoehtoa
user_input = input("a, b, c tai d")
if user_input == "a":
    print("Tehdään jotain, käyttäjä valitsi kirjaimen a")
elif user_input == "b":
    print("Tehdään jotakin muuta kivaa, käyttäjä valitsi b")
elif user_input == "c":
    print("Käyttäjä valitsi c")
    print("Moikka, saat c luokan hytin")
    a = 4 + 4
    print(f"Saat buffaan {a} euroa bonuksena")
else:
    print("käyttäjä ei syöttänyt a, b tai c. Ei tehdä siis mitään.")
    print("Ohjelma loppuu, hei hei !")

# Loogiset operattorit:

ikä = 5
nimi = "Matti"

#lauseke a and b on tosi täsmälleen silloin, kun sekä lauseke a että lauseke b ovat tosia.'
# True True
print(ikä < 18 and nimi == "Matti") #True

#True False
print(ikä < 18 and nimi == "ulla") #False

#lauseke a or b on tosi täsmälleen silloin, kun vähintään jompikumpi lausekkeista a ja b on tosi.
print(ikä < 18 or nimi == "ulla") #true
