# -*- coding: utf-8 -*-
# @Date    : 2018-11-24 09:30:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

import redis
from ..password import redis_passwd

# 连接Redis，选择 db0
r = redis.Redis(host='localhost', port=6379, password=redis_passwd, db=0)

# set参数：
# ex，过期时间（秒）
# px，过期时间（毫秒）
# nx，如果设置为True，则只有name不存在时，当前set操作才执行
# xx，如果设置为True，则只有name存在时，岗前set操作才执行
r.set('name', 'redis', ex=60)
print(r.get('name'))
ret = r.getset('name', 'new value')
print(ret)
print(r.get('name'))

r.setnx('num', 123)
print(r.get('num'))

# time，过期时间（数字s/ms 或 timedelta对象）
r.setex('ex', 20, 'guoqi')
print(r.get('ex'))
r.psetex('pex', 20000, 'weimiao')
print(r.get('ex'))

# 批量设置
tom = {'tname': 'Tom', 'age': 20, 'id': 1}
r.mset(tom)
print(f"name:{r.get('tname')}\n'age':{r.get('age')}\n'id':{r.get('id')}")
r.msetnx(tom)

# 获取字符串的子序列，包括起始、结束
r.set('num', '0123456')
ret = r.getrange('num', 1, 4)
print(ret)
# 用 value 参数覆写给定 key 所储存的字符串值，从偏移量 offset 开始
r.setrange('num', 4, 'adcde')
print(r.get('num'))

r.set('bit', '012345')
# 012345 ascii = 30 31 32 33 34 35
# = 00110000 00110001 00110010 ...
# 对 key 所储存的字符串值，设置或清除指定偏移量上的位(bit)
r.setbit('bit', 1, 1)  # 00110000 -> 01110000=70=p
print(r.get('bit'))
print(r.getbit('bit', 2))

# 获取1的个数
r.set('bit', '1')  # 1 = 31 = 00110001
print(r.bitcount('bit', 0, -1))

# bit 操作 与 或 亦或 非
# dest, 新的Redis的name
# *keys,要查找的Redis的name
r.set('a', 0x11)  # 17 = 31 37 = 00110001 00110111
r.set('b', 0x22)  # 34 = 33 34 = 00110011 00110100
r.bitop('AND', 'yu', 'a', 'b')  # 00110001 00110100 = 31 34 = 14
r.bitop('OR', 'huo', 'a', 'b')  # 00110011 00110111 = 33 37 = 37
r.bitop('XOR', 'yihuo', 'a', 'b')  # 00000010 00000011 = 02 03
r.bitop('NOT', 'fei', 'a')  # 11001110 11001000 = ce c8
print(r.get('yu'))
print(r.get('huo'))
print(r.get('yihuo'))
print(r.get('fei'))

r.set('len', '012345678')
ret = r.strlen('len')
print(ret)

# 加
r.set('num', 1)
r.incr('num')
print(r.get('num'))
r.incrby('num', 3)
print(r.get('num'))
r.incrbyfloat('num', 2.1)
print(r.get('num'))

# 减
r.set('num', 10)
r.decr('num')
print(r.get('num'))
r.decrby('num', 4)
print(r.get('num'))

# 追加
r.set('code', 'abcdefg')
r.append('code', 'hijk')
print(r.get('code'))
