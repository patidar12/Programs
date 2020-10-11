'''
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the Minimum Spanning Tree (MST) using Prim's algorithm.
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
0 1 3
1 2 1
0 3 5


Note : to optimize instead of adjacany matrix need to use adjacency list, and for finding min_key need to use priority queue(heap)(need to update priority queue when weight is updated)
'''

def minKey(weight,visited):
    min = 2**31
    min_index = -1
    for i in range(len(weight)):
        if(min > weight[i] and (not visited[i])):
            min = weight[i]
            min_index = i
    return min_index

def Prims(arr,V):
    parrent = [-1]*V
    weight = [2**31]*V
    visited = [False]*V
    weight[0] = 0
    count = 0
    while(count < V):
        count += 1
        min_index = minKey(weight,visited)
        visited[min_index] = True
        for i in range(V):
            if(arr[min_index][i] > 0 and (not visited[i]) and arr[min_index][i] < weight[i]):
                weight[i] = arr[min_index][i]
                parrent[i] = min_index
    result = [None]*(V-1)
    for i in range(1,V):
        result[i-1] = (i,parrent[i],weight[i])
    return result

V,E = map(int,input().split())
arr = [[0 for i in range(V)] for j in range(V)]
for i in range(E):
    v1,v2,w = map(int,input().split())
    arr[v1][v2] = w
    arr[v2][v1] = w

result = Prims(arr,V)
for edge in result:
    if(edge[0] < edge[1]):
        print(edge[0],edge[1],edge[2])
    else:
        print(edge[1],edge[0],edge[2])

