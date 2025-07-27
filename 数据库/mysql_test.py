
from pymysql import Connection
import pymysql

# conn = Connection(
#     host='10.211.55.4',
#     port=3306,
#     user='root',
#     password='mysql110',
# )

conn = pymysql.connect(host='10.211.55.4', port=3306, user='root', passwd='mysql110', db='learning', autocommit=True, charset='utf8')

print(conn.get_server_info())

cursor = conn.cursor()
cursor.execute('select * from student')

res = cursor.fetchall()

print(res)




cursor.execute("insert into student values('10002', '李四', 20, '女', '河南省南阳市', '二年级')")



# conn.commit()   # 数据库连接时设置自动提交则不需要commit




conn.close()


