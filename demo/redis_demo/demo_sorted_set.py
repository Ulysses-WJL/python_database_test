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
