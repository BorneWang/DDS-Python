import numpy as np

def Intersect(a, b):
	to = max(a[1], b[1])
	le = max(a[0], b[0])
	bo = min(a[3]+a[1], b[3]+b[1])
	ri = min(a[2]+a[0], b[2]+b[0])

	w = max(0, ri-le)
	h = max(0, bo-to)

	return w * h


def Area(a):
	w = max(0, a[2])
	h = max(0, a[3])
	return w * h


def IOU(a, b):
	ss = Intersect(a, b)
	return ss / (Area(a) + Area(b) - ss)

def f1_eval(pred,truth,metric_iou=0.3):
    n = len(pred)
    m = len(truth)

    if n == 0 and m == 0:
        return 1
    elif n == 0 or m == 0:
        return 0
    
    hit = np.zeros(m)
    TP = 0.
    FP = 0.
    FN = 0.
    for x,y,w,h,label in pred:
        bbox_pred = [x,y,w,h]
        iou = -1
        match = -1
        for j in range(m):
            if hit[j] == 0:
                bbox_truth = [truth[j][0],truth[j][1],truth[j][2],truth[j][3]]
                now = IOU(bbox_pred, bbox_truth)
            if now > iou:
                iou = now
                match = j
        if iou > metric_iou:
            if int(label) == int(truth[match][4]):
                TP += 1
            else:
                FN += 1
        else:
            FP += 1


    f1 = 2*TP/(float(m)+float(n))
    #print("TP :",TP)
    #print("########################")

    return f1
