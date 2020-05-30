'''
Code : Get Path - BFS
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), find and print the path from v1 to v2 (if exists). Print nothing if there is no path between v1 and v2.
Find the path using BFS and print the shortest path available.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Print the path in reverse order. That is, print v2 first, then intermediate vertices and v1 at last.
Note : Save the input graph in Adjacency Matrix.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
Line (E+2) : Two integers v1 and v2 (separated by space)
Output Format :
Path from v1 to v2 in reverse order (separated by space)
Constraints :
2 <= V <= 1000
1 <= E <= 1000
0 <= v1, v2 <= V-1
Sample Input 1 :
4 4
0 1
0 3
1 2
2 3
1 3
Sample Output 1 :
3 0 1
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3

'''

def getPath(arr,src,dst,V):
    queue = []
    map = {}
    visited = [False]*V
    queue.append(src)
    visited[src] = True
    while(len(queue) >= 1):
        ele = queue.pop(0)
        for i in range(V):
            if(ele != i and arr[ele][i] == 1):
                if(not visited[i]):
                    map[i] = ele
                    queue.append(i)
                    visited[i] = True
                    if(i == dst):
                        return map
    return map

V,E = map(int,input().split())
arr = [[0 for i in range(V)] for j in range(V)]
for i in range(E):
    first,second = map(int,input().split())
    arr[first][second] = 1
    arr[second][first] = 1

src,dst = map(int,input().split())
map = getPath(arr,src,dst,V)
flag = False
while(dst in map):
   flag = True
   print(dst,end = ' ')
   dst = map[dst]

if(flag):
    print(dst)
