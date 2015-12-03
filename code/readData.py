import networkx as nx
from math import sqrt, cos, acos

def findDistance(i,j,point,type):
    if(type.lower()=='euc_2d'):
        return (long)(sqrt((point[i][0]-point[j][0])*(point[i][0]-point[j][0])+(point[i][1]-point[j][1])*(point[i][1]-point[j][1]))+0.5)
    elif(type.lower()=='geo'):
        PI = 3.141592;

        deg = (int)(point[i][0]) 
        min1 = point[i][0]- deg; 
        lat1 = PI * (deg + 5.0 * min1/ 3.0) / 180.0; 
        
        deg = (int)(point[i][1]); 
        min1 = point[i][1]- deg; 
        long1 = PI * (deg + 5.0 * min1/ 3.0) / 180.0; 
  
        deg = (int)(point[j][0]) 
        min1 = point[j][0]- deg; 
        lat2 = PI * (deg + 5.0 * min1/ 3.0) / 180.0; 
        
        deg = (int)(point[j][1]); 
        min1 = point[j][1]- deg; 
        long2 = PI * (deg + 5.0 * min1/ 3.0) / 180.0; 
  
        RRR = 6378.388;
        q1 = cos( long1  - long2)
        q2 = cos( lat1 - lat2 )
        q3 = cos( lat1 + lat2)
        dij = (int) ( RRR * acos( 0.5*((1.0+q1)*q2 - (1.0-q1)*q3) ) + 1.0)
        return dij
    
def createGraph(fileName):    
    with open(fileName) as fin:
        G = nx.Graph()
        lines=fin.readlines()
        i=0
        while not lines[i].split(':')[0].lstrip().lower()=='dimension':
            i+=1
        dimension=int(lines[i].split(':')[1].lstrip())
        while not lines[i].split(':')[0].lstrip().rstrip().lower()=='edge_weight_type':
            i+=1
        type=lines[i].split(':')[1].lstrip().rstrip()
        
        while not lines[i].split(':')[0].lstrip().rstrip().lower()=='optimal_cost':
            i+=1
        optimal=lines[i].split(':')[1].lstrip().rstrip()
        
        while not lines[i].split(':')[0].lstrip().rstrip().lower()=='node_coord_section':
            i+=1
        i+=1
        
        points={}
        for line in lines[i:]:
            line=' '.join(line.split())
            if(len(line.split(' '))==3):
                city,x,y=line.split(' ')
                city=int(city)
                x=float(x)
                y=float(y)
                points[city]=(x,y)
            else:
                break

        for i in xrange(1,dimension+1):
            for j in xrange(1,dimension+1):
                if i!=j:
                    G.add_edge(i,j, weight=findDistance(i,j,points,type))
            
    return G,int(optimal)

