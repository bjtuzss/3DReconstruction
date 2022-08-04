# user模块
from flask import request
from utils import get_json
from user import user_blue
import userSQL as database

db = database.DatabaseContract()


@user_blue.route('/register', methods=['GET', 'POST'])
def register():
    return 'register'


@user_blue.route('/login', methods=['GET', 'POST'])
def login():
    data = request.json
    username = data.get('name')
    password = data.get('password')
    res = db.login(username, password)
    print(res)
    if res == 1:
        code = 0
        data = []
        message = '登录成功'
    else:
        code = -1
        data = []
        message = '用户名或密码错误'

    return get_json(code, data, message)


@user_blue.route('/modify_password', methods=['GET', 'POST'])
def modify_password():
    return 'modify_password'
