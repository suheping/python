# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: investorANDuser_data.py
@time: 2016/12/22 11:02
"""


def prepare_sql(fs,start_num,range_num,head_str):
    # pass
    for i in range(range_num):
        userid = start_num + i
        print(userid)
        login_name = "'" + head_str + str('%09d' % (i + 1)) + "'"
        # print(login_name)
        # insert_sql_user1 = "insert into tbl_cc_user1 (user_id,login_name,password,status,ca_cert,valid_time,delete_time,can_ch_password,ca_cert_type,user_type) values (1010000001,'gdylcs000000001','96E79218965EB72C92A549DD5A330112',10,683,'2016-10-28 13:46:53.617',null,0,0,2);"
        insert_sql_user1 = "insert into tbl_cc_user (user_id,login_name,password,status,ca_cert,valid_time,delete_time,can_ch_password,ca_cert_type,user_type) values" \
                           " (%d,%s,'96E79218965EB72C92A549DD5A330112',10,683,'2016-10-28 13:46:53.617',null,0,0,1);" % (userid, login_name)
        insert_sql_investor1 = "insert into tbl_cc_investor (investor_id,name,investor_type,cert_no,cert_type,address,zip,mobile,telephone,participant_id,contact_name,fax,email) values " \
                               "(%d,'name',610,'certNo',111,'','','','',100000,'','','12345@126.com');" % userid
        fs.write(insert_sql_user1 + '\n')
        fs.write(insert_sql_investor1 + '\n')
    fs.close()


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    fs = open('e:/vote_data/investor_user2.sql','w')
    prepare_sql(fs,123001000000,4000000,'gdxshp')
