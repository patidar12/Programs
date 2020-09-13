'''
Maximum Sum Rectangle

Given a 2D array, find the maximum sum rectangle in it. In other words find maximum sum over all rectangles in the matrix.

Input
First line contains 2 numbers n and m denoting number of rows and number of columns.
Next n lines contain m space separated integers denoting elements of matrix nxm.

Output
Output a single integer, maximum sum rectangle.

Constraints
1<=n,m<=100

Sample Input
4 5
1 2 -1 -4 -20
-8 -3 4 2 1
3 8 10 1 3
-4 -1 1 7 -6

Sample Output
29

'''

def kadnan(arr,n):
    max_sum = -2**31
    curr_sum = 0
    for i in range(n):
        curr_sum = max(curr_sum+arr[i],arr[i])
        max_sum = max(max_sum,curr_sum)
    return max_sum

def maxSumRect(arr,R,C):
    maxSum = -2**31
    for left in range(C):
        #dp = [0]*R
        dp = [0 for x in range(R)]
        for right in range(left,C):
            for i in range(R):
                dp[i] += arr[i][right]
            currSum = kadnan(dp,R)
            maxSum = max(maxSum,currSum)
    return maxSum


R,C = map(int,input().split())
arr = [0]*R
for i in range(R):
    val = [int(x) for x in input().split()]
    arr[i] = val

print(maxSumRect(arr,R,C))
