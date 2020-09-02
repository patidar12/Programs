'''
Available on codeChef:
https://www.codechef.com/problems/AX06

Write a program to find a solution to a sudoku puzzle. The input will consist of puzzles with exactly one solution. Or in other words, the Sudoku solved must be a legitimate Sudoku!

Input
The input consists of one test case. Each test case will consist of nine lines with nine digits on each line. There will not be any blanks between the digits. The digits '1' through '9' will represent a number and the digit '0' will represent a blank square. The end of input is indicated by the end of the file.

Output
For each test case print, in the format shown below, the solved puzzle. There should be no spaces between digits and lines.

Example
Input:
023456789
406789123
780123456
234067891
567801234
891230567
345678012
678912305
912345670


Output:
123456789
456789123
789123456
234567891
567891234
891234567
345678912
678912345
912345678

'''
# Python

def findEmptyPosition(grid,emptyPosition,n):
    for i in range(n):
        for j in range(n):
            if(grid[i][j] == 0):
                emptyPosition[0] = i
                emptyPosition[1] = j
                return True
    return False

def isSafeInRow(grid,row,num,n):
    for i in range(n):
        if(grid[row][i] == num):
            return False
    return True

def isSafeInCol(grid,col,num,n):
    for i in range(n):
        if(grid[i][col] == num):
            return False
    return True

def isSafeInBoard(grid,row,col,num,n):
    rowFactor = row - (row%3)
    colFactor = col - (col%3)
    for i in range(3):
        for j in range(3):
            if(grid[i+rowFactor][j+colFactor] == num):
                return False
    return True

def isSafe(grid,row,col,i,n):
    if(isSafeInRow(grid,row,i,n) and isSafeInCol(grid,col,i,n)\
    and isSafeInBoard(grid,row,col,i,n)):
        return True
    return False

def solveSudoku(grid,n):
    '''
    emptyPosition is a list
    lenght = 2
    0 th position have row number
    1st position have column number
    '''
    emptyPosition = [-1]*2
    if(not findEmptyPosition(grid,emptyPosition,n)):
        return True
    row = emptyPosition[0]
    col = emptyPosition[1]
    for i in range(1,10):
        if(isSafe(grid,row,col,i,n)):
            grid[row][col] = i
            if(solveSudoku(grid,n)):
                return True
            grid[row][col] = 0
    return False

grid = [[int(x) for x in input().strip()] for i in range(9)]
solveSudoku(grid,9)
for i in range(9):
    for j in range(9):
        print(grid[i][j],end = '')
    print()

