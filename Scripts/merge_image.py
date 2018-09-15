# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 14:58:01 2018

@author: admin
"""

import cv2
import numpy as np
RES_LOW = 0.8
#RES_MID = 0.6
#RES_HIGH = 0.8

class Imageprocesor():
    def __init__(self,args):
        self.imagelist = {}
        self.regionlist = {}
        self.logic = args.logic
        
    def merge_image(self,impath,region):
        if self.logic == 'DDS':
            frameID = impath[len(impath)-15:len(impath)-5]
            if region.res == RES_LOW:
                self.imagelist[frameID] = []
                self.imagelist[frameID].append(impath)
                self.regionlist[frameID] = []
                self.regionlist[frameID].append(region)
                img = cv2.imread(impath)
                return img.astype(np.uint8)
            else:
                self.imagelist[frameID].append(impath)
                self.regionlist[frameID].append(region)
                im_list = self.imagelist[frameID]
                if region.num <= len(im_list)-1:
                    im_back = cv2.imread(im_list[0])
                    if region.res == 1:
                       scale = 10.0 / 8.0
                    #elif region.res == RES_HIGH:
                    #   scale = 1.33
                    #elif region.res == 1:
                    #   scale = 1.25
                    im_back = cv2.resize(im_back,None,fx=scale, fy=scale, interpolation = cv2.INTER_CUBIC)
                    for i in range(1,len(im_list)):
                        im_front = cv2.imread(im_list[i])
                        one_region = self.regionlist[frameID][i]
                        w_begin = int(im_back.shape[1]*one_region.x)
                        h_begin = int(im_back.shape[0]*one_region.y)
                        w_end = int(w_begin + im_back.shape[1]*one_region.w - 1)
                        h_end = int(h_begin + im_back.shape[0]*one_region.h - 1)
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        print(one_region.x,one_region.y,one_region.w,one_region.h)
                        print(h_begin,h_end,w_begin,w_end)
                        print(im_back.shape)
                        print(im_front.shape)
                        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                        front_w = min(im_front.shape[1],w_end-w_begin)
                        front_h = min(im_front.shape[0],h_end-h_begin)
                        for i in range(h_begin,h_begin+front_h):
                            for j in range(w_begin,w_begin+front_w):
                                im_back[i][j][0] = im_front[i-h_begin][j-w_begin][0]
                                im_back[i][j][0] = im_front[i-h_begin][j-w_begin][1]
                                im_back[i][j][0] = im_front[i-h_begin][j-w_begin][2]
                    outpath = 'CropReserve/' + frameID + '.jpeg'
                    cv2.imwrite(outpath,im_back)
                    self.imagelist[frameID] = []
                    self.imagelist[frameID].append(outpath)
                    self.regionlist[frameID] = []
                    self.regionlist[frameID].append([0,0,1,1])
                    return im_back.astype(np.uint8)
                else:
                    return None
        else:
            img = cv2.imread(impath)
            return img.astype(np.uint8)
