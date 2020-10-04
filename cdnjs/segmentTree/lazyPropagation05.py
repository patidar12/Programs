'''
úpdate the value in range(left - right) in an array


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
    tree[treeNode] = min(tree[2*treeNode], tree[2*treeNode+1])

# tree, lazy tree, start, end (0 to n-1), left, right (range), treeNode, increment value
def updateTree(tree,lazy, start, end,left,right, treeNode, inc):
    if(start > end):
        return
    if(lazy[treeNode] != 0):
        tree[treeNode] += lazy[treeNode]
        if(start != end):
            lazy[2*treeNode] += lazy[treeNode]
            lazy[2*treeNode + 1] += lazy[treeNode]
        lazy[treeNode] = 0
    # no overlap
    if(end < left or start > right ):
        return
    # complete overlap
    if(left <= start and right >= end):
        tree[treeNode] += inc
        if(start != end):
            lazy[2*treeNode] += inc
            lazy[2*treeNode+1] += inc
        return
    # partial overlap
    mid = (start+end)//2
    updateTree(tree,lazy, start, mid,left,right, 2*treeNode, inc)
    updateTree(tree,lazy, mid+1, end,left,right, 2*treeNode+1, inc)
    tree[treeNode] = min(tree[2*treeNode], tree[2*treeNode+1])

arr = [1,3,-2,4]
# Tree 4*N size, started from 1st index
tree = [0]* 16
buildTree(arr,tree,0,3,1)
lazy = [0]* 16
updateTree(tree,lazy,0,3,0,3,1,3)
updateTree(tree,lazy,0,3,0,1,1,2)

print(tree)
print(lazy)
