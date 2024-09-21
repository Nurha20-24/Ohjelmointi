
# Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä,
# että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

connection = mysql.connector.connect(
            host='127.0.0.1',
            port=3306,
            database='lentopeli',
            user='newuser',
            password='newpassword',
            autocommit=True,
            collation='utf8mb4_general_ci'
            )
def fetch_airport_by_type(code):
    code = input("Syötä maakoodi: ")
    sql = (f"select type, count(*) from airport where iso_country = '{code}' group by type;")
    cursor = connection.cursor()
    cursor.execute(sql)
    result_row = cursor.fetchall()
    print(result_row)
    return result_row

airport = fetch_airport_by_type("")
if airport:
    for row in airport:
        print(f"Haettu maassa on {row}")
else:
    print("Lentokenttä ei löydetty annetulla koodilla")