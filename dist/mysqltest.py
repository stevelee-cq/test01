print("进入了测试文件02")
from pymysql import Connection
print("进入了测试文件03")
#下一步这里的两个变量要等另外一个模块执行过后才能得到结果
from tkinter02 import name_str, xiaofei_num

print("正式进入了测试文件，tkinter02包及变量被成功导入！")
conn = Connection(
    host='localhost',  # 主机名
    port=3306,
    user="root",
    password="@Zz004662",  # 密码
)
#测试是否监测到更改
cursor = conn.cursor()
conn.select_db("sys")
try:
    conn.select_db("sys")
    print("select_db 执行成功")
except Exception as e:
    print("select_db 执行失败:", str(e))
print("数据库连接成功")
i=1
print(f"i,name_str, xiaofei_num的内容分别是:{i,name_str,xiaofei_num}")
sql = "INSERT INTO xiaofei (name, num) VALUES (%s, %s)"
params = (name_str, xiaofei_num)
print(f"第二次输出：i,name_str, xiaofei_num的内容分别是:{i,name_str,xiaofei_num}")
cursor.execute(sql, params)


print(f"第三次次输出：name_str, xiaofei_num的内容分别是:{name_str,xiaofei_num}")
print("读取到了")
#print(f"读取到了：{name_str}")
conn.commit()
conn.close()