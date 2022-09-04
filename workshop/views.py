# user模块
from flask import request
from utils import get_json, creatUniqueCode
from workshop import workshop_blue
import workshopSQL as database
import time

db = database.DatabaseContract()


@workshop_blue.route('/project/create', methods=['POST'])
def creat():
    data = request.json
    projectid = creatUniqueCode()
    userid = data.get('userid')
    projectName = data.get('project_name')
    res = db.createProject(projectid, userid, projectName)
    if res == 'ok':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '项目创建成功, 项目标识码为' + projectid
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '创建失败，同名项目已存在'
    return get_json(code, data, message)


@workshop_blue.route('/images/upload', methods=['POST'])
def upload():
    data = request.json
    userid = data.get('userid')
    projectName = data.get('project_name')
    projectid = data.get('projectid')
    res = db.upload(username, password)
    if res == 1:
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '登录成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '用户名或密码错误'

    return get_json(code, data, message)


@workshop_blue.route('/models/getAll', methods=['GET'])
def getAll():
    data = request.json
    userid = data.get('userid')
    res = db.getAll(userid)
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '修改失败'
    return get_json(code, data, message)


@workshop_blue.route('/models/display', methods=['POST'])
def display():
    data = request.json
    userid = data.get('userid')
    projectName = data.get('project_name')
    projectid = data.get('projectid')
    res = db.display(userid, projectName, projectid)
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '修改失败'
    return get_json(code, data, message)


@workshop_blue.route('/models/delete', methods=['POST'])
def delete():
    data = request.json
    userid = data.get('userid')
    projectName = data.get('project_name')
    projectid = data.get('projectid')
    res = db.delete(userid, projectName, projectid)
    if res == 'ok':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '模型删除成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '模型删除失败'
    return get_json(code, data, message)


@workshop_blue.route('/models/share', methods=['POST'])
def share():
    data = request.json
    userid = data.get('userid')
    projectName = data.get('project_name')
    projectid = data.get('projectid')
    type= data.get('type')
    desc = data.get('desc')
    res = db.share(userid, projectName, projectid, type, desc)
    if res == 'ok':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '模型分享成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '模型分享失败'
    return get_json(code, data, message)
