import pymysql
# # pymysql.connect(host="127.0.0.1")
# db = pymysql.connect(host="localhost", user="root", password="123456",port=3306)
# # 登录mysql
# cursor = db.cursor() # 创建游标
# cursor.execute("create database testmysqlstudy") # 存放命令
# db.close()
# print("创建数据库完成，结束任务")
# db = pymysql.connect(host="127.0.0.1", user="root", password="123456",
#                      port=3306)
# # db = pymysql.connect(host="localhost", user="root",
# # password="123456",port=3306) # 登录mysql
# cursor = db.cursor() # 创建游标
# cursor.execute("drop database testmysqlstudy") # 存放命令
# db.close()
# print("创建数据库完成，结束任务")
# db = pymysql.connect(host="localhost", user="root", password="123456",
#                      port=3306, db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# cursor.execute("create table c_tab(id int auto_increment, name varchar(20), age int ,primary key(id))")
# db.close()
# print("创建数据表成功")
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# cursor.execute("insert into `c_tab`(id, name, age) values(1, '胡耀明', 22)") # 这里
# # 不是执行代码吗,将insert语句执行到mysql数据库
# db.commit() # 表示确认，直接写入表中。
# db.close() # 关闭和数据库的连接
# print("新增数据库数据信息")
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# try:
#     cursor.execute("insert into `c_tab`(id, name, age) values(4, '张三', 18)") #
# # 这里不是执行代码吗,将insert语句执行到mysql数据库
#     cursor.execute("insert into `c_tab`(id, name, age) values(5, '张四', 18)") #
# # 这里不是执行代码吗,将insert语句执行到mysql数据库
#     i = 5/0
#     db.commit() # 表示确认，直接写入表中。
#     print("确认提交数据")
# except:
#     db.rollback() # 回滚,就是将本次的事务（指的可以是一条或多条语句）取消，不进行操作。
#     print("进行了回滚操作")
# db.close() # 关闭和数据库的连接
# print("新增数据库数据信息")
# db = pymysql.connect(host="localhost", user="root", password="123456",
#                      db="testmysqlstudy")
# cursor = db.cursor()
# cursor.execute("select * from c_tab")
# print(cursor.rowcount) # 数量为5条。
# one = cursor.fetchone() # 查询一条与数据
# print(cursor.rownumber)
# alist = cursor.fetchall() # 查询所有的数据
# print(cursor.rownumber) # 位于第几条
# print(one)
# print(alist)
# db.close()
# db = pymysql.connect(host="localhost", user='root', password="123456", db =
# "testmysqlstudy")
# cursor = db.cursor()
# cursor.execute("delete from c_tab where id = 3")
# db.commit()
# db.close()
# print("删除成功")
# db = pymysql.connect(host="localhost", user='root', password="123456", db =
# "testmysqlstudy")
# cursor = db.cursor()
# cursor.execute("update c_tab set name='胡耀明' where id = 1")
# db.commit()
# db.close()
# print("更新成功")
# cid = 2
# name = "'王杰欣'"
# age = 20
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# sql = 'insert into `c_tab`(id, `name`, age) values({cid}, {name},{age})'.format(cid = cid, name = name, age = age)
# cursor.execute(sql) # 这里不是执行代码吗,将insert语句执行到mysql数据库
# db.commit() # 表示确认，直接写入表中。
# # db.rollback() # 回滚
# db.close() # 关闭和数据库的连接
# print("新增数据库数据信息")
# cid = 3
# name = "郭美娟"
# age = 23
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# sql = 'insert into `c_tab`(id, `name`, age) values(%s, %s, %s)'
# cursor.execute(sql,(cid, name, age)) # 通过位置进行对应数据，同时执行sql语句
# db.commit() # 表示确认，直接写入表中。
# # db.rollback() # 回滚
# db.close() # 关闭和数据库的连接
# print("新增数据库数据信息")
# cid = 4
# name = "尹银英"
# age = 22
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# sql = 'insert into `c_tab`(id, `name`, age) values('+str(cid)+', "'+name+'",'+str(age)+')'
# cursor.execute(sql) # 通过位置进行对应数据，同时执行sql语句
# db.commit()  # 表示确认，直接写入表中。 'insert into `c_tab`(id, `name`, age)
# # values(9, 武人, 18)'
# # db.rollback() # 回滚
# db.close() # 关闭和数据库的连接
# print("新增数据库数据信息")
# 动态的保存一个字典数据。
# adict = {
#     "id":7,
#     "name":"肖舒",
#     "age":22
# }
# keys = ",".join(adict.keys())
# values = ", ".join(['%s'] * len(adict))
# print(values)
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor() # 创建游标
# sql = 'insert into `c_tab`({keys}) values({values})'.format(keys=keys, values =
# values)
# cursor.execute(sql,tuple(adict.values())) # 通过位置进行对应数据，同时执行sql语句
# db.commit() # 表示确认，直接写入表中。 'insert into `c_tab`(id, `name`, age)
# # values(9, 武人, 18)'
# # db.rollback() # 回滚
# db.close() # 关闭和数据库的连接
# print("新增数据库数据信息")
# db = pymysql.connect(host="localhost", user="root",
#                      password="123456",db="testmysqlstudy")
# cursor = db.cursor()
# name = "罗子怡"
# age = 20
# sql = "update c_tab set age = %s where name = %s "
# print(type(age))
# cursor.execute(sql, (age, name))
# db.commit()
# db.close()
# print("更新成功")
# db = pymysql.connect(host="localhost", user='root', password="123456",
#                      db="testmysqlstudy")
# cursor = db.cursor()
# name = "武人"
# sql = f"delete from c_tab where name = '{name}'"
# cursor.execute(sql)
# db.commit()
# db.close()
# print("删除成功")