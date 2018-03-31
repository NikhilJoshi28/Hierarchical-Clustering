from Agglomerative import hierarchical_agglomerative as ha
import random
import pickle

class hierarchical_divisive:
    def __init__(self):
        self.linkage_mat = []
        self.labels = []

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
            points = (new_clt[0][0],new_clt[1][0])
            return new_clt,similarity[new_clt[0][0]][new_clt[1][0]],points

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
            min_distance_points = 1000000
            for i in range(len(new_cluster[0])):
                for j in range(len(new_cluster[1])):
                    if similarity[new_cluster[0][i]][new_cluster[1][j]]<min_distance_points:
                        min_distance_points = similarity[new_cluster[0][i]][new_cluster[1][j]]
                        points = (i,j)

            return new_cluster,min_distance_points,points


    def divisive(self):
        data = self.get_data('data.festa')
        Ncluster = [[0]]
        for i in range(1,len(data)):
            Ncluster[0].append(i)

        id = 0
        while len(Ncluster)!=len(data):
            min_dis=1000000
            for cluster in Ncluster:
                if len(cluster)>1:
                    new_cltr,min_dis_bwClusters,points=self.K_medioids(cluster,2)
                    if min_dis>min_dis_bwClusters:
                        min_dis=min_dis_bwClusters
                        OptimalCluster = new_cltr
                        to_remove_cluster = cluster

            linkage_row = []
            no=0
            for clt in OptimalCluster:
                if clt!=None:
                    Ncluster.append(clt)
                    if len(clt)>1:
                        linkage_row.append(float(id))
                        id+=1
                    elif len(clt)==1:
                        linkage_row.append(float(id))
                        id+=1

                    no+=len(clt)

            linkage_row.append(float(min_dis))
            linkage_row.append(float(no))


            Ncluster.remove(to_remove_cluster)
            self.linkage_mat.append(linkage_row)


            """
                To print clustering distribution in each division (iteration)
            """
            #print((Ncluster))

        """
            For printing linkage matrix
        """
        self.labels = Ncluster
        self.linkage_mat = sorted(self.linkage_mat, key=lambda x: x[0])
        
if __name__== '__main__':
    hcd = hierarchical_divisive()
    hcd.divisive()
    #print(hcd.K_medioids([0,1,3,4,5,6,7,8,9],2))