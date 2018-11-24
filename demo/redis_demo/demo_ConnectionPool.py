# -*- coding: utf-8 -*-
# @Date    : 2018-11-23 10:29:41
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
"""
连接池
"""
import redis
from ..password import redis_passwd
pool = redis.ConnectionPool(host='localhost', port=6379, db=0, password=redis_passwd)
r = redis.Redis(connection_pool=pool, decode_responses=True)
r.set('name', 'Redis')
ret = r.get('name')
print(ret, type(ret))
