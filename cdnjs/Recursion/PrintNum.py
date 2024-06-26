"""
Print Numbers
Send Feedback
Given is the code to print numbers from 1 to n in increasing order recursively. But it contains few bugs that you need to rectify such that all the test cases pass.
Input Format :
Integer n
Output Format :
Numbers from 1 to n (separated by space)
Constraints :
1 <= n <= 10000
Sample Input 1 :
 6
Sample Output 1 :
1 2 3 4 5 6
Sample Input 2 :
 4
Sample Output 2 :
1 2 3 4

"""
import sys
sys.setrecursionlimit(10**5)
def print1toN(n):
    if(n == 1):
        print(n,end = ' ')
        return
    print1toN(n-1)
    print(n,end=' ')

n = int(input())
print1toN(n)
