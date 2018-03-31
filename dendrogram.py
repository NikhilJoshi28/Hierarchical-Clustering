import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt
from Agglomerative import hierarchical_agglomerative as ha
from divisive import  hierarchical_divisive as hd
import pickle

class HCA_dendrogram:
    """
        Below functions is used to plot dendogram agglomerative
        we obtain linkage-matrix which is stored in class instance variable which
        calculating agglomerative approach
        we obtain lables which is basically data names indexed from 1 to N where N is no of datapoints
    """

    def plot_dendrogram_agglomerative(self):
        hca = ha()
        hca.agglomerative()
        print(np.array(hca.link_mat))
        data = hca.get_data_list('data.festa')
        Y = []
        for i in range(len(data)):
            Y.append(i)

        dendrogram(np.array(hca.link_mat),
                   color_threshold=1,
                   labels=Y,
                   show_leaf_counts=True,
                   orientation='right')
        plt.show()

    def plot_dendrogram_divisive(self):
        hcd = hd()
        hcd.divisive()
        print(np.array(hcd.linkage_mat))
        dendrogram(np.array(hcd.linkage_mat),
                   color_threshold=1,
                   labels=hcd.labels,
                   show_leaf_counts=True,
                   orientation='left')

        plt.show()

if __name__ == "__main__":
    dendro = HCA_dendrogram()
    """
        To plot agglomerative dendrogram 
    """
    dendro.plot_dendrogram_agglomerative()
    """
        to plot divisive dendrogram
    """
    #dendro.plot_dendrogram_divisive()
