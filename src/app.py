from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
from decouple import config


app = Flask(__name__)
app.config["MONGO_URI"] = config("MONGO_URI")
mongo = PyMongo(app)

db = mongo.db.users

