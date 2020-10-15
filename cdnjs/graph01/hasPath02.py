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

## Read input as specified in the question.
## Print output as specified in the question.


class Graph:
    def __init__(self,V):
        self.adjMat = [[0 for i in range(V)] for _ in range(V)]
        self.V = V
    def addEdge(self,fv, sv):
        self.adjMat[fv][sv] = 1
        self.adjMat[sv][fv] = 1
    def hasPath(self,visited,src,dst):
        visited[src] = True
        if(src == dst):
            return True
        for i in range(self.V):
            if(self.adjMat[src][i] == 1 and not visited[i]):
                if(self.hasPath(visited,i,dst)):
                    return True
        return False

V, E = map(int,input().split())
g = Graph(V)
for i in range(E):
    fv, sv = map(int,input().split())
    g.addEdge(fv, sv)
src, dst = map(int,input().split())
visited = [False]*V
if(g.hasPath(visited,src,dst)):
    print('true')
else:
    print('false')
