# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:22:42 2018
@author: admin
"""
import argparse
from server import Server
from client import Client
from util import ConfigOS

def main():
    parser = argparse.ArgumentParser(description='client and server',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--src', type=str, help='base network')
    parser.add_argument('--logic', type=str, help='logic')
    parser.add_argument('--modelpath', type=str, default='/home/bowen/model/faster_rcnn_resnet101_coco_2018.pb', help='CNN model')
    parser.add_argument('--crf', type=int, default=23, help='crf')
    parser.add_argument('--qp', type=int, default=-1, help='qp')
    parser.add_argument('--res', type=float, default=1, help='res')
    parser.add_argument('--test', type=str, default='0', help='res')
    parser.add_argument('--video', type=str, help='video src')
    srcargs = parser.parse_args()

    ConfigOS(srcargs)
   
    Srv = Server(srcargs)
    Clt = Client(srcargs,Srv)
    
    Clt.Run()
    
    
if __name__ == '__main__':
    main()
