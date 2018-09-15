# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 00:38:33 2018

@author: admin
"""
from tracker import KCF_tracker
import os
import time
from util import increaseRes, Region, Result,checkexistInServer
from opencv_resize import OPCV_resize, OPCV_mpeg_resize
RES_LOW = 0.8
#RES_MID = 0.6
#RES_HIGH = 0.8

class Filtering():
    def __init__(self,args):
        self.logic = args.logic
        
    def Run(self,segment):
        if self.logic == 'DDS':
            return segment
        else:
            return segment

def MpegVideo(args):
    tempPath = 'tempReserve/temp_video.mp4'
    #if args.qp == -1:
    #    os.system("ffmpeg -loglevel error -i {0} -crf {1} -vcodec libx264 -vf scale=iw*{2}:ih*{2} tempReserve/temp_video.mp4".format(args.video,args.crf,args.res))
    #else:
    #    os.system("ffmpeg -loglevel error -i {0} -qp {1} -vcodec libx264 -vf scale=iw*{2}:ih*{2} tempReserve/temp_video.mp4".format(args.video,args.qp,args.res))
    videoPath = '/home/bowen/videos/fromPng_' + args.video + '.mp4'
    os.system("ffmpeg -loglevel error -i {0} -vcodec libx264 -pix_fmt yuv420p -crf 35 -vf scale=iw*{1}:ih*{1} tempReserve/temp_video.mp4".format(videoPath,args.res))
    os.system("ffmpeg -y -i {} -vcodec mjpeg -pix_fmt yuvj420p -q:v 18 -vsync 0 -start_number 0 Sendtoserver/%010d.jpeg".format(tempPath))
    src = 'tempReserve'
    return src


class DecisionMaker():
    def __init__(self,args):
        self.logic = args.logic
        self.src = args.src
        # DDS fields
        self.Maxpick = 4
        self.pick_count = 0
        self.maxThres = 0.6
        self.minThres = 0.1
        self.DiffDic = {}
        self.tracker_last = 0
        self.resdict = {}
        # GroundTruth fields
        self.test = args.test
        # MPEG
        if args.logic == 'MPEG':
           self.mpegsrc = MpegVideo(args)
        else:
           self.mpegsrc = 0

    def getImage(self,region):
        frameID = str(region.frameID)
        frameID = frameID.zfill(10)
        if self.test == '0':
            framePath = self.src + '/' + frameID + '.jpeg'
        else:
            framePath = self.src + '/' + frameID + '.png'
        new_frameID = checkexistInServer(frameID)
        print("new_frameID is :",new_frameID)
        if self.logic == 'GroundTruth':
            impath = framePath
            return impath
        elif self.logic == 'MPEG':
            #tempPath = self.mpegsrc + '/' + frameID + '.png'
            impath = 'Sendtoserver' + '/' + frameID + '.jpeg'
            #OPCV_mpeg_resize(tempPath,impath,region.res,frameID)
            return impath
        else:
            tempPath = 'tempReserve/' + new_frameID + '.png'
            impath = 'Sendtoserver/' + new_frameID + '.jpeg'
            w = region.w
            h = region.h
            x = region.x
            y = region.y
            #os.system("ffmpeg -loglevel error -i {0} -vcodec mjpeg -pix_fmt yuvj420p -q:v 18 -vf scale=iw*{1}:ih*{1} {2}".format(framePath,region.res,tempPath))
            OPCV_resize(framePath,tempPath,impath,region)
            #os.system("ffmpeg -loglevel error -i {} -vcodec mjpeg -pix_fmt yuvj420p -q:v 5 -filter:v \"crop=iw*{}:ih*{}:iw*{}:ih*{}\" -y {}".format(tempPath,w,h,x,y,impath))
            os.system("rm {}".format(tempPath))
            #os.system("rm {}".format(temp_png))
            return impath




    
    def GetNextRegionToQuery(self, segment, Results):
        regions = []
        frames = segment.GetFrameIdList()
        if self.logic == 'GroundTruth' or self.logic == 'MPEG':
            for frameId in frames:
                regions.append(Region(frameId,0,0,1,1,1))
            return regions
        if self.logic == 'DDS':
            #print("Begin DDS logic")
            if len(Results.unitResults) == 0:
                self.DiffDic = {}
                regions.append(Region(frames[0],0,0,1,1,RES_LOW))
                regions.append(Region(frames[len(frames)-1],0,0,1,1,RES_LOW))
                self.DiffDic[(frames[0],frames[len(frames)-1])] = -1
                self.resdict[frames[0]] = RES_LOW
                self.resdict[frames[len(frames)-1]] = RES_LOW
                self.pick_count +=2
                return regions
            else:
                #Croping
                for ret in Results.unitResults:
                    if ret.confidence > self.minThres and ret.confidence < self.maxThres:
                        ret.res = self.resdict[ret.frameID]
                        if ret.res != 1:
                           print("Before renew resolution")
                           print("frameID:",ret.frameID," res:",ret.res," boxID",ret.boxID,"confidence:",ret.confidence)
                           newResolution = increaseRes(ret.res)
                           print("frameID:",ret.frameID," res:",newResolution," boxID",ret.boxID)
                           regions.append(Region(ret.frameID,
                                                 ret.x,
                                                 ret.y,
                                                 ret.w,
                                                 ret.h,
                                                 newResolution,
                                                 ret.boxID,
                                                 ret.num))
                for feID in self.resdict:
                    self.resdict[feID] = increaseRes(self.resdict[feID])
                    #print("!!!!!!!!!!!!!!!!!!!!!!",self.resdict[feID],"!!!!!!!!!!!!!")
                if self.pick_count == self.Maxpick:
                    self.pick_count = 0
                    return regions
                objs = Results.CountObjts()          #type objs is DIC
                #print("objs are", objs)
                #update DiffDic
                #print("my diffDIc are",self.DiffDic)
                maxkey = ()
                maxdiff = -1
                for key in self.DiffDic:
                    #print("key is",key)
                    diff = objs[key[0]] - objs[key[1]]
                    if diff < 0:
                       diff = -diff
                    self.DiffDic[key] = diff
                    if diff > maxdiff:
                        maxkey = key
                        
                #FrameSelection
                #print("maxkey is",maxkey)
                if maxkey[1] - maxkey[0] > 1:
                    midframe = int((maxkey[1] + maxkey[0]) / 2)
                    print("midframe is :",midframe)
                    del self.DiffDic[maxkey]
                    self.DiffDic[(maxkey[0],midframe)] = -1
                    self.DiffDic[(maxkey[1],midframe)] = -1
                    regions.append(Region(midframe,0,0,1,1,RES_LOW))
                    self.resdict[midframe] = RES_LOW
                    self.pick_count += 1
            return regions
        #if self.logic == Noscope:
        #    return None
       # if self.logic == Vigil:
        #    return None
    
    def updateResults(self,results):
        if self.logic == 'DDS':
            remove_index = []
            new_results = Result()
            for i in range(len(results.unitResults)):
                for j in range(i+1,len(results.unitResults)):
                    if results.unitResults[i].frameID == results.unitResults[j].frameID:
                        if results.unitResults[i].boxID == results.unitResults[j].boxID:
                            print("Before recover res !!!")
                            print("frameID :",results.unitResults[i].frameID," res:",results.unitResults[i].res,"confidence:",results.unitResults[
i].confidence,"bbox :",results.unitResults[i].boxID)
                            print("frameID :",results.unitResults[j].frameID," res:",results.unitResults[j].res,"confidence:",results.unitResults[
j].confidence,"bbox :",results.unitResults[j].boxID)
                            results.unitResults[i].res = results.unitResults[j].res
                            print("After recover res !!!")
                            results.unitResults[i].confidence = results.unitResults[j].confidence
                            print("frameID :",results.unitResults[i].frameID," res:",results.unitResults[i].res,"confidence:",results.unitResults[
i].confidence,"bbox :",results.unitResults[i].boxID)
                            remove_index.append(j)
            for i in range(len(results.unitResults)):
                if i in remove_index:
                    continue
                else:
                    new_results.unitResults.append(results.unitResults[i])
            return new_results
        else: 
            return results
    
    
    
    def Tracking_label(self,frameID,now_boxes,results):
        #OutPath = 'Clienttracking/' + frameID + '.result'
        Out = open('Results/trackingResults','a')
        i = 0
        for result in results.unitResults:
            if result.frameID == self.tracker_last and result.confidence >self.maxThres:
                if i < len(now_boxes):
                    print(frameID,now_boxes[i][0],now_boxes[i][1],
                          now_boxes[i][2],now_boxes[i][3],result.label,
                          sep=',',file=Out)
                    i += 1
                else:
                    break
        Out.close()
                
    
    
    def Tracking(self,frames,results):
        if self.logic == 'DDS': 
            refe_boxes = []
            for result in results.unitResults:
                if result.frameID == self.tracker_last and result.confidence > self.maxThres:
                    one_box = [result.x,result.y,result.w,result.h]
                    refe_boxes.append(one_box)
            tracker = KCF_tracker(self.tracker_last,refe_boxes,self.src)
            for frameID in frames.frameIdList:
                now_boxes = tracker.Update(frameID)
                self.Tracking_label(frameID,now_boxes,results)
                
        else:
            return None

