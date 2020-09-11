'''
Hackerearth: Recursion and Backtracking
https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/algorithm/simran-and-stairs/description/

Simran is running up a staircase with N steps, and can hop(jump) either 1 step, 2 steps or 3 steps at a time.You have to count, how many possible ways Simran can run up to the stairs.

Input Format:
Input contains integer N that is number of steps

Output Format:
Output for each integer N the no of possible ways w.

Constraints:
    1 <= N <= 30

Input:
    4
Output:
    7

# Write your code here
# Recursive
def numWays(n,dp):
    if(n <= 0):
        return 0
    if(n == 1):
        return 1
    #if(dp[n] != -1):
    #    return dp[n]
    result = numWays(n-1,dp) + numWays(n-2,dp) + numWays(n-3,dp)
    #dp[n] = result
    return result
n = int(input())
dp = [-1]*(n+2)
print(numWays(n+1,dp))

'''

# Pytohn 
# Dp
# Write your code here
def numWays(n,dp):
    if(n <= 0):
        return 0
    if(n == 1):
        return 1
    if(dp[n] != -1):
        return dp[n]
    result = numWays(n-1,dp) + numWays(n-2,dp) + numWays(n-3,dp)
    dp[n] = result
    return result
n = int(input())
dp = [-1]*(n+2)
print(numWays(n+1,dp))
