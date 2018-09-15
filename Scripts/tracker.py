import cv2
import numpy as np
import sys


class KCF_tracker():
    def __init__(self,last_img,boxes,src):
        self.src = src
        self.tracker = cv2.MultiTracker_create()
        last_img = str(last_img)
        last_img = last_img.zfill(10)
        framePath = self.src + '/' + last_img + '.png'
        print("refer img is", last_img)
        image = cv2.imread(framePath)
        im_w = image.shape[1] 
        im_h = image.shape[0]
        for bbox in boxes:
            x = bbox[0]*im_w
            y = bbox[1]*im_h
            w = bbox[2]*im_w
            h = bbox[3]*im_h
            box = (x,y,w,h)
            ok = self.tracker.add(cv2.TrackerMIL_create(), image, box)
        
    def Update(self,now_img):
        now_img = str(now_img)
        now_img = now_img.zfill(10)
        framePath = self.src + '/' + now_img + '.png'
        print("img need track, id is", now_img)
        image = cv2.imread(framePath)
        im_h = float(image.shape[0])
        im_w = float(image.shape[1])
        ok, boxes = self.tracker.update(image)
        #print("boxes is", boxes)
        conv_boxes = []
        for i,bbox in enumerate(boxes):
            x = bbox[0] / im_w
            y = bbox[1] / im_h
            w = bbox[2] / im_w
            h = bbox[3] / im_h
            box = [x,y,w,h]
            print(x,y,w,h)
            conv_boxes.append(box)
        return conv_boxes
