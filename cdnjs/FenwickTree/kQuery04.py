'''
KQUERY
Given a sequence of n numbers a1, a2, ..., an and a number of k- queries. A k-query is a triple (i, j, k) (1 ≤ i ≤ j ≤ n).
For each k-query (i, j, k), you have to return the number of elements greater than k in the subsequence ai, ai+1, ..., aj.

Input Format
Line 1: n (1 ≤ n ≤ 30000).

Line 2: n numbers a1, a2, ..., an (1 ≤ ai ≤ 10^9).

Line 3: q (1 ≤ q ≤ 200000), the number of k- queries.

In the next q lines, each line contains 3 numbers i, j, k representing a k-query (1 ≤ i ≤ j ≤ n, 1 ≤ k ≤ 10^9).

Output Format
For each k-query (i, j, k), print the number of elements greater than k in the subsequence ai, ai+1, ..., aj in a single line.

Sample Input
5
5 1 2 3 4
3
2 4 1
4 4 4
1 5 2 

Sample Output
2
0
3 

'''

class Ele:
    def __init__(self, val, i):
        self.val = val
        self.idx = i
class Query:
    def __init__(self, left, right, idx, val):
        self.i = left
        self.j = right
        self.idx = idx
        self.k = val

def update(index, val, bit, max):
    while(index < max):
        bit[index] += val
        index += index&(-index)

def query(index, bit):
    sum = 0
    while (index > 0):
        sum += bit[index]
        index -= index&(-index)
    return sum

n = int(input())
temp = [int(x) for x in input().split()]
arr = [None]*(n+1)
arr[0] = Ele(2**31, 0)
for i in range(1,n+1):
    arr[i] = Ele(temp[i-1], i)

arr.sort(key = lambda a:a.val, reverse = True)

q = int(input())
Q = [None]*(q)
for i in range(q):
    a, b, k = map(int, input().split())
    Q[i] = Query(a, b, i, k)

Q.sort(key = lambda a:a.k, reverse = True)

bit = [0]*30005
ans = [0]*q
z = 1
for i in range(q):
    while(z <= n and Q[i].k < arr[z].val):
        update(arr[z].idx, 1, bit, 30005)
        z += 1
    ans[Q[i].idx] = query(Q[i].j, bit) - query(Q[i].i-1, bit)

for i in range(q):
    print(ans[i])

