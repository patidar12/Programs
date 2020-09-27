'''
CodeChef:
    https://www.codechef.com/problems/SVENGY


There are N towns in a line, numbered from 0 to N - 1. Starting from town 0, we want to reach town N - 1. From town i,
we can jump to any town j > i with an energy cost of (j-i)*A[i] + (j2 - i2)*A[i]2, where A[i] for all i are given in input.

Find the minimum total energy cost to reach town N - 1 from town 0.

Input

The first line contains a single integer, N.
The next line contains N space separated integers, ith integer denoting the value of A[i] , 0 ≤ i ≤ N - 1.

Output

Output the minimum cost to reach town N.

Constraints

1 ≤ N ≤ 105
-103 ≤ A[i] ≤ 103

Example 1

Input:
5
1 -1 2 2 2

Output:
14

Example 2

Input:
4
2 2 3 4

Output:
42

'''


def minCost(arr, n):
    i = 0
    cost = 0
    for j in range(n):
        if(abs(arr[j]) < abs(arr[i]) or (abs(arr[i]) == abs(arr[j])\
        and arr[i] > 0) or j == n-1):
            res = (j - i)*arr[i] + (j*j - i*i)*(arr[i]*arr[i])
            cost += res
            i = j
    return cost


n = int(input())
arr = list(map(int, input().split()))
print(minCost(arr, n))
