import pymysql
from itertools import chain

def get_information(sql,host, db,condition=None):
    # 链接数据库
    conn = pymysql.connect(host=host,
                 user='root',
                 passwd='epochn',
                 db=db,
                 port=13306,
                 charset='utf8')
    # 获取游标
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 提交数据库执行
    # conn.commit()
    # 使用 fetchall() 方法获取数据对象，可以得到表中所有的信息
    if condition:
      resultlist=cur.fetchone()
    else:
      data1 = cur.fetchall()
      resultlist = list(chain.from_iterable(data1))
    # print(f"数据对象:{resultlist}")
    cur.close()
    conn.close()
    return resultlist

if __name__ == '__main__':

  host = '192.168.188.12'
  db = 'epodb_20201028'
  sql = f"select phone  from backend_member where `status`='正常' GROUP BY phone having count(phone)>1"
  try:
    a=get_information(sql,host,db)
    b=tuple(a)
    sql = f"select id,phone from backend_member WHERE phone in {b}"
    print(sql)
    b=get_information(sql,host,db)
    print(b)
  except:
    pass