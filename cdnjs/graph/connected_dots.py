'''
Connecting Dots
Send Feedback
Gary has a board of size NxM. Each cell in the board is a coloured dot. There exist only 26 colours denoted by uppercase Latin characters (i.e. A,B,...,Z). Now Gary is getting bore and wants to play a game. The key of this game is to find a cycle that contain dots of same colour. Formally, we call a sequence of dots d1, d2, ..., dk a cycle if and only if it meets the following condition:
1. These k dots are different: if i ≠ j then di is different from dj.
2. k is at least 4.
3. All dots belong to the same colour.
4. For all 1 ≤ i ≤ k - 1: di and di + 1 are adjacent. Also, dk and d1 should also be adjacent. Cells x and y are called adjacent if they share an edge.
Since Gary is colour blind, he wants your help. Your task is to determine if there exists a cycle on the board.
Assume input to be 0-indexed based.
Input Format :
Line 1 : Two integers N and M, the number of rows and columns of the board
Next N lines : a string consisting of M characters, expressing colors of dots in each line. Each character is an uppercase Latin letter.
Output Format :
Return 1 if there is a cycle else return 0
Constraints :
2 ≤ N, M ≤ 50
Sample Input :
3 4
AAAA
ABCA
AAAA
Sample Output :
1

'''

def search(arr,src_row,src_col,row,col,N,M,visited,length):
    visited[row][col] = True
    if(src_row == row and src_col == col-1 and length >= 4):
        return True
    if(col-1 >= 0 and (not visited[row][col-1]) and arr[row][col-1] == arr[src_row][src_col]):
        if(search(arr,src_row,src_col,row,col-1,N,M,visited,length+1)):
            return True
    if(row-1 >= 0 and (not visited[row-1][col]) and arr[row-1][col] == arr[src_row][src_col]):
        if(search(arr,src_row,src_col,row-1,col,N,M,visited,length+1)):
            return True
    if(col+1 < M and (not visited[row][col+1]) and arr[row][col+1] == arr[src_row][src_col]):
        if(search(arr,src_row,src_col,row,col+1,N,M,visited,length+1)):
            return True
    if(row+1 < N and (not visited[row+1][col]) and arr[row+1][col] == arr[src_row][src_col]):
        if(search(arr,src_row,src_col,row+1,col,N,M,visited,length+1)):
            return True
    visited[row][col] = False
    return False

def maxLength(arr,N,M):
    visited = [[False for i in range(M)] for j in range(N)]
    for i in range(N):
        for j in range(M):
            if(not visited[i][j]):
                if(search(arr,i,j,i,j,N,M,visited,1)):
                    return 1
    return 0

N,M = map(int,input().split())
arr = []
for i in range(N):
    arr.append([x for x in input()])

result = maxLength(arr,N,M)
print(result)
