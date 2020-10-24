'''
Adjacent Bit Counts
For a string of n bits x1,x2,x3,...,Xn the adjacent bit count of the string (AdjBC(x)) is given by
X1*X2 + X2*X3 + X3*X4 + ... + Xn-1 * Xn
which counts the number of times a 1 bit is adjacent to another 1 bit. For example:
AdjBC(011101101) = 3
AdjBC(111101101) = 4
AdjBC(010101010) = 0
Write a program which takes as input integers n and k and returns the number of bit strings x of n bits (out of 2ⁿ) that satisfy AdjBC(x) = k.
For example, for 5 bit strings, there are 6 ways of getting AdjBC(x) = 2:
11100, 01110, 00111, 10111, 11101, 11011

Input
The first line of input contains a single integer P, (1 ≤ P ≤ 1000), which is the number of data sets that follow. Each data set is a single line 
that contains the data set number, followed by a space, followed by a decimal integer giving the number (n) of bits in the bit strings,
followed by a single space, followed by a decimal integer (k) giving the desired adjacent bit count. The number of bits (n) will not be greater than 100.

Output
For each data set there is one line of output. It contains the data set number followed by a single space, followed by the number of n-bit strings 
with adjacent bit count equal to k. As answer can be very large print your answer modulo 10^9+7.

Sample Input
10
1 5 2
2 20 8
3 30 17
4 40 24
5 50 37
6 60 52
7 70 59
8 80 73
9 90 84
10 100 90

Sample Output
1 6
2 63426
3 1861225
4 168212501
5 44874764
6 160916
7 22937308
8 99167
9 15476
10 23076518


'''

mod = 1000000007
def adjacentBits(n, k, first, dp):
    if(k < 0):
        return 0
    if(n == 1):
        if(k == 0):
            dp[n][k][first] = 1
            return 1
        else:
            dp[n][k][first] = 1
            return 0

    if( dp[n][k][first] != -1):
        return dp[n][k][first]
    if(first == 1):
        ans  = adjacentBits(n-1, k-1, 1, dp) + adjacentBits(n-1, k, 0, dp)
    else:
        ans  = adjacentBits(n-1, k, 1, dp) + adjacentBits(n-1, k, 0, dp)

    ans = ans%mod
    dp[n][k][first] = ans
    return ans

dp = [ [ [0 for _ in range(2)] for i in range(101) ] for j in range(101) ]
dp[1][0][0] = 1
dp[1][0][1] = 1
for i in range(2, 101):
    dp[i][i-1][0] = 0
    dp[i][i-1][1] = 1
    dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1]
    dp[i][0][1] = dp[i-1][0][0]
    dp[i][0][0] %= mod

for i in range(2, 101):
    for j in range(1, i):
        dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
        dp[i][j][1] = dp[i-1][j][0] + dp[i-1][j-1][1]
        dp[i][j][0] %= mod
        dp[i][j][1] %= mod

tcs = int(input())
for tc in range(tcs):
    n, s, k = map(int, input().split())
    #dp = [ [ [-1 for _ in range(2)] for i in range(k+1) ] for j in range(s+1) ]
    #ans = adjacentBits(s, k, 0, dp) + adjacentBits(s, k, 1, dp)
    ans = dp[s][k][0] + dp[s][k][1]
    print(n,ans%mod)

