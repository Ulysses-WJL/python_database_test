# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 08:36:47
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
# Subdocument key order matters in a few of these examples so we have
# to use bson.son.SON instead of a Python dict.
from bson.son import SON
db = pymongo.MongoClient().first_demo
# db.inventory.insert_many([
#     {"item": "journal",
#      "qty": 25,
#      "size": SON([("h", 14), ("w", 21), ("uom", "cm")]),
#      "status": "A"},
#     {"item": "notebook",
#      "qty": 50,
#      "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
#      "status": "A"},
#     {"item": "paper",
#      "qty": 100,
#      "size": SON([("h", 8.5), ("w", 11), ("uom", "in")]),
#      "status": "D"},
#     {"item": "planner",
#      "qty": 75,
#      "size": SON([("h", 22.85), ("w", 30), ("uom", "cm")]),
#      "status": "D"},
#     {"item": "postcard",
#      "qty": 45,
#      "size": SON([("h", 10), ("w", 15.25), ("uom", "cm")]),
#      "status": "A"}])

# 查询  需要包含排序
cursor_1 = db.inventory.find(
    {"size": SON([("h", 14), ("w", 21), ("uom", "cm")])})
for x in cursor_1:
    print(x)
print("-------")
cursor_2 = db.inventory.find(
    {"size": SON([("w", 21), ("h", 14), ("uom", "cm")])})

for x in cursor_2:
    print(x)
print("-------")
cursor_3 = db.inventory.find({"size.h": {'$gt': 10}, "status": "A"})

for doc in cursor_3:
    print(doc)
# {'_id': ObjectId('5c0db6828c70ac252a102c85'), 'item': 'journal', 'qty': 25, 'size': {'h': 14, 'w': 21, 'uom': 'cm'}, 'status': 'A'}
