
#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
#Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
#Laskenta perustuu tietokannasta haettuihin koordinaatteihin. Laske etäisyys geopy-kirjaston avulla.
from geopy import distance
import mysql.connector

connection = mysql.connector.connect(
             host='127.0.0.1',
             port=3306,
             database='lentopeli',
             user='newuser',
             password='newpassword',
             autocommit=True,
             collation= 'utf8mb4_general_ci'
             )
def fetch_airport_by_icao():
   icao = input("Syötä lentokenttien icao-koodi: ")
   sql = (f"select latitude_deg, longitude_deg from airport where ident = '{icao}';")
   cursor = connection.cursor()
   cursor.execute(sql)
   result_row = cursor.fetchall()
   print(result_row)
   return result_row

airport1 = fetch_airport_by_icao()
airport2 = fetch_airport_by_icao()
print(f"Kahden lentokenttien välsen etäisyys on {(distance.distance(airport1, airport2).km):.2f} kilometriä.")
