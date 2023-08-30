from pymysql import Connection

conn = Connection(
    host='localhost',  # 主机名
    port=3306,
    user="root",
    password="@Zz004662",  # 密码
)
#sql="drop table count "
#sql = "ALTER TABLE shouru MODIFY id INT AUTO_INCREMENT"
#sql = "create table count (data varchar(18),num float)
#sql = "ALTER TABLE my_table MODIFY column_name INT AUTO_INCREMENT PRIMARY KEY"
#
cursor = conn.cursor()
conn.select_db("sys")
sql = "ALTER TABLE xiaofei MODIFY id INT AUTO_INCREMENT PRIMARY KEY"
cursor.execute(sql)
conn.commit()
conn.close()