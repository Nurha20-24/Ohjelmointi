
#Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen.
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän.
#Yksi gallona on 3,785 litraa.

def gallons_to_liters(gallonmäärä):

    litraa = gallonmäärä*3.785
    return litraa

while True:
    gallonmäärä = int(input("Kerro gallonmäärä: "))
    if gallonmäärä <= -1:
        break
    litrat = gallons_to_liters(gallonmäärä)
    print(f"{litrat} litraa")



#print(f"{gallonmäärä }")
