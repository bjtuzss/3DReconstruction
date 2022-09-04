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

    def basic(self):  # 获取社区基础信息
        try:
            sql = "select * from form_basic"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data)
        except:
            return 'error'
        else:
            return data

    def getAll(self, type):  # 获取所有帖子
        try:
            sql = "select * from first_comment where type = " + type
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data

    def get1(self, commentId):  # 获取单个帖子的主体信息
        try:
            sql = "select * from first_comment where commentId = " + commentId
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data

    def get2(self, commentId):  # 获取单个帖子的回复信息
        try:
            sql = "select * from second_comment where fCommentId = " + commentId
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data

    def post(self, userid, title, content, type):
        try:
            sql = "insert into first_comment values (' " + userid + "', '" + content + "','" + userid + "','" +  + "'"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
        except:
            return 'error'
        else:
            return data
