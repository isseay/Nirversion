# -*- coding: UTF-8 -*-

"""
    非极大值抑制算法测试

    @author : isseay
    @create on 2017/7/18
"""

import numpy as np
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

fig, ax1 = plt.subplots(1,1,figsize=(12,12))
ax1.set_xlim((0, 10))
ax1.set_ylim((0, 10))

color=['r','g','b']


def Rectanle(coor, ax, i):
    line1 = [(coor[0], coor[1]), (coor[2], coor[1])]
    line2 = [(coor[0], coor[1]), (coor[0], coor[3])]
    line3 = [(coor[0], coor[3]), (coor[2], coor[3])]
    line4 = [(coor[2], coor[3]), (coor[2], coor[1])]

    (line1x, line1y) = zip(*line1)
    (line2x, line2y) = zip(*line2)
    (line3x, line3y) = zip(*line3)
    (line4x, line4y) = zip(*line4)

    ax.add_line(Line2D(line1x, line1y, color=color[i]))
    ax.add_line(Line2D(line2x, line2y, color=color[i]))
    ax.add_line(Line2D(line3x, line3y, color=color[i]))
    ax.add_line(Line2D(line4x, line4y, color=color[i]))




#Rectanle(line_coor[0,:], ax1, 0)
#Rectanle(line_coor[1,:], ax1, 1)
#Rectanle(line_coor[2,:], ax1, 2)





"""
def NMS(rect, overlapThreshold):
    x1 = rect[:,0]
    y1 = rect[:,1]
    x2 = rect[:,2]
    y2 = rect[:,3]

    score = rect[:,4]
    sotd = np.argsort(score)[::-1]
    is_suppressed = []

    #  计算面积
    area = (x2-x1+1)*(y2-y1+1)

    numbox = rect.shape[0]

    for i in np.arange(numbox):
        is_suppressed.append(sotd[i])

        xmax1 = np.maximum(x1[sotd[i]], x1[sotd[1:]])
        xmin2 = np.minimum(x2[sotd[i]], x2[sotd[1:]])
        ymax1 = np.maximum(y1[sotd[i]], y1[sotd[1:]])
        ymin2 = np.minimum(y2[sotd[i]], y2[sotd[1:]])

        overlapx = xmin2 - xmax1 + 1
        overlapy = ymin2 - ymax1 + 1
        inter = overlapx*overlapy
        if( overlapx > 0) and (overlapy > 0):
            overlapprob = inter/(area[sotd[i]]+area[sotd[1:]]-inter)
            inds = np.where(overlapprob <= overlapThreshold)[0]
            sotd = sotd[inds + 1]

    print is_suppressed

    count = 0
    for i in np.arange(numbox):
        if is_suppressed[i] != 1:
            count += 1

    index = 0
    ret = np.zeros((count, 4))
    for i in np.arange(numbox):
        if is_suppressed[i] != 1:
            ret[index, 0] = rect[sotd[i],0]
            ret[index, 1] = rect[sotd[i], 1]
            ret[index, 2] = rect[sotd[i], 2]
            ret[index, 3] = rect[sotd[i], 3]
            index += 1

    return ret



rect = NMS(line_coor, 0.1)


rs = rect.shape[0]
for i in np.arange(rs):
    Rectanle(rect[i, :], ax1, 0)
"""
line_coor = np.array([
                    [1,7,6,3, 0.99],
                    [2,6,5,2, 0.8],
                    [4,5,7,1, 0.82]])

def py_cpu_nms(dets, thresh):
    """Pure Python NMS baseline."""
    x1 = dets[:, 0]
  #  print x1
    y1 = dets[:, 1]
   # print y1
    x2 = dets[:, 2]
   # print x2
    y2 = dets[:, 3]
    #print y2
    scores = dets[:, 4]
   # print scores

    areas = (x2 - x1 + 1) * (y2 - y1 + 1)
    #print areas
    # 从大到小排列，取index
    order = scores.argsort()[::-1]
    #print order
    # keep为最后保留的边框
    keep = []
    while order.size > 0:
        # order[0]是当前分数最大的窗口，之前没有被过滤掉，肯定是要保留的
        i = order[0]
        keep.append(i)
        # 计算窗口i与其他所以窗口的交叠部分的面积
        xx1 = np.maximum(x1[i], x1[order[1:]])
        print xx1
        yy1 = np.maximum(y1[i], y1[order[1:]])
        print '-----------------------------------'
        print yy1
        xx2 = np.minimum(x2[i], x2[order[1:]])
        print '-----------------------------------'
        print xx2
        yy2 = np.minimum(y2[i], y2[order[1:]])
        print '-----------------------------------'
        print yy2

        w = np.maximum(0.0, xx2 - xx1 + 1)
        print '-----------------------------------'
        print w
        h = np.maximum(0.0, yy2 - yy1 + 1)
        print '-----------------------------------'
        print h
        inter = w * h
       # print inter
        # 交/并得到iou值
        ovr = inter / (areas[i] + areas[order[1:]] - inter)
        print 'over'
        print ovr
        # ind为所有与窗口i的iou值小于threshold值的窗口的index，其他窗口此次都被窗口i吸收
        inds = np.where(ovr <= thresh)[0]
        # 下一次计算前要把窗口i去除，所有i对应的在order里的位置是0，所以剩下的加1
        order = order[inds + 1]

    return keep


keeep = py_cpu_nms(line_coor, 0.1)
print keeep
plt.plot()
#plt.show()



