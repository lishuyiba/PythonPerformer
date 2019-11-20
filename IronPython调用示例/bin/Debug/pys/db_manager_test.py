#.coding=utf-8

import db_manager
class performer():
    def __init__(self):
        self.out = ''
    def query_test(self):
        sql = "select * from user_info"
        querys = db_manager.sqlserver().execute_query(sql)
        for row in querys:
            print(row)

    def insert_test(self):
        sql = "insert into user_info(user_name,user_pwd) values('ssss','ssssbb')"
        db_manager.sqlserver().execute_update(sql)

    def delete_test(self):
        sql = "delete from user_info where id='4'"
        db_manager.sqlserver().execute_update(sql)

    def update_test(self):
        sql = "update user_info set user_name = 'aaaa' where user_name = '6666'"
        db_manager.sqlserver().execute_update(sql)

    def get_user_count(self):
        sql = "select * from user_info"
        querys = db_manager.sqlserver().execute_query(sql)
        if(len(querys) >= 5):
            self.out = '业务办理失败，此用户在全国范围内办理号码已经超过了5个！'
        else:
            self.out = '审核通过！'

# per = performer()
# per.insert_test()
# per.delete_test()
# per.update_test()
# per.query_test()

per = performer()
per.get_user_count()
print per.out