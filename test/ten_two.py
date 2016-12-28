# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: ten_two.py
@time: 2016/11/10 13:54
"""

import random

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    print(bin(666))
    print(int('11111',base=5))

    # -----------------------------------------------
    s = '123asd!ew#q'
    s1 = '1234567890'
    s2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    x = 0
    y = 0
    for i in s:
        if i in s1:
            x = x+1
        if i in s2:
            y = y+1
    print(x)
    print(y)

    # --------------------------------------------
    print('----------------------------------')
    a = 7
    b = 3
    res =0

    while True:
        if b> 0:
            t1 = 0
            for y in range(b+1):
                for i in range(y):
                    t1 =t1 + 10**i
                res = res + a * t1
                print(res)
                t1 =0
                if y ==b:
                    break
        else:
            print('0')
        break
    print(res)

    # ------------------------------------------------

    passwd = '124566734'
    nums = '1234567890'
    words = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums_zt = False
    words_zt =False

    if len(passwd) > 12:
        print('密码超长！！！')
    elif len(passwd)<6:
        print('密码过短！！！')
    else:
        for i in passwd:
            if i in nums:
                nums_zt = True
                continue
            elif i in words:
                words_zt = True
                continue
        if nums_zt and words_zt :
            print('密码符合强度要求1 ~~~~')
        if nums_zt or words_zt :
            print('密码符合强度要求2 ~~~~')

    # ----------------------------------------------
    print('----------------------------------------')

    x = [1,2,3,4,8,7,22,33,88]
    y = []
    for i in x :
        if i%2 ==0:
            y.append(i)
        else:
            y.append(i**2)
    x =y
    print(x)

    # -----------------------------------------------
    print('----------------------------------')

    a = [x for x in range(100)]
    b = random.randint(0,100)

    low =0
    high = len(a) - 1
    while True:
        mid = int((low + high)/2)
        if b > a[mid] :
            low = mid
        elif b < a[mid]:
            high = mid
        else:
            print(a[mid])
            break

    # ---------------------------------------------
    print('-----------------------------------')

    list1 = [1,2,4,6,2,3,5,7,8]
    res1 =[]
    for x in range(len(list1)):
        if x == 0:
            res1.append(list1[x])
        else:
            tmp = res1[-1] + list1[x]
            res1.append(tmp)
    print(res1)


#     -------------------------------------------
    print('----------------------------------')




