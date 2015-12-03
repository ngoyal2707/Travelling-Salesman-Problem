'''
Created on Nov 30, 2014

@author: 

Hill climbing approach as local search method for tsp.

Neighbour search : t opt (if cannot find two opt, go further and find 3 opt if possible)
Random Perturbation: double bridge move

'''
import random
import time
from Approximation import mst_approx

''' find the cost of the whole tour'''
def findCost(G,tour):
    cost=0
    if(len(tour)==1):
        return 0
    for i,node in enumerate(tour):
        if i<len(tour)-1:
            cost+=G.get_edge_data(tour[i],tour[i+1])['weight']
    cost+=G.get_edge_data(tour[i],tour[0])['weight']
    return cost

''' two swap moves'''
def two_swap(tour,city1,city2):
    newTour=[]
    for i in xrange(city1):
        newTour.append(tour[i])
    for i in xrange(city2,city1-1,-1):
        newTour.append(tour[i])
    for i in xrange(city2+1,len(tour)):
        newTour.append(tour[i])
    return newTour

''' one out of possible three swap moves'''
def three_swap(tour,city1,city2,city3):
    newTour=[]
    for i in xrange(city1):
        newTour.append(tour[i])
    for i in xrange(city3,city2-1,-1):
        newTour.append(tour[i])
    for i in xrange(city1,city2,1):
        newTour.append(tour[i])
    for i in xrange(city3+1,len(tour)):
        newTour.append(tour[i])

    return newTour  

''' double bridge move for random perturbation'''
def randomPerturbation(tour):
    cities=random.sample(range(0,len(tour)),4)
    cities.sort()
    c1,c2,c3,c4=cities[0],cities[1],cities[2],cities[3]
    tour1,tour2,tour3,tour4=[],[],[],[]
    length=len(tour)
    i=c1
    while i!=c2:
        tour1.append(tour[i])
        i=(i+1)%length
    i=c2
    while i!=c3:
        tour2.append(tour[i])
        i=(i+1)%length
    
    i=c3
    while i!=c4:
        tour3.append(tour[i])
        i=(i+1)%length
    
    i=c4
    while i!=c1:
        tour4.append(tour[i])
        i=(i+1)%length
        
    newtour = tour1+ tour3[::-1]+tour4[::-1]+tour2

    return newtour
    
    
'''main code for running two opt local search'''
def two_opt(G,seed,cutoff,ftrace):
    tour=G.nodes()
    random.seed(seed)
    random.shuffle(tour)
#     tour,_=mst_approx(G)
    
    nodeCount=len(tour)
    bestDistanceSoFar=findCost(G, tour)
    bestTour=tour
    count=0
    start_time = time.time()
    
    
    while True:
        
        lastBest=bestDistanceSoFar

        for i in xrange(nodeCount):
            for j in xrange(i+1,nodeCount):

#              First find
                newTour=two_swap(tour,i,j)
                newDistance=findCost(G, newTour)
#                 print newDistance
                if newDistance<bestDistanceSoFar:
                    tour=newTour
                    bestDistanceSoFar=newDistance
                    bestTour=newTour
                    ftrace.write("{0:.2f}".format(time.time()-start_time)+','+str(bestDistanceSoFar)+'\n')
                    elapsed_time = time.time() - start_time
                    if elapsed_time>cutoff:
                        return bestTour,bestDistanceSoFar


        foundGood=False     
        if bestDistanceSoFar==lastBest:
            for i in xrange(nodeCount):
                for j in xrange(i+1,nodeCount):
                    for k in xrange(j+1,nodeCount):
                        
                        elapsed_time = time.time() - start_time
                        if elapsed_time>cutoff:
                            return bestTour,bestDistanceSoFar
                        
                        newTour=three_swap(tour,i,j,k)
                        newDistance=findCost(G, newTour)
                      

                        if newDistance<bestDistanceSoFar:
                            tour=newTour
                            bestDistanceSoFar=newDistance
                            ftrace.write("{0:.2f}".format(time.time()-start_time)+','+str(bestDistanceSoFar)+'\n')
                            bestTour=newTour
                            foundGood=True
                    if foundGood==True:
                            break
                if foundGood==True:
                            break
                            

#       Random perturbation
        if bestDistanceSoFar==lastBest:
            count+=1
        else:
            count=0
        if count>3:
            tour=randomPerturbation(bestTour)
                            
    return bestTour,bestDistanceSoFar
