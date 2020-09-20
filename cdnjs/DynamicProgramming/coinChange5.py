'''
Coin Change Problem
Send Feedback
You are given an infinite supply of coins of each of denominations D = {D0, D1, D2, D3, ...... Dn-1}.
You need to figure out the total number of ways W, in which you can make change for Value V using coins of denominations D.

Note : Return 0, if change isn't possible.

Input Format
Line 1 : Integer n i.e. total number of denominations
Line 2 : N integers i.e. n denomination values
Line 3 : Value V

Output Format
Line 1 :  Number of ways i.e. W

Constraints :
1<=n<=10
1<=V<=1000

Sample Input 1 :
3
1 2 3
4

Sample Output
4

Sample Output Explanation :
Number of ways are - 4 total i.e. (1,1,1,1), (1,1, 2), (1, 3) and (2, 2).

'''

## Read input as specified in the question.
## Print output as specified in the question.
def ways(arr,dp,d,value):
    if(value == 0):
        #dp[value][d] = 1
        return 1
    if(value < 0):
        return 0
    if(d == 0):
        #dp[value][d] = 0
        return 0
    if(dp[value][d] > -1):
        return dp[value][d]
    first = ways(arr,dp,d,value - arr[0])
    second = ways(arr[1:],dp,d-1,value)
    dp[value][d] = first + second
    return (first + second)


def coinChange(arr,d,value):
    dp = [[-1 for i in range(d+1)] for j in range(value+1)]
    return ways(arr,dp,d,value)

d = int(input())
arr = [int(x) for x in input().split()]
value = int(input())
print(coinChange(arr,d,value))
