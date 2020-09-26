'''
Miser Man

Jack is a wise and miser man. Always tries to save his money.
One day, he wants to go from city A to city B. Between A and B, there are N number of cities(including B and excluding A) and
in each city there are M buses numbered from 1 to M. And the fare of each bus is different. Means for all N*M busses, fare (K) may
be different or same. Now Jack has to go from city A to city B following these conditions:

1. At every city, he has to change the bus.
2. And he can switch to only those buses which have number either equal or 1 less or 1 greater to the previous.

You are to help Jack to go from A to B by spending the minimum amount of money.

N, M, K <= 100.

Input
Line 1:    N M

Line 2:    NxM Grid

Each row lists the fares the M busses to go form the current city to the next city.

Output
Single Line containing the minimum amount of fare that Jack has to give.

Sample Input
5 5
1  3  1  2  6
10 2  5  4  15
10 9  6  7  1
2  7  1  5  3
8  2  6  1  9

Sample Output
10


'''

def minFairR(cities,r,c,n,m):
    if(r == n):
        return 0
    a1 = 2**31
    b1 = 2**31
    c1 = 2**31
    if(c > 0 and r < n):
        a1 = minFairR(cities,r+1,c-1,n,m)
    if(c < m-1 and r < n):
        b1 = minFairR(cities,r+1,c+1,n,m)
    if(r < n):
        c1 = minFairR(cities,r+1,c,n,m)
    ans = cities[r][c] + min(a1,min(b1,c1))
    return ans

def minFairRD(cities,r,c,n,m,dp):
    if(r == n):
        return 0
    a1 = 2**31
    b1 = 2**31
    c1 = 2**31
    if(dp[r][c] != -1):
        return dp[r][c]

    if(c > 0 and r < n):
        a1 = minFairRD(cities,r+1,c-1,n,m,dp)
    if(c < m-1 and r < n):
        b1 = minFairRD(cities,r+1,c+1,n,m,dp)
    if(r < n):
        c1 = minFairRD(cities,r+1,c,n,m,dp)
    ans = cities[r][c] + min(a1,min(b1,c1))
    dp[r][c] = ans
    return ans

def minFairID(arr,n,m):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(1,n+1):
        dp[i][0] = 2**31
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(j < m):
                dp[i][j] = min(dp[i-1][j-1],min(dp[i-1][j],dp[i-1][j+1]))
            else:
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])
            dp[i][j] += arr[i-1][j-1]
    return min(dp[n])


def minFair(cities,n,m):

    '''
    fair = 2**31
    dp = [[-1 for i in range(m)] for j in range(n)]
    for i in range(m):
        #ans = minFairR(cities,0,i,n,m)
        ans = minFairRD(cities,0,i,n,m,dp)
        if(ans < fair):
            fair = ans
    '''
    fair = minFairID(cities,n,m)
    return fair

n,m = map(int,input().split())
cities = [None]*n
for i in range(n):
    buses = [int(x) for x in input().split()]
    cities[i] = buses
print(minFair(cities,n,m))

