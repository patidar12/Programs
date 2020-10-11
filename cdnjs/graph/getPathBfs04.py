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

Sample Output 2 :


'''

## Read input as specified in the question.
## Print output as specified in the question.

class Graph:
    def __init__(self, V):
        self.adjMat = [[0 for i in range(V)] for _ in range(V)]
        self.v = V
    def addEdge(self, fv, sv):
        self.adjMat[fv][sv] = 1
        self.adjMat[sv][fv] = 1
    def findPath(self, src, dst):


        if(self.adjMat[src][dst] == 1 and src == dst):
            ans = []
            ans.append(src)
            return ans
        visited = [False]*self.v
        map = {}
        q = []
        q.append(src)
        visited[src] = True
        while q:
            ele = q.pop(0)
            for i in range(self.v):
                if(self.adjMat[ele][i] == 1 and not visited[i]):
                    q.append(i)
                    visited[i] = True
                    map[i] = ele
                    if(i == dst):
                        ans = []
                        ans.append(dst)
                        val = map[dst]
                        while(val != src):
                            ans.append(val)
                            val = map[val]
                        ans.append(val)
                        return ans

V, E = map(int, input().split())
g = Graph(V)
for i in range(E):
    fv, sv = map(int, input().split())
    g.addEdge(fv, sv)

src, dst = map(int, input().split())

ans = g.findPath(src, dst)
if ans:
    for ele in ans:
        print(ele, end = ' ')

