'''
Given a string and a pattern, print started index of all the matched pattern in the string


Input:
sfsafsafsa
fsa

Output:
1
4
7

Input:
fsagfsagsag
safg

Output:


'''

def zAlgo(string):
    n = len(string)
    z = [0]*n
    l = 0
    r = 0
    for i in range(1, n):
        if(i > r):
            # i does not lie b/w l and r
            # z for this dose not exist
            l = i
            r = i
            while(r < n and string[r-l] == string[r]):
                r += 1
            z[i] = r - l
            r -= 1
        else:
            k = i - l
            if(z[k] <= r - i):
                # i lies b/w l and r
                # z exist previously
                z[i] = z[k]
            else:
                # some of the z already included
                # start matching further
                l = i
                while(r < n and z[l-r] == z[r]):
                    r += 1
                z[i] = r-l
                r -= 1
    return z

def zSearch(string, pattern):
    nStr = pattern + '$' + string
    n = len(nStr)
    z = zAlgo(nStr)
    for i in range(n):
        if(z[i] == len(pattern)):
            print(i - (len(pattern)+1))

string = input()
pattern = input()
zSearch(string, pattern)
