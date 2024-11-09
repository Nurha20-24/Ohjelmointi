# Tehtävä 2
from flask import Flask, Response, request
import json
import mysql.connector

app = Flask(__name__)
@app.route("/kentta/<EFHK>")
def kentta_efhk(EFHK):
    try:
        connection = mysql.connector.connect(
             host='127.0.0.1',
             port=3306,
             database='lentopeli',
             user='newuser',
             password='newpassword',
             autocommit=True,
             collation= 'utf8mb4_general_ci'
             )

        icao = EFHK
        sql = f"SELECT ident, name, municipality FROM airport WHERE ident ='{icao}';"
        cursor = connection.cursor()
        cursor.execute(sql)
        result_row = cursor.fetchone()
        cursor.close()
        connection.close()

        if result_row:
            tilakoodi = 200
            vastaus = {
                "ICAO":result_row[0],
                "Name":result_row[1],
                "Municipality":result_row[2]
        }

        else:
            tilakoodi = 404
            vastaus = {
                "status": tilakoodi,
                "Teksti": "Kenttää ei löydy"
        }

    except Exception as e:
        tilakoodi = 500
        vastaus = {
            "status": tilakoodi,
            "Teksti": f"Virhe: {str(e)}"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(error):
    vastaus = {
        "status": 404,
        "Teksti": "Virheellinen loppuosa"
    }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype='application/json')

if __name__ == "__main__":
    app.run(use_reloader=True, host='127.0.0.1', port=3000)