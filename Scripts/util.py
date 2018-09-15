# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 00:40:49 2018

@author: admin
"""

import os
RES_LOW = 0.8
#RES_MID = 0.6
#RES_HIGH = 0.8

class Region():
    def __init__(self,frameID,x,y,w,h,res,box_id=-1,num=0):
        self.frameID = frameID
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.res = res
        self.boxID = box_id
        self.num = num

class Segment():
    def __init__(self):
        self.frameIdList = []
    def GetFrameIdList(self):
        return self.frameIdList

class UnitResult():
    def __init__(self,frameID,x,y,w,h,confidence,label,res,box_id=-1,num=0):
        self.frameID = frameID
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.confidence = confidence
        self.label = label
        self.res = res
        self.boxID = box_id
        self.num = num

class Result():
    def __init__(self):
        self.unitResults = []
    def AddResult(self, other):
        for unit in other.unitResults:
            if unit in self.unitResults:
                continue
            else:
                self.unitResults.append(unit)
    def CountObjts(self):
        objs = {}
        for oneresult in self.unitResults:
            frameID = oneresult.frameID
            if frameID in objs:
                objs[frameID] += 1
            else:
                objs[frameID] = 1
        return objs


def increaseRes(oldres):
    if oldres == RES_LOW:
        newres = 1
    #elif oldres == RES_MID:
    #    newres = RES_HIGH
    else:
        newres = 1
    return newres
 
            
def checkexistInServer(frameID):
    count = 1
    new_ID = frameID
    while True:
        path = 'Sendtoserver/' + new_ID + '.jpeg'
        if os.path.exists(path):
            new_ID = str(count) + '+' +frameID
            count += 1
        else:
            break
    return new_ID


def ConfigOS(args):
    os.makedirs(args.logic,exist_ok=True)
    os.chdir(args.logic)
    os.makedirs('Sendtoserver',exist_ok=True)
    os.makedirs('Results',exist_ok=True)
    os.makedirs('tempReserve',exist_ok=True)
    os.makedirs('debug_log',exist_ok=True)
    if args.logic == 'DDS':
        os.makedirs('CropReserve',exist_ok=True)
    if args.logic == 'MPEG':
        os.makedirs('mpeg_resize_reserve',exist_ok=True)


def outputTofile(inputresult):
    if type(inputresult) == list:
        outfile = open('debug_log/regions_bug','a')
        for region in inputresult:
            print("region.frameID :",region.frameID,file=outfile)
            print("region.x :",region.x,file=outfile)
            print("region.y :",region.y,file=outfile)
            print("region.w :",region.w,file=outfile)
            print("region.h :",region.h,file=outfile)
            print("region.res :",region.res,file=outfile)
        print("##########################",file=outfile)
        outfile.close()
    else:
        outfile = open('Results/serverSideResults','a')
        for region in inputresult.unitResults:
            print(region.frameID,region.x,region.y,region.w,region.h,
                  region.label,region.confidence,region.res,sep=',',file=outfile)
        print("#############################")
        outfile.close()
