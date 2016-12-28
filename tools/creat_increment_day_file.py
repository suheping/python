# coding:utf-8
# Created by suhp on 2016/11/7.

'''
    生成按日期递增的参数文件
'''

import datetime
import time
fs = open('E://param//param_1.txt','w')
# now = datetime.datetime.now()
# oneday = datetime.timedelta(day=1)
# 将字符串 20150901 格式化为 YYYYmmdd 的日期格式
thatday = datetime.datetime.strptime( '20150901','%Y%m%d')

for i in range(100):
    # 向文件中写入如下数据：
    # thatday  第一个日期
    # thatday + 1 thatday的后一天
    fs.write(str((thatday + datetime.timedelta(days=i)).strftime('%Y%m%d')) + '\n')
    # fs.write('suheping_'+ str(i))
    # fs.write(' ')
    # fs.write('password_' + str(i) + '\n')
fs.close()
print('end')
