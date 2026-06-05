import pymysql


# 获取连接对象
conn = pymysql.connect(host="localhost",user="root",passwd="9999",database="ai0331",charset="utf8mb4")

# 用于操作数据的对象
cursor = conn.cursor()

# 编写SQL语句
sql = "select * from department"

# 执行SQL语句
cursor.execute(sql)

# 获取结果 打印
print(cursor.fetchall())


