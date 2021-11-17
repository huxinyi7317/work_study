import queue

q = queue.Queue(100) # 调用构造函数，初始化一个大小为3的队列
i = 1
status = False
while not status:
    # 写入一个队列
    q.put(i, block=True, timeout=5)
    i +=1
    # 读取一个队列
    q.task_done()
    print(q.empty()) # 判断队列是否为空，也就是队列中是否有数据

    # 入队，在队列尾增加数据， block参数，可以是True和False 意思是如果队列已经满了则阻塞在这里，

    # timeout 参数 是指超时时间，如果被阻塞了那最多阻塞的时间，如果时间超过了则报错。


    print(q.full())
    status = q.full()
     # 判断队列是否满了，这里我们队列初始化的大小为3

    print(q.qsize()) 
    # 获取队列当前数据的个数

    # block参数的功能是 如果这个队列为空则阻塞，

    # timeout和上面一样，如果阻塞超过了这个时间就报错，如果想一只等待这就传递None

q.join()
print('已阻塞满了100个线程')