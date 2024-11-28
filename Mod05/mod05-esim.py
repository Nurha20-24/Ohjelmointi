
name1 = "Ville"
name2 = "Liisa"
name3 = "Ulla"
age1 = 3
age2 = 5
age3 = 22
print(f"Hei {name1} ja ikäsi on {age1} vuotta")
print(f"Hei {name2} ja ikäsi on {age2} vuotta")
print(f"Hei {name3} ja ikäsi on {age3} vuotta")
print('.........')
names = ['Ville', 'Liisa', 'Ulla', 'Anna', 'Matti']
ages = [age1, age2, age3, 45, 67]
print(names)
print(ages)

#Listan pituus voidaan tarkista len() funktiolla.
length = len(names)
print(f"Listan pituus on: {length}")

#Alkioon viitataan indeksinumerolla
print(names[3])

print(f"Moi {names[2]} ikäsi on {ages[2]}")

#Vittaus listan ulkopuolella tuottaa virheen
#print(names[8])

#Listan läpikäynti while silmukan avulla
iterator = 0
while iterator < len(names):
    print(f"Hei {names[iterator]} ikäsi on {ages[iterator]}")
    iterator += 1


# Tapoja viitata listan alkoihin
lista =['Ville', 'Liisa', 'Ulla', 'Anna', 'Matti', 'Ahmed', 'Neo', 'Viivi']
print(lista[2:5])
print(lista[2:]) #Kaikki loputkin alkiot indeksilla 2: alkaen
print(lista[-1]) #Listan viimeinen alkio
print(lista[2:6:2])

#Listan voi yhdistää ja siellä voi olla erilaisia tietorakenteita
lista1 = ['Ulla', 'Matti', 'Ilkka']
yhdistetty_lista = [23, 45, 66, 67, 67, lista1]
print(yhdistetty_lista)
print(yhdistetty_lista[5][1])


print('listaoperaatiot')

lista.append('Uusi nimi')

print(lista)
#lista.remove('Ulla') #Poistetaan alkio mikäli se löytyy virhe
print(lista)
if 'Ulla' in lista:
    print("Ulla löytyy listasta ja nyt poistetaan samalla.")
    lista.remove('Ulla')
    print(lista)

#Pistetään nimi Ulla takaisin ensimmäiseksi listan alkioksi
lista.insert(   0,      'Ulla')
print(lista)

print(lista.index('Matti'))

lisää_nimiä = ['Ines', 'Aku', 'Tupu', 'Nupu']
lista.extend(lisää_nimiä)
# uusi_lista = lista + lisää_nimiä
print(lista)

lista[2] = 'Lisa' # Muokkataan olemassa oleva alkiota
print(lista)

numero_lista = [19, 6, 22, 66, 1, 499, 0, 55, 34, 889]
numero_lista.sort()
print(numero_lista)
lista.sort()
print(lista)

print('\n.........')
print('Listan läpikäynti for-toistorakenteen avulla\n')

for kirjain in'abcd':
    print(kirjain)

for alkio in [1, 2, 3, 4, 5]:
    print(alkio)

for nimi in lista:
    print(nimi)

for numero in range(5, 50, 2):
    print(numero)

print('.......')


for i in range(999, 0, -3):
     print(i)

print(lista)
for i in range (5):
    print(i)
    print(f'Terve: {lista[i]}')

for nimi in ['Ahmed', 'Aku', 'Anna', 'Ines', 'Lisa', 'Matti', 'Neo', 'Nupu', 'Tupu', 'Ulla', 'Uusi nimi', 'Viivi', 'Ville']:
    print(nimi)

print('.......')

print('Listan pituus rangens: ')

listan_pituus = len(lista)
print(f'Lista on {listan_pituus} alkioita pitkä')

# for i in range (len(lista)):
for i in range(listan_pituus): #Listan pituus maksemeina 0-12
    print(f'Terve: {lista[i]}')





#harjoitus
import random
total = 0
dice_count = int(input("Montas nappaa laitettaan: "))
for i in range(dice_count):
     result = random.randint(1,6)
     total = total + result
     results.append(result)
print(f"Noppien silmälukujen summa on {total}, nopat {result}")


# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan.
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def is_prime_number (num):
    # jätetään nollat ja negatiiviset luvut kokonaan testaamatta.
    if num < 1:
        return False
    for i in range(2, num):
        #print(i)

        if num % i == 0:
            #Jos jaollinen jollain i:n arvolla palautetaan False ja funktion suoritus loppu siihen.
            return False
    #Jos funktion suoritus on jatkunut tähän asti, niin palautetaan True.
    return True

user_input = int(input("Anna testattavat kokonaisluku (>0): "))
if is_prime_number(user_input):
    print(f"Luku {user_input} on alkuluku. ")
else:
    print(f"Luku {user_input} ei ole alkuluku")
#Testataan funktion arvo erilaisilla arvolla
#print(is_prime_number(4))
#print(is_prime_number(280))
#print(is_prime_number(7))