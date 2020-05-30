'''
Minimum In SubArray
Send Feedback
Range Minimum Query
Given an array A of size N, there are two types of queries on this array.
1) q l r: In this query you need to print the minimum in the sub-array A[l:r].
2) u x y: In this query you need to update A[x]=y.
Input:
First line of the test case contains two integers, N and Q, size of array A and number of queries.
Second line contains N space separated integers, elements of A.
Next Q lines contain one of the two queries.
Output:
For each type 1 query, print the minimum element in the sub-array A[l:r].
Contraints:
1≤N,Q,y≤10^5
1≤l,r,x≤N
Sample Input :
5 5
1 5 2 4 3
q 1 5
q 1 3
q 3 5
u 3 6
q 1 5
Sample Output :
1
1
2
1

'''
def buildTree(arr,tree,start,end,treeNode):
    if(start == end):
        tree[treeNode] = arr[start]
        return
    mid  = (start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    tree[treeNode] = min(tree[2*treeNode],tree[2*treeNode+1])

def update(arr,tree,start,end,treeNode,idx,val):
    if(start == end):
        arr[start] = val
        tree[treeNode] = val
        return
    mid = (start+end)//2
    if(idx > mid):
        update(arr,tree,mid+1,end,2*treeNode+1,idx,val)
    else:
        update(arr,tree,start,mid,2*treeNode,idx,val)
    tree[treeNode] =  min(tree[2*treeNode],tree[2*treeNode+1])

def getMin(tree,start,end,treeNode,left,right):

    if(end < left or start > right):
        return 2**31
    if(start >= left and end <= right):
        return tree[treeNode]
    mid = (start+end)//2
    le = getMin(tree,start,mid,2*treeNode,left,right)
    ri = getMin(tree,mid+1,end,2*treeNode+1,left,right)
    return min(le,ri)

n,q = map(int,input().split())
arr = [int(x) for x in input().split()]
tree = [2**31]*(4*n)
buildTree(arr,tree,0,n-1,1)
for i in range(q):
    q_type, first, second = input().split()
    if(q_type == 'q'):
        print(getMin(tree,0,n-1,1,int(first)-1,int(second)-1))
    else:
        update(arr,tree,0,n-1,1,int(first)-1,int(second))

