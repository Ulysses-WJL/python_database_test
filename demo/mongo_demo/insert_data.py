# -*- coding: utf-8 -*-
# @Date    : 2018-11-30 11:25:29
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['first_demo']
col = db['sites']
# 集合内插入
d1 = {'name': 'google', 'id': 2, 'url': 'https://www.google.com'}
x = col.insert_one(d1)
# 方法返回 InsertOneResult 对象，该对象包含 inserted_id 属性，它是插入文档的 id 值
print(x)  # <pymongo.results.InsertOneResult object at 0x7fec2a5f3888>
print(x.inserted_id)  # 5c00af888c70ac6346a4ab25

# 插入多条数据
mylist = [
    {"name": "Taobao", "alexa": "100", "url": "https://www.taobao.com"},
    {"name": "QQ", "alexa": "101", "url": "https://www.qq.com"},
    {"name": "Facebook", "alexa": "10", "url": "https://www.facebook.com"},
    {"name": "知乎", "alexa": "103", "url": "https://www.zhihu.com"},
    {"name": "Github", "alexa": "109", "url": "https://www.github.com"},
]
x = col.insert_many(mylist)
# 输出插入的所有文档对应的 _id 值
print(x.inserted_ids)
# [ObjectId('5c00b2068c70ac67e3a197fe'), ObjectId('5c00b2068c70ac67e3a197ff'), ObjectId('5c00b2068c70ac67e3a19800'), ObjectId('5c00b2068c70ac67e3a19801'), ObjectId('5c00b2068c70ac67e3a19802')]

mylist_2 = [
    {'_id': 1, 'name': 'Jack', 'num': 1233},
    {'_id': 2, 'name': 'Tom', 'num': 1233},
    {'_id': 3, 'name': 'Candy', 'num': 1233},
    {'_id': 4, 'name': 'Ana', 'num': 1233},
]
x = col.insert_many(mylist_2)
print(x.inserted_ids)
# [1, 2, 3, 4]