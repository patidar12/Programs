'''
Number Of Factors
A number is called n-factorful if it has exactly n distinct prime factors. Given positive integers a, b, and n, 
your task is to find the number of integers between a and b, inclusive, that are n-factorful. We consider 1 to be 0-factorful.

Input
Your input will consist of a single integer T followed by a newline and T test cases. Each test cases consists
of a single line containing integers a, b, and n as described above.

Output
Output for each test case one line containing the number of n-factorful integers in [a, b].

Constraints
T < 10000

1 ≤ a ≤ b ≤ 10^6

0 ≤ n ≤ 10

Sample Input
5
1 3 1
1 10 2
1 10 3
1 100 3
1 1000 0

Sample Output
2 
2
0
8
1

'''

import math
class const:
    ROW = 10
    COL = 1000000

def seive(nFact):
    arr = [0 for i in range(const.COL+1)]
    arr[0] = -1
    arr[1] = 0
    for i in range(2, (const.COL + 1)//2 + 1):
        if arr[i] == 0:
            for j in range(i,const.COL+1,i):
                arr[j] += 1
    for i in range(0,const.ROW+1):
        for j in range(0,const.COL+1):
            if arr[j] == i:
                nFact[i][j] = nFact[i][j-1] + 1
            else:
                nFact[i][j] = nFact[i][j-1]

nFact = [[0 for i in range(const.COL+1)] for j in range(const.ROW+1)]
seive(nFact)
tcs = int(input())
for tc in range(tcs):
    a, b, n = map(int, input().split())
    ans = nFact[n][b] - nFact[n][a-1]
    print(ans)
