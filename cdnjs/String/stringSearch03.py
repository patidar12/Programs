'''
String Search

Given two strings S and T, write a function to find if T is present as a substring inside S or not.
If yes, return the starting index otherwise return -1.

Input format :

Line 1 : String S

Line 2 : String T

Sample Input 1:
WelcomeBack
come 

Sample Output 1:
3

Sample Input 2:
WelcomeBack
code

Sample Output 2:
-1

'''

## Read input as specified in the question.
## Print output as specified in the question.

def getLPS(pattern):
    n = len(pattern)
    lps = [0]*n
    i = 1
    j = 0
    while(i < n):
        if(pattern[i] == pattern[j]):
            lps[i] = j+1
            i += 1
            j += 1
        else:
            if(j != 0):
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmpSearch(string, pattern):
    n = len(string)
    m = len(pattern)
    lps = getLPS(pattern)
    i = 0
    j = 0
    while(i < n and j < m):
        if(string[i] == pattern[j]):
            i += 1
            j += 1
        else:
            if(j != 0):
                j = lps[j-1]
            else:
                i += 1

    if(j == m):
        return i - m
    return -1

def getIndex(s,t):
    if(len(t) > len(s)):
        return -1
    if(s == t):
        return 0
    if(len(s) == len(t)):
        return -1

    result = -1
    for i in range(len(s) - len(t)+1):
        matched = True
        for j in range(len(t)):
            if(s[i+j] != t[j]):
                matched = False
                break
        if(matched):
            result = i
            break
    return result

s = input()
t = input()
#print(getIndex(s,t))
print(kmpSearch(s, t))
