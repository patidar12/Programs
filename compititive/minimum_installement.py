'''
There are n friends who live in society. Whenever a friend is in Debt, a friend borrows money from another friend to clear it. A friend has already borrowed money m times from other friends.

Due to a misunderstanding between them, all friends want to clear what they owe each other. So they plan to clear their borrowed money i.e. debt in such a way that their total number of installments is minimized as charges per installment are very high. For example, if the k(th) person pays i(th) person A $, then the amount of particular installment is A.

You are required to minimize the sum of the installment amount.

First line: Two integers n and m.

Next m lines: Three integers v(i), u(i), and w(i) which means that u(i)th person has lent the v(i)th person w(i) amount of dollars.

Sample Input
2 3

1 2 10

1 2 3

2 1 5

Sample Output
8

'''
# cook your dish here
n,m = map(int,input().split())
arr = [0]*(n+1)
for i in range(m):
    first,second,amt = map(int,input().split())
    arr[second] += amt
    arr[first] -= amt
count = 0
for i in range(1,n+1):
    if(arr[i] > 0):
        count += arr[i]
print(count)        
