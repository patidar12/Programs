'''
Samantha and Sam are playing a numbers game. Given a number as a string, no leading zeros, 
determine the sum of all integer values of substrings of the string.
For example, if the string is 42, the substrings are 4,2 and 42. Their sum is 48.

Given an integer as a string, sum all of its substrings cast as integers.
As the number may become large, return the value modulo 10^9 + 7.

Function Description

Complete the substrings function in the editor below. It should return the sum of the integer
values of all substrings in a string representation of a number, modulo 10^9 + 7.

substrings has the following parameter(s):
    n: the string representation of an integer

Input Format

A single line containing an integer as a string without leading zeros.

Constraints
1 <= n <= 2*10*5

Output Format

A single line which is sum of the substrings 

Sample Input 0
16

Sample Output 0
23

Explanation 0

The substring of number 16 are 16, 1 and 6 which sums to 23.

Sample Input 1
123

Sample Output 1
164

Explanation 1

The sub-strings of 123 are 1, 2, 3, 12, 23, 123 which sums to 164.

'''

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the substrings function below.
def substrings(n):
    mod = 1000000007
    lastSum = int(n[0])
    totalSum = int(n[0])
    for i in range(1,len(n)):
        lastSum = (lastSum*10 + int(n[i])*(i+1))%mod
        totalSum = (totalSum + lastSum)%mod
    return totalSum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = input()

    result = substrings(n)

    fptr.write(str(result) + '\n')

    fptr.close()

