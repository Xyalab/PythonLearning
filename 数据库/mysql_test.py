
from pymysql import Connection
import pymysql

# conn = Connection(
#     host='10.211.55.4',
#     port=3306,
#     user='root',
#     password='mysql110',
# )

conn = pymysql.connect(host='10.211.55.4', port=3306, user='root', password='mysql110', db='learning')

print(conn.get_server_info())

conn.close()

# import urllib.request
#
# conn = urllib.request.urlopen("mysql://root:mysql110@10.211.55.4:3306?allowPublicKeyRetrieval=true&useSSL=true&verifyServerCertificate=true")
#
# print(conn.read())
# conn.close()
