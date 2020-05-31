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

def getParrent(parrent,v1):
    while(v1 != parrent[v1]):
        v1 = parrent[v1]
    return v1

def getMST(arr,V):
    parrent = [0]*V
    for i in range(V):
        parrent[i] = i
    arr.sort(key = lambda x:x[2])
    count = 0
    output = [None]*(V-1)
    i = 0
    while(count < V-1 and i < len(arr)):
        v1,v2,w = arr[i]
        i += 1
        p1 = getParrent(parrent,v1)
        p2 = getParrent(parrent,v2)
        if(p1 != p2):
            if(v1 < v2):
                output[count] = (v1,v2,w)
            else:
                output[count] = (v2,v1,w)
            count += 1
            parrent[p1] = p2
    return output

V,E = map(int,input().split())
arr = []
for i in range(E):
    v1,v2,w = map(int,input().split())
    arr.append((v1,v2,w))
result = getMST(arr,V)
for edge in result:
    print(edge[0],edge[1],edge[2])

