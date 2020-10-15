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
def validPoint(row, col, N, M):
    if(row >= 0 and col >= 0 and row < N and col < M):
        return True
    return False

def search(matrix, sr, sc, N, M, visited, pattern, pos):
    visited[sr][sc] = True
    if(len(pattern) == 0):
        return True
    for i in range(len(pos)):
        newX = sr + pos[i][0]
        newY = sc + pos[i][1]
        if(validPoint(newX,newY, N, M) and matrix[newX][newY] == pattern[0] and not visited[newX][newY]):
            if(search(matrix, newX, newY, N, M, visited, pattern[1:], pos)):
                return True
    visited[sr][sc] = False
    return False
        

def isPath(matrix, N, M, pattern):
    visited = [[False for i in range(M)] for j in range(N)]
    pos = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
    for i in range(N):
        for j in range(M):
            if(matrix[i][j] == pattern[0]):
                if(search(matrix, i, j, N, M, visited, pattern[1:], pos)):
                    return True
    return False
            
N, M = map(int, input().split())
matrix = [None]*N
for i in range(N):
    arr = [val for val in input()]
    matrix[i] = arr

pattern = "CODINGNINJA"
if(isPath(matrix, N, M, pattern)):
    print('1')
else:
    print('0')
