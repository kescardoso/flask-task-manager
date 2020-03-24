import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
# Environment Variables
from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

# Constants from pymongo
MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "task_manager"


mongo = PyMongo(app)


@app.route('/')
def hello():
    return 'Hello World ...again'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
