import datetime
from pymongo import MongoClient
import pymongo

client=MongoClient()
db=client['mydatabase']['users']

old_date= datetime.datetime(2016,12,8)
todays_date = datetime.datetime.now()
# print(todays_date)
# uid= db.insert_one({'username':'new_user','date':todays_date})

cou= db.count_documents({'date':{'$gt': old_date}})
cou= db.count_documents({'date':{'$exists': old_date}})

cou=db.create_index([('username', pymongo.ASCENDING)],unique=False)
print(cou)