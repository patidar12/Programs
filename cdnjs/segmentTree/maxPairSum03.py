'''
Maximum Pair Sum
Send Feedback
You are given a sequence A[1], A[2], ..., A[N], ( 0 ≤ A[i] ≤ 10^8 , 2 ≤ N ≤ 10^5 ). There are two types of operations and they are defined as follows:
Update:
This will be indicated in the input by a 'U' followed by space and then two integers i and x.
U i x, 1 ≤ i ≤ N, and x, 0 ≤ x ≤ 10^8.
This operation sets the value of A[i] to x.
Query:
This will be indicated in the input by a 'Q' followed by a single space and then two integers i and j.
Q x y, 1 ≤ x < y ≤ N.
You must find i and j such that x ≤ i, j ≤ y and i != j, such that the sum A[i]+A[j] is maximized. Print the sum A[i]+A[j].
Input
The first line of input consists of an integer N representing the length of the sequence. 
Next line consists of N space separated integers A[i]. Next line contains an integer Q, Q ≤ 10^5, representing the number of operations. Next Q lines contain the operations.
Output
 Output the maximum sum mentioned above, in a separate line, for each Query.
Input:
5
1 2 3 4 5
6
Q 2 4
Q 2 5
U 1 6
Q 1 5
U 1 7
Q 1 5
Output:
7
9
11
12


'''

def buildTree(arr,tree,start,end,treeNode):
    if(start == end):
        tree[treeNode] = (arr[start], -2**31)
        return
    mid = (start+end)//2
    buildTree(arr,tree,start,mid,2*treeNode)
    buildTree(arr,tree,mid+1,end,2*treeNode+1)
    left = tree[2*treeNode]
    right = tree[2*treeNode+1]
    max_ele = max(left[0], right[0])
    max_sum_pair = max(left[0]+right[0],max(left[1],right[1]))
    tree[treeNode] = (max_ele, max_sum_pair)

def query(tree,start,end,treeNode,left,right):

    if(end < left or start > right):
        return (-2**31,-2**31)
    if(start >= left and end <= right):
        return tree[treeNode]
    mid = (start+end)//2
    l_node = query(tree,start,mid,2*treeNode,left,right)
    r_node = query(tree,mid+1,end,2*treeNode+1,left,right)
    max_ele = max(l_node[0], r_node[0])
    max_sum_pair = max(l_node[0] + r_node[0],max(l_node[1],r_node[1]))
    return (max_ele, max_sum_pair)

def update(arr,tree,start,end,treeNode,idx,value):
    if(start == end or start == idx):
        tree[treeNode] = (value,-2**31)
        arr[start] = value
        return
    mid = (start+end)//2
    if(idx > mid):
        update(arr,tree,mid+1,end,2*treeNode+1,idx,value)
    else:
        update(arr,tree,start,mid,2*treeNode,idx,value)
    left = tree[2*treeNode]
    right = tree[2*treeNode+1]
    max_ele = max(left[0], right[0])
    max_sum_pair = max(left[0]+right[0],max(left[1],right[1]))
    tree[treeNode] = (max_ele, max_sum_pair)

n = int(input())
arr = [int(x) for x in input().split()]
tree = [None]*(4*n)
buildTree(arr,tree,0,n-1,1)
q = int(input())
for i in range(q):
    q_type, first, second = input().split()
    if(q_type == 'Q'):
        node = query(tree,0,n-1,1,int(first)-1,int(second)-1)
        print(node[1])
    else:
        update(arr,tree,0,n-1,1,int(first)-1,int(second))
