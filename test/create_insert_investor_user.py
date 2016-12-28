# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: create_insert_investor_user.py
@time: 2016/12/21 16:12
"""


def create_insert_investor_user(fs,start_num,range_num,head_str):
    # pass
    for i in range(range_num):
        investor_id = start_num +i
        login_name = "'" + head_str + str('%09d' % (i + 1)) + "'"
        insert_investor_user = "insert into CCWEB.TBL_N_INVESTOR_USER (INVESTOR_ID, LOGIN_NAME, PASSWORD, STATUS, CA_CERT, VALID_TIME, DELETE_TIME, CAN_CH_PASSWORD, CA_CERT_TYPE, NAME, INVESTOR_TYPE, CERT_NO, CERT_TYPE, ADDRESS, ZIP, MOBILE, TELEPHONE, PARTICIPANT_ID, CONTACT_NAME, FAX, EMAIL, YMTH) values" \
                               " (%d, %s, '96E79218965EB72C92A549DD5A330112', 10, 683, '2008-03-24 17:33:29', null, 1, 0, 'name', 610, 'cert_no', 111, 'addr', 'zip', null, '12312312312', 1, null, null, null, null);"%(investor_id,login_name)
        fs.write(insert_investor_user + '\n')
    fs.close()



class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    fs = open('e:/insert_investor_user.sql', 'w')
    create_insert_investor_user(fs,10000000,10,'gdjkyu')