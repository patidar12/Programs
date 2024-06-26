'''
Balika Vadhu- Problem

Anandi and Jagya were getting married again when they have achieved proper age. Dadi Sa invited Alok Nath to do the kanyadaan and give blessings.
Alok Nath has 2 blessings. Each bessing is in the form of a string consisting of lowercase charaters(a-z) only.
But he can give only one blessing of K length because some priest told him to do so. Thus he decides to generate a blessing using the other two blessings.
While doing this he wants to ensure that happiness brought into their life by his blessing is maximum.
The generated blessing is a common subsequence of length K of the two blessings he has. 
Happiness of the blessing he generates is calculated by the sum of ASCII values of characters in the blessing and he wants the happiness to be maximum.
If he is not able to generate a common subsequence of length K then the happiness is 0 (zero).
Alok Nath comes to you and asks you to find the maximum happiness that can be generated by the two blessings he has.

Input Specification
First line consists of number of test cases t. Each test case consists of two strings b1 (blessing 1),b2 (blessing 2) and an integer K, each of them in separate lines.

Output Specification
Output consists of t lines each containing an integer denoting the maximum happiness value that can be generated by the two blessings.

Constraint
1 <= t <= 50

1 <= length(b1) , length(b2) <= 100 

1 <= K <= 100

Sample Input
2
asdf
asdf
3
anandi
jagya
3

Sample Output
317
0

'''

def ascii(char):
    return ord(char)
def lcsR(s1, s2, k):
    if(k == 0):
        return 0
    if(len(s1) == 0 or len(s2) == 0):
        return -2**31
    ans = 0
    if(s1[0] == s2[0]):
        opt1 = ascii(s1[0]) + lcsR(s1[1:], s2[1:],k-1)
        opt2 = lcsR(s1[1:],s2,k)
        opt3 = lcsR(s1,s2[1:],k)
        ans = max(opt1,max(opt2,opt3))
    else:
        first = lcsR(s1[1:],s2,k)
        second = lcsR(s1,s2[1:],k)
        ans = max(first, second)
    return ans

def lcsRD(s1, s2, m, n, k, dp):
    if(k == 0):
        return 0
    if(m == 0 or n == 0):
        return -2**31
    if(dp[m][n][k] != -1):
        return dp[m][n][k]
    ans = 0
    if(s1[m-1] == s2[n-1]):
        opt1 = ascii(s1[m-1]) + lcsRD(s1, s2,m-1, n-1, k-1, dp)
        opt2 = lcsRD(s1,s2,m-1,n,k,dp)
        opt3 = lcsRD(s1,s2,m,n-1,k,dp)
        ans = max(opt1,max(opt2,opt3))
    else:
        first = lcsRD(s1,s2,m-1,n,k,dp)
        second = lcsRD(s1,s2,m,n-1,k,dp)
        ans = max(first, second)
    dp[m][n][k] = ans
    return ans


def lcsID(s1,s2,m,n,k,dp):
    # if length of second string is 0
    for i in range(m+1):
        for j in range(k+1):
            dp[i][0][j] = -2**31
    # if length of first string is 0
    for i in range(n+1):
        for j in range(k+1):
            dp[0][i][j] = -2**31
    # if length of k is 0
    for i in range(m+1):
        for j in range(n+1):
            dp[i][j][0] = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            for x in range(1, k+1):
                ans = 0
                if(s1[i-1] == s2[j-1]):
                    opt1 = ascii(s1[i-1]) + dp[i-1][j-1][x-1]
                    opt2 = dp[i-1][j][x]
                    opt3 = dp[i][j-1][x]
                    ans = max(opt1,max(opt2,opt3))
                else:
                    opt1 = dp[i-1][j][x]
                    opt2 = dp[i][j-1][x]
                    ans = max(opt1,opt2)
                dp[i][j][x] = ans
    return dp[m][n][k]

def lcs(s1, s2, k):
    m = len(s1)
    n = len(s2)
    dp = [[[-1 for x in range(k+1)] for i in range(n+1)] for j in range(m+1)]
    #ans = lcsR(s1, s2, k)
    #ans = lcsRD(s1, s2, m, n, k, dp)
    ans = lcsID(s1, s2, m, n, k,dp)
    return ans if ans > 0 else 0

tcs = int(input())
for tc in range(tcs):
    s1 = input().strip()
    s2 = input().strip()
    k = int(input())
    print(lcs(s1, s2,k))

