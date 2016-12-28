# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: test_excel.py
@time: 2016/12/16 10:41
"""
import xlwt

def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    # for i in range(10):
    i =1
    id = i
    idcard = 1111111+i
    odid = 'a' + str(i)
    wbk = xlwt.Workbook()
    sheet1 = wbk.add_sheet('user_info',cell_overwrite_ok=True)
    sheet1.write(0,1,'test')
    wbk.save('e:/test1.xls')