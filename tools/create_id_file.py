# coding:utf-8
# Created by suhp on 2016/11/7.

'''
将  一行只有一个字段的数据文件  转换为  一行有n个字段的数据文件
该脚本 用于转换  身份证数据文件
'''

# 原始文件
file1 = open('E:/test_data_20160422/test_data_queryblockch/blockch_id_1.txt','r')
# 目标文件
file2 = open('E:/test_data_20160422/test_data_queryblockch/blockch_id_500.txt','w')
# 计数i
i = 0
t = ''
# 一行参数的个数
x = 500

while True :
    # 取一行数据
    line = file1.readline()
    # 如果这行数据存在，就执行下边的操作
    if line :
        # 判断line的长度，如果符合身份证长度标准（包含换行符），执行下边的操作
        if len(line)==16 or len(line)==19:
            # 去掉换行符后，连接字符串","
            t = t + line[:-1] + '","'
            # 计数+1
            i = i+1
            # 如果达到x的整数倍，执行下边的操作
            if i % x == 0 :
                # 去掉t最后的连接字符串","后拼接换行符，写入file2中
                 t = t[:-3] + '\n'
                 file2.write(t)
                # 将t置为空
                 t = ''
    # 没有取到数据----到了文件尾，结束while
    else:
        break
# 保存并关闭file1、file2
file1.close()
file2.close()

