import datetime
def get_now_time():
    self.out_param = str(datetime.datetime.now())
def get_user_count():
    order_id = self.in_param
    sql = "select * from user_info where id = "+ order_id +""
    querys = db_manager.sqlserver().execute_query(sql)
    if(len(querys) >= 5):
        self.out_param = '业务办理失败，此用户在全国范围内办理号码已经超过了5个！'
    else:
        self.out_param = '初审通过，已进入人工审核阶段！'

get_now_time()
get_user_count()