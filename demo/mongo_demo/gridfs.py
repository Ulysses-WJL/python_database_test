# -*- coding: utf-8 -*-
# @Date    : 2018-12-07 08:29:15
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
from pymongo import MongoClient
from gridfs import GridFS
import base64
db = MongoClient().first_demo
fs = GridFS(db)
print(fs.list())
if not fs.exists({"filename": 'timg.jpg'}):
    with open('/home/ulysses/Pictures/timg.jpg', 'rb') as f:
        kw = {'filename': 'timg.jpg'}
        fs.put(f, **kw)
else:
    cursor = fs.find({"filename": 'timg.jpg'}, no_cursor_timeout=True)
    for grid_out in cursor:
        data = grid_out.read()
        print(data)
        fs.delete(grid_out._id)
    print(fs.list())
