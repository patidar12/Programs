'''
Minimum Count
Send Feedback
Given an integer N, find and return the count of minimum numbers, sum of whose squares is equal to N.
That is, if N is 4, then we can represent it as : {1^2 + 1^2 + 1^2 + 1^2} and {2^2}. Output will be 1, as 1 is the minimum count of numbers required.
Note : x^y represents x raise to the power y.

Input Format :
Integer N

Output Format :
Required minimum count

Constraints :
1 <= N <= 1000

Sample Input 1 :
12

Sample Output 1 :
3

Sample Output 1 Explanation :

12 can be represented as :
1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1
1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 1^1 + 2^2
1^1 + 1^1 + 1^1 + 1^1 + 2^2 + 2^2
2^2 + 2^2 + 2^2

As we can see, the output should be 3.

Sample Input 2 :
9

Sample Output 2 :
1

'''

## Read input as specified in the question.
## Print output as specified in the question.
import math
def minCount(n):
    dp = [0]*(n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in range(4,n+1):
        dp[i] = i
        for j in range(1,math.ceil(math.sqrt(i))+1):
            k = i - j*j
            if(k >= 0):
                dp[i] = min(dp[i], dp[k] + 1)
    return dp[n]

n = int(input())
print(minCount(n))
