# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: play_game.py
@time: 2016/12/21 16:26
"""
import random,time

def guess_number(count):
    # pass
    print('猜数字游戏现在开始！')
    # print('请输入1~100之间的整数，您有5次机会~猜对有奖哦~~~')
    target= random.randint(1,100)
    for i in range(count):
        guess_num = int(input('请输入1~100之间的整数，您共有'+str(count) +'次机会~开始第 '+ str(i+1) +' 次冒险之旅吧~~~~'))
        if target > guess_num:
            if i ==count -1 :
                print('机会用完了，拜拜！')
            else:
                print('很遗憾，没有猜对哦~~还有 ' + str(count - 1 - i) + ' 次机会，继续加油')
                print('偷偷告诉你，猜小了，不要告诉别人哦~')
                continue
        elif target < guess_num:
            if i ==count -1:
                print('很遗憾呐，没有机会了，充值继续吧~~~~')
            else:
                print('很遗憾，没有猜对哦~~还有 ' + str(count - 1 - i) + ' 次机会，继续加油')
                print('你个逗比！！！！猜大了~~')
                continue
        else:
            if i+1 ==1:
                print('OMG！第一次就猜对了，你开挂了吧！我要嫁给你~~~')
            elif i+1 == 2:
                print('我了个擦擦擦，这才第二次，牛逼！！！')
            elif i+1 == 3:
                print('厉害了，第三次就对了哦，可以的！')
            elif i+1 ==4:
                print('一般般了，都第四次了，送个熊抱给你吧！')
            elif i != count -1 :
                print('无所谓了，都多少次了才猜对，去死吧！！！！')
            else:
                print('好险，最后一次机会竟然猜对了，去买彩票吧！')
            break


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    count = 7
    guess_number(count)
    time.sleep(5)