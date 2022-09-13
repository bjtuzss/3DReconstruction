# user模块
import datetime

from flask import request, jsonify
from utils import get_json, creatUniqueCode, resp_file_upload, fileExit
from workshop import workshop_blue
import workshopSQL as database
import time

db = database.DatabaseContract()
dafaultDir = "./results/"


@workshop_blue.route('/project/create', methods=['POST'])
def creat():
    data = request.json
    print(data)
    print(len(data.get('file_path')) != 0)
    if len(data.get('file_path')) == 0:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '创建失败，未上传任何图片信息'
        return get_json(code, data, message)

    projectid = creatUniqueCode()
    username = data.get('username')
    projectName = data.get('project_name')
    type = data.get('type')
    imgdir = data.get('file_path')
    desc = data.get('desc')
    createtime = datetime.datetime.now().strftime('%Y-%m-%d')
    res = db.createProject(projectid, projectName, username, type, imgdir, desc, createtime)
    if res == 'ok':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '项目创建成功, 项目标识码为' + projectid
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '创建失败，您的项目空间中存在同名项目 ' + projectName
    return get_json(code, data, message)


@workshop_blue.route('/images/upload', methods=['POST'])
def upload():
    """返回文件上传结果信息"""
    requ_data = {
        'file': request.files.get('file'),
        'file_info': dict(request.form)
    }
    filePath = dafaultDir + requ_data.get('file_info').get('user_id') + '_' + requ_data.get('file_info').get('pro_name')
    resp_data = resp_file_upload(requ_data, filePath)
    return jsonify(resp_data)


@workshop_blue.route('/models/getAll', methods=['GET'])
def getAll():
    username = request.args.get("username")
    res = db.getAll(username)
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
