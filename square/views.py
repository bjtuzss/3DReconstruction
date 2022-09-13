# user模块
import base64
import os

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


@square_blue.route('/getPic', methods=['GET', 'POST'])
def findpic():
    path = request.args.get("path")
    img = os.listdir(os.getcwd() + path[1:])[0]
    img_url = os.getcwd() + path[1:] + '/' + img
    f = open(img_url, 'rb')
    base64_str = base64.b64encode(f.read())
    return base64_str


# 测试
if __name__ == '__main__':
    img = os.listdir(os.path.dirname(os.getcwd()) + './results/zk_scan7'[1:])[0]
    img_url = os.path.dirname(os.getcwd()) + './results/zk_scan7'[1:] + '/' + img
    f = open(img_url, 'rb')
    base64_str = base64.b64encode(f.read())
    print(base64_str)