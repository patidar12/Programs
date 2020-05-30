'''
Coding Ninjas
Send Feedback
Given a NxM matrix containing Uppercase English Alphabets only. Your task is to tell if there is a path in the given matrix which makes the sentence “CODINGNINJA” .
There is a path from any cell to all its neighbouring cells. A neighbour may share an edge or a corner.
Input Format :
Line 1 : Two space separated integers N  and M, where N is number of rows and M is number of columns in the matrix.
Next N lines : N rows of the matrix. First line of these N line will contain 0th row of matrix, second line will contain 1st row and so on
Assume input to be 0-indexed based
Output Format :
Return 1 if there is a path which makes the sentence “CODINGNINJA” else return 0.
Constraints :
1 <= N <= 100
1 <= M <= 100
Sample Input :
2 11
CXDXNXNXNXA
XOXIXGXIXJX
Sample Output :
1

'''

def search(arr,row,col,N,M,pattern,visited,index,p_size):
    visited[row][col] = True
    if(index == p_size-1):
        return True
    index += 1
    if(col-1 >= 0 and arr[row][col-1] == pattern[index] and (not visited[row][col-1])):
        if(search(arr,row,col-1,N,M,pattern,visited,index,p_size)):
            return True
    if(col-1 >= 0 and row-1 >= 0 and arr[row-1][col-1] == pattern[index] and (not visited[row-1][col-1])):
        if(search(arr,row-1,col-1,N,M,pattern,visited,index,p_size)):
            return True
    if(row-1 >= 0 and arr[row-1][col] == pattern[index] and (not visited[row-1][col])):
        if(search(arr,row-1,col,N,M,pattern,visited,index,p_size)):
            return True
    if(row-1 >= 0 and col+1 < M and arr[row-1][col+1] == pattern[index] and (not visited[row-1][col+1])):
        if(search(arr,row-1,col+1,N,M,pattern,visited,index,p_size)):
            return True
    if(col+1 < M and arr[row][col+1] == pattern[index] and (not visited[row][col+1])):
        if(search(arr,row,col+1,N,M,pattern,visited,index,p_size)):
            return True
    if(col+1 < M and row+1 < N and arr[row+1][col+1] == pattern[index] and (not visited[row+1][col+1])):
        if(search(arr,row+1,col+1,N,M,pattern,visited,index,p_size)):
            return True
    if(row+1 < N and arr[row+1][col] == pattern[index] and (not visited[row+1][col])):
        if(search(arr,row+1,col,N,M,pattern,visited,index,p_size)):
            return True
    if(col-1 >= 0 and row+1 < N and arr[row+1][col-1] == pattern[index] and (not visited[row+1][col-1])):
        if(search(arr,row+1,col-1,N,M,pattern,visited,index,p_size)):
            return True
    visited[row][col] = False
    return False

def isFound(arr,N,M,pattern):
    visited = [[False for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if(arr[i][j] == pattern[0]):
                if(search(arr,i,j,N,M,pattern,visited,0,11)):
                    return True

    return False
N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append([x for x in input()])

pattern = 'CODINGNINJA'
result = isFound(arr,N,M,pattern)
if(result):
    print(1)
else:
    print(0)
