'''

LCS - Problem

Given two strings S1 and S2 with lengths M and N respectively, find the length of the longest common subsequence.
A subsequence of a string S whose length is K, is a string containing characters in same relative order as they are present in S,
but not necessarily contiguous. Subsequences contain all the strings of length varying from 0 to K. For example, 
subsequences of string "abc" are -- ""(empty string), a, b, c, ab, bc, ac, abc.

Input Format :
Line 1: String S1
Line 2: String s2

Output Format :
Length of the longest common subsequence.

Constraints :
1 <= M <= 100
1 <= N <= 100

Time Limit: 1 sec

Sample Input 1:
adebc
dcadb

Sample Output 1:
3

Explanation of Sample Input 1:
"a", "d", "b", "c", "ad", "ab", "db", "dc" and "adb" are present as a subsequence in both the strings in which "adb" has the maximum length. There are no other common subsequence of length greater than 3 and hence the answer.

Sample Input 2:
abcd
acbdef

Sample Output 2:
3

Explanation of Sample Input 2:
"a", "b", "c", "d", "ab", "ac", "ad", "bd", "cd", "abd" and "acd" are present as a subsequence in both the strings S1 and S2 in which "abd" and "acd" are of the maximum length. There are no other common subsequence of length greater than 3 and hence the answer.

'''

def lcsR(s1, s2):
    if(s1 == '' or s2 == ''):
        return 0
    if(s1[0] == s2[0]):
        return 1 + lcsR(s1[1:], s2[1:])
    first = lcsR(s1[1:],s2)
    second = lcsR(s1,s2[1:])
    result = max(first, second)
    return result

def lcsRD(s1, s2,m,n,dp):
    if(m == 0 or n == 0):
        return 0
    if(dp[m-1][n-1] > -1):
        return dp[m-1][n-1]
    ans = 0
    if(s1[m-1] == s2[n-1]):
        ans = 1 + lcsRD(s1, s2, m-1, n -1, dp)
    else:
        first = lcsRD(s1,s2,m-1,n,dp)
        second = lcsRD(s1,s2,m,n-1,dp)
        ans = max(first, second)
    dp[m-1][n-1] = ans
    return ans

def lcsID(s1,s2,m,n):
    dp = [[-1 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        dp[i][0] = 0
    for j in range(n+1):
        dp[0][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            if(s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
    return dp[m][n]

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[-1 for i in range(n)] for j in range(m)]
    #ans = lcsR(s1, s2)
    #ans = lcsRD(s1, s2, m, n, dp)
    ans = lcsID(s1, s2, m , n)
    return ans

s1 = input()
s2 = input()
print(lcs(s1, s2))
