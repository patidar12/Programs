'''
Largest Piece

Its Gary's birthday today and he has ordered his favourite square cake consisting of '0's and '1's . 
But Gary wants the biggest piece of '1's and no '0's . A piece of cake is defined as a part which consist of only '1's,
and all '1's share an edge with eachother on the cake. Given the size of cake N and the cake , can you find the size of the biggest piece of '1's for Gary ?

Constraints :
1<=N<=50

Input Format :
Line 1 : An integer N denoting the size of cake 
Next N lines : N characters denoting the cake

Output Format :
Size of the biggest piece of '1's and no '0's

Sample Input :
2
11
01

Sample Output :
3

'''

## Read input as specified in the question.
## Print output as specified in the question.
## Read input as specified in the question.
## Print output as specified in the question.

def validPoint(x, y, N):
    if(x >= 0 and y >= 0 and x < N and y < N):
        return True
    return False

def search(arr,row,col,N,visited,pos):
    visited[row][col] = True
    if(arr[row][col] == 0):
        return 0
    result = 1
    for i in range(len(pos)):
        newX = row + pos[i][0]
        newY = col + pos[i][1]
        if(validPoint(newX,newY,N) and not visited[newX][newY]):
            result += search(arr,newX,newY,N,visited,pos)
    return result

def maxLength(arr,N):
    visited = [[False for i in range(N)] for j in range(N)]
    ans = 0
    pos = [[1,0],[0,1],[-1,0],[0,-1]]
    for i in range(N):
        for j in range(N):
            if(not visited[i][j]):
                result = search(arr,i,j,N,visited,pos)
                ans = max(ans,result)
    return ans

N = int(input())
arr = []
for i in range(N):
    li = [int(x) for x in input()]
    arr.append(li)
result = maxLength(arr,N)
print(result)

