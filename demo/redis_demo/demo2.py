# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 10:43:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
from ..password import redis_passwd
from redis import Redis
r = Redis(host='localhost', port=6379, password=redis_passwd, db=0)
p = r.pubsub()
# p.subscribe('my-first-channel', 'my-second-channel')
msg_reciver = p.psubscribe('cctv*')
print(msg_reciver)
