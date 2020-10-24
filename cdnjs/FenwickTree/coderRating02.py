'''
Coder's Rating
Some of the more elite (and not-so-elite) coders around take part in a certain unnamed programming contest. In said contest, there are multiple
types of competitions. Here, we consider the Open and High School competition types. For each type, each competitor receives a rating, an integer
between 1 and 100000, inclusive. A coder's rating is based upon his or her level of performance in matches and is calculated using a complicated 
formula which, thankfully, you will not be asked to implement.
Although the Open and High School ratings for a coder who has participated in both competition types lately are usually close, this is not always the case.
In particular, High School matches are more about speed, since many coders are able to solve all the problems, whereas Open matches require more thinking and 
there is a steeper curve in terms of problem difficulty.

Problem Statement
You are given N coders (1 ≤ N ≤ 300000), conveniently numbered from 1 to N. Each of these coders participates in both High School and Open matches. 
For each coder, you are also given an Open rating Ai and a High School rating Hi. Coder i is said to be better than coder j if and only if both of 
coder i's ratings are greater than or equal to coder j's corresponding ratings, with at least one being greater.
For each coder i, determine how many coders coder i is better than.

Input Format
On the first line of input is a single integer N, as described above. N lines then follow.
Line i+1 contains two space-separated integers, Ai and Hi.

Output Format
Line i should contain the number of coders that coder i is better than.

Sample Input
8
1798 1832
862 700
1075 1089
1568 1557
2575 1984
1033 950
1656 1649
1014 1473

Sample Output
6
0
2
4
7
1
5
1

'''

def update(y,BIT):
    while(y<100001):
        BIT[y] += 1
        y += (y&-y)

def query(y,BIT):
    count = 0
    while(y>0):
        count += BIT[y]
        y -= (y&-y)
    return count
n = int(input())
arr = [None]*n
for i in range(n):
    x,y = map(int,input().split())
    arr[i] = (i,x,y)

arr.sort(key=lambda l: (l[1], l[2]))
BIT = [0]*100001
ans = [0]*n
i = 0
while(i < n):
    endindex = i
    while(endindex < n and arr[i][1] == arr[endindex][1] and arr[i][2] == arr[endindex][2]):
        endindex += 1
    for j in range(i,endindex):
        ans[arr[j][0]] = query(arr[j][2],BIT)
    for j in range(i,endindex):
        update(arr[j][2],BIT)
    i = endindex

for i in range(n):
    print(ans[i])

