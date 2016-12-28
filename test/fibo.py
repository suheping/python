# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: fibo.py
@time: 2016/11/14 14:19
"""


def func(x):
    if x == 0:
        s = 0
    elif x ==1:
        s = 1
    else:
        s = func(x-2)+func(x-1)
    return s

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    x = int(input('请输入一个正整数： '))
    print(func(x))
