# -*- coding: utf-8 -*-
# @Date    : 2018-11-27 11:12:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
from random import randint
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)
ip_0101 = []
ip_0102 = []
for i in range(1, 100):
    ip = f'{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'
    ip_0101.append(ip)
for i in range(1, 40):
    ip = f'{randint(0,255)}.{randint(0,255)}.{randint(0,255)}.{randint(0,255)}'
    ip_0102.append(ip)
r.pfadd('ip:20180101', *ip_0101)
r.pfadd('ip:20180102', *ip_0102)
print(r.pfcount('ip:20180101'))
print(r.pfcount('ip:20180102'))
r.pfmerge('ip:201801', 'ip:20180101', 'ip:20180102')
print(r.pfcount('ip:201801'))
