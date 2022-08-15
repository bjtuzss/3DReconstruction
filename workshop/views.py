# user模块
from flask import request
from utils import get_json
from workshop import workshop_blue
import workshopSQL as database
import time

db = database.DatabaseContract()


@workshop_blue.route('/project/create', methods=['POST'])
def register():
    data = request.json
    print(data)
    userid = data.get('userid')
    projectName = data.get('project_name')
    res = db.create_project(userid, projectName)
    if res == 'ok':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '项目创建成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '创建失败，同名项目已存在'
    return get_json(code, data, message)


@workshop_blue.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    res = db.login(username, password)
    print(res)
    if res == 1:
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '登录成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '用户名或密码错误'

    return get_json(code, data, message)


@workshop_blue.route('/modify_password', methods=['POST'])
def modify_password():
    data = request.json
    print(data)
    userid = data.get('userid')
    newpsw = data.get('newpsw')
    res = db.modify_password(userid, newpsw)
    if res == 'ok':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '修改成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '修改失败'
    return get_json(code, data, message)
