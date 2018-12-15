# -*- coding: utf-8 -*-
# @Date    : 2018-12-10 09:46:31
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import pymongo
client = pymongo.MongoClient(host="localhost", port=27018)
print(pymongo.MAX_SUPPORTED_WIRE_VERSION, pymongo.MIN_SUPPORTED_WIRE_VERSION)

sites = client.first_demo.sites
orders = client.first_demo.orders
with client.start_session() as session:
    with session.start_transaction():
        sites.insert_one({"name": "mongoing", 'id': 100, "url": "http://www.mongoing.com"}, session=session)
        orders.update_one({'name': "Rin"}, {"$set", {"url": "http://www.mongoing.com/Rin"}}, session=session)
