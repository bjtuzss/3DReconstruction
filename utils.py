from flask import jsonify
import time
import datetime

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


# 把数据封装为json格式
def get_json(c, d, m):
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


# 测试
if __name__ == '__main__':
    print(creatUniqueCode())
