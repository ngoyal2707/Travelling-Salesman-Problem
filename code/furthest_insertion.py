'''
Created on Nov 20, 2014

Furthest Insertion Greedy Approach
This approach has two step
    *Selection
    *Insertion
Selection step chooses a node which is at the maximum distance from visited nodes.
Then in insertion step we find a location in obtained path which minimizes the total cost of cycle.

'''
from pqdict import PQDict
import readData as read

'''Find Minimum Cost and Location of insertion'''
def minCost(G,path,node):
    min_cost = float('inf')# initialize cost as infinity
    loc = -1
    if len(path) > 1:# We can insert only if there is more than one node in chosen path
        for pos in range(len(path)):
            cost = G.edge[path[pos]][node]['weight'] + G.edge[node][path[pos+1]]['weight'] - G.edge[path[pos]][path[pos+1]]['weight'] if pos+1 < len(path) \
                   else G.edge[path[pos]][node]['weight'] + G.edge[node][path[0]]['weight'] - G[path[pos]][path[0]]['weight']  
            if cost < min_cost: 
                min_cost = cost
                loc = pos+1
    else:# If only one node is in the visited list then only option is to insert new node at the end
        min_cost = G.edge[path[0]][node]['weight'] + G.edge[node][path[0]]['weight']
        loc = 1
    return loc,min_cost
'''Farthest Insertion method'''
def greedy_approx(G):
    """ Return MST of the given undirected graph"""
    vis = set()
    tot_weight = 0
    pq = PQDict()            
    path = []
    
    '''Initialize Priority Queue which will help us find Farthest node after distance is calcualted from visited node''' 
    for node in G.nodes():
        pq.additem(node, float("-inf"))
    
    curr = pq.pop()
    vis.add(curr)
    path.append(curr)
    while len(pq) > 0:
        for s,nod, wt in G.edges(curr, data=True):
            '''Distance calculation'''
            if nod not in vis and -wt['weight'] > pq[nod]: pq.updateitem(nod, -wt['weight']) 
        
        if len(pq)>0:
            ''' Selection Step'''
            top = pq.top()
            vis.add(top)
            curr = pq.pop()
            ''' Insertion Step'''
            loc,cost = minCost(G,path,top)
            '''Insert into the location found by minCost()'''
            path.insert(loc, top)
            tot_weight += cost
            
    return path,tot_weight
