'''
Count BSTs
Send Feedback
Given an integer N, find and return the count of unique Binary search trees (BSTs) are possible with nodes valued from 1 to N.
Output count can be very large, so return the count modulo 10^9+7.

Input Format :
Integer n 

Output Format :
Count of BSTs

Contraints :
1<= N <=1000

Sample Input 1:
8

Sample Output 1:
1430

Sample Input 2:
3

Sample Output 2:
5

'''
## Read input as specified in the question.
## Print output as specified in the question.
def countBSTsR(n,dp):
    if(n == 0 or n == 1):
        return 1
    if(dp[n] > 0):
        return dp[n]
    mod = 1000000007
    for k in range(1,n+1):
        left = countBSTsR(k-1,dp)
        right = countBSTsR(n-k,dp)
        dp[n] = (dp[n] + (left*right)%mod)%mod
    return dp[n]

def countBSTsI(n,dp):
    dp[0] = 1
    dp[1] = 1
    mod = 1000000007
    for i in range(2,n+1):
        for j in range(1,i+1):
            dp[i] = (dp[i] + (dp[j-1] * dp[i-j])%mod)%mod
    return dp[n]
            
def countBSTs(n):
    dp = [0]*(n+1)
    #ans = countBSTsI(n,dp)
    ans = countBSTsR(n,dp)
    return ans

n = int(input())
print(countBSTs(n))

