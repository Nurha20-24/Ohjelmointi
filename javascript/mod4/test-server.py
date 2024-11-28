from flask import Flask
from flask_cors import CORS
import _mysql_connector


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/airport/<icao>')
def airport(icao):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='lentopeli',
        user='newuser',
        password='newpassword',
        autocommit=True,
        collation='utf8mb4_general_ci'
    )
    sql = f'select ident, name from airport where ident={icao}'
    cursor = connection.cursor()
    cursor.execute(sql)
    cursor.fetchone()
    #return {'ICAO': icao, 'Name': 'Airport name'}

app.run()
if __name__ == '__main__':
  app.run(use_reloader=True, host='127.0.0.1', port=3000)
