# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: db2_loadtest.py
@time: 2016/12/23 8:47
"""
from tools import db2_util
import threading,time,datetime


def get_props(fs,curr_num):
    # pass
    # fs = open('e:/select_data.txt','r')
    # 将参数文件的所有数据存入fs_ls列表中
    fs_ls = fs.readlines()
    fs_ls_len = len(fs_ls)
    n = int(fs_ls_len/curr_num)
    # 将参数按照并发用户数等分，存入fs_l2中
    fs_l2 = [fs_ls[i:i+ n] for i in range(0,fs_ls_len,n)]
    return fs_l2



class select_data(threading.Thread): #The timer class is derived from the class threading.Thread
    def __init__(self,conn, fs_l2, curr_no,iteration_num):
        threading.Thread.__init__(self)
        self.conn = conn
        self.fs_l2 = fs_l2
        self.curr_no = curr_no
        self.iteration_num = iteration_num

    def run(self):
        # pass
        # 当前进程的参数列表
        props = fs_l2[self.curr_no]
        n = len(props)
        # 当前循环的参数下标
        index = 0
        # 循环执行
        # 第几次循环
        iteration_no = 1
        while True:
            # 如果当前循环次数大于设置的总循环次数，结束循环；否则，去执行
            if iteration_no > iteration_num:
                break
            else:
                # 如果当前循环次数大于参数个数，下标置为0；否则，去执行
                if iteration_no > n:
                    index = 0
                else:
                    # 执行部分，执行查询，执行完成后，下标+1，循环次数+1
                    login_name = "'" + props[index][:-1] + "'"
                    # print(login_name)
                    sql = "select * from CCWEB.TBL_N_INVESTOR_USER where TBL_N_INVESTOR_USER.LOGIN_NAME = %s and TBL_N_INVESTOR_USER.PASSWORD = '96E79218965EB72C92A549DD5A330112';" % login_name
                    # sql = "select * from CCWEB.TBL_CC_USER where TBL_CC_USER.LOGIN_NAME = %s and TBL_CC_USER.PASSWORD = '96E79218965EB72C92A549DD5A330112';" % login_name
                    time1 = datetime.datetime.now()
                    db2_util.query_data(conn, sql)
                    time2 = datetime.datetime.now()
                    duration = time2 - time1
                    print('--'+ str(self.curr_no) +'------'+ str(iteration_no) + '--------'+ sql + '------' + str(duration))
                    index = index + 1
                    iteration_no = iteration_no + 1
                    # time.sleep(5)


if __name__ == '__main__':
    # pass
    global iteration_num, mutex
    print("线程号--循环次数--sql")
    # 并发数
    curr_num = 10
    # 循环次数
    iteration_num = 10
    conn = db2_util.connect_db2('webdb2','10.131.6.8','60000','ccweb','123456')
    fs = open('e:/select_data.txt','r')
    fs_l2 = get_props(fs,curr_num)
    # print(fs_l2[1])
    fs.close()

    threads = []
    # 创建锁
    mutex = threading.Lock()
    # 创建线程对象
    for i in range(curr_num):
        threads.append(select_data(conn,fs_l2,i,iteration_num))
    # 启动线程
    print(threads)
    start_time = datetime.datetime.now()
    for t in threads:
        t.start()
    # 等待子线程结束
    for t in threads:
        t.join()
    end_time = datetime.datetime.now()
    count = curr_num * iteration_num
    total_duration_ms = (end_time-start_time).microseconds/1000
    # total_duration_ms= int(time.mktime(total_duration.timetuple()) * 1000)
    avg_time_ms = total_duration_ms/(curr_num*iteration_num)
    print('平均响应时间为 ' + str(avg_time_ms))
    db2_util.close_db2(conn)