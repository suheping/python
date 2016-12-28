# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: test_db2.py
@time: 2016/11/29 16:46
"""
from tools import db2_util
import time,datetime,threading

# 向tbl_cc_user1表中插入数据
def insert_user1(conn,start_num,range_num,head_str):
    # time1 = datetime.datetime.now()
    for i in range(range_num):
        userid = start_num + i
        print(userid)
        login_name = "'"+ head_str + str('%09d'%(i+1)) + "'"
        # print(login_name)
        # insert_sql_user1 = "insert into tbl_cc_user1 (user_id,login_name,password,status,ca_cert,valid_time,delete_time,can_ch_password,ca_cert_type,user_type) values (1010000001,'gdylcs000000001','96E79218965EB72C92A549DD5A330112',10,683,'2016-10-28 13:46:53.617',null,0,0,2);"
        insert_sql_user1 = "insert into tbl_cc_user (user_id,login_name,password,status,ca_cert,valid_time,delete_time,can_ch_password,ca_cert_type,user_type) values (%d,%s,'96E79218965EB72C92A549DD5A330112',10,683,'2016-10-28 13:46:53.617',null,0,0,1);"%(userid,login_name)
        result = db2_util.insert_data(conn,insert_sql_user1)
        # return result
    # time2 = datetime.datetime.now()
    # duration_user = time2 - time1
    # # db2_util.close_db2(conn)
    # print(duration_user)

# 向tbl_cc_investor1表中插入数据
def insert_investor1(conn,start_num,range_num):
    # time1 = datetime.datetime.now()
    # print(start_num)
    for i in range(range_num):
        investor_id = start_num + i
        # insert_sql_investor1 = "insert into tbl_cc_investor1 (investor_id,name,investor_type,cert_no,cert_type,address,zip,mobile,telephone,participant_id,contact_name,fax,email) values (1010000001,'name',610,'certNo',111,'','','','',100000,'','','12345@126.com');"
        insert_sql_investor1 = "insert into tbl_cc_investor (investor_id,name,investor_type,cert_no,cert_type,address,zip,mobile,telephone,participant_id,contact_name,fax,email) values (%d,'name',610,'certNo',111,'','','','',100000,'','','12345@126.com');" % investor_id
        # print(insert_sql_investor1)
        result = db2_util.insert_data(conn,insert_sql_investor1)
    # time2 = datetime.datetime.now()
    # duration_investor1 = time2 - time1
    # # db2_util.close_db2(conn)
    # print(duration_investor1)

# 向tbl_cc_investor_account1表中插入数据
def insert_investor_account1(conn):
    time1 = datetime.datetime.now()
    for i in range(100):
        id = 100000001 + i
        investor_id = 1010000001 + i
        account = "'" + 'A' + str(100000001 + i) + "'"
        # insert_sql_investor_account1 = "insert into tbl_cc_investor_account1 (id,investor_id,account,account_registration,account_agency_code,type) values (100000001,1010000001,'A100000001',750,null,350);"
        insert_sql_investor_account1 = "insert into tbl_cc_investor_account1 (id,investor_id,account,account_registration,account_agency_code,type) values (%d,%d,%s,750,null,350);"%(id,investor_id,account)
        result = db2_util.insert_data(conn,insert_sql_investor_account1)

    time2 = datetime.datetime.now()
    duration_investor_account1 = time2 - time1
    # db2_util.close_db2(conn)
    print(duration_investor_account1)

# 向tbl_cc_total_shareholder1表中插入数据
def insert_total_shareholder1(conn):
    time1 = datetime.datetime.now()
    for i in range(100):
        id = 1010000001 + i
        account = "'" + 'A' + str(100000001 + i) + "'"
        # insert_sql_total_shareholder1 = "insert into tbl_cc_total_shareholder1(id, meeting_id, account, ab_flag, account_registration, shareholder_name, cert_no, hold_volume, stock_chrc, account_type, ymth, stock_type) values (1010000001,105765,'A100000001',330,750,'shareholderName','certNo',1000, 310,10,'',10);"
        insert_sql_total_shareholder1 = "insert into tbl_cc_total_shareholder1(id, meeting_id, account, ab_flag, account_registration, shareholder_name, cert_no, hold_volume, stock_chrc, account_type, ymth, stock_type) values (%d,105765,%s,330,750,'shareholderName','certNo',1000, 310,10,'',10);" % (
        id, account)
        result = db2_util.insert_data(conn, insert_sql_total_shareholder1)

    time2 = datetime.datetime.now()
    duration_total_shareholder1 = time2 - time1
    # db2_util.close_db2(conn)
    print(duration_total_shareholder1)


def insert_investor_user(conn,start_num,range_num,head_str):
    '向tbl_n_invertor_user表中插入数据'
    for i in range(range_num):
        investor_id = start_num +i
        login_name = "'" + head_str + str('%09d' % (i + 1)) + "'"
        insert_investor_user = "insert into CCWEB.TBL_N_INVESTOR_USER (INVESTOR_ID, LOGIN_NAME, PASSWORD, STATUS, CA_CERT, VALID_TIME, DELETE_TIME, CAN_CH_PASSWORD, CA_CERT_TYPE, NAME, INVESTOR_TYPE, CERT_NO, CERT_TYPE, ADDRESS, ZIP, MOBILE, TELEPHONE, PARTICIPANT_ID, CONTACT_NAME, FAX, EMAIL, YMTH) values" \
                               " (%d, %s, '96E79218965EB72C92A549DD5A330112', 10, 683, '2008-03-24 17:33:29', null, 1, 0, 'name', 610, 'cert_no', 111, 'addr', 'zip', null, '12312312312', 1, null, null, null, null);"%(investor_id,login_name)
        result = db2_util.insert_data(conn,insert_investor_user)



class Main():
    def __init__(self):
        pass


if __name__ == '__main__':

    # query_sql = 'select * from CCWEB.TBL_CC_USER1;'
    conn = db2_util.connect_db2('webdb2','10.131.6.8','60000','ccweb','123456')
    # result = db2_util.query_data(conn,query_sql)
    start_num = 2000000081
    range_num = 800000
    insert_investor_user(conn,start_num,range_num,'gdyshp')
    # insert_user1(conn,start_num,range_num,'gdshp')
    # insert_investor1(conn,start_num,range_num)
    # insert_investor_account1(conn)
    # insert_total_shareholder1(conn)

    # threads = []
    # t1 = threading.Thread(target=insert_user1, args=(conn, 1010000001, 100000, 'gdylca'))
    # t2 = threading.Thread(target=insert_user1, args=(conn, 1020000001, 100000, 'gdylcb'))
    # t3 = threading.Thread(target=insert_user1, args=(conn, 1030000001, 100000, 'gdylcc'))
    # t4 = threading.Thread(target=insert_user1, args=(conn, 1040000001, 100000, 'gdylcd'))
    # t5 = threading.Thread(target=insert_user1, args=(conn, 1050000001, 100000, 'gdylce'))
    # threads.append(t1)
    # threads.append(t2)
    # threads.append(t3)
    # threads.append(t4)
    # threads.append(t5)
    #
    #
    #
    #
    # start_time = datetime.datetime.now()
    #
    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    #
    # for t in threads:
    #     t.join()
    #
    # end_time = datetime.datetime.now()
    # print('数据插入完成，共消耗 %s'%(end_time-start_time))
    db2_util.close_db2(conn)


