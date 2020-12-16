import os
import dotenv
from pymongo import MongoClient

dotenv.load_dotenv()
PORT = os.getenv("PORT")
DBURL = os.getenv("URL")

#Vamos a conectar con la base de datos de mongo en local
if not (DBURL):
    raise ValueError("Tienes que especificar una URL pls")


client = MongoClient(DBURL)
db = client.get_database()
collection = db["frases"]