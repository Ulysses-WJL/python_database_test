# -*- coding: utf-8 -*-
# @Date    : 2018-11-30 10:57:34
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
# 创建数据库 只有在内容插入后才会创建
db = client['first_demo']

# 返回当前数据库列表
dblist = client.list_database_names()
print(dblist)
if 'first_demo' in dblist:
    print('数据库已存在')

# 创建集合 集合只有在内容插入后才会创建
col = db['sites']

# 返回数据库内集合
collist = db.list_collection_names()
if 'sites' in collist:
    print('集合已存在')
