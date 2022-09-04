# user模块
from flask import request
from utils import get_json
from square import square_blue
import squareSQL as database
import time

db = database.DatabaseContract()


@square_blue.route('/models/getAll', methods=['GET'])
def getAll():
    res = db.getAll()
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '查询失败'
    return get_json(code, data, message)


@square_blue.route('/models/get', methods=['GET'])
def get():
    type = request.args.get("type")
    res = db.get(type)
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '查询失败'
    return get_json(code, data, message)


@square_blue.route('/models/display', methods=['GET'])
def display():
    projectid = request.args.get("projectid")
    res = db.display(projectid)
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '查询失败'
    return get_json(code, data, message)
