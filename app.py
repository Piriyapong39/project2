from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb+srv://datafromgooglesheet:kaluiklui3011@cluster0.7vgowbh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.weather

@app.route("/", methods=["GET"])
def dataforesp():
    collection = db.data
    lastest_data = collection.find_one({}, {"Temperature": 1,"Humidity": 1,"Status": 1, "HumidityADJ": 1, "_id": 0}, sort=[('_id', -1)])
    return jsonify(lastest_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
