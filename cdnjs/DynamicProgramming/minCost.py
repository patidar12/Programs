'''
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost
of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse
through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path 
(including both source and destination). 
You can only traverse down, right and diagonally lower cells from a given cell,i.e., from a given cell (i, j), 
cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed.
You may assume that all costs are positive integers.

Input:

3 3
1 2 3
4 8 2
1 5 3

Output:
8

'''

def getCostR(arr,si,sj,ei,ej,dp):
    if(si == ei and sj == ej):
        return arr[si][sj]
    if(si > ei or sj > ej):
        return 2**31
    if(dp[si][sj] > -1):
        return dp[si][sj]
    down = getCostR(arr,si+1,sj,ei,ej,dp)
    digo = getCostR(arr,si+1,sj+1,ei,ej,dp)
    right = getCostR(arr,si,sj+1,ei,ej,dp)
    result = arr[si][sj] + min(down,min(digo,right))
    dp[si][sj] = result
    return result

def getCostI(arr,R,C,dp):
    dp[R-1][C-1] = arr[R-1][C-1]
    for i in range(R-2,-1,-1):
        dp[i][C-1] = arr[i][C-1] + dp[i+1][C-1]
    for i in range(C-2,-1,-1):
        dp[R-1][i] = arr[R-1][i] + dp[R-1][i+1]
    for i in range(R-2,-1,-1):
        for j in range(C-2,-1,-1):
            dp[i][j] = arr[i][j] + min(dp[i+1][j],min(dp[i+1][j+1],dp[i][j+1]))

    return dp[0][0]
def minCost(arr,R,C):
    dp = [[-1 for i in range(C)] for j in range(R)]
    #ans =  getCostR(arr,0,0,R-1,C-1,dp)
    ans = getCostI(arr,R,C,dp)
    return ans

R, C = map(int, input().split())
arr = [0]*R
for i in range(R):
    value = [int(x) for x in input().split()]
    arr[i] = value
print(minCost(arr,R,C))
