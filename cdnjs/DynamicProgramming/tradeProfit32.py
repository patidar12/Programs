'''
Trader Profit

Mike is a stock trader and makes a profit by buying and selling stocks. He buys a stock at a lower price and sells it at a higher price to book a profit.
He has come to know the stock prices of a particular stock for n upcoming days in future and wants to calculate the maximum profit by doing the right 
transactions (single transaction = buying + selling). Can you help him maximize his profit?

Note: A transaction starts after the previous transaction has ended. Two transactions can't overlap or run in parallel.

The stock prices are given in the form of an array A for n days.

Given the stock prices and a positive integer k, find and print the maximum profit Mike can make in at most k transactions.

Input Format
The first line of input contains an integer q denoting the number of queries.

The first line of each test case contains a positive integer k, denoting the number of transactions. 

The second line of each test case contains a positive integer n, denoting the length of the array A.

The third line of each test case contains n space-separated positive integers, denoting the prices of each day in the array A.

Constraints
1<=q<=100

0<k<10

2<=n<=30

0<=elements of array A<=1000

Output Format
For each query print the maximum profit earned by Mike on a new line. 

Sample Input
3
2
6
10 22 5 75 65 80
3
4
20 580 420 900
1
5
100 90 80 50 25

Sample Output
87
1040
0


'''

def profitR(arr,k,n,ongoing):
    if(n == 0):
        return 0
    ans = profitR(arr[1:],k,n-1,ongoing)
    if(ongoing):
        b = profitR(arr[1:],k-1,n-1,False) + arr[0]
        ans = max(ans,b)
    else:
        if(k > 0):
            c = profitR(arr[1:],k,n-1,True) - arr[0]
            ans = max(ans,c)
        else:
            ans = 0
    return ans

def profitRD(arr,k,n,ongoing,dp):
    if(n == 0):
        return 0
    if(dp[n][k][ongoing] != -1):
        return dp[n][k][ongoing]
    ans = profitRD(arr[1:],k,n-1,ongoing,dp)
    if(ongoing):
        b = profitRD(arr[1:],k-1,n-1,0,dp) + arr[0]
        ans = max(ans,b)
    else:
        if(k > 0):
            c = profitRD(arr[1:],k,n-1,1,dp) - arr[0]
            ans = max(ans,c)
        else:
            ans = 0
    dp[n][k][ongoing] = ans
    return ans

def profit(arr,k,n):

    dp = [[[-1 for i in range(2)] for j in range(k+1)] for x in range(n+1)]
    #ongoing = False
    #ans = profitR(arr,k,n,ongoing)
    ans = profitRD(arr,k,n,0,dp)
    return ans


qrs = int(input())
for q in range(qrs):
    k = int(input())
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(profit(arr,k,n))

