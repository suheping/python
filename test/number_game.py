# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: number_game.py
@time: 2016/11/8 16:55
"""


def get_spec_num1():
    # get num1
    while 1:
        try:
            num1 = int(input('请输入第一个特殊数字（1~9）： '))
        except:
            print('输入有误！')
        else:
            break

    while 1:
        try:
            if num1 > 9:
                num1 = int(input('请重新输入第一个特殊数字（1~9）： '))
            elif num1 < 0:
                num1 = int(input('请重新输入第一个特殊数字（1~9）： '))
            else:
                break
        except:
            print('输入有误！！！')

    return num1

def get_spec_num2():
    # get num2
    while 1:
        try:
            num2 = int(input('请输入第二个特殊数字（1~9）： '))
        except:
             print('输入有误！')
        else:
            break

    while 1:
        try:
            if num2 > 9:
                num2 = int(input('请重新输入第二个特殊数字（1~9）： '))
            elif num2 < 0:
                num2 = int(input('请重新输入第二个特殊数字（1~9）： '))
            elif num2 == num1:
                num2 = int(input('不能与第一个数'+ str(num1) + '相同，请重新输入（0~9）： '))
            else:
                break
        except:
            print('输入有误！！！')

    return num2

def get_spec_num3():
    # get num3
    while 1:
        try:
            num3 = int(input('请输入第三个特殊数字（1~9）： '))
        except:
             print('输入有误！')
        else:
            break

    while 1:
        try:
            if num3 > 9:
                num3 = int(input('请重新输入第二个特殊数字（1~9）： '))
            elif num3 < 0:
                num3 = int(input('请重新输入第二个特殊数字（1~9）： '))
            elif num3 == num1 :
                num3 = int(input('不能与第一个数'+ str(num1) + '相同，请重新输入（0~9）： '))
            elif num3 == num2 :
                num3 = int(input('不能与第二个数'+ str(num2) + '相同，请重新输入（0~9）： '))
            else:
                break
        except:
            print('输入有误！！！')

    return num3

def print_res(num1,num2,num3):
    for i in range(100):
        # 取余数
        yu1 = i%num1
        yu2 = i%num2
        yu3 = i%num3
        # 按照优先级进行处理
        if str(num1) in str(i):
            # 优先级最高的：i中包含num1
            print('Fizz')
            continue
        else:
            # 优先级次之：同时是三个数的倍数
            if yu1 == 0 and yu2 == 0 and yu3 == 0 :
                print('FizzBuzzWhizz')
                continue
            else:
                # 优先级再次之：同时是两个数的倍数
                if yu1 == 0 and yu2 == 0 :
                    print('FizzBuzz')
                    continue
                elif yu1 == 0 and yu3 == 0 :
                    print('FizzWhizz')
                    continue
                elif yu2 == 0 and yu3 == 0 :
                    print('BuzzWhizz')
                    continue
                else:
                    # 优先级最末：只是一个数的倍数
                    if yu1 == 0 :
                        print('Fizz')
                        continue
                    elif yu2 == 0 :
                        print('Buzz')
                        continue
                    elif yu3 == 0 :
                        print('Whizz')
                        continue
                    else:
                        # 所有条件都不满足，直接打印
                        print(i)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    num1 = get_spec_num1()
    num2 = get_spec_num2()
    num3 = get_spec_num3()
    print_res(num1,num2,num3)








