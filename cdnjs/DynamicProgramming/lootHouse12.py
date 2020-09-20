'''
Loot Houses

A thief wants to loot houses. He knows the amount of money in each house.
He cannot loot two consecutive houses. Find the maximum amount of money he can loot.

Input Format
Line 1 : An integer N 
Line 2 : N spaced integers denoting money in each house

Output Format
 Line 1 : Maximum amount of money looted

Input Constraints

1 <= n <= 10^4
1 <= A[i] < 10^4

Sample Input :

6
5 5 10 100 10 5

Sample Output 1 :
110

'''
## Read input as specified in the question.
## Print output as specified in the question.
def maxAmountR(arr,n,dp):
    if(n == 1):
        return arr[0]
    if(n == 2):
        return max(arr[0],arr[1])
    if(dp[n-1] > 0):
        return dp[n-1]
    first = maxAmountR(arr,n-1,dp)
    second = maxAmountR(arr,n-2,dp)
    dp[n-1] = max(arr[n-1]+second,first)
    return dp[n-1]

def maxAmountI(arr,n,dp):
    if(n == 1):
        return arr[0]
    #dp = [0]*(n)
    dp[0] = arr[0]
    dp[1] = max(arr[0],arr[1])
    for i in range(2,n):
        dp[i] = max(arr[i]+dp[i-2],dp[i-1])
    return dp[n-1]

def lootHouse(arr,n):
    dp = [0]*n
    #ans = maxAmountI(arr,n,dp)
    ans = maxAmountR(arr,n,dp)
    return ans

from sys import setrecursionlimit
setrecursionlimit(110000)
n = int(input())
arr = [int(x) for x in input().split()]
print(lootHouse(arr,n))

