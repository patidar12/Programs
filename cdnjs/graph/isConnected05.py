'''
Code : Is Connected ?
Send Feedback
Given an undirected graph G(V,E), check if the graph G is connected graph or not.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
Output Format :
"true" or "false"
Constraints :
2 <= V <= 1000
1 <= E <= 1000
Sample Input 1:
4 4
0 1
0 3
1 2
2 3
Sample Output 1:
true
Sample Input 2:
4 3
0 1
1 3 
0 3
Sample Output 2:
false 

'''
def DFS(arr,V,src,visited):
    visited[src] = True
    for i in range(V):
        if(arr[src][i] == 1):
            if(not visited[i]):
                DFS(arr,V,i,visited)

def isConnected(arr,V):
    visited = [False]*V
    DFS(arr,V,0,visited)
    for i in visited:
        if(not i):
            return 'false'
    return 'true'

V,E = map(int,input().split())
arr = [[0 for i in range(V)] for j in range(V)]
for i in range(E):
    first,second = map(int,input().split())
    arr[first][second] = 1
    arr[second][first] = 1

print(isConnected(arr,V))
