#画出3d点云
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import sys
def pyplot_draw_point_cloud(points, output_filename=None):
    """ points is a Nx3 numpy array """
    fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    ax = Axes3D(fig)
    ax.scatter(points[:, 0], points[:, 1], points[:, 2],c='b',marker='.',s=2,linewidth=0,alpha=1,cmap='spectral')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    plt.show()
    # savefig(output_filename)
points=np.loadtxt('./points/tree/tree1.txt')
pyplot_draw_point_cloud(points)

