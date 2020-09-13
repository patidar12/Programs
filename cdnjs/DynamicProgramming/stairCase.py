'''
StairCase Problem
Send Feedback
A child is running up a staircase with n steps and can hop either 1 step, 2 steps or 3 steps at a time.
Implement a method to count how many possible ways the child can run up to the stairs. You need to return all possible number of ways.
Time complexity of your code should be O(n).

Input format :
Integer n (No. of steps)

Constraints :
n <= 70

Sample Input 1:
4

Sample Output 1:
7

'''

def ways(dp,n):
    if(n == 0 or n == 1):
        return 1
    if(n == 2):
        return 2
    if(dp[n-1] != 0):
        return dp[n-1]
    first = ways(dp,n-1)
    second = ways(dp,n-2)
    third = ways(dp,n-3)
    dp[n-1] = first+second+third
    return dp[n-1]


def staircaseDP(n):
    ''' Return possible no of ways to climb n staircase using using Dynamic Prog'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    dp = [0]*(n+1)
    # recursive dp call
    #return ways(dp,n)
    if(n == 0 or n == 1):
        return 1
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[n]

# Main
n=int(input())
print(staircaseDP(n))

