# -*- coding: utf-8 -*-
# @Date    : 2018-12-01 11:20:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
client = pymongo.MongoClient(host="localhost", port=27017)
db = client['first_demo']
col = db['student']
stu_list = [
    {'_id': 1, 'name': 'Jack', 'score': 90},
    {'_id': 2, 'name': 'Tom', 'score': 85},
    {'_id': 3, 'name': 'Candy', 'score': "A"},
    {'_id': 4, 'name': 'Ana', 'score': "B"},
]
# col.insert_many(stu_list)
for x in col.find():
    print(x)
# {'_id': 1, 'name': 'Jack', 'socre': 90}
# {'_id': 2, 'name': 'Tom', 'socre': 85}
# {'_id': 3, 'name': 'Candy', 'socre': 'A+'}
# {'_id': 4, 'name': 'Ana', 'socre': 'B'}
#
result = col.update_one(filter={'score': {"$type": 'string'}},
                        update={'$set': {"score": "S+"}})
print(result.matched_count)
print(result.modified_count)
# 1
# 1
#
for x in col.find():
    print(x)
# {'_id': 1, 'name': 'Jack', 'socre': 90}
# {'_id': 2, 'name': 'Tom', 'socre': 85}
# {'_id': 3, 'name': 'Candy', 'socre': 'S+'}
# {'_id': 4, 'name': 'Ana', 'socre': 'B'}

result = col.update_many(filter={'score': {'$type': "int"}},
                         update={"$inc": {'score': 1}})
print(result.matched_count)
print(result.modified_count)
# 2
# 2
for x in col.find():
    print(x)
# {'_id': 1, 'name': 'Jack', 'score': 91}
# {'_id': 2, 'name': 'Tom', 'score': 86}
# {'_id': 3, 'name': 'Candy', 'score': 'S+'}
# {'_id': 4, 'name': 'Ana', 'score': 'B'}

ret = col.replace_one({'name': 'Jack'}, {'name': 'John'})
print(ret.matched_count)
print(ret.modified_count)
for doc in col.find():
    print(doc)
