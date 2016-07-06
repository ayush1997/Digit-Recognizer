import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import scale
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
import time
from sklearn.decomposition import PCA
from mpl_toolkits.mplot3d import Axes3D
from pca import *
import csv as csv


#This function reshapes the pixel arrays ti digits and plot them
def plot_digit(X):

    counter =1
    for i in range(1,4):
        for j in range(1,6):
            plt.subplot(3,5,counter)
            plt.imshow(X[(i-1)*4000 + j].reshape((28,28)),cmap=cm.Greys_r)
            plt.axis('off')
            counter+=1
    plt.show()

def load():
    df = pd.read_csv("train.csv",delimiter=",",header=0)
    # print df.describe()
    # print df.head()

    return df





if __name__ == '__main__':
    start_time = time.time()
    df = load()
    print("--- %sload time seconds ---" % (time.time() - start_time))
    df = np.array(df)

    X = df[:,1:]
    Y = df[:,0]
    # plot_digit(X)
    X = X/255.0 * 2 -1

    # reduced_X = pca(X,Y)
    # model(reduced_X,Y)

    model(X,Y)
