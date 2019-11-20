import pymssql
def conn():
    connect = pymssql.connect('(local)', 'sa', '**********', 'test')
    if connect:
        print("connectioned!")
    return connect
if __name__ == '__main__':
    conn = conn()