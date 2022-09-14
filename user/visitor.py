import time
from flask import request
from utils import get_json
from user import user_blue
from SQLs import userSQL as database

db = database.DatabaseContract()


@user_blue.route('/visitorMessage', methods=['POST'])
def visitorMessage():
    data = request.json
    visitorName = data.get('visitorName')
    email = data.get('email')
    content = data.get('content')
    res = db.visitorMessage(visitorName, email, content)
    if res == "ok":
        code = True
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '留存信息成功'
    else:
        code = False
        data = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        message = '请稍后再试'

    return get_json(code, data, message)