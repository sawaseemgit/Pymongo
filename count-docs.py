from pymongo import MongoClient

client = MongoClient()
db = client.mydatabase
Users = db.users
# db=client['mydatabase']['users']
# filter = {'stu_id': '27'}
filter = {'stu_id': '27','username':'jon'}
count = Users.count_documents(filter)

print(count)
