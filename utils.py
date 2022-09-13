import os

from flask import jsonify
import time
import datetime
import uuid
import base64


# 把数据封装为json格式
def get_json(c, d, m):
    """
    接口说明：
    1.返回的是json数据
    2.结构如下
    {
        code： 0, # 非0即错误 1
        data： # 数据
        message： '对本次请求的说明'
    }
    """
    return jsonify({
        'success': c,
        'time': d,
        'msg': m
    })


# 利用时间戳生成不重复的八位随机码
def creatUniqueCode():
    now_tm = (datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
    time_array = time.strptime(now_tm, '%Y%m%d%H%M%S')
    stamp_tm = int(time.mktime(time_array))
    return_tm = hex(stamp_tm)[2:]

    return return_tm


# 使用uuid生成唯一的账号
def getShortId():
    return uuid.uuid4().hex[:8]


# 在指定路径保存图片
def resp_file_upload(requ_data, filePath):
    # 保存文件
    file_content = requ_data['file']
    file_name = requ_data['file'].filename
    file_path = filePath + '/' + file_name
    fileExit(filePath)
    if os.path.exists(file_path):
        return {'msg': '该文件已存在',
                'code': 0}
    else:
        file_content.save(file_path)
        return {'msg': '上传文件' + file_name + '成功',
                'filePath': filePath,
                'code': 1}


# 检查路径是否存在
def fileExit(filePath):
    if not os.path.exists(filePath):
        os.makedirs(filePath)


# 测试
if __name__ == '__main__':
    img = os.listdir(os.getcwd() + './results/zk_scan1'[1:])[0]
    print(os.getcwd() + './results/zk_scan1'[1:] + '/' + img)
