'''
Maximum Square Matrix With All Zeros
Send Feedback
Given a n*m matrix which contains only 0s and 1s, find out the size of maximum square sub-matrix with all 0s. You need to return the size of square with all 0s.
Input format :
Line 1 : n and m (space separated positive integers)
Next n lines : m elements of each row (separated by space).
Output Format:
Line 1 : Size of maximum square sub-matrix
Sample Input :
3 3
1 1 0
1 1 1
1 1 1
Sample Output :
1


'''

## Read input as specified in the question.
## Print output as specified in the question.
def maxSqareMatrixWithZerosR(arr,R,C,dp,maxSize):
    if(R == 1 or C == 1):
        dp[R-1][C-1] = 1 if arr[R-1][C-1] == 0 else 0
        maxSize[0] = dp[R-1][C-1] if dp[R-1][C-1] > maxSize[0] else maxSize[0]
        return dp[R-1][C-1]

    if(dp[R-1][C-1] > -1):
        return dp[R-1][C-1]
    left = maxSqareMatrixWithZerosR(arr,R,C-1,dp,maxSize)
    upper = maxSqareMatrixWithZerosR(arr,R-1,C,dp,maxSize)
    digo = maxSqareMatrixWithZerosR(arr,R-1,C-1,dp,maxSize)
    result = 0
    if(arr[R-1][C-1] == 0):
        result = min(left,min(upper,digo))+1
    dp[R-1][C-1] = result
    maxSize[0] = dp[R-1][C-1] if dp[R-1][C-1] > maxSize[0] else maxSize[0]
    return result

def maxSqareMatrixWithZerosI(arr,R,C):
    maxSize = 0
    for i in range(R):
        arr[i][0] = 1 if arr[i][0] == 0 else 0
        maxSize = arr[i][0] if maxSize < arr[i][0] else maxSize
    for i in range(C):
        arr[0][i] = 1 if arr[0][i] == 0 else 0
        maxSize = arr[0][i] if maxSize < arr[0][i] else maxSize
    for i in range(1,R):
        for j in range(1,C):
            if(arr[i][j] == 0):
                arr[i][j] = min(arr[i-1][j],min(arr[i-1][j-1],arr[i][j-1])) + 1
                maxSize = arr[i][j] if maxSize < arr[i][j] else maxSize
            else:
                arr[i][j] = 0

    return maxSize

def maxSqareMatrixWithZeros(arr,R,C):
    maxSize = [0]
    dp = [[-1 for x in range(C)] for y in range(R)]
    ans = maxSqareMatrixWithZerosI(arr,R,C)
    return ans
    #maxSqareMatrixWithZerosR(arr,R,C,dp,maxSize)
    #return maxSize[0]

from sys import setrecursionlimit
setrecursionlimit(110000)
R, C = map(int, input().split())
arr = []
for i in range(R):
    val = [int(x) for x in input().split()]
    arr.append(val)

print(maxSqareMatrixWithZeros(arr,R,C))
