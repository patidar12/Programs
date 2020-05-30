'''
When Hanuman reached Lanka for the first time to see Sita Mata, he was caught by the soldiers of Lanka and was brought in front of the King of Lanka, Raavan. Just before, his tail was fired, he was given a problem by Raavan to solve and prove his strength. Raavan gave him a "tree", with N vertices. He also gave Hanuman, Q queries, and each query consisted of a node (vertex) and an integer d. For each query, Hanuman was asked to print the ancestor (vertex) of the node (vertex), such that the distance between node and ancestor vertices, is exactly d or print −1, when there exists no such ancestor (vertex) of node vertex. Hanuman found this problem time-consuming for him, and since he had to solve the problem in time limit, given by Raavan to him, please, help him solve the problem to prove his strength to Raavan.

Input:
The first line contains two integers, N (Number of Vertices, in the tree) and Q (Number of Queries).
Next N−1 lines contain two integers, u and v (1≤u,v≤N), denoting there is an edge between u and v vertices.
Next Q lines, contain node (vertex) and an integer, d .
Output:
Output Q lines, with the answer for each query.
Print −1, as the query answer, if there is no ancestor vertex of node vertex, with distance, exactly equal to d. Else, print ancestor (vertex) as the query answer.
Constraints:
1≤N,Q≤105
Sample Input:
6 3
1 2
1 3
2 4
2 5
3 6
4 2
6 3
5 1
Sample Output:
1
-1
2

'''

import math
class CalAncestor :
    def __init__(self):
        pass
    def initialization(self,n):
        self.height = int(math.ceil(math.log10(n) / math.log10(2)))
        self.table = [0] * (n + 1)
        i = 0
        while ( i < len(self.table)) :
            self.table[i] = [-1]*(self.height + 1)
            i = i + 1
    def fillTable(self, u, v):
        self.table[v][0] = u
        i = 1
        while ( i <= self.height) :
            self.table[v][i] = self.table[self.table[v][i - 1]][i - 1]
            if (self.table[v][i] == -1):
                break
            i = i + 1
    def getancestor(self, v, d):
        i = 0
        while ( i <= self.height) :
            if ((d& (1 << i)) != 0) :
                v = self.table[v][i]
                if (v == -1):
                    break
            i = i + 1

        return v


n,q = [int(x) for x in input().split()]
obj = CalAncestor()
obj.initialization(n)

for i in range(0,n-1):
    u,v = [int(x) for x in input().split()]
    obj.fillTable(u, v)
for i in range(0,q):
    v,d = [int(x) for x in input().split()]
    print(obj.getancestor(v, d))

