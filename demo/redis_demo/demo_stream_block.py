# -*- coding: utf-8 -*-
# @Date    : 2018-11-28 10:50:52
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)
r.xadd('stream_2', {'name': 'jack', 'age': 11})
