from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import time
#import humidSensorTest

app = Flask(__name__)
CORS(app)

# DB 연결 정보
db_config = {
    'host':'localhost',
    'user':'root',
    'password':'1587',
    'database':'IOT01'
}

@app.route('/')
def home():
    return 'Hello, Flask!'

@app.route('/api/data', methods=['GET'])
def get_sensor_data():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM temp_humid_log ORDER BY timestamp DESC LIMIT 20")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
