import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client["mydatabase"] # alternate way
# db = client.mydb
Users = db.users  # users(=collection)=>tables in mysql
# define records
user1 = {'username': 'bob', 'password': 'abc789', 'stu_id': '23', 'hobbies': ['python', 'games']}
# Add Single record
# user_id= users.insert_one(user1).inserted_id
#define many users
users = [{'username':'Ann','password': '1233', 'stu_id': '25'},
         {'username':'jon','password': '4512', 'stu_id': '27'}]
#Add multiple records
add_mul= Users.insert_many(users)

print(add_mul.inserted_ids)
