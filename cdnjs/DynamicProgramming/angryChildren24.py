'''
Angry Children

Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to distribute 
one packet to each of the K children in the village (each packet may contain different number of candies). To avoid a fight between 
the children, he would like to pick K out of N packets such that the unfairness is minimized.
Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi denotes the number of candies in the ith packet, then we define unfairness as

unfairness=0;
for(i=0;i<n;i++)
for(j=0;j<n;j++)
    unfairness+=abs(xi-xj)
abs(x) denotes absolute value of x.

Input Format
The first line contains an integer N.
The second line contains an integer K.
N lines follow each integer containing the candy in the ith packet.

Output Format
A single integer which will be minimum unfairness.
Constraints
2<=N<=10^5

2<=K<=N

0<= number of candies in each packet <=10^9

Sample Input
7
3
10
100
300
200
1000
20
30

Sample Output
40
Explanation
Bill Gates will choose packets having 10, 20 and 30 candies.So unfairness will be |10-20| + |20-30| + |10-30| = 40. We can verify that it will be minimum in this way.


'''

n = int(input())
k = int(input())
arr = [0]*n
for i in range(n):
    arr[i] = int(input())

arr.sort()
target = 0
sum = [0]*(n+1)
sum[0] = 0
for i in range(n):
    sum[i+1] = sum[i] + arr[i]

c = 0
ans = -1
for i in range(k):
    c += arr[i]*(2*i+1)
i = 0
while(i+k <= n):
    z = c - k*(sum[i+k] - sum[i])
    ans = z if(ans == -1) else min(z, ans)
    if(i+k < n):
        c = c - 2*(sum[i+k] - sum[i+1]) - arr[i] + (2*k - 1)*arr[i+k]
    i += 1

print(ans)

