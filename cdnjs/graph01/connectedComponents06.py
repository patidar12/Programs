'''
Code : All connected components
Send Feedback
Given an undirected graph G(V,E), find and print all the connected components of the given graph G.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
You need to take input in main and create a function which should return all the connected components. And then print them in the main, not inside function.
Print different components in new line. And each component should be printed in increasing order (separated by space). Order of different components doesn't matter.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next 'E' lines, each have two space-separated integers, 'a' and 'b', denoting that there exists an edge between Vertex 'a' and Vertex 'b'.
Output Format :
Different components in new line
Constraints :
2 <= V <= 1000
1 <= E <= 1000
Sample Input 1:
4 2
0 1
2 3
Sample Output 1:
0 1 
2 3 
Sample Input 2:
4 3
0 1
1 3 
0 3
Sample Output 2:
0 1 3 
2

'''

def DFS(arr,V,visited,comp):
    visited[V] = True
    comp.append(V)
    for i in range(len(arr)):
        if(arr[V][i] == 1):
            if(not visited[i]):
                DFS(arr,i,visited,comp)

def getAllConnected(arr,V):
    visited = [False]*V
    result = []
    for i in range(V):
        if(not visited[i]):
            comp = []
            DFS(arr,i,visited,comp)
            comp.sort()
            result.append(comp)
    return result


V,E = map(int,input().split())
arr = [[0 for i in range(V)] for j in range(V)]
for i in range(E):
    first,second = map(int,input().split())
    arr[first][second] = 1
    arr[second][first] = 1

result = getAllConnected(arr,V)
for comp in result:
    for v in comp:
        print(v,end = ' ')
    print()
