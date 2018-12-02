# -*- coding: utf-8 -*-
# @Date    : 2018-12-02 09:42:08
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
db = client['first_demo']
col = db['student']
for doc in col.find():
    print(doc)
print('--------')
col.delete_one({'name': 'Ana'})
for doc in col.find():
    print(doc)
print('--------')
query = {'$or': [{'_id': 2}, {'_id': 3}]}
ret = col.delete_many(query)
print(ret.deleted_count)
for doc in col.find():
    print(doc)

query = {'name': 'John'}
ret = col.find_one_and_delete({'name': 'John'})
print(ret)
print(col.count_documents(query))
# col = db['sites']
col.drop()