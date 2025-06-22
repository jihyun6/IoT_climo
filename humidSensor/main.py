import sys
import os
import time
import mysql.connector
from flask import Flask, jsonify
from flask_cors import CORS

# secure_config 모듈 경로 추가 (부모 폴더 기준)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from secure_config import db_config

#import humidSensorTest

app = Flask(__name__)
CORS(app)


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
