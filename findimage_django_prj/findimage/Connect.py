import ssl, os

from pymongo import MongoClient

ssl._create_default_https_context = ssl._create_unverified_context
client = MongoClient(
    "mongodb+srv://findimage123:findimagecapstone@cluster0.p7r2e.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client['Instagram']
collection_Instagram = db.get_collection('posts')

# cursor = collection_Instagram.find()
# list_cur = list(cursor)
# json_string = dumps(list_cur)
# json_object = json.loads(json_string)