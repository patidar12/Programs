'''
Given an integer h, find the possible number of balanced binary trees of height h. You just need to return the count of possible binary trees which are balanced.
This number can be huge, so return output modulus 10^9 + 7.
Write a simple recursive solution.
Input Format :
Integer h
Output Format :
Count % 10^9 + 7
Input Constraints :
1 <= h <= 40
Sample Input 1:
3
Sample Output 1:
15
Sample Input 2:
4
Sample Output 2:
315


'''

prime = 1000000007
def balancedBTBF(n):
    ''' Return no of balanced BT of height n using Brute Force'''
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    if(n == 0 or n == 1):
        return 1
    x = balancedBTBF(n-1)
    y = balancedBTBF(n-2)
    a = int(((x*x)%prime))
    b = int(((2*x*y)%prime))
    return (a+b)%prime

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
n=int(input())
print(balancedBTBF(n))
