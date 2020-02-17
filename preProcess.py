#读取txt文件的前三列数据
import numpy as np
import sys
import os
# 读入txt文件的坐标
def changPoint(filename):

    a=np.loadtxt(filename)
    print(a.shape)
    point=a[:,0:3]
    print(point.shape)
    np.savetxt(filename, point)

if __name__ == '__main__':
    for i in range(1,7):
        changPoint('./points/new_test1/'+str(i)+'.txt')