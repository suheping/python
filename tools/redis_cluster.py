# coding:utf-8
# Created by suhp on 2016/11/7.

from rediscluster import RedisCluster
import threading
import time


class connect_set(threading.Thread): #The timer class is derived from the class threading.Thread
    def __init__(self, num,):
        threading.Thread.__init__(self)
        self._run_num = num

    def run(self): #Overwrite run() method, put what you want the thread do here
        global count, mutex
        threadname = threading.currentThread().getName()
        startup_nodes = [{"host": "10.131.9.239", "port": "5001"}]
        rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)

        for x in range(0, int(self._run_num)):
            mutex.acquire()
            count = count + 1
            rkey = "name" + str(count)
            rvalue = "csdc" + str(count)
            mutex.release()
            # print(threadname, x, count)
            # # print("-------- get/set ---------")
            if not rc.set(rkey, rvalue):
                print('set ' + rkey + ' to cluster failed!!!')
                return -1
            print(rkey + ' 对应的value是  ' + rc.get(rkey))
            time.sleep(1)



if __name__ == '__main__':
    global count, mutex
    threads = []
    num = 3  # thread num
    count = 4  #iteration  num
    # 创建锁
    mutex = threading.Lock()
    # 创建线程对象
    for x in range(0, num):
        threads.append(connect_set(count))
    # 启动线程
    for t in threads:
        t.start()
    # 等待子线程结束
    for t in threads:
        t.join()





