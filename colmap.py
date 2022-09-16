import argparse
import sys
from collections import OrderedDict
from utils import *
import cv2
import torch
import matplotlib.pyplot as plt
from plyfile import PlyData, PlyElement
import json
import os
import shutil

parser = argparse.ArgumentParser(description='Use colmap to get pose')

parser.add_argument('--work_path', default='./scans', help='working path')
parser.add_argument('--scan_name', default='scan4-short', help='select one scan')
parser.add_argument('--outdir', default='./data/scan4-short', help='output dir')

# parse arguments and check
args = parser.parse_args()
print("argv:", sys.argv[1:])
print_args(args)

if __name__ == '__main__':

    ROOT = args.work_path
    workspace_path = os.path.join(ROOT, args.scan_name)  # 指定scan所在位置
    image_path = os.path.join(workspace_path, "images")  # 指定scan的images所在位置
    database_path = os.path.join(workspace_path, "database.db")  # 指定colmap database
    sparse_path = os.path.join(workspace_path, "sparse")  # 指定scan的sparse所在位置
    output_path = args.outdir

    FileSeqRename(os.path.join(image_path))  # rename 图片名，使得符合MVSNet格式
    # cal_norm.py.相机标定
    # 自动构建
    # print("colmap automatic_reconstructor --workspace_path "+workspace_path + " --image_path "+image_path)
    # os.system("colmap automatic_reconstructor --workspace_path "+workspace_path + " --image_path "+image_path)
    # 拆解
    # 1.1 提取特征
    os.system("colmap feature_extractor --database_path " + database_path + " --image_path " + image_path)
    # 1.2 特征匹配
    os.system("colmap exhaustive_matcher --database_path " + database_path)
    # 1.3 稀疏建图与ba
    if not os.path.exists(sparse_path):
        os.mkdir(sparse_path)
    os.system(
        "colmap mapper --database_path " + database_path + " --image_path " + image_path + " --output_path " + sparse_path)
    # 1.4 畸变校正
    os.system(
        "colmap image_undistorter --image_path " + image_path + " --input_path " + os.path.join(sparse_path, "0") + \
        " --output_path " + os.path.join(workspace_path, "dense") + " --output_type COLMAP --max_image_size 2000")
    # 1.4.5 导出位姿为txt ，可选
    # os.system("colmap model_converter --input_path " + os.path.join(sparse_path,"0") + \
    #           " --output_path " + os.path.join(workspace_path,"dense\\sparse") + " --output_type TXT")
    # 1.5 colmap2MVSNet
    os.system("python colmap2mvsnet1.py --dense_folder " + os.path.join(workspace_path,
                                                                        "dense") + " --max_d 192 --interval_scale 1.06")
    os.system("python colmap_input.py --folder " + os.path.join(workspace_path,
                                                                "dense"))
    # 1.6 复制所需文件到指定文件夹
    if not os.path.exists(output_path):
        os.mkdir(output_path)
    shutil.copytree(os.path.join(workspace_path, "dense", "cams"), os.path.join(output_path, 'cams'))
    shutil.copytree(os.path.join(workspace_path, "images"), os.path.join(output_path, 'images'))
    shutil.copyfile(os.path.join(workspace_path, "dense", "pair.txt"), os.path.join(output_path, 'pair.txt'))
