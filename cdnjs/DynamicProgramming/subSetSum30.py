'''
Subset Sum - Problem

Given a set of n integers, find if a subset of sum k can be formed from the given set. Print Yes or No.

Input Format
First line contains a single integer n (1<=n<=1000)
Second line contains n space separated integers (1<=a[i]<=1000)
Last line contains a single positive integer k (1<=k<=1000)

Output Format
Output Yes if there exists a subset whose sum is k, else output No.

Sample Input
3
1 2 3
4

Sample Output
Yes

'''

## Read input as specified in the question.
## Print output as specified in the question.
def subsetSumR(arr,sum,n):
    # if sum is Zero
    if(sum == 0):
        return True
    # if sum is not Zero, and arr is empty
    if(n == 0):
        return False

    ans = False
    if(arr[n-1] > sum):
        ans = subsetSumR(arr,sum,n-1)
    else:
        ans = subsetSumR(arr,sum,n-1) or subsetSumR(arr,sum - arr[n-1], n-1)
    return ans

def subsetSumRD(arr,sum,n,dp):
    # if sum is Zero
    if(sum == 0):
        return True
    # if sum is not Zero, and arr is empty
    if(n == 0):
        return False
    if(dp[n][sum] != 0):
        return dp[n][sum]

    ans = False
    if(arr[n-1] > sum):
        ans = subsetSumRD(arr,sum,n-1,dp)
    else:
        ans = subsetSumRD(arr,sum,n-1,dp) or subsetSumRD(arr,sum - arr[n-1], n-1,dp)
    dp[n][sum] = ans
    return ans

def subsetSumID(arr, sum, n):
    dp = [[False for i in range(sum+1)] for j in range(n+1)]
    for i in range(n+1):
        dp[i][0] = True
    for i in range(1,n+1):
        for j in range(1, sum+1):
            dp[i][j] = dp[i-1][j]
            if(arr[i-1] <= j):
                dp[i][j] = dp[i][j] or dp[i-1][j-arr[i-1]]
    return dp[n][sum]

def subsetSumIDw(arr, sum, n):
    dp = [False]*(sum+1)
    dp[0] = True
    for i in range(n):
        '''
        using inner loop reverse, because we want to use previous
        result, If we start loop from zero than half of the fiels 
        fill with current value
        '''
        for j in range(sum,arr[i]-1,-1):
            dp[j] = dp[j] or dp[j-arr[i]]
    return dp[sum]

def subsetSum(arr,sum,n):

    #dp = [[0 for i in range(sum+1)] for j in range(n+1)]
    #ans = subsetSumR(arr,sum,n)
    #ans = subsetSumRD(arr, sum, n, dp)
    #ans = subsetSumID(arr, sum, n)
    ans = subsetSumIDw(arr, sum, n)
    return ans


n = int(input())
arr = [int(x) for x in input().split()]
sum = int(input())
if(subsetSum(arr,sum,n)):
    print("Yes")
else:
    print("No")
