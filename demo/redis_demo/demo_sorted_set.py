# -*- coding: utf-8 -*-
# @Date    : 2018-11-26 10:47:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)

if r.exists('zs1'):
    r.delete('zs1')
zs = {'us': 1, 'cn': 2, 'jp': 2.5, 'kr': 4, 'eu': 3.5}
r.zadd('zs1', zs)
print(r.zcard('zs1'))
print(r.zcount('zs1', 2, 4))
print(r.zscore('zs1', 'jp'))
print(r.zrange('zs1', 0, -1, withscores=True))
print(r.zrevrange('zs1', 0, -1))

print('-----------------')
if r.exists('zs2'):
    r.delete('zs2')
zs2 = {'a': 1, 'b': 2, 'c': 2.5, 'd': 2.2, 'e': 3.5, 'f': 0.5}
r.zadd('zs2', zs2)
r.zincrby('zs2', 2, 'c')
print(r.zscore('zs2', 'c'))
print(r.zlexcount(name="zs2", min="-", max="+"))
print(r.zrangebylex(name='zs2', min="-", max="+"))
print(r.zrevrangebylex('zs2', "[f", "[a"))
print(r.zrangebyscore('zs2', 0, 4))
print(r.zrevrangebyscore('zs2', 5, 1, withscores=True))
print('-----------------')
if r.exists('zs2'):
    r.delete('zs2')
zs3 = {'a': 1, 'b': 2, 'c': 2.5, 'd': 3.2, 'e': 3.5, 'f': 3.55, 'g': 4, 'h': 4.1,
       'i': 4.3, 'j': 4.5, 'k': 5, 'l': 5.3, 'm': 5.6, 'n': 5.8, 'o': 6}
r.zadd('zs3', zs3)
print(r.zrank('zs3', 'f'))
print(r.zrevrank('zs3', 'f'))
r.zrem('zs3', 'a')
print(r.zrange('zs3', 0, -1, withscores=True))
r.zremrangebylex('zs3', '[b', '[d')
print(r.zrange('zs3', 0, -1, withscores=True))
r.zremrangebyrank('zs3', '2', '4')
print(r.zrange('zs3', 0, -1, withscores=True))
r.zremrangebyscore('zs3', 3, 5)
print(r.zrange('zs3', 0, -1, withscores=True))

print('-----------------')
if r.exists('zs4'):
    r.delete('zs4')
if r.exists('zs5'):
    r.delete('zs5')
zs4 = {'baidu': 1, 'google': 2, 'sina': 4, 'twitter': 3, 'facebook': 3.54}
zs5 = {'taobao': 1, 'youtube': 2, 'twitch': 4, 'google': 5, 'sina': 5.5}
r.zadd('zs4', zs4)
r.zadd('zs5', zs5)
r.zinterstore('zs_inter', ('zs4', 'zs5'))
r.zunionstore('zs_union', ('zs4', 'zs5'))
print(r.zrange('zs_inter', 0, -1, withscores=True))
print(r.zrange('zs_union', 0, -1, withscores=True))

print('-----------------')
if r.exists('zs6'):
    r.delete('zs6')
zs6 = {'a': 1, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}
r.zadd('zs6', zs6)
print(r.zpopmax('zs6', 2))
print(r.zpopmin('zs6', 2))
print(r.zrange('zs6', 0, -1))
