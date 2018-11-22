# -*- coding: utf-8 -*-
# @Date    : 2018-11-18 11:44:26
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org

'''
用Redis统计用户上线次数
理解：
A用户 100010001000001  //活跃了4天
B用户 111111111111111  //每日必到
'''
import redis
from ..password import redis_passwd

# 连接Redis，选择 db0
r = redis.Redis(host='localhost', port=6379, password=redis_passwd, db=0)

# A用户，一年中，每3天上线一次
for i in range(0, 365, 3):
    r.setbit('usera', i, 1)

# B用户 每10天上线一次

for i in range(0, 365, 10):
    r.setbit('userb', i, 1)

# 用户列表
# "Returns a list of keys matching ``pattern``"
userList = r.keys('user*')
print(userList)

Au = []
Nau = []

# 判断是否为活跃用户，(用户，登录天数)
for u in userList:
    logincount = r.bitcount(u)
    if logincount > 100:
        Au.append((u, logincount))
    else:
        Nau.append((u, logincount))

for u in Au:
    print(f'用户{u[0]}: 活跃用户, 共登录{u[1]}天')

for u in Nau:
    print(f'用户{u[0]}: 非活跃用户, 共登录{u[1]}天')
