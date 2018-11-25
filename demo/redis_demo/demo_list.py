# -*- coding: utf-8 -*-
# @Date    : 2018-11-25 11:08:02
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)

if r.exists('l1'):
    r.delete('l1')
l1 = [0, 1, 2, 3, 4, 5, 6, 7]
r.lpush('l1', *l1)
print(r.lrange('l1', 0, -1))
r.lpush('l1', 'a')
r.lpushx('l1', 'b')
ret = r.lpop('l1')
print(ret)
print(r.lrange('l1', 2, 5))
print(r.lrange('l1', 10, 15))
print(r.lrange('l1', 4, 1))

if r.exists('l2'):
    r.delete('l2')
l2 = ['a', 'b', 'c', 'd', 'e']
r.rpush('l2', *l2)
print(r.lrange('l2', 0, -1))
r.linsert('l2', 'before', 'b', '0')
r.linsert('l2', 'after', 'd', '1')
print(r.lrange('l2', 0, -1))
print(r.llen('l2'))
print(r.lindex('l2', 1))
print(r.lindex('l2', 4))
