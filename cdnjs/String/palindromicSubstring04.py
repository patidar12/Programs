'''
Palindromic Substrings

Given a string S, count and return the number of substrings of S that are palindrome.
Single length substrings are also palindromes. You just need to calculate the count, not the substrings.

Input Format :
String S

Output Format :
count of palindrome substrings

Constraints :
1 <= Length of S <= 1000

Sample Input :
aba

Sample Output :
4

**Note : Here 4 corresponds to ("a","b","a","aba").

'''

## Read input as specified in the question.
## Print output as specified in the question.

# Note: both the approaches also used to calculate length of longest palinduram
def isPalinduram(s):
    # O(n^3) approach
    l = 0
    r = len(s) - 1
    while(l < r):
        if(s[l] != s[r]):
            return False
        l += 1
        r -= 1
    return True

def countPalinduramNavie(s):
    # O(n^2) approach
    n = len(s)
    count = 0
    for i in range(n):
        for j in range(i,n):
            if(isPalinduram(s[i:j+1])):
                count += 1
    return count


def countPaliduram(s):
    count = 0
    n = len(s)
    for i in range(n):
        # odd length
        l = i
        r = i
        while(l >= 0 and r < n and s[l] == s[r]):
            count += 1
            l -= 1
            r += 1

        # even length
        l = i
        r = i+1
        while(l >= 0 and r < n and s[l] == s[r]):
            count += 1
            l -= 1
            r += 1

    return count

s = input()
print(countPaliduram(s))
#print(countPalinduramNavie(s))
