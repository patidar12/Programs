'''
Connected horses

You all must be familiar with the chess-board having 8*8 squares of alternate black and white cells.
Well, here we have for you a similar N*M size board with similar arrangement of black and white cells.

A few of these cells have Horses placed over them. Each horse is unique. Now these horses are not the 
usual horses which could jump to any of the 8 positions they usually jump in. They can move only if there is another horse on one of the 8-positions that it can  
go to usually and then both the horses will swap their positions. This swapping can happen infinitely times.
A photographer was assigned to take a picture of all the different ways that the horses occupy the board! Given the state of the board, calculate answer.

Sincethis answer may be quite large, calculate in modulo 10^9+7

Input:
First line contains 
T which is the number of test cases.
T test cases follow first line of each containing three integers 
N, M and Q where 
N,M is the size of the board and 
Q is the number of horses on it.
Q lines follow each containing the 2 integers 
X and Y which are the coordinates of the Horses.

Output:
For each test case, output the number of photographs taken by photographer.

Constraints:
 1<=T<=10
 1<=N,M<=1000
 1<=Q<=N*M

SAMPLE INPUT
2
4 4 4
1 1
1 2
3 1
3 2
4 4 4
1 1
1 2
3 1
4 4

SAMPLE OUTPUT
4
2

'''

## Read input as specified in the question.
## Print output as specified in the question.
def factorial(fact, n):
    fact[0] = 1
    mod = 1000000007
    for i in range(1,n):
        fact[i] = (fact[i-1] * i)%mod

def validPoint(x, y, N, M):
    if(x >= 0 and y >= 0 and x < N and y < M):
        return True
    return False

def dfs(board, dx, dy, N, M, visited, pos):
    visited[dx][dy] = True
    sum = 1
    for i in range(8):
        newX = dx + pos[i][0]
        newY = dy + pos[i][1]
        if(validPoint(newX,newY,N,M) and board[newX][newY] and not visited[newX][newY]):
            sum += dfs(board, newX, newY, N, M, visited, pos)
    return sum

from sys import setrecursionlimit
setrecursionlimit(110000)
tcs = int(input())
fact = [0]*100006
factorial(fact, 100006)
pos = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [1,-2], [-1,2], [-1,-2]]
mod = 1000000007
for tc in range(tcs):
    N, M, Q = map(int, input().split())
    board = [[False for i in range(M)] for _ in range(N)]
    for i in range(Q):
        x,y=map(int,input().split())
        board[x-1][y-1] = True
    visited = [[False for i in range(M)] for _ in range(N)]
    photos = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] and not visited[i][j]:
                curr = dfs(board, i, j, N, M, visited, pos)
                photos = (photos*fact[curr])%mod
    print(photos)
