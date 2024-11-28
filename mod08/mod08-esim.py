'''
import mysql.connector
# connect()- funktion palauttaa tietokantayhteyden, joka sijoitetaan muuttujan
connection = mysql.connector.connect(
             host='127.0.0.1',  # localhost
             port=3306,
             database='lentopeli',
             user='newuser',
             password='newpassword',
             autocommit=True,
             collation= 'utf8mb4_general_ci'
             )
print(connection)
#CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword';
#GRANT SELECT, INSERT, UPDATE ON lentopeli.* TO 'newuser'@'localhost';
# Luodaan osoitajan ja sijoitetaan
cursor = connection.cursor()
# ajetaan SQL-kielinen kysely osoittimen avulla
cursor.execute("SELECT name, iso_country, continent FROM country")
# fetchone hakee rivi kerrallaan, palauttaa monikon
result = cursor.fetchone()
print(result)
# fetchmany() palauttaa halutun määrän rivejä (monikon) kerrallaan listana
result = cursor.fetchmany(1)
print(result)
# fetchall() palauttaa kaikki (loput) rivit listana
rows = cursor.fetchmany()
print(result)
# Tuloslista käsitellään toistorakenteella
#for row in result:
#    print(row)
for row in rows:
    print(f"{row[1]}, maakoodi: {row[2]}, maanosa: {row[0]}")
'''

