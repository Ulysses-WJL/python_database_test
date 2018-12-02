# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 11:02:12
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import pymongo

client = pymongo.MongoClient(host="localhost", port=27017)
db = client['first_demo']
col = db['profile']
mylist = [
    {'user_id': 200, 'name': 'Tom'},
    {'user_id': 201, 'name': 'Tommy'},
    {'user_id': 202, 'name': 'Drew'},
    {'user_id': 213, 'name': 'Zodiac'},
    {'user_id': 220, 'name': 'Luke'},
    {'user_id': 230, 'name': 'David'},
    {'user_id': 204, 'name': 'James'},
    {'user_id': 206, 'name': 'Paul'},
]
# col.insert_many(mylist)
for doc in col.find():
    print(doc)
# col.create_index([('name', pymongo.ASCENDING)], unique=True)
print(col.index_information())
# col.delete_many({'$or': [{'user_id': 201}, {'user_id': 206}]})
new_profile = {'user_id': 1001, 'name': 'Ace'}
duplicate_profile = {'user_id': 1001, 'name': 'Alan'}
result = col.insert_one(new_profile)
result = col.insert_one(duplicate_profile)
