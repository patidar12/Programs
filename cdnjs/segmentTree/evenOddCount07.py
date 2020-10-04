'''

Counting Even/Odd

Ashu and Shanu are best buddies. One day Shanu gives Ashu a problem to test his intelligence.He gives him an array of N natural numbers and asks him to solve the following queries:-

Query 0 :- modify the element present at index i to x.
Query 1:- count the number of even numbers in range l to r inclusive.
Query 2:- count the number of odd numbers in range l to r inclusive.

Input:
First line of the input contains the number N. Next line contains N natural numbers. 
Next line contains an integer Q followed by Q queries.

0 x y - modify the number at index x to y. 

1 x y - count the number of even numbers in range l to r inclusive.

2 x y - count the number of odd numbers in range l to r inclusive.

Constraints:
1<=N,Q<=10^5

1<=l<=r<=N 

0<=Ai<=10^9

1<=x<=N

0<=y<=10^9

Note:-
indexing starts from 1.

Sample Input
6
1 2 3 4 5 6
4
1 2 5
2 1 4
0 5 4
1 1 6

Sample Output
2
2
4

'''
'''
Note:
we can create for evenCount only
and for oddCount we can subtract evenCount from total Count in range

'''

class TreeNode:
    def __init__(self):
        self.even = 0
        self.odd = 0

def buildTree(arr, tree ,start, end, treeNode):

    if(start == end):
        if(arr[start] % 2 == 0):
            tree[treeNode].even = 1
        else:
            tree[treeNode].odd = 1
        return

    mid = (start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    tree[treeNode].even = tree[2*treeNode].even + tree[2*treeNode+1].even
    tree[treeNode].odd = tree[2*treeNode].odd + tree[2*treeNode+1].odd

def updateTree(arr, tree, start, end, treeNode, idx, val):

    if(start == end):
        arr[idx] = val
        if(val % 2 == 0):
            tree[treeNode].even = 1
            tree[treeNode].odd = 0
        else:
            tree[treeNode].odd = 1
            tree[treeNode].even = 0
        return

    mid = (start + end)//2
    if(idx > mid):
        updateTree(arr, tree, mid+1,end,2*treeNode+1,idx,val)
    else:
        updateTree(arr,tree,start,mid,2*treeNode,idx,val)

    tree[treeNode].even = tree[2*treeNode].even + tree[2*treeNode+1].even
    tree[treeNode].odd = tree[2*treeNode].odd + tree[2*treeNode+1].odd


def evenCount(tree,start,end,treeNode,left,right):
    if(start > end):
        return 0
    # outside from range
    if(end < left or start > right):
        return 0
    # inside in range
    if(start >= left and end <= right):
        return tree[treeNode].even
    # partially inside or outside
    mid = (start+end)//2
    leftCount = evenCount(tree,start,mid,2*treeNode,left,right)
    rightCount = evenCount(tree,mid+1,end,2*treeNode+1,left,right)
    return leftCount + rightCount


def oddCount(tree,start,end,treeNode,left,right):
    if(start > end):
        return 0
    # outside from range
    if(end < left or start > right):
        return 0
    # inside in range
    if(start >= left and end <= right):
        return tree[treeNode].odd
    # partially inside or outside
    mid = (start+end)//2
    leftCount = oddCount(tree,start,mid,2*treeNode,left,right)
    rightCount = oddCount(tree,mid+1,end,2*treeNode+1,left,right)
    return leftCount + rightCount


n = int(input())
arr = [int(x) for x in input().split()]
tree = [TreeNode() for x in range(4*n)]
buildTree(arr,tree,0,n-1,1)
query = int(input())
for i in range(query):
    q,x,y = map(int,input().split())
    if(q == 0):
        updateTree(arr, tree, 0, n-1, 1, x-1, y)
    elif(q == 1):
        ans = evenCount(tree, 0, n-1, 1, x-1, y-1)
        print(ans)
    else:
        ans = oddCount(tree, 0, n-1, 1, x-1, y-1)
        print(ans)
