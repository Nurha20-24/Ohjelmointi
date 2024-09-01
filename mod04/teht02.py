#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
# Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm

tuuma_cm = 2.54
tuumia = float(input("Anna tuuma määrä: "))
while True:
    if tuumia < 0:
        print("Toiminta lopetettu.")
        break

    cm = tuumia * tuuma_cm
    print(f"{tuumia} tuumia on {cm:.2f} cm")
    tuumia = float(input("Anna tuuma määrä: "))







