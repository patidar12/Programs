'''

Hasan and Trip
Hasan has finally finished his final exams and he decided to go in a trip among cities in Syria.
There are N cities in Syria and they are numbered from 1 to N, each city has coordinates on plane, i-th city is in (Xi, Yi).
Hasan is in first city and he wants to visit some cities by his car in the trip but the final destination should be N-th city and 
the sequence of cities he will visit should be increasing in index (i.e. if he is in city i he can move to city j if and only if i < j ).
Visiting i-th city will increase Hasan's happiness by Fi units (including first and last cities), also Hasan doesn't like traveling too much, 
so his happiness will decrease by total distance traveled by him.
Help Hasan by choosing a sequence of cities to visit which maximizes his happiness.

Input format:
First line contain integer N.
Next N lines contains three integers each, i-th line contains coordinates of i-th city Xi, Yi and Fi.

Output format:
Output one number rounded to 6 digits after floating point, the maximum possible happiness Hasan can get. Note: If answer is 2 print 2.000000

Constraints:
1 <= N <= 3,000
0 <= Xi, Yi, Fi <= 100,000

Sample Input
3
0 0 1
3 1 1
6 0 9

Sample Output
4.675445


'''

import math

def dis(d1, d2):
    return math.sqrt( (d2[0]-d1[0])* (d2[0]-d1[0]) + (d2[1]-d1[1])*(d2[1]-d1[1])   )

n = int(input())
d = [None]*n
F = [0]*n
for i in range(n):
    f, s, fun = map(int, input().split())
    d[i] = (f, s)
    F[i] = fun

dp = [0]*n
dp[0] = F[0]
for i in range(1, n):
    dp[i] = -2**31
    for j in range(0, i):
        x = dis(d[i], d[j])
        dp[i] = max(dp[i], dp[j] - x)
    dp[i] +=F[i]

print("{:.6f}".format(dp[i]))
