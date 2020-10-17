'''
Given a string and a pattern, find pattern exist in the given string or not


Input:
sfsafsafsa
fsa

Output:
True

Input:
fsagfsagsag
safg

Output:
False

'''
# time complaxity O(N) for finding one pattern
# for finding all the pattern it will take O(M + N)

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
        return True
    return False

string = input()
pattern = input()
print(kmpSearch(string, pattern))
