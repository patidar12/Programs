'''
Horrible Queries

World is getting more evil and it's getting tougher to get into the Evil League of Evil. Since the legendary Bad Horse has retired,
now you have to correctly answer the evil questions of Dr. Horrible, who has a PhD in horribleness (but not in Computer Science).
You are given an array of N elements, which are initially all 0. After that you will be given C commands. They are -

0 p q v - you have to add v to all numbers in the range of p to q (inclusive), where p and q are two indexes of the array.

1 p q - output a line containing a single integer which is the sum of all the array elements between p and q (inclusive)

Input
In the first line you'll be given T, number of test cases.

Each test case will start with N (N <= 100 000) and C (C <= 100 000). After that you'll be given C commands in the format as mentioned above. 1 <= p, q <= N and 1 <= v <= 10^7.

Output
Print the answers of the queries.

Input:
1
8 6
0 2 4 26
0 4 8 80
0 4 5 20
1 8 8 
0 5 7 14
1 4 8

Output:
80  
508

'''

# tree, lazy tree, start, end (0 to n-1), left, right (range), treeNode, increment value
def updateTree(tree,lazy, start, end,left,right, treeNode, inc):
    if(start > end):
        return
    if(lazy[treeNode] != 0):
        tree[treeNode] += (end-start+1)*lazy[treeNode]
        if(start != end):
            lazy[2*treeNode] += lazy[treeNode]
            lazy[2*treeNode + 1] += lazy[treeNode]
        lazy[treeNode] = 0
    # no overlap
    if(end < left or start > right ):
        return
    # complete overlap
    if(left <= start and right >= end):
        tree[treeNode] += (end-start+1)*inc
        if(start != end):
            lazy[2*treeNode] += inc
            lazy[2*treeNode+1] += inc
        return
    # partial overlap
    mid = (start+end)//2
    updateTree(tree,lazy, start, mid,left,right, 2*treeNode, inc)
    updateTree(tree,lazy, mid+1, end,left,right, 2*treeNode+1, inc)
    tree[treeNode] = tree[2*treeNode] + tree[2*treeNode+1]

def query(tree,lazy, start, end,left,right, treeNode):
    if(start > end):
        return 0
    # no overlap
    if(end < left or start > right ):
        return 0
    if(lazy[treeNode] != 0):
        tree[treeNode] += (end - start + 1)*lazy[treeNode]
        if(start != end):
            lazy[2*treeNode] += lazy[treeNode]
            lazy[2*treeNode + 1] += lazy[treeNode]
        lazy[treeNode] = 0

    # complete overlap
    if(left <= start and right >= end):
        return tree[treeNode]
    # partial overlap
    mid = (start+end)//2
    l = query(tree,lazy, start, mid,left,right, 2*treeNode)
    r = query(tree,lazy, mid+1, end,left,right, 2*treeNode+1)
    return l+r

tcs = int(input())
for tc in range(tcs):
    n, q = map(int, input().split())
    # Tree 4*N size, started from 1st index
    tree = [0]* (4*n)
    lazy = [0]* (4*n)
    for i in range(q):
        que = [int(x) for x in input().split()]
        if(que[0] == 0):
            updateTree(tree,lazy,0,n-1,que[1]-1,que[2]-1,1,que[3])
        else:
            ans = query(tree,lazy,0,n-1,que[1]-1,que[2]-1,1)
            print(ans)

