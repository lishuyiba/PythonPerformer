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

def execute_query(sqlText):
	conn = create_connection()
	crsr = conn.cursor()	
	crsr.execute(sqlText)
	for row in crsr.fetchall():
	    print(row)
	crsr.close()
	conn.close()

def execute_update(sqlText):
	conn = create_connection()
	crsr = conn.cursor()	
	crsr.execute(sqlText)
	conn.commit()

def execute_query_test():
	sqlText = "select * from user_info"
	execute_query(sqlText)

def execute_update_test():
	sqlText = "update user_info set user_name = 'sasddddd'"
	execute_update(sqlText)

print '------------------------ '+str(datetime.datetime.now())+' 以下是Python执行日志信息------------------------'

execute_update_test()
execute_query_test()

print '执行完成了'