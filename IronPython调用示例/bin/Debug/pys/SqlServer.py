# coding=utf-8
import adodbapi

class MSSQL:
    def __init__(sel,host,user,pwd,db):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db
    def __GetConnect(self):
        print 'connection_string'
    def ExecuteQuery(self,sql):
        print sql
    def ExecNonQuery(self,sql):
        print sql
def main()
    mssql = MSSQL(host='127.0.0.1',user='sa',pwd='sql',db='testdb')
if __name__ == '__main__':
    main()