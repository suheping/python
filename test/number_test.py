# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: number_test.py
@time: 2016/11/8 14:58
"""
import random

def create_file1(filename,lines):
    fs = open(filename,'w')

    for i in range(lines):
        # strs = 5000000000 + i
        strs = int(random.uniform(1000000000,5000000000))
        fs.write(str(strs)+'\n')
    fs.close()


def create_file2(filename,lines,lenth):
    fs2 = open(filename,'w')
    s1 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for x in range(lines):
        s2 = ''
        for y in range(lenth):
            index = int(random.uniform(0,52))
            strs = s1[index]
            s2 = s2 + strs
        fs2.write(s2 + '\n')
    fs2.close()

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # x =9
    # lenth = len(str(x))
    # print(lenth)
    # create_file1('e:/param/test2.txt',10000)
    # print('一码通帐号为%10d'%x)
    create_file2('e:/param/test4.txt',100000,15)

