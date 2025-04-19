from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Replace this URI with your MongoDB Atlas connection string
client = MongoClient("mongodb+srv://user:user@cluster0.kdxcuxk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
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
    app.run(host='0.0.0.0', port=5000)
