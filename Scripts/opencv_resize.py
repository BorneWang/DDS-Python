# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:22:42 2018
@author: admin
"""
import cv2
import argparse
import os
import numpy as np
np.set_printoptions(threshold=np.inf)

def OPCV_mpeg_resize(tempPath,impath,scale,frameID):
    #opencv_resize
    img = cv2.imread(tempPath)
    ww = int(img.shape[1] * scale)
    hh = int(img.shape[0] * scale)
    img_small = cv2.resize(img,(ww,hh),fx=0,fy=0, interpolation=cv2.INTER_CUBIC)
    outputPath = 'mpeg_resize_reserve/' + frameID + '.png'
    cv2.imwrite(outputPath,img_small)

    #ffmpeg_sws_scale
    os.system("ffmpeg -loglevel error -i {} -vcodec mjpeg -pix_fmt yuvj420p -q:v 18 -vf scale=iw*1:ih*1 {}".format(outputPath,impath))

    os.system("rm {}".format(outputPath))

def OPCV_resize(framePath,tempPath,impath,region):

    scale = region.res
    x = region.x
    y = region.y
    w = region.w
    h = region.h

    #opencv_resize
    img = cv2.imread(framePath)
    ww = int(img.shape[1] * scale)
    hh = int(img.shape[0] * scale)
    img_small = cv2.resize(img,(ww,hh),fx=0,fy=0, interpolation=cv2.INTER_CUBIC)

    #crop
    iw = img_small.shape[1]
    ih = img_small.shape[0]
    cx = int(x * iw)
    cy = int(y * ih)
    cw = int(iw * w)
    ch = int(ih * h)
    img_crop = img_small[cy:cy+ch,cx:cx+cw,:]
    cv2.imwrite(tempPath,img_crop)

    #ffmpeg_sws_scale
    os.system("ffmpeg -loglevel error -i {} -vcodec mjpeg -pix_fmt yuvj420p -q:v 18 -vf scale=iw*1:ih*1 {}".format(tempPath,impath))


    
'''
def main():
    parser = argparse.ArgumentParser(description='client and server',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--src', type=str, help='src')
    parser.add_argument('--scale', type=float, help='scale')
    srcargs = parser.parse_args()

    OPCV_resize(srcargs.src,srcargs.scale,'tempReserve/ff_resize.jpeg','0000000000')

if __name__ == '__main__':
    main()
'''
