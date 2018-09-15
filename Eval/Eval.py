# -*- coding: utf-8 -*-
"""
Created on Tue Sep  4 10:24:59 2018

@author: admin
"""
import argparse
from f1_score import f1_eval

def Load_Truth(truthPath):
    truth = {}
    with open(truthPath) as f:
        for line in f:
            ret = line.split(',')
            frameID = int(ret[0])
            x = float(ret[1])
            y = float(ret[2])
            w = float(ret[3])
            h = float(ret[4])
            label = ret[5]
            confidence = float(ret[6])
            if frameID in truth:
                if confidence > 0.8:
                    truth[frameID].append([x,y,w,h,label])
            else:
                truth[frameID] = []
                if confidence > 0.8:
                    truth[frameID].append([x,y,w,h,label])
    return truth
            
def Load_Pred(args):
    pred = {}
    with open(args.ServerSideResults) as f:
        for line in f:
            ret = line.split(',')
            frameID = int(ret[0])
            x = float(ret[1])
            y = float(ret[2])
            w = float(ret[3])
            h = float(ret[4])
            label = ret[5]
            confidence = float(ret[6])
            if frameID in pred:
                if confidence > 0.8:
                    pred[frameID].append([x,y,w,h,label])
            else:
                pred[frameID] = []
                if confidence > 0.8:
                    pred[frameID].append([x,y,w,h,label])
    if args.logic == 'DDS':
        with open(args.ClientSideResults) as f:
            for line in f:
                ret = line.split(',')
                frameID = int(ret[0])
                x = float(ret[1])
                y = float(ret[2])
                w = float(ret[3])
                h = float(ret[4])
                #print(frameID)
                #print(x,y,w,h)
                label = ret[5]
                #print('label : ',label)
                #print("######################")
                if frameID in pred:
                    pred[frameID].append([x,y,w,h,label])
                else:
                    pred[frameID] = []
                    pred[frameID].append([x,y,w,h,label])
    return pred
                    



def main():
    parser = argparse.ArgumentParser(description='evaluation',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--truth', type=str, default='',help='GroundTruth')
    parser.add_argument('--logic', type=str, help='logic')
    parser.add_argument('--ServerSideResults', type=str, default='Results/serverSideResults', help='Server')
    parser.add_argument('--ClientSideResults', type=str, default='DDS/Results/trackingResults', help='client side results')
    parser.add_argument('--ImageSendToServer', type=str, default='Sendtosercer',help='Image send to server')
    args = parser.parse_args()
   
    truth = Load_Truth(args.truth)
    pred = Load_Pred(args)
    f1_scores = []
    for key in pred:
        #print(key)
        #print(len(pred[key]),len(truth[key]))
        f1_scores.append(f1_eval(pred[key],truth[key]))
        #print("###################################")
        
    summ = 0
    for i in f1_scores:
        summ += i
    
    F1 = summ / len(f1_scores)
    
    print(F1,end=' ')
    
    
if __name__ == '__main__':
    main()
