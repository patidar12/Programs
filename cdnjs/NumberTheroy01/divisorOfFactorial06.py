'''
Divisors Of Factorial

Given a number, find the total number of divisors of the factorial of the number.
Since the answer can be very large, print answer modulo 10^9+7.

Input
The first line contains T, number of testcases.
T lines follows each containing the number N.

Output
Print T lines of output each containing the answer.

Constraints
1 <= T <= 500

0 <= N <= 50000

Sample Input:
3
2
3
4

Sample Output:
2
4
8

'''


import math

MAX = 50001
MOD = 1000000007

def seive():
    primes = [True]*MAX
    primes[0] = False
    primes[1] = False
    for i in range(2, int(math.sqrt(MAX)) + 1):
        if primes[i]:
            for j in range(i*i,MAX, i):
                primes[j] = False
    v = []
    v.append(2)
    for i in range(3,MAX,2):
        if(primes[i]):
            v.append(i)
    return v

def getDivisors(n, primes):
    result = 1
    i = 0
    while(primes[i] <= n):
        count = 0
        k = primes[i]
        while(n//k != 0):
            count = (count + n//k)%MOD
            k = k*primes[i]
        result = (result* ((count+1)%MOD))%MOD
        i += 1
    return result

tcs  = int(input())

primes = seive()
for tc in range(tcs):
    n = int(input())
    ans = getDivisors(n, primes)
    print(ans)
