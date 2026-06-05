import pymysql


# 获取连接对象
conn = pymysql.connect(host="localhost",user="root",passwd="9999",database="ai0331",charset="utf8mb4")

# 用于操作数据的对象
cursor = conn.cursor()

# 编写SQL语句
sql = "update department set depname=%s where depid=%s"

cursor.execute(sql,('销售1部',1))

conn.commit()




