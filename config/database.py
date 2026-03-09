from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()  

mongo_uri = os.getenv("MONGO_URI")

cliente = MongoClient(mongo_uri)

db_name = os.getenv("MONGO_DB")

db = cliente[db_name]

print(f"Conectado ao banco: {db_name}")

tasks_collection = db["tasks"]