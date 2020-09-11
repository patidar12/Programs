'''
GFG:
    https://www.geeksforgeeks.org/hamiltonian-cycle-backtracking-6/
 
Hamiltonian Path in an undirected graph is a path that visits each vertex exactly once.
A Hamiltonian cycle (or Hamiltonian circuit) is a Hamiltonian Path such that there is an 
edge (in the graph) from the last vertex to the first vertex of the Hamiltonian Path.
Determine whether a given graph contains Hamiltonian Cycle or not.

Input:
A 2D array graph[V][V] where V is the number of vertices in graph and graph[V][V] is adjacency matrix representation of the graph. A value graph[i][j] is 1 if there is a direct edge from i to j, otherwise graph[i][j] is 0.

Output:
An array path[V] that should contain the Hamiltonian Path. path[i] should represent the ith vertex in the Hamiltonian Path. The code should also return false if there is no Hamiltonian Cycle in the graph.

For Input:
2
4 5
1 2 2 3 3 4 2 4 1 4
4 3
1 2 2 3 2 4
Your Output is:
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

def isCycle(g,path,V,pos):
    if(pos == V):
        if(g[path[pos-1]][path[0]] == 1):
            return True
        return False
    for v in range(0,V):
        if(isSafe(v,pos,g,path)):
            path[pos] = v
            if(isCycle(g,path,V,pos+1)):
                return True
            path[pos] = -1
    return False

def isHamiltonCycle(g,V):
    path = [-1]*V
    path[0] = 0
    if(isCycle(g,path,V,1)):
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
