import numpy as np
import os
import json
import pickle
import plotly.plotly as py
import plotly.figure_factory as ff


class hierachical_agglomerative:
    """
    	This function is used to parse datafile which is in festa format

    	In festa format each datapoint starts with > symbol following name of the datapoint

    	next lines consist of data about DNA or amino acid sequence with atmost 82 characters
    	in one line.

    	"""
    def read_festa(self,file):
        name = None
        seq = []
        for line in file:
            line = line.rstrip()
            if line.startswith(">"):
                if name: yield (name, ''.join(seq))
                name, seq = line, []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))

    """
    	
    	This Function parses data and stores it in the form of list with first attribute as name and 
    	second attribute as the string of sequence

    """
    def get_data_list(self,file_path):
        data_list = []
        with open(file_path) as file:
            for name, seq in self.read_festa(file):
                list = []
                list.append(name)
                list.append(seq)
                data_list.append(list)

        return data_list
        #print((data_list))
    """
		
		This functions return similarity between two DNA sequence 
		Similarity is calculated using dynamic programming algorithm 

		Time Complexity:  O(M*N)
		Space Complexity: O(M*N)

		where N is length of first string and M is the length of second string

    """
    
    def get_similarity(self,string1,string2):
        M = len(string2)+1
        N = len(string1)+1
        dp = [[0]*M for _ in range(N)]
        gap = 2
        x=0
        for i in range(1,len(string2)+1):
            dp[0][i]=dp[0][i-1]+gap
            x+=gap

        for j in range(1,len(string1)+1):
            dp[j][0]=(dp[j-1][0]+gap)


        for i in range(1,len(string1)+1):
            for j in range(1,len(string2)+1):
                score = 0
                if string2[j-1] == string1[i-1]:
                    score = 0
                else:
                    score = 1

                dp[i][j] = min((dp[i-1][j-1]+score),(dp[i-1][j]+gap),dp[i][j-1]+gap)

        #print(dp)
        #print(dp[N-1][M-1])
        return dp[N-1][M-1]

    def get_similarity_matrix(self,data):
        N = len(data)
        similarity_matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                print(i,j,data[i][0],data[j][0])
                if i<j:
                    similarity_matrix[i][j]=(similarity_matrix[j][i])
                if i == j :
                    similarity_matrix[i][j]=1
                else:
                    similarity_matrix[i][j]=(self.get_similarity(data[i][1],data[j][1]))

        pickle.dump(similarity_matrix,open("similarity_matrix.pkl","wb"),pickle.HIGHEST_PROTOCOL)
        return similarity_matrix

    def generate_sim_matrix(self):
        file_path = 'data.festa'
        data = self.get_data_list(file_path)
        similarity_matrix = self.get_similarity_matrix(data)


    def agglomerative(self):
        file_path = 'data.festa'
        data = self.get_data_list(file_path)
        similarity_file = "similarity_matrix.pkl"
        similarity = pickle.load(open(similarity_file,"rb"))
        cluster = []
        for i in range(len(similarity)):
            cluster.append([i])

        print(cluster)
        while len(cluster) != 1:
            min_data = 1000000
            min_x=0
            min_y=0
            for i in range(len(similarity)):
                for j in range(i+1,len(similarity[i])):
                    if min_data>similarity[i][j]:
                        min_data = similarity[i][j];
                        min_x = i
                        min_y = j

            cluster[min_x] = cluster[min_x]+cluster[min_y]
            del cluster[min_y]

            for i in range(len(similarity[0])):
                similarity[min_x][i] = min(similarity[min_x][i],similarity[min_y][i])

            del similarity[min_y]
            for row in similarity:
                del row[min_y]
            print(cluster)
		

if __name__ == '__main__':
    hca = hierachical_agglomerative()
    """To generate SIMILARITY matrix"""
    #hca.generate_sim_matrix()
    hca.agglomerative()