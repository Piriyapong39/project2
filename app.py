from flask import Flask, jsonify
from pymongo import MongoClient
app = Flask(__name__)
client = MongoClient('mongodb+srv://virote3011:kaluiklui3011@cluster0.ivzlivk.mongodb.net/?retryWrites=true&w=majority')
db = client.AEP
@app.route('/', methods=['GET'])
def get_seconds_amount():
    collection = db.scheduler
    latest_data = collection.find_one({}, {'_id': 0, 'seconds_amount': 1}, sort=[('_id', -1)])
    return jsonify(latest_data)
if __name__ == '__main__':
    app.run()
#host='0.0.0.0', port=5000