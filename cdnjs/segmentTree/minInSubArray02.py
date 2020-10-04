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


def buildTree(arr,tree,start,end,treeIndex):

    if(start == end):
        tree[treeIndex] = arr[start]
        return

    mid = (start+end)//2
    buildTree(arr,tree,start,mid,2*treeIndex)
    buildTree(arr,tree,mid+1,end,2*treeIndex+1)
    tree[treeIndex] = min(tree[2*treeIndex], tree[2*treeIndex+1])

def updateTree(arr,tree,start,end,treeIndex,idx,val):

    if(start == end):
        arr[idx] = val
        tree[treeIndex] = val
        return

    mid = (start+end)//2
    if(idx > mid):
        updateTree(arr,tree,mid+1,end,2*treeIndex+1,idx,val)
    else:
        updateTree(arr,tree,start,mid,2*treeIndex,idx,val)

    tree[treeIndex] = min(tree[2*treeIndex], tree[2*treeIndex+1])

def query(tree,start,end,treeIndex,left,right):

    # outside of given range
    if(end < left or start > right):
        return 2**31

    # inside of given range
    if(left <= start and right >= end):
        return tree[treeIndex]

    mid = (start+end)//2
    li = query(tree,start,mid,2*treeIndex,left,right)
    ri = query(tree,mid+1,end,2*treeIndex+1,left,right)
    return min(li,ri)


n,m = map(int,input().split())
arr = [int(x) for x in input().split()]
tree = [2**31]*(4*n)
buildTree(arr,tree,0,n-1,1)
for i in range(m):
    q,a,b = input().split()
    a, b = int(a), int(b)
    if(q == 'q'):
        print(query(tree,0,n-1,1,a-1,b-1))
    else:
        updateTree(arr,tree,0,n-1,1,a-1,b)

