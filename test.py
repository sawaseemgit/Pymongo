from pymongo.errors import ConnectionFailure
from pymongo import MongoClient

client = MongoClient()
try:
# The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
    db = client.test_db
    collection = db['test_coll']
    # print(collection)
except ConnectionFailure:
    print("Server not available")




