
from gevent._semaphore import Semaphore
from locust import HttpLocust,TaskSet,events,task,HttpUser
 
all_locusts_spawned = Semaphore()
all_locusts_spawned.acquire()
 
 
class TestUserTask(TaskSet):
    @task()
    def job(self):
 
        print("进来了{}".format(self.user))
        data = self.user.myflag.get(0)
        is_wait = data['is_wait']
        flag = data['flag']
        print("flag={}".format(flag))
 
        if flag >= 19:
            is_wait = True
        print("is_wait={}".format(is_wait))
        if is_wait:
            flag = flag - 1
            if flag == 0:
                is_wait = False
            data = {"flag": flag, "is_wait": is_wait}
            self.user.myflag.put(data)
            all_locusts_spawned.release()
            print("123123123123123123")
        else:
            flag += 1
            data = {"flag": flag, "is_wait": is_wait}
            self.user.myflag.put(data)
            all_locusts_spawned.wait()
 
 
class TestUser(HttpUser):
    import queue
    myflag = queue.Queue()
    tasks = {TestUserTask: 1}
    min_wait = 3000
    max_wait = 5000
    host = 'http://www.baidu.com'
    data = {"flag": 0, "is_wait": False}
    myflag.put(data)
 
 
if __name__ == "__main__":
    import os
 
    os.system("locust -f demo_locust.py --headless -u 20 -r 1 ")