'''
Given an undirected, connected and weighted graph G(V, E) with V number of vertices (which are numbered from 0 to V-1) and E number of edges.
Find and print the shortest distance from the source vertex (i.e. Vertex 0) to all other vertices (including source vertex also) using Dijkstra's Algorithm.
Print the ith vertex number and the distance from source in one line separated by space. Print different vertices in different lines.
Note : Order of vertices in output doesn't matter.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next E lines : Three integers ei, ej and wi, denoting that there exists an edge between vertex ei and vertex ej with weight wi (separated by space)
Output Format :
In different lines, ith vertex number and its distance from source (separated by space)
Constraints :
2 <= V, E <= 10^5
Sample Input 1 :
4 4
0 1 3
0 3 5
1 2 1
2 3 8
Sample Output 1 :
0 0
1 3
2 4
3 5

Note : to optimize instead of adjacany matrix need to use adjacency list, and for finding min_key need to use priority queue(heap)(need to update priority queue when dist is updated)
'''
def min_key(dist,visited):
    min_index = -1
    min = 2**31
    for i in range(len(dist)):
        if(min > dist[i] and (not visited[i])):
            min = dist[i]
            min_index = i
    return min_index

def Dijkstra(arr,V):
    visited = [False]*V
    dist = [2**31]*V
    dist[0] = 0
    count = 0
    while(count < V-1):
        count += 1
        min_index = min_key(dist,visited)
        visited[min_index] = True
        for i in range(V):
            if((arr[min_index][i] != 0) and (not visited[i]) and (dist[i] > (dist[min_index]+arr[min_index][i]))):
                dist[i] = dist[min_index]+arr[min_index][i]

    return dist            
V,E = map(int,input().split())
arr = [[0 for x in range(V)] for y in range(V)]
for i in range(E):
    v1,v2,w = map(int,input().split())
    arr[v1][v2] = w
    arr[v2][v1] = w   
   
result = Dijkstra(arr,V)
for i in range(V):
    print(i,result[i])

