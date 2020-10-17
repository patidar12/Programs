'''
Implement kosarajus algorithm to found Strongle connected components(SCC).
Directed Graph

Input Format:
First line contain two number V, E
V -> number of vertex
E -> number of edges
next E lines contain two number a b
i.e edges from a to b

Output Format:
print all connected components in different line


Input:
6 7
1 2
2 3
3 4
4 1
3 5
5 6
6 5

Output:
1 4 3 2 
5 6

Input:

10 12
1 2
2 3
3 4
4 1
3 5
5 6
6 7
7 5
8 6
8 9
9 8
9 10

Output:
8 9 
10 
1 4 3 2 
5 7 6

'''

from collections import deque
def dfs(edges, src, stack, visited):
    visited[src] = True
    for ele in edges[src]:
        if not visited[ele]:
            dfs(edges, ele, stack, visited)
    stack.append(src)

def dfs2(edges, src, comp, visited):
    visited[src] = True
    comp.append(src)
    for ele in edges[src]:
        if not visited[ele]:
            dfs2(edges, ele, comp, visited)

def getSCC(edges, edgesT, V):
    visited = [False for _ in range(V)]
    stack = deque()
    for i in range(V):
        if not visited[i]:
            dfs(edges, i, stack, visited)

    visited = [False for _ in range(V)]
    components = []
    while stack:
        ele = stack.pop()
        if not visited[ele]:
            comp = []
            dfs2(edgesT, ele, comp, visited)
            components.append(comp)
    return components


V, E = map(int, input().split())
edges = [[] for _ in range(V)]
edgesT = [[] for _ in range(V)]
for i in range(E):
    src, dst = map(int, input().split())
    edges[src-1].append(dst-1)
    edgesT[dst-1].append(src-1)
components = getSCC(edges, edgesT, V)
for comp in components:
    for ele in comp:
        print(ele+1,end = ' ')
    print()
