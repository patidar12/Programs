'''
Check given graph is Bipartite or not
Bipartite:
We have to color a graph with two different colors
and make sure that two adjacent node not have same color

Input:
5 5
0 1
1 2
2 3
3 4
0 4

Output:
False

Input:
4 4
0 1
1 3
2 3
0 2

Output:
True

'''

from collections import deque
def bipartite(edges, V):
    # two sets for storing red and black color nodes
    sets = [[] for _ in range(2)]
    # for storing the pending nodes
    pending = deque()
    # start with vertex 0
    pending.append(0)
    sets[0].append(0)
    while pending:
        curr = pending.pop()
        currentSet = 0 if sets[0].count(curr) > 0 else 1
        for ele in edges[curr]:
            if(sets[0].count(ele) == 0 and sets[1].count(ele) == 0):
                sets[1-currentSet].append(ele)
                pending.append(ele)
            elif(sets[currentSet].count(ele) > 0):
                return False
    return True

def dfs(edges, src, c, color):
    if(color[src] != -1 and color[src] != c):
        return False
    if(color[src] != -1):
        return True
    color[src] = c
    for ele in edges[src]:
        if not dfs(edges, ele, 1 - c, color):
            return False
    return True

V, E = map(int, input().split())
edges = [[] for _ in range(V)]
for i in range(E):
    fv, sv = map(int, input().split())
    edges[fv].append(sv)
    edges[sv].append(fv)

result = bipartite(edges, V)
#color = [-1]*V
#result = dfs(edges, 0, 0, color)
print(result)
