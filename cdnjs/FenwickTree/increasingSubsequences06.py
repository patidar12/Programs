'''
INCSEQ
Given a sequence of N (1 ≤ N ≤ 10,000) integers S1, ..., SN (0 ≤ Si < 100,000), compute the number of increasing subsequences 
of S with length K (1 ≤ K ≤ 50 and K ≤ N); that is, the number of K-tuples i1, ..., iK such that 1 ≤ i1 < ... < iK ≤ N and Si1 < ... < SiK.

Input
The first line contains the two integers N and K. The following N lines contain the integers of the sequence in order.

Output
Print a single integer representing the number of increasing subsequences of S of length K, modulo 5,000,000.

Sample Input
4 3
1
2
2
10

Output:
2


'''

mod = 5000000

def b_search(x, lo, hi, s):
    mid = 0
    while(lo <= hi):
        mid = (lo+hi)//2
        if(s[mid] == x):
            return mid
        if(s[mid] < x):
            lo = mid + 1
        else:
            hi = mid - 1
    return mid
def update(i, j, n, val, bit):
    while(i <= n):
        bit[i][j] += val
        if(bit[i][j] >= mod):
            bit[i][j] -= mod
        i += i&(-i)

def query(i, j, bit):
    sum = 0
    while(i > 0):
        sum += bit[i][j]
        if(sum >= mod):
            sum -= mod
        i -= i&(-i)
    return sum



n, k = map(int, input().split())
arr = [0]*(n+1)
t = [0]*(n+1)
for i in range(1, n+1):
    arr[i] = int(input())
    t[i] = arr[i]

t.sort()
z = 2
s = [0]*(n+1)
s[1] = t[1]
for i in range(2, n+1):
    if(t[i-1] != t[i]):
        s[z] = t[i]
        z += 1

for i in range(1, n+1):
    arr[i] = b_search(arr[i],1,z,s)

dp = [[0 for _ in range(52)] for i in range(n+1)]
bit = [[0 for _ in range (52)] for i in range(n+1)]
sum = 0
for i in range(1, n+1):
    dp[i][1] = 1
    for j in range(1, min(i, k)+1):
        dp[i][j] += query(arr[i]-1, j-1, bit)
        if(dp[i][j] >= mod):
            dp[i][j] -= mod
        update(arr[i], j, n, dp[i][j], bit)
    sum += dp[i][k]
    if(sum >= mod):
        sum -= mod
print(sum)

