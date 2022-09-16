# coding= utf-8
import argparse
import os
import sys
from utils import print_args

parser = argparse.ArgumentParser(description='Main')
parser.add_argument('--scan_name', default='123', help='select one scan')
parser.add_argument('--imw', type=int, default=1600, help='image width')
parser.add_argument('--imh', type=int, default=1200, help='image height')
args = parser.parse_args()
print("argv:", sys.argv[1:])
print_args(args)

if __name__ == "__main__":
    data_path = os.path.join('./data',args.scan_name)
    outdir = os.path.join('./outputs',args.scan_name)
    os.system("python colmap.py --scan_name " + args.scan_name + " --outdir " + data_path)
    os.system("python eval_custom.py --testpath " + data_path + " --imw " + str(args.imw) + " --imh " + str(args.imh) + ' --outdir ' + outdir)