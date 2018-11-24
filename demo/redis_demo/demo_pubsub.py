# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 10:43:13
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
"""
发布publish/订阅subscirbe
"""
import time
from ..password import redis_passwd
from redis import Redis
r = Redis(host='localhost', port=6379, password=redis_passwd, db=0)
# ignore_subscribe_messages 订阅或取消 不会发送消息
p = r.pubsub(ignore_subscribe_messages=True)
# p.subscribe('my-first-channel', 'my-second-channel')
p.subscribe('cctv1')
msg_reciver = p.psubscribe('cctv*')
print(msg_reciver)
print(p.get_message())
# {'type': '', 'pattern': '', 'channel': '', 'data': ''}

# 取消订阅
r.publish('cctv1', 'ni hao ')
p.unsubscribe('cctv1')
p.punsubscribe('cctv*')


def my_handler(message):
    """
    消息处理函数
    """
    print(f"my handler: {message['data']}")


p.subscribe(**{"channel_1", my_handler})
r.publish('channel_1', 'channel_1 data')
message = p.get_message()  # my handler： channel_1 data
print(message)  # None, 消息已被my_handler处理


# 在事件循环中使用消息
while True:
    message = p.get_message()
    if message:
        pass
        # ...do something
    time.sleep(0.001)  # be nice to the system :

# 阻塞， 直到获取消息
for message in p.listen():
    # do something with the message
    pass

# 在独立的线程中运行
p.subscribe(**{'cctv1', my_handler})
thread = p.run_in_thread(sleep_time=0.001)
thread.stop()  # 结束
