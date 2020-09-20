'''
Hackerrank:
    https://www.hackerrank.com/challenges/construct-the-array/problem
Your goal is to find the number of ways to construct an array such that consecutive positions contain different values.

Specifically, we want to construct an array with n elements such that each element between 1  and k, inclusive. We also want the first and last elements of the array to be 1 and x.

Given n, k and x, find the number of ways to construct such an array.
Since the answer may be large, only find it modulo 10^9 + 7.

For example, for n = 4, k = 3, x = 2, there are 3 ways.
1 2 1 2
1 2 3 2
1 3 1 2

Complete the function countArray which takes input n, k and x. 
Return the number of ways to construct the array such that consecutive elements are distinct.

Constraints
3 <= n <= 10^5
2 <= k <= 10^5
1 <= x <= k

Sample Input

n = 4, k = 3, x = 2 

Sample Output
3

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countArray function below.
def countArray(n, k, x):
    # Return the number of ways to fill in the array.
    oneCount = 1
    nonOneCount = 0
    mod = 1000000007
    for i in range(1,n):
        prevOneCount = oneCount
        oneCount = (nonOneCount * (k-1))%mod
        nonOneCount = (prevOneCount + (nonOneCount*(k-2))%mod)%mod
    if(x == 1):
        return oneCount
    return nonOneCount

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()

