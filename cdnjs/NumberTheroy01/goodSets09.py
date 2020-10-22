'''
Find the good sets!
You are given array a consisting of n distinct integers. A set s of numbers is called good if you can rearrange the
elements in such a way that each element divides the next element in the order, i.e. 'si' divides 'si + 1', 
such that i < |s|, where |s| denotes size of set |s|.
Find out number of distinct good sets that you can create using the values of the array. You can use one value only once in a particular set;
ie. a set cannot have duplicate values. Two sets are said to be different from each other if there exists an element in one set, which does not exist in the other.
As the answer could be large, print your answer modulo 10^9 + 7.

Input
First line of the input contains an integer T denoting the number of test cases. T test cases follow.

First line of each test case contains an integer n denoting number of elements in array a.

Next line contains n space separated integers denoting the elements of array a.

Output
For each test case, output a single line containing the corresponding answer.

Constraints
1 ≤ T ≤ 3

1 ≤ n ≤ 7.5 * 10^5

1 ≤ ai ≤ 7.5 * 10^5

All the elements of array a are distinct.

Example

Input
2
2
1 2
3
6 2 3

Output:
3
5

Explanation
Test case 1. There are three sets which are good {1}, {2}, {1, 2}.

Test case 2. There are five sets which are good {6}, {2}, {3}, {6 2}, {6, 3

'''


def seive(sets, n):
    for i in range(1, n//2 + 1):
        if sets[i] != 0:
            for j in range(2*i,n,i):
                if sets[j] != 0:
                    sets[j] += sets[i]
    sum = 0
    mod = 1000000007
    for i in range(n):
        if sets[i] != 0:
            sum = (sum + sets[i] % mod)%mod
    return sum

tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = [int(x) for x in input().split()]
    high = max(arr)
    sets = [0 for _ in range(high+1)]
    for val in arr:
        sets[val] = 1
    ans = seive(sets, high+1)
    print(ans)
