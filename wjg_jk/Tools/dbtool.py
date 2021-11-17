import pymysql
class Dbtools():
    def __init__(self):
        
        self.db = {
        'host':'159.75.17.184',
        'port':3306,
        'user':'root',
        'password':'a123456.',
        'db':'wq_com',
        'charset':'utf8'} 

    def dbchaxun(self,sql,more=False):
        # 查询数据
        conn = pymysql.connect(host=self.db['host'],port=self.db['port'],db=db.db['db'],user=self.db['user'],password=db.db['password'],charset=self.db['charset'])
        yb = conn.cursor()
        yb.execute(sql)
        if more:
            one = yb.fetchall()
        else:
            one =yb.fetchone()
        conn.close()
        return one
    def dbconnect(self,sql):
        conn = pymysql.connect(host=self.db['host'],port=self.db['port'],db=db.db['db'],user=self.db['user'],password=self.db['db'],charset=self.db['charset'])
        yb = conn.cursor()
        yb.execute(sql)
        conn.commit()

    def more_inster(self,sql,data=None,more=False):
        # more参数=False，为单条数据插入，直接执行sql
        if more:
            # 批量插入数据
            # data可以列表和元祖，没有一组数据为一个元祖放在data列表或元祖中，多组插入数据
            conn = pymysql.connect(host=self.db['host'],port=self.db['port'],db=db.db['db'],user=self.db['user'],password=self.db['db'],charset=self.db['charset'])        
            yb=conn.cursor()
            try:
                # 执行sql语句
                yb.executemany(sql,data)    #使用executemany做批量处理
                conn.commit()   #把修改提交到数据库
            except Exception as e :
                conn.rollback()
        else:
            yb.execute(sql)
           conn.commit()
        yb.close()
        conn.close()
if __name__ == "__main__":
    db = Dbtools()
    sql = "SELECT m.login_name FROM backend_member m WHERE m.`status`='正常' limit 5;"#查询可用账号
    data = list(db.dbchaxun(sql=sql))

    print(data)
