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

    def getAll(self):  # 获得所有已分享模型
        try:
            sql = "select projectid, projectname, imgdir, type from projects where share = 1"
            print(sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data

    def get(self, type):  # 获得所有已分享模型
        try:
            sql = "select projectid, projectname, imgdir, type from projects where share = 1 and type = '" + type +"'"
            print(sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data

    def display(self, projectid):  # 获得所有已分享模型
        try:
            sql = "select * from projects where share = 1 and projectId = '" + projectid +"'"
            print(sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data