import matplotlib.pyplot as plt
import matplotlib.cm as cm
import pandas as pd
import numpy as np



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
    print df.describe()
    # print df.head()

    return df



if __name__ == '__main__':
    df = load()
    df = np.array(df)

    X = df[:,1:]
    Y = df[:,0]
    # plot_digit(X)
