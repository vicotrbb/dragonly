from pymongo import MongoClient
import os

mongo_client = MongoClient(os.environ.get('MONGODB_URL'))
db = mongo_client.dragonly
