'''
Code : BFS Traversal
Send Feedback
Given an undirected and disconnected graph G(V, E), print its BFS traversal.
Here you need to consider that you need to print BFS path starting from vertex 0 only.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Note : 1. Take graph input in the adjacency matrix.
2. Handle for Disconnected Graphs as well
Input Format :
Line 1: Two Integers V and E (separated by space)
Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
Output Format :
BFS Traversal (separated by space)
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
0 1 3 2

'''

def printBFS(adjMat, V, visited, src):
    q = []
    q.append(src)
    visited[src] = True
    while q:
        val = q.pop(0)
        print(val,end = ' ')
        for i in range(V):
            if(adjMat[val][i] == 1 and not visited[i]):
                q.append(i)
                visited[i] = True


def BFS(adjMat, V):
    visited = [False]*V
    for i in range(V):
        if(not visited[i]):
            printBFS(adjMat, V, visited, i)
    print()
            
def printDFS(adjMat, V, visited, src):
    print(src,end = ' ')
    visited[src] = True
    for i in range(V):
        if(adjMat[src][i] == 1 and not visited[i]):
            printDFS(adjMat, V, visited, i)
            

def DFS(AdjMat, V):
    visited = [False]*V
    for i in range(V):
        if(not visited[i]):
            printDFS(adjMat, V, visited, i)
    


V,E = map(int,input().split())
adjMat = [[0 for i in range(V)] for _ in range(V)]
for i in range(E):
    a, b = map(int, input().split())
    adjMat[a][b] = 1 
    adjMat[b][a] = 1
    
BFS(adjMat, V)
#DFS(adjMat, V)
