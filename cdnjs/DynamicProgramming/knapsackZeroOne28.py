'''
Knapsnack - Problem

A thief robbing a store and can carry a maximal weight of W into his knapsack.
There are N items and ith item weigh wi and is of value vi.
What is the maximum value V, that thief can take ?

Space complexity should be O(W).

Input Format :
Line 1 : N i.e. number of items
Line 2 : N Integers i.e. weights of items separated by space
Line 3 : N Integers i.e. values of items separated by space
Line 4 : Integer W i.e. maximum weight thief can carry

Output Format :
Line 1 : Maximum value V

Constraints
1 <= N <= 10^4
1<= wi <= 100
1 <= vi <= 100

Sample Input 1 :
4
1 2 4 5
5 4 8 6
5

Sample Output :
13

'''

## Read input as specified in the question.
## Print output as specified in the question.
def knapsackR(wt, val, w, n):
    if(w == 0 or n == 0):
        return 0
    if(wt[n-1] > w):
        return knapsackR(wt, val, w, n-1)
    return max(val[n-1] + knapsackR(wt, val, w - wt[n-1],n-1), knapsackR(wt, val, w, n-1))

def knapsackRD(wt, val, w, n, dp):
    if(w == 0 or n == 0):
        return 0
    if(dp[n][w] > -1):
        return dp[n][w]
    ans = 0
    if(wt[n-1] > w):
        ans = knapsackRD(wt, val, w, n-1, dp)
    else:
        ans = max(val[n-1] + knapsackRD(wt, val, w - wt[n-1], n-1, dp), knapsackRD(wt, val, w, n-1, dp))
    dp[n][w] = ans
    return ans

def knapsackID(wt, val, w, n):
    dp = [[0 for i in range(w+1)] for j in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, w+1):
            if(wt[i-1] <= j):
                dp[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]

def knapsackIDw(wt, val, w, n):
    dp = [0 for i in range(w+1)]
    for i in range(n):
        for j in range(w,wt[i]-1,-1):
            dp[j] = max(dp[j], val[i] + dp[j-wt[i]])
    return dp[w]


def knapsack(wt, val, w, n):
    #dp = [[-1 for i in range(w+1)] for j in range(n+1)]
    #ans = knapsackR(wt, val, w, n)
    #ans = knapsackRD(wt, val, w, n, dp)
    #ans = knapsackID(wt, val, w, n)
    ans = knapsackIDw(wt, val, w, n)
    return ans

#from sys import setrecursionlimit
#setrecursionlimit(110000)
n = int(input().strip())
wt = [int(x) for x in input().strip().split()]
val = [int(x) for x in input().strip().split()]
w = int(input().strip())
print(knapsack(wt,val,w,n))
