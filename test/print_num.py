# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: print_num.py
@time: 2016/11/9 16:21
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    list1 =[]
    for i in range(2000,3000):
        if i%7 ==0 and i%5 != 0:
            list1.append(i)
    fs = open('e:/param/print_num.txt','w')
    for x in list1:
        fs.write(str(x) + ',')
    fs.close()
    fs = open('e:/param/print_num.txt','r')
    print(fs.readline()[:-1])



