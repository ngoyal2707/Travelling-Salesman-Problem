'''
Created on Nov 20, 2014

@author: 

MST 2-Approximation algorithm for tsp.

'''


import sys
import time

import prim
import readData


'''
DFS search of the graph nodes
'''
def dfs(G, i,visited,record):
    visited[i - 1] = True
    record.append(i)
    for s, t, w in G.edges(i, data=True):
        if visited[t - 1] == False:
            dfs(G, t,visited,record)
	
'''
main function to calculate the approximated tsp tour and it's length
'''
def mst_approx(G):
    start_time = time.time()
    T, non = prim.primMST(G)
    
    visited = [False] * len(T)
    record = []

    dfs(T, 1,visited,record)
	# print record
    length = 0
    for i in xrange(len(record) - 1):
	    length += G.get_edge_data(record[i], record[i + 1])['weight']
    length = length + G.get_edge_data(record[0], record[-1])['weight']

    total_time = (time.time() - start_time)
#     print total_time, length, optimal, float(length - int(optimal)) / float(optimal)
    return record, length

