'''
Charlie and Pilots

Charlie acquired airline transport company and to stay in business he needs to lower the expenses by any means possible. 
There are N pilots working for his company (N is even) and N/2 plane crews needs to be made. A plane crew consists of two pilots - a captain and his assistant.
A captain must be older than his assistant. Each pilot has a contract granting him two possible salaries - one as a captain and the other as an assistant.
A captain's salary is larger than assistant's for the same pilot. However, it is possible that an assistant has larger salary than his captain. Write a program that 
will compute the minimal amount of money Charlie needs to give for the pilots' salaries if he decides to spend some time to make the optimal (i.e. the cheapest) 
arrangement of pilots in crews.

Input

The first line of input contains integer N, 2 ≤ N ≤ 10,000, N is even, the number of pilots working for the Charlie's company.
The next N lines of input contain pilots' salaries. The lines are sorted by pilot's age, the salaries of the youngest pilot are given the first.
Each of those N lines contains two integers separated by a space character, X i Y, 1 ≤ Y < X ≤ 100,000, a salary as a captain (X) and a salary as an assistant (Y).

Output

The first and only line of output should contain the minimal amount of money Charlie needs to give for the pilots' salaries. 

Sample Input

4 
5000 3000 
6000 2000 
8000 1000 
9000 6000 

Sample Output

19000 




'''
# DP solution can improve, need to try different method

def minExpR(cap, ass, n, x):

    if(n == 0):
        return 0
    if(x == 0):
        return ass[0] + minExpR(cap[1:],ass[1:],n-1,1)
    if(x == n):
        return cap[0] + minExpR(cap[1:],ass[1:],n-1,x-1)

    makeCap = cap[0] + minExpR(cap[1:],ass[1:],n-1,x-1)
    makeAss = ass[0] + minExpR(cap[1:],ass[1:],n-1,x + 1)
    ans = min(makeCap, makeAss)
    return ans

def minExpRD(cap, ass, n, x, dp):

    if(n == 0):
        return 0
    if(dp[n][x] != -1):
        return dp[n][x]
    if(x == 0):
        dp[n][x] =  ass[0] + minExpRD(cap[1:],ass[1:],n-1,1, dp)
        return dp[n][x]
    if(x == n):
        dp[n][x] = cap[0] + minExpRD(cap[1:],ass[1:],n-1,x-1, dp)
        return dp[n][x]

    makeCap = cap[0] + minExpRD(cap[1:],ass[1:],n-1,x-1, dp)
    makeAss = ass[0] + minExpRD(cap[1:],ass[1:],n-1,x + 1, dp)
    ans = min(makeCap, makeAss)
    dp[n][x] = ans
    return ans




def minExp(cap, ass, n):

    dp = [[-1 for i in range(n//2 + 2)] for j in range(n+1)]
    #ans = minExpR(cap, ass, n, 0)
    ans = minExpRD(cap, ass, n, 0, dp)
    return ans


from sys import setrecursionlimit
setrecursionlimit(110000)
n = int(input())
cap = [0]*n
ass = [0]*n
for i in range(n):
    c,a = map(int,input().split())
    cap[i], ass[i] = c, a
print(minExp(cap, ass, n))
