# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: test.py
@time: 2016/12/15 18:19
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    fs = open('e:/test1.txt','r')
    # print(fs.readline())
    # s = fs.readline()
    str = ''
    while True:
        s = fs.readline()
        if s:
            str = str + s[:-1] + "','"
        else:
            break
    print(str)
    s1 = "'" + str[:-2]
    fs.close()
    fs1 = open('e:/test2.txt','w')
    fs1.write(s1)
    fs1.close()
    print('end')
