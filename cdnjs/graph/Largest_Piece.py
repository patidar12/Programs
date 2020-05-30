'''
Largest Piece
Send Feedback
Its Gary's birthday today and he has ordered his favourite square cake consisting of '0's and '1's . But Gary wants the biggest piece of '1's and no '0's . A piece of cake is defined as a part which consist of only '1's, and all '1's share an edge with eachother on the cake. Given the size of cake N and the cake , can you find the size of the biggest piece of '1's for Gary ?
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

def search(arr,row,col,N,visited):
    visited[row][col] = True
    if(arr[row][col] == 0):
        return 0
    result = 1
    if(col-1 >= 0 and (not visited[row][col-1])):
        result += search(arr,row,col-1,N,visited)
    if(row-1 >= 0 and (not visited[row-1][col])):
        result += search(arr,row-1,col,N,visited)
    if(col+1 < N and (not visited[row][col+1])):
        result += search(arr,row,col+1,N,visited)
    if(row+1 < N and (not visited[row+1][col])):
        result += search(arr,row+1,col,N,visited)
    return result

def maxLength(arr,N):
    visited = [[False for i in range(N)] for j in range(N)]
    max = 0
    for i in range(N):
        for j in range(N):
            if(not visited[i][j]):
                result = search(arr,i,j,N,visited)
                if(max < result):
                    max = result
    return max


N = int(input())
arr = []
for i in range(N):
    li = [int(x) for x in input()]
    arr.append(li)
result = maxLength(arr,N)
print(result)

