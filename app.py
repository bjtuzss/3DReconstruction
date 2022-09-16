# coding= utf-8
import os
import ssl
from datetime import time
import time as time1
import requests
from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
import cv2


app = Flask(__name__)
app.config.from_object('config')
CORS(app, supports_credentials=True)

def upload(http_url, obj_path,project_name,username):
    f = open(obj_path, 'rb')
    file = {'file': f.read()}
    f.close()
    data = {
        'filename': os.path.split(obj_path)[-1],
        'project_name': project_name,
        'username': username
    }
    res = requests.post(url=http_url, files=file, data=data)
    return res

@app.route('/')
def hello_world():  # put application's code here
    return send_file('D:\\Code\\AI-learning\\Project\\3D-Restruction\\Main\\outputs\\WY_scan9\\WY_scan9.obj')

@app.route('/go', methods=['POST'])
def go():
    # 读取post数据
    data = request.json
    project_name = data.get('project_name')
    username = data.get('username')
    images_url = data.get('images_url')
    images_num = data.get('images_num')
    scan_name = username + '_' + project_name


    scan_path = os.path.join('./scans', scan_name)
    scan_img_path = os.path.join(scan_path,'images')
    data_path = os.path.join('./data', scan_name)
    outdir = os.path.join('./outputs', scan_name)
    # 创建图片文件夹并下载图片
    if not os.path.exists(scan_path):
        os.mkdir(scan_path)
    if not os.path.exists(scan_img_path):
        os.mkdir(scan_img_path)

    # 下载图片至指定文件夹
    baseURL = 'http://43.143.151.191:888'
    for i in range(int(images_num)):
        url = baseURL + images_url +'/%08d.jpg' % i
        # os.path.join(baseURL,images_url,'%08d.jpg' % i)
        print(url)
        response = requests.get(url=url).content
        open(os.path.join(scan_img_path, '%08d.jpg' % i), 'wb').write(response)
        # print('Successfully downloaded ' + url)
    file_path = scan_img_path + '/00000000.jpg'
    print("img_file_path:",file_path)
    img = cv2.imread(file_path)  # 读取图片信息
    imw, imh = img.shape[0] , img.shape[1]
    os.system("python colmap.py --scan_name " + scan_name + " --outdir " + data_path)
    os.system("python eval_custom.py --testpath " + data_path + " --imw " + str(imw) + " --imh " + str(
        imh) + ' --outdir ' + outdir + ' --outfile_name ' + scan_name + '.obj')
    print(123)
    print(os.path.join(outdir,scan_name,'.obj'))
    # 发送obj回服务器
    res = upload('http://43.143.151.191:443/workshop/obj/upload',
                 os.path.join(outdir,scan_name + '.obj'),
                 project_name,username)
    print(res)
    return 'ok'



if __name__ == '__main__':
    # res = upload('http://43.143.151.191:443','D:\\Code\\AI-learning\\Project\\3D-Restruction\\Main\\outputs\\WY_scan9\\WY_scan9.obj')
    # print(res)
    app.run(port=5001)
    # img = cv2.imread('D:\\Code\\AI-learning\\Project\\3D-Restruction\\Main\\scans\\wy_scan118-2\\images\\00000000.jpg')  # 读取图片信息
    # imw, imh = img.shape[0], img.shape[1]
    # print(imw)
