# -*- coding: utf-8 -*-
# @Date    : 2018-11-21 10:53:07
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
"""
pipeline管道用于在一次请求中执行多个命令
"""
from redis import Redis, ConnectionPool, WatchError
from ..password import redis_passwd
r = Redis(host='localhost', port=6379, password=redis_passwd, db=0)
# ``transaction`` indicates whether all commands should be executed atomically
pipe = r.pipeline(transaction=True)
pipe.set('foo', 'bar')
pipe.set('name', 'jack')
pipe.lpush('l1', 'a')
# the EXECUTE call sends all buffered commands to the server, returning
# a list of responses, one for each command.
pipe.execute()


pipe.set('num', 2).rpush('l1', 'b').incr('num').execute()

# 使用piple管道实现 事务
with r.pipeline() as pipe:
    while True:
        try:
            # 监听某个键
            pipe.watch('num')
            # 监听之后，管道会立即进入执行状态，直到我们告知要将命令缓存起来
            current_value = pipe.get('num')
            next_value = int(current_value) + 1
            # 管道进行缓存模式，缓存输入的命令，事务开始
            pipe.multi()
            pipe.set('num', next_value)
            pipe.lpop('l1')
            # 执行缓存在pipe的事务
            pipe.execute()

            # 没有WatchError，事务就被原子性地执行了，退出
            break
        except WatchError:
            # 有其他客户端对监听的键进行了设置，事务失败，所有操作都不会执行
            # 事务重试
            continue
        finally:
            pipe.reset()


# 只有一个参数 Pipeline对象
def num_incr_l1_pop(pipe):
    current_value = pipe.get('num')
    next_value = int(current_value) + 1
    pipe.multi()
    pipe.set('num', next_value)
    pipe.lpop('l1')


# 使用 transaction 执行事务
r.transaction(num_incr_l1_pop, 'num')
