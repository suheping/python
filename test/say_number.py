# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: say_number.py
@time: 2016/11/9 9:58
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':

    n = int(input('请输入总人数： '))
    m = int(input('请输入间隔人数： '))
    k = int(input('请输入从第几个开始报数： '))

    list1 =[]
    for i in range(1,n+1):
        list1.append(i)
        print(list1)

    while True:
        if len(list1) == 1 :
            break
        else:
            del_num_index_tmp = (m+k)% len(list1)
            # print('拉出去枪毙的为： '+ str(del_num))
            print('拉出去枪毙的为： '+ str(list1[del_num_index_tmp]))
            list1.remove(list1[del_num_index_tmp])
            print(list1)
            k = del_num_index_tmp

    print('幸存者为： '+ str(list1.pop(0)))
