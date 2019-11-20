#.coding=utf-8

import db_manager

class performer(object):

    def __init__(self,in_param):
        self.out_param = ''
        self.in_param = in_param

    def run(self):



        import datetime

        def a():
            self.out_param = str(datetime.datetime.now())
        def get_user_count():
            order_id = self.in_param
            sql = "select * from user_info where id = "+ order_id +""
            querys = db_manager.sqlserver().execute_query(sql)
            for x in querys:
                print x
            if(len(querys) >= 5):
                self.out_param = '业务办理失败，此用户在全国范围内办理号码已经超过了5个！'
            else:
                self.out_param = '审核通过！'
        a()
        get_user_count()

# def start(in_param):
#     per = performer(in_param)
#     per.run()
#     print per.out



# per = performer('1005')
# per.run()
# print per.out