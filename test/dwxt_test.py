# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: dwxt_test.py
@time: 2016/12/16 9:22
"""
from tools import db2_util
import xlwt,xlrd

def create_user(conn):
    # pass
    select_sql = "select TBL_DW_USER.OAID,TBL_DW_USER.ID,TBL_DW_USER.DEPT from CCWEB.TBL_DW_USER where TBL_DW_USER.COMPANY = '1000'and TBL_DW_USER.OAID is not null fetch first 100 rows only;"
    # update_sql = "update CCWEB.TBL_DW_USER set TBL_DW_USER.BRANCH = 10068 , TBL_DW_USER.ISPARTY = '1'  where TBL_DW_USER.OAID = 'lnma';"
    idcard = 771111111111111
    result = db2_util.query_data(conn,select_sql)
    row = db2_util.get_row(result)
    wbk = xlwt.Workbook()
    sheet1 = wbk.add_sheet('user_info',cell_overwrite_ok=True)
    x = 0
    while row:
        oaid = row.get('OAID')
        id = row.get('ID')
        dept = row.get('DEPT')
        update_sql = "update CCWEB.TBL_DW_USER set TBL_DW_USER.BRANCH = 1010 , TBL_DW_USER.ISPARTY = '1',TBL_DW_USER.IDCARD = '" + str(idcard) + "' where TBL_DW_USER.OAID = '" + oaid + "';"
        db2_util.update_data(conn, update_sql)
        delete_sql_1 = "delete from CCWEB.TBL_DW_USER_ROLE where TBL_DW_USER_ROLE.USERID = " + str(id) + ";"
        db2_util.delete_data(conn,delete_sql_1)
        insert_sql_1 = "insert into CCWEB.TBL_DW_USER_ROLE values (default," + str(id) + ",1050);"
        db2_util.insert_data(conn,insert_sql_1)
        delete_sql_2 = "delete from CCWEB.TBL_DW_PARTY_INFO where TBL_DW_PARTY_INFO.USERID = " + str(id) + ";"
        db2_util.delete_data(conn,delete_sql_2)
        insert_sql_2 = "insert into CCWEB.TBL_DW_PARTY_INFO values (default," + str(id) + ",null,null,null,'正常党费','" + str(idcard) + "','1');"
        db2_util.insert_data(conn,insert_sql_2)
        row = db2_util.get_row(result)
        print(id,oaid,idcard)
        sheet1.write(x,0,id)
        sheet1.write(x,1,oaid)
        sheet1.write(x,2,"'"+ str(idcard))
        sheet1.write(x,3,dept)
        idcard = idcard + 1
        x = x + 1

    # db2_util.update_data(conn,update_sql)
    wbk.save('e:/user_info2.xls')
    # db2_util.close_db2(conn)

def add_fee(conn):
    wkb = xlrd.open_workbook('e:/user_info2.xls')
    sheet1 = wkb.sheet_by_index(0)
    rows = sheet1.nrows
    cols = sheet1.ncols
    # print(rows,cols)
    insert_header = ""
    for i in range(rows):
        user_id = int(sheet1.cell(i, 0).value)
        # print(user_id)
        oaid = sheet1.cell(i, 1).value
        print(oaid)
        account = sheet1.cell(i, 2).value[1:]
        # print(account)
        dept = int(sheet1.cell(i, 3).value)
        # print(dept)
        # 取得期数id
        select_sid = "select TBL_DW_FEES_HEADER.ID from CCWEB.TBL_DW_FEES_HEADER"
        res = db2_util.query_data(conn, select_sid)
        row = db2_util.get_row(res)
        while row:
            sid = row.get('ID')
            # print(sid)
            delete_exit = "delete from CCWEB.TBL_DW_FEES_ITEM  where TBL_DW_FEES_ITEM.SID =" + str(
                sid) + " and TBL_DW_FEES_ITEM.USERID = " + str(user_id) + ";"
            db2_util.delete_data(conn, delete_exit)
            insert_fee = "insert into CCWEB.TBL_DW_FEES_ITEM values(default," + str(sid) + "," + str(
                user_id) + "," + str(dept) + ",1010,0.00,0.00,'" + account + "',0.00,null,'1');"
            print(insert_fee)
            db2_util.insert_data(conn, insert_fee)
            row = db2_util.get_row(res)


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    conn = db2_util.connect_db2('dwxtdb3', '192.168.61.55', '60000', 'ccweb', 'ccweb55')
    create_user(conn)
    add_fee(conn)
    db2_util.close_db2(conn)