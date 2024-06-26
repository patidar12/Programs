'''
Magic Grid Problem
Send Feedback
You are given a magrid S ( a magic grid ) having R rows and C columns. Each cell in this magrid has either
a Hungarian horntail dragon that our intrepid hero has to defeat, or a flask of magic potion that his teacher
Snape has left for him. A dragon at a cell (i,j) takes away |S[i][j]| strength points from him, and 
a potion at a cell (i,j) increases Harry's strength by S[i][j]. If his strength drops to 0 or less at 
any point during his journey, Harry dies, and no magical stone can revive him.
Harry starts from the top-left corner cell (1,1) and the Sorcerer's Stone is in the bottom-right corner cell (R,C).
From a cell (i,j), Harry can only move either one cell down or right i.e., to cell (i+1,j) or cell (i,j+1)
and he can not move outside the magrid. Harry has used magic before starting his journey to determine which cell
contains what, but lacks the basic simple mathematical skill to determine what minimum strength he needs to start with 
to collect the Sorcerer's Stone. Please help him once again.

Input (STDIN)
The first line contains the number of test cases T. T cases follow. Each test case consists of R C in the first line followed
by the description of the grid in R lines, each containing C integers.
Rows are numbered 1 to R from top to bottom and columns are numbered 1 to C from left to right.
Cells with S[i][j] < 0 contain dragons, others contain magic potions.

Output (STDOUT):
Output T lines, one for each case containing the minimum strength Harry should start with from the cell (1,1) 
to have a positive strength through out his journey to the cell (R,C).

Constraints:
1 ≤ T ≤ 5

2 ≤ R, C ≤ 500

-10^3 ≤ S[i][j] ≤ 10^3

S[1][1] = S[R][C] = 0

Sample Input
3
2 3
0 1 -3
1 -2 0
2 2
0 1
2 0
3 4
0 -2 -3 1
-1 4 0 -2
1 -2 -3 0

Sample Output
2
1
2

'''


def minHelthR(arr,si,sj,ei,ej,dp):
    if(si == ei and sj == ej):
        dp[si][sj] = (abs(arr[si][sj])+1) if (arr[si][sj] < 0) else 1
        return dp[si][sj]
    if(si > ei or sj > ej):
        return 2**31
    if(dp[si][sj] > -1):
        return dp[si][sj]
    down = minHelth(arr,si+1,sj,ei,ej,dp)
    right = minHelth(arr,si,sj+1,ei,ej,dp)
    need = min(down,right)
    if(need != 2**31):
        need -= arr[si][sj]
    result = 1 if need <= 0 else need
    dp[si][sj] = result
    return result

def minHelthI(arr,R,C,dp):
    dp[R-1][C-1] = abs(arr[R-1][C-1]) + 1 if arr[R-1][C-1] < 0 else 1
    for i in range(R-2,-1,-1):
        need = dp[i+1][C-1] - arr[i][C-1]
        dp[i][C-1] = 1 if need <= 0 else need
    for i in range(C-2,-1,-1):
        need = dp[R-1][i+1] - arr[R-1][i]
        dp[R-1][i] = 1 if need <= 0 else need

    for i in range(R-2,-1,-1):
        for j in range(C-2,-1,-1):
            need = min(dp[i+1][j],dp[i][j+1]) - arr[i][j]
            dp[i][j] = 1 if need <= 0 else need
    return dp[0][0]

def magicGrid(arr,R,C):
    dp = [[-1 for i in range(C)] for j in range(R)]
    #ans = minHelthR(arr,0,0,R-1,C-1,dp)
    ans = minHelthI(arr,R,C,dp)
    return ans

from sys import setrecursionlimit
setrecursionlimit(11000)
tcs = int(input())
for tc in range(tcs):
    R,C = map(int,input().split())
    arr = []
    for i in range(R):
        val = [int(x) for x in input().split()]
        arr.append(val)
    print(magicGrid(arr,R,C))
