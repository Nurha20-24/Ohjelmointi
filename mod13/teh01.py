# Tehtävä 1
from flask import Flask, Response
import json
import math
app = Flask(__name__)
@app.route('/alkuluku/<alkuluku>')
def alkuluku(alkuluku):
    try:
        luku = int(alkuluku)

        if luku < 2:
            is_prime = False
        else:
            is_prime = True
            for i in range(2, int(math.sqrt(luku))+1):
                if luku % i == 0:
                    is_prime = False
                    break

        tilakoodi = 200
        vastaus = {
            "Number": luku,
            "isPrime": is_prime
        }
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Virheellinen luku"
        }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=tilakoodi, mimetype="application/json")

@app.errorhandler(404)
def page_not_found(error):
    vastaus = {
        "status": "404",
        "teksti": "Virheelinen loppuosa"
    }

    jsonvast = json.dumps(vastaus)
    return Response(response=jsonvast, status=404, mimetype="application/json")

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3500)