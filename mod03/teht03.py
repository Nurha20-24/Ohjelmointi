#Kirjoita ohjelma, joka kysyy käyttäjän biologisen sukupuolen ja hemoglobiiniarvon (g/l).
# Ohjelma ilmoittaa, onko hemoglobiiniarvo alhainen, normaali vai korkea..

#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.

sukupuoli = input("Mikä on sinun biologisen sukupuoli: ")
hemoglobiiniarvo = int(input("Mikä on sinun hemoglobiiniarvo (g/l): "))

if sukupuoli == "nainen":

    if hemoglobiiniarvo <117:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo >= 175:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")
elif sukupuoli == "mies":
    if hemoglobiiniarvo <= 134:
        print("Hemoglobiiniarvo on alhainen")
    elif hemoglobiiniarvo >= 195:
        print("Hemoglobiiniarvo on korkea")
    else:
        print("Hemoglobiiniarvo on normaali")