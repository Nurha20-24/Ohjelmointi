
import random
# kikkailua loogisella operattorilla
print(not True)
print(True and True)
print(True and False)
print(True or True)
print(True and (False or True))
result = (False or False) and (False or True)
print(f"Vertailun tulos: {result}")
print(2 < 4 or (1==1 and result))

# While-silmukat (loopit)
# Ikuinen silmukka, ei hyvä!

while True:
    print("Moro")
    print("Matti")

    break

max_count = int(input("Montaa kertaa kukutaan? "))
counter = 9
while counter < max_count:
    #counter < 5:(
        counter + 1 #lyhyt versio: counter +=1
        counter -= 1
        print(f"{counter}. kerran Kukkuu!")
print(f"Laskurin arvonlopuksi: {counter}")

# Tulostetaan 2 potenssit

while x < 1000:
    print("x")
     x *= 2 # sama kuin x = x * 2


# noppasimulaattori (import random)
# Mikä on kahden yhtäaikaisen kutosen todennäköisyys?

rounds = 1000
round_counter = 0
total_rolls = 0
while round_counter < rounds:
    round_counter += 1
    die1 = die2 = roll_counter = 0
    while die1 < 6 or die2 < 6:
        roll_counter += 1
        die1 = random.randint(1, 6)
        die2 =random.randint(1, 6)
        #print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}")
    #print(f"Noppa heitettiin {roll_counter}. kertaa. ")
    total_rolls = total_rolls + roll_counter
print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla. ")



# Ohjelma komentorivikäyttöliittymällä
# (välikko, johon sisällytetty ylläolevat esimerkit)
command = ""
while command != "lopeta":
    command = input("Komento, kiitos> ")
    if command == "lopeta":
        print("Lopetetaan.")
         # break # "heittä ulos" silmukasta, ei paras ohjelmointikäytäntö
    elif command == "kukkuu":
        max_count = int(input("Montaa kertaa kukutaan? "))
        counter = 0
        while counter < max_count:
            # while counter < 5:
            counter = counter + 1
            print(f"{counter}. kerran Kukkuu!")
        print(f"Laskurin arvonlopuksi: {counter}")
    elif command == "noppa":
        rounds = 1000
        round_counter = 0
        total_rolls = 0
        while round_counter < rounds:
            round_counter += 1
            die1 = die2 = roll_counter = 0
            while die1 < 6 or die2 < 6:
                roll_counter += 1
                die1 = random.randint(1, 6)
                die2 = random.randint(1, 6)
                # print(f"{roll_counter}. heiton silmäluvut: {die1} ja {die2}")
            # print(f"Noppa heitettiin {roll_counter}. kertaa. ")
            total_rolls = total_rolls + roll_counter
        print(f"Kaksi kutosta saatiin keskimäärin {total_rolls / rounds} heitolla. ")

    else:
        print("En ymmärrä komentoa. Yritä uudestaan, kiitti. ")
print("Ohjelma sammutettu.")
