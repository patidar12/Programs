'''
Islands
Send Feedback
An island is a small piece of land surrounded by water . A group of islands is said to be connected if we can reach from any given island to any other island in the same group . Given N islands (numbered from 1 to N) and two lists of size M (u and v) denoting island u[i] is connected to island v[i] and vice versa . Can you count the number of connected groups of islands.
Constraints :
1<=N<=100
1<=M<=(N*(N-1))/2
1<=u[i],v[i]<=N
Input Format :
Line 1 : Two integers N and M
Line 2 : List u of size of M
Line 3 : List v of size of M
Output Return Format :
The count the number of connected groups of islands
Sample Input :
2 1
1
2
Sample Output :
1

'''
def BFS(arr,V,src,visited):
    queue = []
    queue.append(src)
    visited[src] = True
    while(len(queue) >= 1):
        node = queue.pop(0)
        for i in range(V):
            if(arr[node][i] == 1 and (not visited[i])):
                queue.append(i)
                visited[i] = True

def getAllConnectd(arr,V):
    visited = [False]*V
    count = 0
    for i in range(V):
        if(not visited[i]):
            BFS(arr,V,i,visited)
            count += 1
    return count

V,E = map(int,input().split())
arr = [[0 for i in range(V)] for j in range(V)]
first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]
for i in range(E):
    arr[first[i]-1][second[i]-1] = 1
    arr[second[i]-1][first[i]-1] = 1

result = getAllConnectd(arr,V)
print(result)
