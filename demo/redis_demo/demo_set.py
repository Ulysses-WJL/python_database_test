# -*- coding: utf-8 -*-
# @Date    : 2018-11-26 09:48:11
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)
s1 = ['a', 1, 2, 3, 'b', 'z', 'US', 'CN', 'Jack', 'Tom']
if r.exists('s1'):
    r.delete('s1')
r.sadd('s1', *s1)
print(r.scard('s1'))
if r.sismember('s1', 'US'):
    r.srem('s1', 'US')
print(r.smembers('s1'))

s2 = ['baidu', 'google', 'sina', 'sohu', 'twitter']
if r.exists('s2'):
    r.delete('s2')
r.sadd('s2', *s2)
ret = r.spop('s2')
print(ret)
print(r.smembers('s2'))
ret = r.srandmember('s2', 3)
print(ret)
print(r.smembers('s2'))

print('-----------------')
s3 = ['baidu', 'google', 'sina', 'sohu', 'twitter', 1, 2, 3, 'a', 'b']
s4 = ['a', 'b', 'c', 1, 2, 'google']
# s_diff = []
# s_inter = []
# s_union = []
if r.exists('s3'):
    r.delete('s3')
if r.exists('s4'):
    r.delete('s4')
r.sadd('s3', *s3)
r.sadd('s4', *s4)
# r.sadd('s_diff', *s_diff)
# r.sadd('s_inter', *s_inter)
# r.sadd('s_union', *s_union)

diff = r.sdiff('s3', 's4')
r.sdiffstore('s_diff', 's3', 's4')
print(diff)
print(r.smembers('s_diff'))

inter = r.sinter('s3', 's4')
r.sinterstore('s_inter', 's3', 's4')
print(inter)
print(r.smembers('s_inter'))

union = r.sunion('s3', 's4')
r.sunionstore('s_union', 's3', 's4')
print(union)
print(r.smembers('s_union'))

r.smove('s3', 's4', 'sina')
print(r.smembers('s3'))
print(r.smembers('s4'))
