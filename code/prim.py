from pqdict import PQDict
import networkx as nx

def primMST(G):
    """ Return MST of the given undirected graph"""
    vis = set()
    tot_weight = 0
    pq = PQDict()            
    Gprime = nx.Graph()
    
    ''' Add all nodes to PQDict with infinite distance'''
    for node in G.nodes():
        pq.additem(node, float("inf"))
    
    curr = pq.pop()    #Select initial node
    vis.add(curr)
    while len(pq) > 0:
        for s,nod, wt in G.edges(curr, data=True):
            if nod not in vis and wt['weight'] < pq[nod]: pq.updateitem(nod, wt['weight']) 
        
        if len(pq)>0:            
            top = pq.top()
            source,destination, dist = [data for data in sorted(G.edges(top, data=True), key=lambda (source,target,data): data['weight']) if data[1] in vis][0]
            Gprime.add_edge(source, destination, weight = dist['weight'])
            vis.add(top)
            tot_weight += pq[top]
            curr = pq.pop()
            
    return Gprime, tot_weight

def primWeight(G):
    """ Return MST of the given undirected graph"""
    vis = set()
    tot_weight = 0
    pq = PQDict()            
    
    for node in G.nodes():
        pq.additem(node, float("inf"))
    
    curr = pq.pop()
    vis.add(curr)
    while len(pq) > 0:
        for s,nod, wt in G.edges(curr, data=True):
            if nod not in vis and wt['weight'] < pq[nod]: pq.updateitem(nod, wt['weight']) 
        
        if len(pq)>0:
            top = pq.top()
            vis.add(top)
            tot_weight += pq[top]
            curr = pq.pop()
    return tot_weight