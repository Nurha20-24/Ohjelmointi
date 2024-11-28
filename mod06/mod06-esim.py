

def do_something():
    print("Doing")
    print("Something")
    return " Tässä on palautettava arvo, voi olla ihan minkä tyyppinen vaan"

#do_something()
return_value = do_something()
print(return_value)

# Funktio, jolla parametreja (argumentteja)
def combine_words(word1, word2):
    combination = f"{word1}, {word2}"
    print(combination)

combine_words("auto", "ajaa")
combine_words("Kuski", "jarruttaa")

def combine_strings(strings1, strings2):
    combination = f"{strings1}, {strings2}"
    #print(combination)
    return combination

print(combine_strings("auto", "ajaa"))
combination = combine_strings("Kuski", "jarruttaa")
print(combination)
combination = combine_strings(combination,"nopeasti")
print(combination)


# Yksinkertainen laskin, joille voi antaa vain 2 parametria
def calculator(calc_type, number1, number2):
    if calc_type == "sum":
        return number1 + number2
    elif calc_type == "division":
        return number1 / number2
   # return None # oletustoiminallisuus

print(calculator("sum", 2.4, 3.5))
print(calculator("division", 2.4, 8))


#Listat ja funktiot, funktio otttaa parametrina listan lukuja ja laskee
#ja palauttaa niiden summa
def calculate_sum(numbers):
    total_sum = 0
    # Kaksi tapaa tehdä for-loop listan käsittelyyn
    #for i in range(len(numbers)):
    # total_sum = total_sum + numbers[i]
    for i in range(len(numbers)):
        total_sum = total_sum + numbers[i]
    for num in numbers:
        total_sum =total_sum + num
    return total_sum

nums = [3, 4, 5]
print(nums)
print(calculate_sum(nums))
# Funktio muokkasi sama listaa, mihin pääohjelma nums muuttuja viittaa
print (nums)
calculate_sum([3, 4, 5])

print(calculate_sum([3, 4, 10]))


# vaihtuva määrä parametreja
# + tekee kaikista syötetysta parametreista (arvoista) listan
# Ja sijoittaa listaan numbers muuttujaan
def calculate_sum2(numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum2([2, 3, 8]))

"""
#extra: nimetyt parametrit ja oletusarvot
#Yksinkertainen laskin, joille voi antaa tason 2-3 parametria
def calculate2(number1, number2, calc_type = "sum"):
    if calc_type == "sum":
        return number1 + number2
    elif calc_type == "division":
        return number1 / number2
# Useita tapoja syötää parametrien arvot
print(calculate2("sum", 2.4, 3.5))
print(calculate2(2.4, 8, "division"))
print(calculate2(calc_type='division', number2=2.4, number1=3.5))