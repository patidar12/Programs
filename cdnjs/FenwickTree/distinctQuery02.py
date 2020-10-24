'''
Distinct Query Problem
Given a sequence of n numbers a1, a2, ..., an and a number of d-queries. A d-query is a pair (i, j) (1 ≤ i ≤ j ≤ n). 
For each d-query (i, j), you have to return the number of distinct elements in the subsequence ai, ai+1, ..., aj.

Input
Line 1: n (1 ≤ n ≤ 30000).
Line 2: n numbers a1, a2, ..., an (1 ≤ ai ≤ 10^6).
Line 3: q (1 ≤ q ≤ 200000), the number of d-queries.
In the next q lines, each line contains 2 numbers i, j representing a d-query (1 ≤ i ≤ j ≤ n).

Output
For each d-query (i, j), print the number of distinct elements in the subsequence ai, ai+1, ..., aj in a single line.

Sample Input
5
1 1 2 1 3
3
1 5
2 4
3 5

Sample Output
3
2
3 

'''

class Event:
    def __init__(self, a, b, i):
        self.first = a
        self.second = b
        self.index = i

def update(index, val, n, bit):
    while(index <= n):
        bit[index] += val
        index += index&(-index)


def value(index, bit):
    count = 0
    while(index > 0):
        count += bit[index]
        index -= (index&(-index))

    return count

n = int(input())
temp = [int(x) for x in input().split()]
arr = [0]*(n+1)
for i in range(1, n+1):
    arr[i] = temp[i-1]

q = int(input())
query = [0]*q
for i in range(q):
    a, b = map(int, input().split())
    query[i] = Event(a, b, i)

query.sort(key = lambda val:val.second)

bit = [0 for _ in range(n+1)]
ans = [0 for _ in range(q)]
last = [-1 for _ in range(1000001)]

k = 0
total = 0
for i in range(1,n+1):

    if last[arr[i]] != -1:
        update(last[arr[i]], -1, n, bit)
    else:
        total += 1
    last[arr[i]] = i
    update(i, 1, n, bit)
    while(k < q and query[k].second == i):
        ans[query[k].index] = total - value(query[k].first-1, bit)
        k += 1

for i in range(q):
    print(ans[i])
