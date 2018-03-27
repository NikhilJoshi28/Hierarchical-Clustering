from Agglomerative import hierarchical_agglomerative as ha
import random
import pickle

class hierarchical_divisive:
    def get_data(self,file_path):
        hca = ha()
        return hca.get_data_list(file_path)

    def K_medioids(self,cluster,no_cluster):
        similarity = pickle.load(open("similarity_matrix.pkl", "rb"))
        v = []
        new_centroids= []
        N = len(cluster)

        if N==2:
            new_clt = [[],[]]
            new_clt[0].append((cluster[0]))
            new_clt[1].append((cluster[1]))
            return new_clt

        else:
            ran_sample = random.sample(range(0,N-1),no_cluster)
            for i in range(no_cluster):
                v.append(cluster[ran_sample[i]])
                new_centroids.append(-1)

            point_distance = []
            for i in range(no_cluster):
                dis = []
                for j in range(N):
                    dis.append(similarity[v[i]][cluster[j]])
                point_distance.append(dis)

            while True :
                new_cluster = [[] for _ in range(no_cluster)]
                for i in range(len(cluster)):
                    min_dis = 10000
                    for j in range(no_cluster):
                        if point_distance[j][i]<min_dis:
                            min_dis = point_distance[j][i]
                            index = j

                    new_cluster[index].append(cluster[i])

                for i in range(no_cluster):
                    new_cluster[i].sort()
                    new_centroids[i]=new_cluster[i][int(len(new_cluster[i])/2)]

                if v==new_centroids:
                    break
                else:
                    v=new_centroids

            #print('#',v,new_cluster)
            return new_cluster


    def divisive(self):
        data = self.get_data('data.festa')
        Ncluster = [[0]]
        for i in range(1,len(data)):
            Ncluster[0].append(i)

        while len(Ncluster)!=len(data):
            for cluster in Ncluster:
                if len(cluster)>1:
                    new_cltr=self.K_medioids(cluster,2)
                    #print(new_cltr)
                    for clt in new_cltr:
                        if clt!=None:
                            Ncluster.append(clt)

                    Ncluster.remove(cluster)
                    break
            print((Ncluster))



if __name__== '__main__':
    hcd = hierarchical_divisive()
    hcd.divisive()
    #print(hcd.K_medioids([0,1,3,4,5,6,7,8,9],2))