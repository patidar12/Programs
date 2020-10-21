'''
GCD
Calculate and return GCD of two given numbers x and y. Numbers are within range of Integer.

Input format :
x and y (separated by space)

Output format :
GCD of x and y

Sample Input 1:
20 
5

Sample Output 1:
5

Sample Input 2:
96 
14

Sample Output 2:
2

'''
## Read input as specified in the question.
## Print output as specified in the question.
def gcdNieve(a, b):
    # Time Complexity O(min(a, b))
    ans = 0
    for i in range(1, min(a, b) + 1):
        if a%i == 0 and b%i == 0:
            ans = i
    return ans


def gcd(a, b):
    # Euclid Algorithm
    # Time Complexity O(log(min(a, b)))
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

a = int(input())
b = int(input())
print(gcd(a, b))
#print(gcdNieve(a, b))
