# Tehtävä 4. Kirjoita ohjelma, joka kysyy vuosiluvun ja ilmoittaa, onko annettu vuosi karkausvuosi..
# Vuosi on karkausvuosi, jos se on jaollinen neljällä.
# Sadalla jaolliset vuodet ovat karkausvuosia vain jos ne ovat jaollisia myös neljälläsadalla.

vuosi = int(input("Anna vuosiluvun: "))

if vuosi % 400 == 0 or (vuosi % 4 == 0 and vuosi % 100 != 0):
        print("On karkausvuosi. ")
else:
    print("Ei ole karkausvuosi.")

