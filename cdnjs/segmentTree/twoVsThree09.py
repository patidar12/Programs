'''
2 vs 3

The fight for the best number in the globe is going to finally come to an end.The top two contenders for the best number are number 2 and number 3.
It's the final the entire world was waiting for. Expectorates from all across the globe came to witness the breath taking finals.
The finals began in an astonishing way.A common problem was set for both of them which included both these number.The problem goes like this.
Given a binary string (that is a string consisting of only 0 and 1). They were supposed to perform two types of query on the string.
Type 0: Given two indices l and r.Print the value of the binary string from l to r modulo 3.

Type 1: Given an index l flip the value of that index if and only if the value at that index is 0.
The problem proved to be a really tough one for both of them.Hours passed by but neither of them could solve the problem.
So both of them wants you to solve this problem and then you get the right to choose the best number in the globe.

Input:
The first line contains N denoting the length of the binary string .
The second line contains the N length binary string.Third line contains the integer Q indicating the number of queries to perform.
This is followed up by Q lines where each line contains a query.

Output:
For each query of Type 0 print the value modulo 3.
Constraints:

1<= N <=10^5

1<= Q <= 10^5

0 <= l <= r < N

Sample Input
5
10010
6
0 2 4
0 2 3
1 1
0 0 4
1 1
0 0 3

Sample Output
2
1
2
1


'''
def fastPow():
    p[0] = 1
    for i in range(1,100006):
        p[i] = (p[i-1]*2)%3

def buildTree(arr, tree, start, end, treeNode):

    if(start == end):
        tree[treeNode] = int(arr[start])
        return

    mid = (start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    tree[treeNode] = (p[end-mid] * tree[2*treeNode] + tree[2*treeNode+1])%3

def updateTree(arr,tree,start,end,treeNode,idx):

    if(start == end):
        if(arr[start] == '0'):
            arr[start] = '1'
            tree[treeNode] = int(arr[start])
        return

    mid = (start+end)//2
    if(idx > mid):
        updateTree(arr,tree,mid+1,end,2*treeNode+1,idx)
    else:
        updateTree(arr,tree,start,mid,2*treeNode,idx)
    tree[treeNode] = (p[end-mid] * tree[2*treeNode] + tree[2*treeNode+1])%3

def query(tree,start,end,treeNode,left,right):
    if(start > end):
        return 0
    if(end < left or start > right):
        return 0
    if(left <= start and right >= end):
        return (tree[treeNode] * p[right-end])%3
    mid = (start+end)//2
    l = query(tree,start,mid,2*treeNode,left,right)
    r = query(tree,mid+1,end,2*treeNode+1,left,right)
    return (l+r)%3


global p
p = [0]*(100006)
fastPow()
n = int(input())
arr = list(input())
tree = [0]*(4*n)
buildTree(arr,tree, 0, n-1, 1)
q = int(input())
for i in range(q):
    que = list(map(int,input().split()))
    if(que[0] == 0):
        ans = query(tree,0,n-1,1,que[1],que[2])
        print(ans)
    else:
        updateTree(arr,tree,0,n-1,1,que[1])

