# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: dofile.py
@time: 2016/11/22 13:22
"""


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    fs  = open('e:\\\out.txt','r')
    fs1 =  open('e:\\\in.txt','w')
    while True:
        line = fs.readline()
        if line:
            s = line[1:-2]
            print(s)
            fs1.write(s + '\n')
        else:
            break
    fs.close()
    fs1.close()
