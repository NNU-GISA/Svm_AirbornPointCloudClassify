from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import MyHelper
import FileOperator

f = open(".\FeatureVectors.txt",'a')
f.seek(0)
f.truncate()
f.close()

print("-----trees-----")
tree_array=np.zeros((10,2))#创建
for i in range(1,11):

    p= np.loadtxt("./points/new_trees/tree"+str(i)+".txt")
    print('No.',str(i),MyHelper.GetFeatureVector(p))
    v = MyHelper.GetFeatureVector(p)
    tree_array[i-1,:]=v[0,:]
    tree=plt.scatter(v[0,0],v[0,1],c = 'g')

    FileOperator.WriteData(".\FeatureVectors.txt",v,1)

print('tree_array.shape: ',tree_array.shape)



print("-----buildings-----")
building_array=np.zeros((10,2))
for i in range(1,11):
    p= np.loadtxt("./points/new_building/building"+str(i)+".txt")
    print('No.',str(i),MyHelper.GetFeatureVector(p))
    v = MyHelper.GetFeatureVector(p)
    tree_array[i-1, :] = v[0,:]
    # print(tree_array[i-1,:])
    building=plt.scatter(v[0,0],v[0,1],c = 'r')
    FileOperator.WriteData(".\FeatureVectors.txt",v,-1)

print('building_array.shape: ',building_array.shape)
plt.legend([tree,building],['tree','building'],)


#绘制
# plt.figure()
# tree=plt.scatter(tree_array[:,0],tree_array[:,1],c='g')
# building=plt.scatter(building_array[:,0],building_array[:,1],c='r')
# plt.legend([tree,building],['tree','building'])

plt.show()
