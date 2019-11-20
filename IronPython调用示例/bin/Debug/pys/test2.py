#coding=utf-8

import adodbapi

class DBTestor:
	def __init__(self):
		self.conn = None
	def __del__(self):
		self.conn.close()
    def connectDB(self, connectString):
		self.conn = adodbapi.connect(connectString) 
	def closeDB(self):
		self.conn.close()
	def testQuery(self):
		cursor = self.conn.cursor()
		sql = "select * from user_info"
		cursor.execute(sql)
		print cursor.fetchall()
		cursor.close() 
		
if __name__ == "__main__":
	test = DBTestor()
	test.connectDB("Provider=SQLOLEDB.1;Persist Security Info=True;Password=sql;User ID=sa;Initial Catalog=testdb;Data Source=127.0.0.1")
    test.testQuery()