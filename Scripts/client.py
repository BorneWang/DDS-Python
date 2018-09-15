# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:23:17 2018
@author: admin
"""

import glob
import os
import time
from logic import DecisionMaker, Filtering
from util import checkexistInServer, outputTofile, Segment, UnitResult, Result


class Client():
    def __init__(self,args,srv):
        self.src = args.src
        self.logic = DecisionMaker(args)
        self.filtering = Filtering(args)
        self.server = srv
        self.lastupdatetime = 0
        self.tracker_last = 0
        self.test = args.test
        #self.outPath = args.output
       
              
    def QueryCNN(self, Regions):
        Results = Result()
        for region in Regions:
            tic = time.time()
            impath = self.logic.getImage(region)
            tic2 = time.time()
            print("**********************the time of get image is ************************************",tic2-tic)
            print("the box id is :",region.boxID)
            infresult,num_low_conf = self.server.RUNCNN(impath,region)
            if num_low_conf == -1:
                continue
            for line in infresult:
                x = line[0] 
                y = line[1]
                w = line[2]
                h = line[3]
                conf = line[4]
                label = line[5]
                box_id = line[6]
                uniret = UnitResult(region.frameID,x,y,w,h,conf,label,region.res,box_id,num_low_conf)
                Results.unitResults.append(uniret)
        return Results
    
    def getNextSegment(self,now,maxsize=8):
        if self.test == '0':
            Allframes = sorted(glob.glob('{}/*.jpeg'.format(self.src)))
        else:
            Allframes = sorted(glob.glob('{}/*.png'.format(self.src)))
        print("src is ",self.src)
        seg = Segment()
        if now == len(Allframes):
            return seg
        print("======================================= one segment time: ",time.time()-self.lastupdatetime)
        self.lastupdatetime = time.time()
        count = 0
        for frame in Allframes[now:]:
            now +=1
            #print("frame is ",frame[len(frame)-14:len(frame)-4])
            if self.test == '0':
                frameID = int(frame[len(frame)-15:len(frame)-5])
            else:
                frameID = int(frame[len(frame)-14:len(frame)-4])
            seg.frameIdList.append(frameID)
            count += 1
            if count == maxsize:
                return seg, now
        return seg,now      
    
    
    
    def UpdateFrameList(self,frames,Results):
        for ret in Results.unitResults:
            #print("ret.frameID is",ret.frameID)
            if ret.frameID in frames.frameIdList:
                frames.frameIdList.remove(ret.frameID)
        return frames
    
    
    def Run(self):
        now = 0
        while True:
            segment,now = self.getNextSegment(now)
            self.logic.tracker_last = segment.frameIdList[0]
            print("the last tracker is ",self.tracker_last)
            if segment.GetFrameIdList == []:
                return None
            FramdIDAfterLoacalFiltering = self.filtering.Run(segment)
            results = Result()
            RegionsToQuery = []
            while True:
                ticc0 = time.time()
                RegionsToQuery = self.logic.GetNextRegionToQuery(FramdIDAfterLoacalFiltering,
                                                                results)
                ticc1 = time.time()
                print("GetNextRegionToQuery time is :",ticc1-ticc0)
                #outputTofile(RegionsToQuery)
                if len(RegionsToQuery) == 0:
                    break
                CNNResult = self.QueryCNN(RegionsToQuery)
                ticc2 = time.time()
                print("QueryCNN time is :",ticc2-ticc1)
                results.AddResult(CNNResult)
                FramdIDAfterLoacalFiltering = self.UpdateFrameList(FramdIDAfterLoacalFiltering,results)
                results = self.logic.updateResults(results)
                ticc3 = time.time()
                print("update Results time is :",ticc3-ticc2)
               
                
            if len(FramdIDAfterLoacalFiltering.frameIdList) != 0:
                ticc = time.time()
                self.logic.Tracking(FramdIDAfterLoacalFiltering,results)
                ticc1 = time.time()
                print("tracking time is :",ticc1-ticc)
            outputTofile(results)
