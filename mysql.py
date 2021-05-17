import pymysql


# 打开数据库连接
db = pymysql.Connect(host='192.168.0.104',
                               user='root',
                               passwd='123456',
                               port=3306,
                               db='mysql',
                               charset='utf8'
)
# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT * FROM `mysql`.`user` LIMIT 0,1000")

# 使用 fetchone() 方法获取一条数据
data = cursor.fetchall()

print("Database version : " + str(data))

# 关闭数据库连接
db.close()