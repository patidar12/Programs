'''
Sum Of Squares

Segment trees are extremely useful. In particular "Lazy Propagation" (i.e. see here, for example) allows one to compute sums over a range in O(lg(n)),
and update ranges in O(lg(n)) as well. In this problem you will compute something much harder:
The sum of squares over a range with range updates of 2 types:
1) increment in a range
2) set all numbers the same in a range.

Input
There will be T (T <= 25) test cases in the input file. First line of the input contains two positive integers, N (N <= 100,000) and Q (Q <= 100,000). 
The next line contains N integers, each at most 1000. Each of the next Q lines starts with a number, which indicates the type of operation:

2 st nd -- return the sum of the squares of the numbers with indices in [st, nd] {i.e., from st to nd inclusive} (1 <= st <= nd <= N).

1 st nd x -- add "x" to all numbers with indices in [st, nd] (1 <= st <= nd <= N, and -1,000 <= x <= 1,000).

0 st nd x -- set all numbers with indices in [st, nd] to "x" (1 <= st <= nd <= N, and -1,000 <= x <= 1,000).

Output
For each test case output the “Case <caseno>:” in the first line and from the second line output the sum of squares for each operation of type 2.
Intermediate overflow will not occur with proper use of 64-bit signed integer.

Input:
2
4 5
1 2 3 4
2 1 4
0 3 4 1
2 1 4
1 3 4 1
2 1 4
1 1
1
2 1 1

Output:
Case 1:
30
7
13
Case 2:
1


'''

class TreeNode:
    def __init__(self):
        self. seqSum = 0
        self.tSum = 0

class LazyNode:
    def __init__(self):
        self.set = 0
        self.update = 0

def makeTree(s,e,i,tree,arr):
    if(s == e):
        tree[i].seqSum = arr[s-1]*arr[s-1]
        tree[i].tSum = arr[s-1]
        return
    mid = (s+e)//2
    makeTree(s,mid,2*i,tree,arr)
    makeTree(mid+1,e,2*i+1,tree,arr)
    tree[i].seqSum = tree[2*i].seqSum + tree[2*i+1].seqSum
    tree[i].tSum = tree[2*i].tSum + tree[2*i+1].tSum

def update(s,e,l,r,v,qtype,i,tree,lazy):
    if(s > e):
        return
    if(lazy[i].set != 0):
        x = lazy[i].set
        tree[i].tSum = x*(e-s+1)
        tree[i].seqSum = x*x*(e-s+1)
        if( s != e):
            lazy[2*i].update = 0
            lazy[2*i].set = x
            lazy[2*i + 1].update = 0
            lazy[2*i+1].set = x
        lazy[i].set = 0
    if(lazy[i].update != 0):
        x = lazy[i].update
        tree[i].seqSum += x*x*(e-s+1) + 2*x*(tree[i].tSum)
        tree[i].tsum += x*(e-s+1)
        if(s != e):
            lazy[2*i].update += x
            lazy[2*i+1].update += x
        lazy[i].update = 0
    if(e < l or s > r):
        return
    if(l <= s and r >= e):
        if(qtype == 0):
            # set value
            tree[i].tSum = v*(e-s+1)
            tree[i].seqSum = v*v*(e-s+1)
            if( s != e):
               lazy[2*i].update = 0
               lazy[2*i].set = v
               lazy[2*i + 1].update = 0
               lazy[2*i+1].set = v
        else:
            # update value
            tree[i].seqSum += v*v*(e-s+1) + 2*v*(tree[i].tSum)
            tree[i].tSum += v*(e-s+1)
            if(s != e):
                lazy[2*i].update += v
                lazy[2*i+1].update += v
        return
    mid = (s+e)//2
    update(s,mid,l,r,v,qtype,2*i,tree,lazy)
    update(mid+1,e,l,r,v,qtype,2*i+1,tree,lazy)
    tree[i].seqSum = tree[2*i].seqSum + tree[2*i+1].seqSum
    tree[i].tSum = tree[2*i].tSum + tree[2*i+1].tSum

def query(s,e,l,r,i,tree,lazy):
    if(s > e):
        return 0
    if(lazy[i].set != 0):
        x = lazy[i].set
        tree[i].tSum = x*(e-s+1)
        tree[i].seqSum = x*x*(e-s+1)
        if( s != e):
            lazy[2*i].update = 0
            lazy[2*i].set = x
            lazy[2*i + 1].update = 0
            lazy[2*i+1].set = x
        lazy[i].set = 0
    if(lazy[i].update != 0):
        x = lazy[i].update
        tree[i].seqSum += x*x*(e-s+1) + 2*x*(tree[i].tSum)
        tree[i].tsum += x*(e-s+1)
        if(s != e):
            lazy[2*i].update += x
            lazy[2*i+1].update += x
        lazy[i].update = 0
    if(e < l or s > r):
        return 0
    if(l <= s and r >= e):
        return tree[i].seqSum
    mid = (s + e)//2
    a1 = query(s,mid,l,r,2*i,tree,lazy)
    a2 = query(mid+1,e,l,r,2*i+1,tree,lazy)
    return a1 + a2

tcs = int(input())
for tc in range(tcs):
    s = "Case "+str(tc+1)+":"
    print(s)
    n, q = map(int, input().split())
    arr = [int(x) for x in input().split()]
    tree = [TreeNode() for i in range(4*n)]
    makeTree(1,n,1,tree,arr)
    lazy = [LazyNode() for i in range(4*n)]
    for j in range(q):
        que = [int(x) for x in input().split()]
        if(que[0] == 0 or que[0] == 1):
            update(1,n,que[1],que[2],que[3],que[0],1,tree,lazy)
        else:
            ans = query(1,n,que[1],que[2],1,tree,lazy)
            print(ans)

