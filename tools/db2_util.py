# encoding: utf-8

"""
@author: suhp
@contact: peace_su@163.com
@software: PyCharm
@file: db2_util.py
@time: 2016/11/29 12:36
"""
import ibm_db_dbi,ibm_db,time,datetime,random
import config

# 创建db2连接
def connect_db2(dbname,ip,port,user,pw):
    '连接db2数据库，传入库名、ip、端口、用户名、密码即可'
    dsn = 'DRIVER={IBM DB2 ODBC DRIVER};DATABASE='+ dbname +';HOSTNAME='+ ip +';PORT='+ port + '; PROTOCOL=TCPIP;UID='+ user +';PWD='+ pw +';'

    conn = ibm_db.connect(dsn,'','')

    return conn

# 插入数据
def insert_data(conn,insert_sql):
    '插入数据'
    result = ibm_db.exec_immediate(conn,insert_sql)
    return result

def get_row(result):
    '获取查询结果中的行数据'
    row = ibm_db.fetch_assoc(result)
    return row

# 查询数据
def query_data(conn,query_sql):
    '查询数据'
    result = ibm_db.exec_immediate(conn,query_sql)
    # row = ibm_db.fetch_assoc(result)
    return result

def update_data(conn,update_sql):
    '更新数据'
    result = ibm_db.exec_immediate(conn,update_sql)
    return result

def delete_data(conn,delete_sql):
    '删除数据'
    result = ibm_db.exec_immediate(conn,delete_sql)
    return result

def close_db2(conn):
    '关闭数据库连接'
    ibm_db.close(conn)

class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    # pass
    now = time.strftime('%H%M%S')
    num1 = random.randint(0,1000)
    num2 = random.randint(0,100000000)

    # 连接数据库
    conn = connect_db2('webdb2','192.168.61.55','60000','ccweb','ccweb55')

    # conn = ibm_db.connect('DRIVER={IBM DB2 ODBC DRIVER};DATABASE=webdb2;HOSTNAME=192.168.61.55;PORT=60000; PROTOCOL=TCPIP;UID=ccweb;PWD=ccweb55;','','')
    # conn = ibm_db_dbi.connect('driver={IBM DB2 ODBC DRIVER };port=60000;protocol=tcpip;','ccweb','ccweb55','192.168.61.55','webdb2',{})

    # 建表
    # create = 'create table test1 (name1 char(8) not null primary key,depid smallint,pay bigint)'
    # result = ibm_db.exec_immediate(conn,create)
    # if result:
    #     print('建表成功！')
    # else:
    #     print('建表失败！')

    # 插入数据
    insert = "insert into test1(name1,depid,pay) values(%s,%d,%d)"%(now,num1,num2)
    # result = ibm_db.exec_immediate(conn,insert)
    result = insert_data(conn,insert)
    if result:
        print('插入数据成功！')
    else:
        print('插入数据失败！')


    # 查询
    select = 'select * from test1'
    # result = ibm_db.exec_immediate(conn,select)
    result = query_data(conn,select)
    row = ibm_db.fetch_assoc(result)
    print('----------------------')
    while row:
        print(row.get('NAME1') +'    '+ str(row.get('DEPID')) + '   ' +str(row.get('PAY')))
        row = ibm_db.fetch_assoc(result)

    close_db2(conn)