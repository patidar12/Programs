'''
Find Prime Numbers From 1 to N
Given a number N, find number of primes in the range [1,N].

Input:
The only line of input consists of a number N

Output:
Print the number of primes in the range [1,N].`

Constraints:
1≤N≤1000000

Sample Input :
3 

Sample Output -
2

'''
import math
def checkPrimeNaive(n):
    # using this time complexity for finding prime numbers from 1 to N
    # n*sqrt(n)

    if(n <= 1):
        return False
    last = int(math.sqrt(n)) + 1
    for i in range(2, last):
        if(n%i == 0):
            return False
    return True

def checkPrime(prime, n):
    # using this time complexity for finding prime numbers from 1 to N
    # n*log(log(n))

    prime[0] = False
    prime[1] = False
    last = int(math.sqrt(n)) + 1
    for i in range(2, last):
        if(prime[i] == True):
            for j in range(i*i,n+1,i):
                prime[j] = False
    
def getPrimes(n):
    prime = [True]*1000001
    checkPrime(prime, 1000000)
    count = 0
    for i in range(1,n+1):
        if prime[i]:
            count += 1
        '''
        if(checkPrimeNaive(i)):
            count+=1
        '''
    return count        

num = int(input())
print(getPrimes(num))
