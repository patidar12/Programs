'''
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Kruskal's algorithm.
For printing MST follow the steps -
1. In one line, print an edge which is part of MST in the format -
v1 v2 w
where, v1 and v2 are the vertices of the edge which is included in MST and whose weight is w. And v1 <= v2 i.e. print the smaller vertex first while printing an edge.
2. Print V-1 edges in above format in different lines.
Note : Order of different edges doesn't matter.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
Output Format :
MST
Constraints :
2 <= V, E <= 10^5
Sample Input 1 :
4 4
0 1 3
0 3 5
1 2 1
2 3 8
Sample Output 1 :
1 2 1
0 1 3
0 3 5


Note : need to try using union rank find algorithm to optimize solution
'''
## Read input as specified in the question.
## Print output as specified in the question.
class Edge:
    def __init__(self,v1,v2,weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

def findParrent(v1, parrent):
    while(v1 != parrent[v1]):
        v1 = parrent[v1]
    return v1
        
def kruskal(edge, V, E):
    parrent = [i for i in range(V)]
    output = [None]*(V-1)
    edge.sort(key = lambda v:v.weight)
    count = 0
    i = 0
    while(count < V-1 and i < E):
        e = edge[i]
        i += 1
        v1,v2,weight = e.v1,e.v2,e.weight
        p1 = findParrent(v1, parrent)
        p2 = findParrent(v2, parrent)
        if(p1 != p2):
            output[count] = e
            parrent[p1] = p2
            count += 1
            
    return output    
        
def printMST(result):
    for edge in result:
        if(edge.v1 < edge.v2):
            print(edge.v1, edge.v2, edge.weight)
        else:
            print(edge.v2, edge.v1, edge.weight)
def MST(edge, V, E):
    result = kruskal(edge, V, E)
    printMST(result)
        
        
V, E = map(int, input().split())
edge = [None]*E
for i in range(E):
    v1,v2,w = map(int, input().split())
    edge[i] = Edge(v1, v2, w)

MST(edge, V, E)

