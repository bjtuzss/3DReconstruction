from pymysql import connect
import datetime
from pymysql.cursors import DictCursor  # 为了返回字典形式
from config import MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE


class DatabaseContract(object):
    def __init__(self):  # 创建对象同时要执行的代码
        self.conn = connect(
            host=MYSQL_HOST,
            port=MYSQL_PORT,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DATABASE,
            charset='utf8'
        )
        self.cursor = self.conn.cursor(DictCursor)  # 让数据库数据返回字典的形式

    def __del__(self):  # 释放对象同时要执行的代码
        self.cursor.close()
        self.conn.close()

    def modify_project(self, username, password):  # 登录
        try:
            sql = "select * from user where userid='" + username + "' and password='" + password + "'"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data)
        except:
            return 'error'
        else:
            return len(data)

    def create_project(self, projectid, projectname, password):  # 注册
        try:
            sql = "insert into projects values('" + projectid + "','" + projectname + "','" + password + "' , '')"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'

    def modify_password(self, userid, newpsw):  # 修改密码
        try:
            sql = "update user set password = '" + newpsw + "'where userid='" + userid + "'"
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'