import pymysql
class Dbtools():
    def __init__(self):
        
        self.db = {'host':'192.168.188.12','port':13306,'user':'root','password':'epochn','db':'epodb_20201110','charset':'utf8'} 

    def dbchaxun(self,sql,more=False):
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

    
if __name__ == "__main__":
    db = Dbtools()
    sql = "SELECT m.login_name FROM backend_member m WHERE m.`status`='正常' limit 5;"#查询可用账号
    data = list(db.dbchaxun(sql=sql))

    print(data)

# 批量导入数据
# cursor=conn.cursor()
# # 写sql语句
# sql="insert into userinfo(name,pwd) values(%s,%s);"
# user1='dww1'
# pwd1='123456'
# user2='dww2'
# pwd2='123456'
#  把所有要插入的信息保存在元祖或列表中
# data=((user1,pwd1),(user2,pwd2))
# try:
#     # 执行sql语句
#     cursor.executemany(sql,data)    #使用executemany做批量处理
#     conn.commit()   #把修改提交到数据库
# except Exception as e :
#     conn.rollback()
# cursor.close()
# conn.close()