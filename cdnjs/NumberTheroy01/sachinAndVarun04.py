'''
Sachin And Varun Problem
Varun and you are talking about a movie that you have recently watched while Sachin is busy teaching Number Theory.
Sadly, Sachin caught Varun talking to you and asked him to answer his question in order to save himself from punishment. The question says:
Given two weights of a and b units, in how many different ways you can achieve a weight of d units using only the given weights?
Any of the given weights can be used any number of times (including 0 number of times).
Since Varun is not able to answer the question, he asked you to help him otherwise he will get punished.
Note: Two ways are considered different if either the number of times a is used or number of times b is used is different in the two ways.

Input Format:
The first line of input consists of an integer 
T denoting the number of test cases.
Each test case consists of only one line containing three space separated integers a, b and d.

Output Format:
For each test case, print the answer in a separate line.

Constraints:
1 ≤T≤ 10^5

1 ≤ a < b ≤ 10^9

0≤d≤10^9

Sample Input 1
4
2 3 7
4 10 6
6 14 0
2 3 6

Sample Output 1
1
0
1
2

Explanation
Test case 1: 7 can only be achieved by using 2 two times and 3 one time.

Test case 2: 6 can't be achieved by using 4 and 10 .So, 0ways are there.

'''
class Triplet:
	gcd = 0
	x = 0
	y = 0

def gcd(a, b):
    # Euclid Algorithm
    # Time Complexity O(log(min(a, b)))
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    return gcd(b, a%b)

def extendedEuclid(a, b):
    if(b == 0):
        ans = Triplet()
        ans.gcd = a
        # aX + bY = gcd(a,b)
        # if b == 0 then Y = 0
        # aX = a if X = 1
        ans.x = 1
        ans.y = 0
        return ans
    smallAns = extendedEuclid(b, a%b)
    ans = Triplet()
    ans.gcd = smallAns.gcd
    #X = Y1
    #Y = X1 - (a/b)Y1
    ans.x = smallAns.y
    ans.y = smallAns.x - (a//b)*smallAns.y
    return ans


def modInverse(A, M):
    ans = extendedEuclid(A, M)
    x = ans.x
    return (x % M + M) % M

def main():
    t = int(input())
    while(t != 0):
        t -= 1
        a, b , d = map(int, input().split())
        g = gcd(a,b)

        # Special Cases
        if(d%g):
            print('0')
            continue
        if(d == 0):
            print('1')
            continue
        a//=g
        b//=g
        d//=g
        y1  = ((d%a) * modInverse(b,a) ) %a
        firstValue = d//b
        if(d < y1*b):
            print('0')
            continue

        n = (firstValue - y1)//a
        ans = n +1
        print(ans)

if __name__ == '__main__':
    main()
