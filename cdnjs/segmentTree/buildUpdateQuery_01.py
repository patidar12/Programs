'''
Build, update and query on segment tree from input array

Input:
    arr = [1,2,3,4,5,6,7,8,9]
Output:
    build segment tree
    update and range query on input

'''

# input array, tree array, start ,end, tree index
def buildTree(arr, tree, start, end, treeNode):
    # array have only one element
    if(start == end):
        tree[treeNode] = arr[start]
        return
    mid = (start+end) // 2
    # call for left child
    buildTree(arr, tree, start,mid,2*treeNode)
    # call for right child
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    # generate answer from left and right child
    tree[treeNode] = tree[2*treeNode] + tree[2*treeNode+1]

def updateTree(arr, tree, start, end, treeNode, idx, value):

    # reached to given index
    if( start == end):
        arr[idx] = value
        tree[treeNode] = value
        return

    mid = (start+end)//2
    if(idx > mid):
        # call on right subtree
        updateTree(arr, tree, mid+1, end, 2*treeNode+1, idx, value)
    else:
        # call on left subtree
        updateTree(arr, tree, start, mid, 2*treeNode, idx, value)

    tree[treeNode] = tree[2*treeNode] + tree[2*treeNode + 1]

def query(tree, start, end, treeNode, left, right):
    # left and right are query range index
    # comopletely outside of given range
    if(start > right or end < left):
        return 0
    # completely inside of given range
    if(start >= left and end <= right):
        return tree[treeNode]
    # partially inside and partially outside
    mid = (start+end)//2
    # call on left subtree
    ans1 = query(tree,start,mid,2*treeNode,left,right)
    # call on right subtree
    ans2 = query(tree,mid+1,end,2*treeNode+1,left,right)
    return ans1 + ans2

arr = [1,2,3,4,5,6,7,8,9]
# Tree 2*N size, started from 1st index
tree = [0]*(18)
buildTree(arr,tree,0,8,1)
updateTree(arr,tree,0,8,1,2,15)

for i in range(1,18):
    print(tree[i],end = ' ')

print()
ans = query(tree,0,8,1,2,5)
print("Sum b/w interval 2-5 is : ",ans)

