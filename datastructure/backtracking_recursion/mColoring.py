'''
GFG: Practice(Backtracking)
    https://www.geeksforgeeks.org/m-coloring-problem-backtracking-5/


Given an undirected graph and an integer M. The task is to determine if the graph can be colored with at most M colors such that no two adjacent vertices of the graph are colored with the same color. Here coloring of a graph means assignment of colors to all vertices. Print 1 if it is possible to colour vertices and 0 otherwise.

Vertex are 1-based (vertext number starts with 1, not 0).

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case consists of four lines. The first line of each test case contains an integer N denoting the number of vertices. The second line of each test case contains an integer M denoting the number of colors available. The third line of each test case contains an integer E denoting the number of edges available. The fourth line of each test case contains E pairs of space separated integers denoting the edges between vertices.

Output:
Print the desired output.

Constraints:
1 <= T <= 30
1 <= N <= 50
1 <= E <= N*(N-1)
1 <= M <= N

Example:
Input :
2
4
3
5
1 2 2 3 3 4 4 1 1 3
3
2
3
1 2 2 3 1 3

Output:
1
0

Explanation:
Testcase 1: It is possible to colour the given graph using 3 colours.


'''


# Python

#code
def isSafe(vertices,V,g,i,v):
    for j in range(V):
        if(g[v][j] == 1 and vertices[j] == i ):
            return False
    return True

def fillColour(vertices,V,C,g,v):
    if(v == V):
        return True
    for i in range(C):
        if(isSafe(vertices,V,g,i+1,v)):
            vertices[v] = i+1
            if(fillColour(vertices,V,C,g,v+1)):
                return True
            vertices[v] = 0
    return False

def isFilled(V,C,E,g):
    vertices = [0]*(V)
    return fillColour(vertices,V,C,g,0)


tcs = int(input())
for tc in range(tcs):
    V = int(input())
    C = int(input())
    E = int(input())
    edges = [int(x) for x in input().split()]
    g = [[0 for x in range(V)] for y in range(V)]
    for i in range(0,2*E,2):
        a = edges[i]
        b = edges[i+1]
        g[a-1][b-1] = 1
        g[b-1][a-1] = 1
    if(isFilled(V,C,E,g)):
        print(1)
    else:
        print(0)
