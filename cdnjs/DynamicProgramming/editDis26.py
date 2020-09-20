'''
Edit Distance - Problem

Given two strings s and t of lengths m and n respectively, find the Edit Distance between the strings.
Edit Distance of two strings is minimum number of steps required to make one string equal to other.
In order to do so you can perform following three operations only :

1. Delete a character

2. Replace a character with another one

3. Insert a character

Note - Strings don't contain spaces

Input Format :
Line 1 : String s
Line 2 : String t

Output Format :
Line 1 : Edit Distance value

Constraints
1<= m,n <= 20

Sample Input 1 :
abc
dc

Sample Output 1 :
2

'''

## Read input as specified in the question.
## Print output as specified in the question.
def editDisR(str1, str2, m, n):
    if(m == 0):
        return n
    if(n == 0):
        return m
    ans = 0
    if(str1[0] == str2[0]):
        ans = editDisR(str1[1:], str2[1:], m-1, n-1)
    else:
        replace = editDisR(str1[1:], str2[1:], m-1, n-1)
        delete = editDisR(str1[1:],str2, m-1, n)
        insert = editDisR(str1, str2[1:], m, n-1)
        ans = 1 + min(replace, min(delete, insert))
    return ans

def editDisRD(str1, str2, m, n, dp):
    if(m == 0):
        return n
    if(n == 0):
        return m
    ans = 0
    if(dp[m][n] > -1):
        return dp[m][n]
    if(str1[0] == str2[0]):
        ans = editDisRD(str1[1:], str2[1:], m-1, n-1, dp)
    else:
        replace = editDisRD(str1[1:], str2[1:], m-1, n-1, dp)
        delete = editDisRD(str1[1:],str2, m-1, n, dp)
        insert = editDisRD(str1, str2[1:], m, n-1, dp)
        ans = 1 + min(replace, min(delete, insert))
    dp[m][n] = ans
    return ans

def editDisID(str1, str2, m, n, dp):
    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1, m+1):
        for j in range(1, n+1):
            ans = 0
            if(str1[i-1] == str2[j-1]):
                ans = dp[i-1][j-1]
            else:
                ans = 1 + min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))
            dp[i][j] = ans
    return dp[m][n]

def editDis(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[-1 for i in range(n+1)] for j in range(m+1)]
    #ans = editDisR(str1, str2, m, n)
    #ans = editDisRD(str1, str2, m, n, dp)
    ans = editDisID(str1, str2, m, n, dp)
    return ans

str1 = input()
str2 = input()
print(editDis(str1, str2))
