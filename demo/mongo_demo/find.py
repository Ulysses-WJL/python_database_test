# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 08:40:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['first_demo']
col = db['sites']

for x in col.find():
    print(x)

print("-------------")
# 查询指定字段数据
for x in col.find({}, {"_id": 0, 'name': 1, 'url': 1}):
    print(x)

print("-------------")
# 指定条件查询 类似 sql where name = googel and id =1
query_1 = {'name': 'google', 'id': 1}
doc_1 = col.find(query_1)
for x in doc_1:
    print(x)
# {'_id': ObjectId('5c00ad0c8c70ac5e7746832d'), 'name': 'google', 'id': 1, 'url': 'https://www.google.com'}
# {'_id': ObjectId('5c00ad1b8c70ac5e8b08ce09'), 'name': 'google', 'id': 1, 'url': 'https://www.google.com'}

print("-------------")
# or  where name = Jack or _id = 2
query_2 = {"$or": [{'name': 'Jack'}, {'_id': 2}]}
doc_2 = col.find(query_2)
for x in doc_2:
    print(x)
# {'_id': 1, 'name': 'Jack', 'num': 1233}
# {'_id': 2, 'name': 'Tom', 'num': 1233}

print("-------------")
# 大于 where id > 2
query_3 = {'_id': {'$gt': 2}}
doc_3 = col.find(query_3)
for x in doc_3:
    print(x)
# {'_id': 3, 'name': 'Candy', 'num': 1233}
# {'_id': 4, 'name': 'Ana', 'num': 1233}

print("-------------")
# where name='QQ' or (_id > 1 and name = 'google')
query_4 = {'$or': [{"name": "QQ"}, {"id": {"$gt": 1}, "name": "google"}]}
doc_4 = col.find(query_4)
for x in doc_4:
    print(x)
# {'_id': ObjectId('5c00af888c70ac6346a4ab25'), 'name': 'google', 'id': 2, 'url': 'https://www.google.com'}
# {'_id': ObjectId('5c00b2068c70ac67e3a197fd'), 'name': 'google', 'id': 2, 'url': 'https://www.google.com'}
# {'_id': ObjectId('5c00b2068c70ac67e3a197ff'), 'name': 'QQ', 'alexa': '101', 'url': 'https://www.qq.com'}
# {'_id': ObjectId('5c01d7ed8c70ac1f294fb30a'), 'name': 'google', 'id': 2, 'url': 'https://www.google.com'}
# {'_id': ObjectId('5c01d7ed8c70ac1f294fb30c'), 'name': 'QQ', 'alexa': '101', 'url': 'https://www.qq.com'}

print("-------------")

col_2 = db['student']
stu_list = [
    {'_id': 1, 'name': 'Jack', 'socre': 90},
    {'_id': 2, 'name': 'Tom', 'socre': 85},
    {'_id': 3, 'name': 'Candy', 'socre': "A"},
    {'_id': 4, 'name': 'Ana', 'socre': "B"},
]
# col_2.insert_many(stu_list)
for x in col_2.find():
    print(x)
print('-----')
query_5 = {'socre': {"$type": "string"}}
doc_5 = col_2.find(query_5)
for x in doc_5:
    print(x)
# -------------
# {'_id': 1, 'name': 'Jack', 'socre': 90}
# {'_id': 2, 'name': 'Tom', 'socre': 85}
# {'_id': 3, 'name': 'Candy', 'socre': 'A'}
# {'_id': 4, 'name': 'Ana', 'socre': 'B'}
# -----
# {'_id': 3, 'name': 'Candy', 'socre': 'A'}
# {'_id': 4, 'name': 'Ana', 'socre': 'B'}

print("-------------")
# 正则表达式 查询 只能用于字符串
query_6 = {"name": {"$regex": "^g\w+e$"}}
doc_6 = col.find(filter=query_6, projection={"_id": 0, 'url': 0})
for x in doc_6:
    print(x)
# {'name': 'google', 'id': 1}
# {'name': 'google', 'id': 1}
# {'name': 'google', 'id': 2}
# {'name': 'google', 'id': 2}
# {'name': 'google', 'id': 2}

print("-------------")
# 指定查询返回条数
# doc_7 = col.find(filter={'name': "google"}, projection={"url": 0}, limit=3)
doc_7 = col.find(filter={'name': "google"}, projection={"url": 0}).limit(3)
for x in doc_7:
    print(x)
# {'_id': ObjectId('5c00ad0c8c70ac5e7746832d'), 'name': 'google', 'id': 1}
# {'_id': ObjectId('5c00ad1b8c70ac5e8b08ce09'), 'name': 'google', 'id': 1}
# {'_id': ObjectId('5c00af888c70ac6346a4ab25'), 'name': 'google', 'id': 2}
# 