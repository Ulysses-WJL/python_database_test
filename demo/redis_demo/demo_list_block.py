# -*- coding: utf-8 -*-
# @Date    : 2018-11-26 09:38:21
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)
ret1 = r.blpop('l6', timeout=10)
ret2 = r.brpop('l7', timeout=10)
print(ret1)
print(ret2)
