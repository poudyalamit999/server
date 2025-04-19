from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import datetime
import os

app = Flask(__name__)
CORS(app)

# Load MongoDB URI from environment variable
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client['Gps']
collection = db['Gps']

@app.route('/upload', methods=['POST'])
def upload_data():
    try:
        data = request.get_json()
        lat = data.get('lat')
        lng = data.get('lng')
        timestamp = datetime.datetime.utcnow()

        doc = {
            "latitude": lat,
            "longitude": lng,
            "timestamp": timestamp
        }

        collection.insert_one(doc)
        return jsonify({"status": "success", "message": "Data stored."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use port from environment
    app.run(host='0.0.0.0', port=port)
