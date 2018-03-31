import numpy as np
from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram
import matplotlib.pyplot as plt
from Agglomerative import hierarchical_agglomerative as ha
from divisive import  hierarchical_divisive as hd
import pickle

class HCA_dendrogram:
    def plot_dendrogram_agglomerative(self):
        similarity = pickle.load(open("similarity_matrix.pkl", "rb"))
        hca = ha()
        hca.agglomerative()
        print(np.array(hca.link_mat))
        data = hca.get_data_list('data.festa')
        Y = []
        for i in range(len(data)):
            Y.append(i)

        print(len(np.array(hca.link_mat)),len(Y))

        dendrogram(np.array(hca.link_mat),
                   color_threshold=1,
                   labels=Y,
                   show_leaf_counts=True,
                   orientation='right')
        plt.show()

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
    dendro.plot_dendrogram_agglomerative()
