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

## Read input as specified in the question.
## Print output as specified in the question.

def minKey(dis, visited):
    index = -1
    min = 2**31
    for i in range(len(dis)):
        if(min > dis[i] and not visited[i]):
            min = dis[i]
            index = i
    return index

def prims(graph, V):
    visited = [False]*V
    dis = [2**31]*V
    dis[0] = 0
    for i in range(V):
        src = minKey(dis, visited)
        visited[src] = True
        for i in range(V):
            if(graph[src][i] > 0 and graph[src][i] + dis[src] < dis[i] and not visited[i]):
                dis[i] = graph[src][i] + dis[src]
    return dis

def printMST(result):
    for i in range(len(result)):
        print(i,result[i])

def MST(adjMatrix, V):
    result = prims(adjMatrix, V)
    printMST(result)

V, E = map(int, input().split())
adjMatrix = [[0 for i in range(V)] for _ in range(V)]
for i in range(E):
    fv,sv,w = map(int, input().split())
    adjMatrix[fv][sv] = w
    adjMatrix[sv][fv] = w

MST(adjMatrix, V)
