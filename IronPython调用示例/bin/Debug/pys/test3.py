# coding=utf-8

import adodbapi
import datetime

def create_connection():
    provider = 'SQLOLEDB.1'
    host = '127.0.0.1'
    user = 'sa'
    pwd = 'sql'
    database = 'testdb'
    conn_string = 'Provider=%s;Data Source=%s;Initial Catalog=%s;User ID=%s;Password=%s;' % (provider, host, database, user, pwd)
    try:
    	return adodbapi.connect(conn_string)
    except Exception as e:
    	print e 

#核查目标用户
def hcmbyh():
	sqlText = 'select * from user_info'
	conn = create_connection()
	crsr = conn.cursor()	
	crsr.execute(sqlText)
	flag = False
	for row in crsr.fetchall():
		if row.user_name == 'sa':
			flag = True
	if flag == True:
		print 'CZ'#存在
	else:
		print 'BCZ'#不存在
	crsr.close()
	conn.close()


#执行测试
hcmbyh()