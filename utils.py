from flask import jsonify
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
        'success': c ,
        'time': d,
        'msg': m
    })