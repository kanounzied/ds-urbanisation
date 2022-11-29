from flask import Flask
# import pymongo
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['MONGO_URI'] = "mongodb://localhost:27017/ds-urbanisation"

# client = pymongo.MongoClient(conc)
mongo = PyMongo(app)
# db = client.cerise_db
Employee = mongo.db['employee']