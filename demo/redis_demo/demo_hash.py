# -*- coding: utf-8 -*-
# @Date    : 2018-11-25 09:54:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

# d1 = {'name': 'Jack', 'id': 1, 'location': 'US'}
# item = []
# print(type(d1.items()))
# print(type(iter(d1.items())))
# for pair in iter(d1.items()):
#     print(pair)
#     item.extend(pair)
# print(item)
from datetime import datetime
import redis
from ..password import redis_passwd
pool = redis.ConnectionPool(host='localhost', port=6379, password=redis_passwd, db=0)
r = redis.Redis(connection_pool=pool)

r.hset('t1', 'name', 'jack')
print(r.hget('t1', 'name'))
r.hsetnx('t1', 'name', 'ulysses')
print(r.hget('t1', 'name'))
d1 = {'name': 'Jack', 'id': 1, 'location': 'US'}
r.hmset('t1', d1)
print(r.hgetall('t1'))
keys = ['name', 'location']
print(r.hmget('t1', keys, 'id'))

d2 = {'date': str(datetime.now().date()), 'name': 'Akali', 'age': '16', 'id': 2}
r.hmset('t2', d2)
print(r.hlen('t2'))
print(r.hkeys('t2'))
print(r.hvals('t2'))

print(r.hgetall('t1'))
if r.hexists('t1', 'name'):
    r.hdel('t1', 'name')
print(r.hgetall('t1'))

print(r.hget('t2', 'id'))
if r.hexists('t2', 'id'):
    r.hincrby('t2', 'id', 25)
    print(r.hget('t2', 'id'))
    r.hincrbyfloat('t2', 'id', 3.14)
    print(r.hget('t2', 'id'))
