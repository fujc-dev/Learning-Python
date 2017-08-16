import pymysql
import calendar

# 打开数据库连接
db = pymysql.connect('localhost', 'root', 'ailsabe@126.com', 'TESTDB')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

cal = calendar.month(2016, 1)
print("以下输出2016年1月份的日历:")
print(cal)

L = list(range(100))
print(L)
print(L[:])
print(L[0:10])  # 取索引0-索引10之间的数字(索引从0开始可以省略为L[:10])
print(L[-10:])  # 取倒数索引后10个数字
print(L[10:20:2])  # 取索引10-索引20之间的数，每隔2个取一个
