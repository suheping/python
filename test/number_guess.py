# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: number_guess.py
@time: 2016/11/9 9:24
"""

import random

def get_guess_num():
    # get num1
    while 1:
        try:
            guess_num = int(input('请输入你认为正确的数字（0~100）： '))
        except:
            print('输入有误！')
        else:
            break
    return guess_num


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    target_num = random.randint(0,100)
    print('猜数字游戏开始~~~')
    guess_num = -1
    i = 0
    while True:
        guess_num = get_guess_num()
        if guess_num == target_num :
            break
        elif guess_num > target_num :
            print('猜大了了')
        else:
            print('猜小了')
        i = i +1
    print('恭喜你猜对了，共猜了 '+ str(i) + ' 次 ~')



