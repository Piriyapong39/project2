from flask import Flask, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# เชื่อมต่อ MongoDB
client = MongoClient('mongodb+srv://virote3011:kaluiklui3011@cluster0.ivzlivk.mongodb.net/?retryWrites=true&w=majority')
db = client.AEP  # เลือกฐานข้อมูลที่ต้องการใช้งาน

# Route สำหรับดึงข้อมูล seconds_amount ล่าสุดจาก MongoDB และส่งออกเป็น JSON
@app.route('/', methods=['GET'])
def get_seconds_amount():
    collection = db.scheduler  # เลือกคอลเล็กชันที่ต้องการใช้งาน
    # ดึงข้อมูล seconds_amount ล่าสุด
    latest_data = collection.find_one({}, {'_id': 0, 'seconds_amount': 1}, sort=[('_id', -1)])

    # แปลงข้อมูลให้เป็นรูปแบบ JSON ด้วย jsonify() ฟังก์ชันของ Flask
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
