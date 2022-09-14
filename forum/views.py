# user模块
from flask import request
from utils import get_json
from forum import forum_blue
from SQLs import forumSQL as database
import time

db = database.DatabaseContract()


@forum_blue.route('/basic', methods=['GET'])
def basic():
    res = db.basic()
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '查询失败'
    return get_json(code, data, message)


@forum_blue.route('/getAll', methods=['GET'])
def getAll():
    type = request.args.get("type")
    res = db.getAll(type)
    if res != 'error':
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '查询失败'

    return get_json(code, data, message)


@forum_blue.route('/get', methods=['GET'])
def get():
    commentId = request.args.get("postid")
    res1 = db.get1(commentId)
    if res1 != 'error':
        res2 = db.get2(commentId)
        res1[0]['reply'] = res2
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res1
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '查询失败'
    return get_json(code, data, message)


@forum_blue.route('/post', methods=['POST'])
def post():
    data = request.json
    userid = data.get('userid')
    title = data.get('title')
    content = data.get('content')
    type = data.get('type')
    res = db.post(userid, title, content, type)
    if res != "error":
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = res
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '用户名或密码错误'

    return get_json(code, data, message)