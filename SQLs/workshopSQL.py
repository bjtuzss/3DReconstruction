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

    def createProject(self, projectid, projectname, username, type, imgdir, desc, createtime):  # 注册
        try:
            sql = "insert into projects values('" + projectid + "','" + projectname + "','" + username + "' , '' , '', '"\
                  + type + "','" + imgdir + "', 0,'" + desc + "', '" + createtime + "')"
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'

    def getAll(self, userid):  # 模型列表返回
        try:
            sql = "select * from projects where userId = '" + userid + "'"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            print(data)
        except:
            return 'error'
        else:
            return data

    def display(self, userid, projectName, projectid):  # 模型列表返回
        try:
            sql = "select ply from projects where userId = '" + userid + "' and projectName = '" + projectName + "'"
            self.cursor.execute(sql)
            ply = self.cursor.fetchall()
            print(ply)
        except:
            return 'error'
        else:
            return ply

    def delete(self, userid, projectName, projectid):  # 模型删除
        try:
            sql = "delete from projects where userId = '" + userid + "' and projectMame = '" + projectName + "'"
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'

    def share(self, userid, projectId):  # 模型分享到模型广场
        try:
            sql = "update projects set share = " + "1 where userId = '" + userid + "' and projectId = '" + projectId + "'"
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'

    def save(self, ply, projectId):  # 模型分享到模型广场
        try:
            sql = "update projects set ply = '" + ply + "' where projectId = '" + projectId + "'"
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'

    def sav2(self, ply, projectId):  # 模型分享到模型广场
        try:
            sql = "update projects set ply = '" + ply + "' where projectId = '" + projectId + "'"
            print(sql)
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            self.conn.rollback()
            return 'error'
        else:
            return 'ok'


