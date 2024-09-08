
#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän.
# Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

def roll_dice(maksimi2):

    return  random.randint(1, maksimi2)


maksimi = int(input("Kuinka monta noppa heitetään: "))

#roll_dice()
result = 0
while result != maksimi:
    result = roll_dice(maksimi)
    print(result)
#print(result)