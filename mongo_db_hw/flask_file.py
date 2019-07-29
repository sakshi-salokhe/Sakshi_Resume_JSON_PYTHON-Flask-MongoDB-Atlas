from flask import Flask, render_template
from pymongo import MongoClient
from pprint import pprint
import json, ast
import jinja2

#for local
'''
client = MongoClient('mongodb://localhost:27017/')
db = client.sakshiDb
records = db.sakshiCollection
data = records.find_one({},{'_id': False})
x = ast.literal_eval(json.dumps(data))
pprint.pprint(x,indent=4)
'''


#'''
#for server hosting
#'''
client = MongoClient('mongodb+srv://salokhesakshi:test@c1-hlryq.mongodb.net/test?retryWrites=true&w=majority')
db = client.sakshi_db
records = db.sakshi_collection
data = records.find_one({},{'_id': False})
x = ast.literal_eval(json.dumps(data))
#print(type(x))
#pprint(json.dumps(x, indent=4))


#'''


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",x=x)

@app.route('/Sakshi_Sanjay_Salokhe')
def Sakshi():
    return render_template("sakshi.html",data = x)
	
if __name__ == "__main__":
    app.run()
