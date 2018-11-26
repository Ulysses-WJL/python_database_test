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

if r.exists('l3'):
    r.delete('l3')
l3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
r.rpush('l3', *l3)
r.lset('l3', 1, 1)
r.lset('l3', 3, 1)
print(r.lrange('l3', 0, -1))
# count > 0: Remove elements equal to value moving from head to tail.
# count < 0: Remove elements equal to value moving from tail to head.
# count = 0: Remove all elements equal to value.
r.lrem('l3', 2, 1)
print(r.lrange('l3', 0, -1))
r.ltrim('l3', 1, 4)
print(r.lrange('l3', 0, -1))

if r.exists('l4'):
    r.delete('l4')
if r.exists('l5'):
    r.delete('l5')
l4 = ['US', 'CN', 'JP', 'FR', 'UK']
l5 = ['baidu', 'google', 'facebook', 'twitter']
r.rpush('l4', *l4)
r.rpush('l5', *l5)
r.rpoplpush('l4', 'l5')
print(r.lrange('l4', 0, -1))
print(r.lrange('l5', 0, -1))

if r.exists('l6'):
    r.delete('l6')
if r.exists('l7'):
    r.delete('l7')
l6 = [1, 2, 3, 4, 5, 6]
l7 = ['a', 'b', 'c', 'd']
# ret1 = r.blpop('l6', timeout=10)
# ret2 = r.brpop('l7', timeout=10)
r.rpush('l6', *l6)
r.rpush('l7', *l7)
print(r.lrange('l6', 0, -1))
print(r.lrange('l7', 0, -1))
