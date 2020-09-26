'''
Weighted Job Scheduling

You are given N jobs where every job is represented as:

1.Start Time
2.Finish Time
3.Profit Associated

Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

Input
The first line of input contains one integer denoting N.
Next N lines contains three space separated integers denoting the start time, finish time and the profit associated with the ith job. 

Output
Output one integer, the maximum profit that can be achieved.

Constraints
1 ≤ N ≤ 10^6
1 ≤ ai, di, p ≤ 10^6

Sample Input
4
3 10 20
1 2 50
6 19 100
2 100 200

Sample Output
250


'''

def maxProfit(arr, n):
    arr.sort(key = lambda x:x[1])
    dp = [0]*n
    dp[0] = arr[0][2]
    for i in range(1,n):
        ans = arr[i][2]
        index = -1
        min_index = 0
        max_index = i-1
        while(min_index <= max_index):
            mid = min_index + (max_index - min_index)//2
            if(arr[i][0] >= arr[mid][1]):
                index = mid
                min_index = mid + 1
            else:
                max_index = mid - 1
        if(index != -1):
            ans += dp[index]
        dp[i] = max(dp[i-1], ans)
    return dp[n-1]


n = int(input())
arr = [None]*n
for i in range(n):
    st,ft,pa = map(int, input().split())
    arr[i] = (st, ft, pa)
print(maxProfit(arr, n))
