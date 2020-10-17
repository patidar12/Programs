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

# Note: Navie approach O(N*M)

def isMatching(string, pattern):
    n = len(string)
    m = len(pattern)
    isFound = True
    for i in range(n-m+1):
        isFound = True
        for j in range(m):
            if(string[i+j] != pattern[j]):
                isFound = False
                break
    return isFound

string = input()
pattern = input()
print(isMatching(string, pattern))

