#Tehtävä 5
#Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina.
# Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle.

#Yksi leiviskä on 20 naulaa.
#Yksi naula on 32 luotia.
#Yksi luoti on 13,3 grammaa.

leiviskät = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

naulaTot = leiviskät * 20 + naulat
luodiTot = naulaTot * 32 + luodit
grammaTot = luodiTot * 13 * 3
print(grammaTot)
kg = grammaTot // 100
gr = grammaTot % 100
print(f"Massa nykymittojen mukaan: {kg} kilogrammaa ja {gr} grammaa.")
