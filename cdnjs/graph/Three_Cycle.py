'''
3 Cycle
Send Feedback
Given a graph with N vertices (numbered from 1 to N) and Two Lists (U,V) of size M where (U[i],V[i]) and (V[i],U[i]) are connected by an edge , then count the distinct 3-cycles in the graph. A 3-cycle PQR is a cycle in which (P,Q), (Q,R) and (R,P) are connected an edge.
Input Format :
Line 1 : Two integers N and M
Line 2 : List u of size of M
Line 3 : List v of size of M
Return Format :
The count the number of 3-cycles in the given Graph
Constraints :
1<=N<=100
1<=M<=(N*(N-1))/2
1<=u[i],v[i]<=N
Sample Input:
3 3
1 2 3
2 3 1
Sample Output:
1

'''

def getThreeCycles(arr,V):
    count = 0
    for i in range(V):
        for j in range(V):
            if(i != j and arr[i][j] == 1):
                for k in range(V):
                    if(i != k and j!= k and arr[j][k] == 1 and arr[k][i] == 1):
                        count += 1
    return count//6
V,E = map(int,input().split())
arr = [[0 for i in range(V)] for j in range(V)]
first = [int(x) for x in input().split()]
second = [int(x) for x in input().split()]
for i in range(E):
    arr[first[i]-1][second[i]-1] = 1
    arr[second[i]-1][first[i]-1] = 1

result = getThreeCycles(arr,V)
print(result)
