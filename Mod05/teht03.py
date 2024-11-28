# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
# Tässä tehtävässä alkulukuja ovat luvut, jotka ovat jaollisia vain ykkösellä ja itsellään.
#
# Esimerkiksi luku 13 on alkuluku, koska se voidaan jakaa vain luvuilla 1 ja 13 siten, että jako menee tasan..
# Toisaalta esimerkiksi luku 21 ei ole alkuluku, koska se voidaan jakaa tasan myös luvulla 3 tai luvulla 7.

def is_prime_number (num):

    if num < 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

user_input = int(input("Anna testattavat kokonaisluku (>0): "))
if is_prime_number(user_input):
    print(f"Luku {user_input} on alkuluku. ")
else:
    print(f"Luku {user_input} ei ole alkuluku")

