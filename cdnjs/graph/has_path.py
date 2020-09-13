'''
Code : Has Path
Send Feedback
Given an undirected graph G(V, E) and two vertices v1 and v2(as integers), check if there exists any path between them or not. Print true or false.
V is the number of vertices present in graph G and vertices are numbered from 0 to V-1.
E is the number of edges present in graph G.
Input Format :
Line 1: Two Integers V and E (separated by space)
Next E lines : Two integers a and b, denoting that there exists an edge between vertex a and vertex b (separated by space)
Line (E+2) : Two integers v1 and v2 (separated by space)
Output Format :
true or false
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
true
Sample Input 2 :
6 3
5 3
0 1
3 4
0 3
Sample Output 2 :
false

'''

ef hasPath(arr,src,dst,visited,V):
    visited[src] = True
    if(src == dst):
        return True
    for i in range(V):
        if(arr[src][i] == 1):
            if(not visited[i]):
                if(hasPath(arr,i,dst,visited,V)):
                    return True

    return False

V,E  = map(int, input().split())
arr = []
for i in range(V):
    arr.append([0]*V)

for i in range(E):
    first,second = map(int,input().split())
    arr[first][second] = 1
    arr[second][first] = 1

src, dst = map(int, input().split())
visited = [False]*V
print('true' if hasPath(arr,src,dst,visited,V) else 'false')
