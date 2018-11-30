# -*- coding: utf-8 -*-
# @Date    : 2018-11-30 08:01:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)
r.flushdb()
for key, value in (('A', '1'), ('B', '2'), ('C', '3')):
    r.set(key, value)
for key in r.scan_iter():
    print(key, r.keys(key))
# b'C' [b'C']
# b'B' [b'B']
# b'A' [b'A']


s1 = [1, 2, 3, 4, 'white', 'black']
s2 = ['a', 'b', 'c', 'Jack']
r.sadd('s1', *s1)
r.sadd('s2', *s2)
for member in r.sscan_iter('s1'):
    print(member)
print('---------')
for member in r.sscan_iter('s2'):
    print(member)
# b'2'
# b'3'
# b'black'
# b'4'
# b'white'
# b'1'
# ---------
# b'Jack'
# b'b'
# b'a'
# b'c'
print('---------')
d1 = {'name': 'Jack', 'id': 1, 'location': 'US'}
r.hmset('h1', d1)
for field in r.hscan_iter('h1'):
    print(field)
# (b'name', b'Jack')
# (b'id', b'1')
# (b'location', b'US')
print('---------')
zs = {'a1': 1, 'a2': 2, 'a3': 2.5, 'b1': 4, 'b2': 3.5}
r.zadd('zs1', zs)
for field in r.zscan_iter('zs1', match='a*'):
    print(field)
(b'a1', 1.0)
(b'a2', 2.0)
(b'a3', 2.5)
