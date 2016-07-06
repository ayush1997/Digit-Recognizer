import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from digit import *
import time

def pca(X,Y):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    pca= PCA(n_components=3)
    start_time = time.time()
    reduced_X = pca.fit_transform(X)
    print("--- %spca fit time seconds ---" % (time.time() - start_time))

    print reduced_X

    # x_0,x_1,x_2,x_3,x_4,x_5,x_6,x_7,x_8,x_9,y_0,y_1,y_2,y_3,y_4,y_5,y_6,y_7,y_8,y_9,z_0,z_1,z_2,z_3,z_4,z_5,z_6,z_7,z_8,z_9 = ([] for i in range(30))
    # for i in range(len(reduced_X)):
    #     if Y[i] == 1:
    #         x_1.append(reduced_X[i][0])
    #         y_1.append(reduced_X[i][1])
    #         z_1.append(reduced_X[i][2])
    #     elif Y[i] ==2:
    #         x_2.append(reduced_X[i][0])
    #         y_2.append(reduced_X[i][1])
    #         z_2.append(reduced_X[i][2])
    #     elif Y[i] ==3:
    #         x_3.append(reduced_X[i][0])
    #         y_3.append(reduced_X[i][1])
    #         z_3.append(reduced_X[i][2])
    #     elif Y[i] ==4:
    #         x_4.append(reduced_X[i][0])
    #         y_4.append(reduced_X[i][1])
    #         z_4.append(reduced_X[i][2])
    #     elif Y[i] ==5:
    #         x_5.append(reduced_X[i][0])
    #         y_5.append(reduced_X[i][1])
    #         z_5.append(reduced_X[i][2])
    #     elif Y[i] ==6:
    #         x_6.append(reduced_X[i][0])
    #         y_6.append(reduced_X[i][1])
    #         z_6.append(reduced_X[i][2])
    #     elif Y[i] ==7:
    #         x_7.append(reduced_X[i][0])
    #         y_7.append(reduced_X[i][1])
    #         z_7.append(reduced_X[i][2])
    #     elif Y[i] ==8:
    #         x_8.append(reduced_X[i][0])
    #         y_8.append(reduced_X[i][1])
    #         z_8.append(reduced_X[i][2])
    #     elif Y[i] ==9:
    #         x_9.append(reduced_X[i][0])
    #         y_9.append(reduced_X[i][1])
    #         z_9.append(reduced_X[i][2])
    #     elif Y[i] ==0:
    #         x_0.append(reduced_X[i][0])
    #         y_0.append(reduced_X[i][1])
    #         z_0.append(reduced_X[i][2])
    #
    #
    # ax.scatter(x_0,y_0,z_0,c='r',marker="d")
    # ax.scatter(x_1,y_1,z_1,c='g',marker="1")
    # ax.scatter(x_2,y_2,z_2,c='b',marker="2")
    # ax.scatter(x_3,y_3,z_3,c='y',marker="3")
    # ax.scatter(x_4,y_4,z_4,c='m',marker="4")
    # ax.scatter(x_5,y_5,z_5,c='c',marker="<")
    # ax.scatter(x_6,y_6,z_6,c='w',marker="h")
    # ax.scatter(x_7,y_7,z_7,c='k',marker="+")
    # ax.scatter(x_8,y_8,z_8,c='b',marker="8")
    # ax.scatter(x_9,y_9,z_9,c='r',marker="p")
    # plt.show()

    return reduced_X
