from flask import Flask,request
from pymongo import MongoClient
import time,os
app = Flask(__name__)

client = MongoClient(os.getenv('MONGOHQ_URL'))
db = client.DummyData
cn = db.keyLogs

@app.route('/',methods=['GET'])
def boo():
	
	return "This server logs every value POST'd to it on url /log"




@app.route('/log',methods=['POST'])
def foo():
	data =str(request.get_data())
	now = time.time()
	cn.insert({"data":data,"time_stamp":now})
	return "logged"

if __name__ == '__main__':
    app.run(debug=True)