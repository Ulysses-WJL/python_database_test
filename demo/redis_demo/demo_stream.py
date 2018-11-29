# -*- coding: utf-8 -*-
# @Date    : 2018-11-28 08:54:48
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
import redis
from ..password import redis_passwd
r = redis.Redis(host='localhost', port=6379, db=0, password=redis_passwd)
if r.exists('stream_1'):
    r.delete('stream_1')
message1 = {'name': 'Flask', 'price': 10}
message1_id = r.xadd('stream_1', message1)
message2 = {'name': 'Django', 'price': 15}
message2_id = r.xadd('stream_1', message2)
print(f"message1_id:{message1_id}\nmessage2_id: {message2_id}")
print(f"stream len:{r.xlen('stream_1')}")
print(f"stream messages:{r.xrange('stream_1')}")
r.xdel('stream_1', message1_id)
print(f"stream messages:{r.xrange('stream_1')}")

print('------------------------')
if r.exists('stream_2'):
    r.delete('stream_2')
countrys = ['CN', 'US', 'UK', 'EU', 'JP']
i = 0
ret = []
for country in countrys:
    ret.append(r.xadd('stream_2', {'country': country, 'id': i}))
print(r.xread({'stream_2': ret[1], 'stream_1': 0}, 2))
# 0-0 从头开始
print(r.xread({'stream_2': '0-0'}))
# 从尾端读取数据, 阻塞时间60s
# print(r.xread({'stream_2': '$'}, block=1000 * 60))

print('-------------------------')
if r.exists('stream_3'):
    r.delete('stream_3')
r.xadd('stream_3', {'id': 0})
r.xadd('stream_3', {'id': 1})
# 从头部开始消费
r.xgroup_create('stream_3', 'group_2', id=0)
# 从尾部开始消费
r.xgroup_create('stream_3', 'group_1', id="$")
# 流的信息
print(r.xinfo_stream('stream_3'))
# 消费组信息
print(r.xinfo_groups('stream_3'))
# 移除消费组
r.xgroup_destroy('stream_3', 'group_2')
print(r.xinfo_groups('stream_3'))

print('-------------------------')
if r.exists('stream_4'):
    r.delete('stream_4')
r1 = r.xadd('stream_4', {'name': 'jack'})
r2 = r.xadd('stream_4', {'name': 'Tom'})
r3 = r.xadd('stream_4', {'name': 'Will'})
r.xgroup_create('stream_4', 'group_1', id=0)
# >号表示从当前消费组的last_delivered_id后面开始读
# 每当消费者读取一条消息，last_delivered_id变量就会前进
ret = r.xreadgroup('group_1', 'consumer_1', {'stream_4': ">"}, count=1)
print(ret)
r.xreadgroup('group_1', 'consumer_1', {'stream_4': ">"}, count=2)
print(r.xinfo_consumers('stream_4', 'group_1'))
print(r.xpending('stream_4', 'group_1'))
# ack 2条消息
r.xack('stream_4', 'group_1', *[r1, r2])
print(r.xinfo_consumers('stream_4', 'group_1'))

print('-------------------------')
if r.exists('stream_5'):
    r.delete('stream_5')
for i in range(0, 10):
    r.xadd('stream_5', {'id': i})
print(r.xlen('stream_5'))
r.xadd('stream_5', {'id': 10}, maxlen=5, approximate=False)
print(r.xlen('stream_5'))
r.xtrim('stream_5', maxlen=3, approximate=False)
print(r.xlen('stream_5'))
print(r.xrange('stream_5'))
