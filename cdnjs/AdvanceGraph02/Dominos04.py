'''
Dominos

Dominos are lots of fun. Children like to stand the tiles on their side in long lines. When one domino falls, 
it knocks down the next one, which knocks down the one after that, all the way down the line.
However, sometimes a domino fails to knock the next one down. In that case, we have to knock it down by hand to get the dominos falling again.
Your task is to determine, given the layout of some domino tiles, the minimum number of dominos that must 
be knocked down by hand in order for all of the dominos to fall.

Input
The first line of input contains one integer specifying the number of test cases to follow.
Each test case begins with a line containing two integers,each no larger than 100000. The first integer n is the number of domino tiles and 
the second integer m is the number of lines to follow in the test case. The domino tiles are numbered from 1 to n.
Each of the following lines contains two integers x and y indicating that if domino number x falls, it will cause domino number y to fall as well.

Output
For each test case, output a line containing one integer, the minimum number of dominos that must be knocked over by hand in order for all the dominos to fall.

Sample Input
1
3 2
1 2
2 3

Sample Output
1

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

def dfs2(edges, src, visited):
    visited[src] = True
    for ele in edges[src]:
        if not visited[ele]:
            dfs2(edges, ele, visited)

def minNumOfDominos(edges, V):
    visited = [False for _ in range(V)]
    stack = deque()
    for i in range(V):
        if not visited[i]:
            dfs(edges, i, stack, visited)

    visited = [False for _ in range(V)]
    count = 0
    while stack:
        ele = stack.pop()
        if not visited[ele]:
            count += 1
            dfs2(edges, ele, visited)
    return count

tcs = int(input())
for tc in range(tcs):
    V, E = map(int, input().split())
    edges = [[] for _ in range(V)]
    for i in range(E):
        src, dst = map(int, input().split())
        edges[src-1].append(dst-1)
    print(minNumOfDominos(edges, V))

