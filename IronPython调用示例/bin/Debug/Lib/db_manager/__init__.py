#.coding=utf-8

import adodbapi
class sqlserver():

    def __init__(self):
        provider = 'SQLOLEDB.1'
        host = '127.0.0.1'
        user = 'sa'
        pwd = 'sql'
        db_name = 'testdb'
        self.connection_string  = 'Provider=%s;Data Source=%s;Initial Catalog=%s;User ID=%s;Password=%s;' % (provider, host, db_name, user, pwd)

    def create_connection(self):
        try:
            return adodbapi.connect(self.connection_string)
        except Exception as e:
            print e

    def execute_query(self,sql):
        conn = self.create_connection()
        crsr = conn.cursor()
        crsr.execute(sql)
        querys = []
        for row in crsr.fetchall():
            querys.append(row)
        crsr.close()
        conn.close()
        return querys

    def execute_insert(self,sql):
        self.execute_sql(sql)

    def execute_delete(self,sql):
        self.execute_sql(sql)

    def execute_update(self,sql):
        self.execute_sql(sql)

    def execute_sql(self,sql):
        conn = self.create_connection()
        crsr = conn.cursor()
        crsr.execute(sql)
        conn.commit()
        crsr.close()
        conn.close()