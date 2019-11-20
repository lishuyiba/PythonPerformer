#.coding=utf-8
import adodbapi
class sqlserver():
    def __init__(self):
        self.out = ''
    def create_connection(self):
        provider = 'SQLOLEDB.1'
        host = '127.0.0.1'
        user = 'sa'
        pwd = 'sql'
        database = 'testdb'
        connection_string = 'Provider=%s;Data Source=%s;Initial Catalog=%s;User ID=%s;Password=%s;'%(provider, host, database, user, pwd)
        try:
            return adodbapi.connect(connection_string)
        except Exception as e:
            print e

    def execute_query(self,sqlText):
        conn = self.create_connection()
        crsr = conn.cursor()
        crsr.execute(sqlText)
        for row in crsr.fetchall():
            print(row)
        crsr.close()
        conn.close()

    def execute_update(self,sqlText):
        conn = create_connection(self)
        crsr = conn.cursor()
        crsr.execute(sqlText)
        conn.commit()