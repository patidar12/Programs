'''
GFG: Practice
    https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/

A Hamiltonian path, is a path in an undirected or directed graph that visits each vertex exactly once. Given an undirected graph  the task is to check if a Hamiltonian path is present in it or not.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. Each test case contains two lines. The first line consists of two space separated integers N and M denoting the number of vertices and number of edges.Then in the next line are M space separated pairs u,v denoting an edge from u to v.

Output:
For each test case in a new line print 1 if a Hamiltonean path exists else print 0.

Constraints:
1<=T<=100
1<=N<=10
1<=M<=15

Example:
Input:
2
4 4
1 2 2 3 3 4 2 4
4 3
1 2 2 3 2 4
Output:
1
0


'''

#code
def isSafe(v,pos,g,path):
    if(g[path[pos-1]][v] == 0):
        return False
    for vertax in path:
        if(v == vertax):
            return False
    return True
def allVisited(path):
    for val in path:
        if(val == False):
            return False
    return True

def isCycle(g,path,V,pos):
    path[pos] = True
    if(allVisited(path)):
        return True
    for v in range(0,V):
        if(g[pos][v] == 1 and path[v] == False):
            if(isCycle(g,path,V,v)):
                return True
    path[pos] = False
    return False

def isHamiltonCycle(g,V):
    for i in range(V):
        path = [False]*V
        if(isCycle(g,path,V,i)):
            return 1
    return 0

tcs = int(input())
for tc in range(tcs):
    n,m = map(int, input().split())
    arr = [int(x) for x in input().split()]
    g = [[0 for x in range(n)] for y in range(n)]
    for i in range(0,2*m,2):
        x,y = arr[i], arr[i+1]
        g[x-1][y-1] = 1
        g[y-1][x-1] = 1
    print(isHamiltonCycle(g,n))
