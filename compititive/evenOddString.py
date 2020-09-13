'''
Hackerearth:
    https://www.hackerearth.com/problem/algorithm/even-the-odds-85c214b5/description/

There are n strings of even length and m strings of odd length. You can select any number of strings (non-zero)
from these collections and the resulting string is the concatenation of the chosen strings.
You cannot break any string, therefore, you either select the whole string or you do not select it at all.

The total_length of the string is equal to the sum of the length of all the selected strings. 
Your task is to determine how many of these total_length are even.
Since this number can be very large, print it modulo 10^9 + 7.

Input format

The first line contains a single integer T denoting the number of test cases.
(1 <= T <= 10^5)
Next T lines contain two space-separated integers n and m as described in the problem statement.
(1 <= n,m <= 10^6)

Output format

Print a single integer denoting the answer to the problem modulo 10^9 + 7.

SAMPLE INPUT
3
2 1
1 2
1 1

SAMPLE OUTPUT
3
3
1

Explanation
In the first case, the 3 possibilities are: choose the first even length string, choose the second even length string or 
choose the first and second string both. In no other case you can have an even total_length.

In the second case, the 3 possibilities are: choose the first even length string, choose both the odd length strings or choose all the strings

'''

"""
tcs = int(input())
for tc in range(tcs):
    evenString,oddString = map(int,input().split())
    mod = 1000000007
    '''
    e1 = ((1<<evenString)-1)%mod
    e2 = ((1<<oddString)//2 - 1)%mod
    e1e2 = (e1*e2)%mod
    total = (e1+e2+e1e2)%mod
    '''
    total = ((1 << (evenString+oddString-1)) - 1) %mod
    print(total)
"""
t = int(input())
while t > 0:
	[n, m] = list(map(int, input().split(' ')))
	print(pow(2, n + m - 1, 1000000007) - 1)
	t -= 1
