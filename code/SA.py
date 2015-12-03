'''
Created on Dec 3, 2014

@author:

Simulated annealing code for finding solution for tsp.  
'''
import networkx as nx
import readData
import sys
import time
import random
import math
from Approximation import mst_approx

''' finding the distance of the tour'''
def weight(path, G):
	length = 0
	for i in range(0, len(path) - 1):
		length = length + G.get_edge_data(path[i], path[i+1])['weight']
	length = length + G.get_edge_data(path[0], path[-1])['weight']
	return length

''' two swap move'''
def two_swap(nodes):
	length = len(nodes) - 1
	idx1 = random.randint(0, length)
	idx2 = random.randint(idx1, length)
	new_nodes = nodes[:idx1] + nodes[idx1:idx2][::-1] + nodes[idx2:]
	return new_nodes

''' SA code
 when reaches to local minima, temperature is increased again and this approach gives good results.
 
 Tried varying with cooling parameter also, then the algorithm terminates faster but the solution is not that good.
'''
def SA(nodes, T, T_min, r, G,cutoff,ftrace):
	T_init=T
	global_best_nodes=nodes
	global_best_distance=weight(nodes, G)
	start_time = time.clock()
	while True:
		
		elapsed_time = time.clock() - start_time
		if elapsed_time>cutoff:
			return global_best_nodes

		new_nodes = two_swap(nodes)
		bestDistanceSoFar=weight(nodes, G)
		dE = -(weight(new_nodes, G) - bestDistanceSoFar)
		if dE > 0:
			nodes = new_nodes
			if bestDistanceSoFar<global_best_distance:
				global_best_nodes=nodes
				global_best_distance=weight(global_best_nodes, G)
				ftrace.write("{0:.2f}".format(elapsed_time*1.0)+','+str(global_best_distance)+'\n')
		else:
			if math.exp(dE / T) > random.random():
				nodes = new_nodes
		T = T * r
		if T < T_min:
			T=T_init*0.1
	return global_best_nodes

def simulated_annealiing(G,seed,cutoff,ftrace):
# 	G, optimal = readData.createGraph(sys.argv[1])
	nodes = G.nodes()
	random.seed(seed)
	random.shuffle(nodes)
	
	nodes,_=mst_approx(G)
	T =  G.get_edge_data(max(G.edges())[0], max(G.edges())[1])['weight'] * len(G.nodes())
	r =  0.9999
	final_nodes = SA(nodes, T, 0.0001, r, G,cutoff,ftrace)
# 	print weight(final_nodes, G), optimal
	return final_nodes, weight(final_nodes, G)

# print simulated_annealiing()
