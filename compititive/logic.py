'''
Statement
One day while visiting an unknown place, Chef found the person playing with logic and found it interesting. Chef also join the game and now the person gave him an integer N and ask him to build a logic. Now as Chef is new to logic, help him to find a better logic.

In other words, find the logic between Input and Output.

Input Format
The first line contains the number of test cases t. Each of the next t lines contains an integer N.

Output Format
For each test case print the required output.

Constraints
1 <= t <= 10

1 <= N <= 10000

Sample Input
4

5

10

23

1

Sample Output
15

50

276

1

'''

t = int(input())
for i in range(t):
    n = int(input())
    rem = n%2
    div = n//2
    print(n*(div+rem))
