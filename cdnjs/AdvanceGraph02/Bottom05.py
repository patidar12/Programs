'''
BOTTOM

We will use the following (standard) definitions from graph theory. Let V be a non-empty and finite set, 
its elements being called vertices (or nodes). Let E be a subset of the Cartesian product V×V, its elements
being called edges. Then G=(V,E) is called a directed graph.

Let n be a positive integer, and let p=(e1,…,en) be a sequence of length n of edges ei∈E such that ei=(vi,vi+1)
for a sequence of vertices (v1,…,vn+1). Then p is called a path from vertex v1 to vertex vn+1 in G and we say 
that vn+1 is reachable from v1, writing (v1→vn+1).

Here are some new definitions. A node v in a graph G=(V,E) is called a sink, if for every node w in G that is 
reachable from v, v is also reachable from w. The bottom of a graph is the subset of all nodes that are sinks, 
i.e., bottom(G)={v∈V∣∀w∈V:(v→w)⇒(w→v)}. You have to calculate the bottom of certain graphs.

Input Specification
The input contains several test cases, each of which corresponds to a directed graph G. Each test case starts 
with an integer number v, denoting the number of vertices of G=(V,E) where the vertices will be identified by
the integer numbers in the set V={1,…,v}. You may assume that 1≤v≤5000. That is followed by a non-negative integer e
and, thereafter, e pairs of vertex identifiers v1,w1,…,ve,we with the meaning that (vi,wi)∈E. There are no edges other
than specified by these pairs. The last test case is followed by a zero.

Output Specification
For each test case output the bottom of the specified graph on a single line. To this end, print the numbers of all 
nodes that are sinks in sorted order separated by a single space character. If the bottom is empty, print an empty line.

Sample Input
3 3
1 3 2 3 3 1
2 1
1 2
0

Sample Output
1 3
2

'''

## Read input as specified in the question.
## Print output as specified in the question.
from collections import deque
def dfs(edges, src, stack, visited):
    visited[src] = True
    for ele in edges[src]:
        if not visited[ele]:
            dfs(edges, ele, stack, visited)
    stack.append(src)

def dfs2(edges, src, components, comp, visited):
    visited[src] = True
    components[src] = comp
    for ele in edges[src]:
        if not visited[ele]:
            dfs2(edges, ele, components, comp, visited)

def getSCC(edges, edgesT, V):
    visited = [False for _ in range(V)]
    stack = deque()
    for i in range(V):
        if not visited[i]:
            dfs(edges, i, stack, visited)

    visited = [False for _ in range(V)]
    components = [0]*V
    comp = 0
    sol = [False]*V
    while stack:
        ele = stack.pop()
        if not visited[ele]:
            dfs2(edgesT, ele,components, comp, visited)
            sol[comp] = True
            comp += 1
    for i in range(V):
        for j in edges[i]:
            if components[i] != components[j]:
                sol[components[i]] = False
                break
    for i in range(V):
        if sol[components[i]]:
            print(i+1, end = ' ')


while(True):
    ve = input().strip()
    while(ve == ''):
        ve = input().strip()
    if(ve[0] == '0'):
        break
    V, E = map(int, ve.split())
    edges = [[] for _ in range(V)]
    edgesT = [[] for _ in range(V)]
    for i in range(E):
       src, dst = map(int, input().split())
       edges[src-1].append(dst-1)
       edgesT[dst-1].append(src-1)
    getSCC(edges, edgesT, V)
    print()
