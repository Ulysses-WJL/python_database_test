# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 10:36:45
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client['first_demo']
col = db['sites']
for doc in col.find({"alexa": {"$gt": '100'}}).sort('name', pymongo.DESCENDING):
    print(doc)

index = col.create_index()
