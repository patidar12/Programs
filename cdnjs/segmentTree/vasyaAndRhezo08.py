'''
Vasya vs Rhezo

Queen Vasya is preparing for a war against Rhezo. She has N warriors in total arranged in a line.
Let us number the warriors by numbers from 1 to N. She will fight Rhezo's army for Q days,
and each day she can choose only one warrior.
For each warrior, we know 2 values associated with him, let us call these A and B. Each day Vasya 
can choose her warrior from a range Li to Ri, she must choose the warrior with maximum A value.
If there is more than 1 warrior having the same maximum A value, she chooses the warrior with minimum B value.
If still there is more than 1 warrior with same maximum A value and same minimum B value, she chooses the one with lower index in line.
You being the hand of Queen Vasya, need to help her in choosing the warrior for each day.

Input:

First line contains a single integer N, denoting the number of warriors Queen Vasya has. 
Second line contains N space separated integers Ai. Third line contains N space separated integers Bi.
Next line contains a single integer Q, denoting the number of days Queen Vasya chooses a warrior. 
Each of the next Q lines contains 2 integers Li and Ri.

Output:

For each Li and Ri, print the index of the warrior that Queen Vasya should choose.

Constraints:
1≤ N,Q ≤10^6
1≤ Ai,Bi ≤10^9
1≤Li≤Ri

Sample Input
5
1 8 4 6 8
4 8 6 3 7
4
1 4
2 4
3 4
1 5

Sample Output
2
2
4
5

'''

class Node:
    def __init__(self):
        self.first = -2**31
        self.second = 2**31
        self.index = 2**31

def buildTree(arr, tree, start, end, treeNode):

    if(start == end):
        tree[treeNode].first = arr[start].first
        tree[treeNode].second = arr[start].second
        tree[treeNode].index = start
        return

    mid = (start+end)//2
    buildTree(arr, tree, start, mid, 2*treeNode)
    buildTree(arr, tree, mid+1, end, 2*treeNode+1)
    left = tree[2*treeNode]
    right = tree[2*treeNode+1]
    curr = tree[treeNode]
    if(left.first > right.first):
        curr.first = left.first
        curr.second = left.second
        curr.index = left.index
    elif(left.first < right.first):
        curr.first = right.first
        curr.second = right.second
        curr.index = right.index
    else:
        if(left.second < right.second):
            curr.first = left.first
            curr.second = left.second
            curr.index = left.index
        elif(left.first > right.first):
            curr.first = right.first
            curr.second = right.second
            curr.index = right.index
        else:
            curr.first = right.first
            curr.second = right.second
            if(left.index < right.index):
                curr.index = left.index
            else:
                curr.index = right.index

def query(tree, start, end, treeNode, left, right):
    if(start > end):
        return Node()

    if(end < left or start > right):
        return Node()
    if(left <= start and right >= end):
        return tree[treeNode]

    mid = (start + end) // 2
    le = query(tree, start, mid, 2*treeNode, left, right)
    ri = query(tree, mid+1, end, 2*treeNode+1, left, right)
    curr = Node()
    if(le.first > ri.first):
        curr.first = le.first
        curr.second = le.second
        curr.index = le.index
    elif(le.first < ri.first):
        curr.first = ri.first
        curr.second = ri.second
        curr.index = ri.index
    else:
        if(le.second < ri.second):
            curr.first = le.first
            curr.second = le.second
            curr.index = le.index
        elif(le.first > ri.first):
            curr.first = ri.first
            curr.second = ri.second
            curr.index = ri.index
        else:
            curr.first = ri.first
            curr.second = ri.second
            if(le.index < ri.index):
                curr.index = le.index
            else:
                curr.index = ri.index
    return curr

n = int(input())
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
arr = [Node() for x in range(n)]
for i in range(n):
    arr[i].first = A[i]
    arr[i].second = B[i]
    arr[i].index = i
tree = [Node() for x in range(4*n)]
buildTree(arr,tree,0,n-1,1)
q = int(input())
for i in range(q):
    left,right = map(int,input().split())
    ans = query(tree,0,n-1,1,left-1,right-1)
    print(ans.index+1)

