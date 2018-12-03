# -*- coding: utf-8 -*-
# @Date    : 2018-12-03 08:09:06
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
import pprint
from bson.son import SON
from bson.code import Code

client = pymongo.MongoClient(host='localhost', port=27017)
db = client['first_demo']
col = db['orders']
ord_list = [
    {'cust_id': 'A122', 'amount': 123, 'status': 'A'},
    {'cust_id': 'A122', 'amount': 500, 'status': 'A'},
    {'cust_id': 'B112', 'amount': 300, 'status': 'A'},
    {'cust_id': 'B112', 'amount': 200, 'status': 'B'},
]
# col.insert_many(ord_list)
pipleline = [
    {'$match': {'status': 'A'}},
    {'$group': {'_id': '$cust_id', 'total': {'$sum': '$amount'}}},
    {'$sort': SON([('total', 1)])}
]
ret = col.aggregate(pipleline)

pprint.pprint(list(ret))
# [{'_id': 'B112', 'total': 300}, {'_id': 'A122', 'total': 623}]
#
mapper = Code("""
            function () {
                emit(this.cust_id, this.amount);
            }
            """)
reducer = Code("""
                function (key, values) {
                    return Array.sum(values)
                }
                """)
result = col.map_reduce(mapper, reducer, 'myresult', full_response=True)
print(result)
# {'result': 'myresult', 'timeMillis': 40, 'counts': {'input': 4, 'emit': 4, 'reduce': 2, 'output': 2}, 'ok': 1.0}
query = {'status': 'A'}
result = col.map_reduce(mapper, reducer, 'myresult_1', query=query)
for doc in result.find():
    pprint.pprint(doc)
# {'_id': 'A122', 'value': 623.0}
# {'_id': 'B112', 'value': 300.0}
print(f"counts: {col.count()}")
print(f"distinct: {col.distinct('cust_id')}")
print(f"estimate num: {col.estimated_document_count()}")
# counts: 4
# distinct: ['A122', 'B112']
# estimate num: 4
