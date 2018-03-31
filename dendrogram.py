import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt
from Agglomerative import hierarchical_agglomerative as ha
from divisive import  hierarchical_divisive as hd
import pickle

class HCA_dendogram:
    def plot_dendogram_agglomerative(self):
        similarity = pickle.load(open("similarity_matrix.pkl", "rb"))
        hca = ha()
        hca.agglomerative()
        print(np.array(hca.link_mat))
        data = hca.get_data_list('data.festa')
        Y = []
        for i in range(len(data)):
            Y.append(i)

        dendrogram(hca.dendogram(),
                   color_threshold=1,
                   labels=Y,
                   show_leaf_counts=True,
                   orientation='right')
        plt.show()

if __name__ == "__main__":
    dendo = HCA_dendogram()
    dendo.plot_dendogram_agglomerative()
