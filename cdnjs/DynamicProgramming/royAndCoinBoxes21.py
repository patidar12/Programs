'''
Roy and Coin Boxes
Roy has N coin boxes numbered from 1 to N.
Every day he selects two indices [L,R] and adds 1 coin to each coin box starting from L to R (both inclusive).
He does this for M number of days.

After M days, Roy has a query: How many coin boxes have atleast X coins.
He has Q such queries.

Input
First line contains N - number of coin boxes.
Second line contains M - number of days. Each of the next M lines consists of two space separated integers L and R. Followed by integer Q - number of queries.
Each of next Q lines contain a single integer X.a

Output
For each query output the result in a new line.

Constraints
1 ≤ N ≤ 1000000

1 ≤ M ≤ 1000000

1 ≤ L ≤ R ≤ N

1 ≤ Q ≤ 1000000

1 ≤ X ≤ N

Sample Input
7
4
1 3
2 5
1 2
5 6
4
1
7
4
2

Sample Output
6
0
0
4


'''


n = int(input())
m = int(input())
strt = [0]*1000001
end = [0]*1000001
ans = [0]*1000001
days = [0]*1000001

for i in range(m):
    l, r = map(int, input().split())
    strt[l] += 1  #noting the time the starting box was kth box
    end[r] += 1  #noting the time the ending box was kth box

c = 0
for i in range(1,n+1):
    c += strt[i]
    days[i] = c # number of coin in a box is same as number of days the coin was put in the box
    c -= end[i]

# now calculate how many boxes has excetly i couns
for i in range(1, n+1):
    ans[days[i]] += 1

'''
now calculate how many boxes have atleast i coins which is same as
number of boxes having atleast i+ coins + number of boxes having exect i coins
Note: box with atleas max coins is same as box with exact k coins
In other word we can take max as n ans start iterating from n-1
'''
for i in range(n-1,0,-1):
    ans[i] = ans[i] + ans[i+1]

q = int(input())
for i in range(q):
    x = int(input())
    print(ans[x])

