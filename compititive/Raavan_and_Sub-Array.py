'''
Raavan gave a problem to his son, Indrajeet, and asked him to solve the problem to prove his intelligence and power. The Problem was like: Given 3 integers, N, K, and X, produce an array A of length N, in which the XOR of all elements of each contiguous sub-array, of length K, is exactly equal to X. Indrajeet found this problem very tricky and difficult, so, help him to solve this problem.

Note:
Ai must be an integer between 0 to 1018 (both inclusive), where Ai denotes the ith element of the array, A.
If there are multiple solutions, satisfying the problem condition(s), you can print any "one" solution.
Input:
First line will contain T, number of testcases. Then, the testcases follow.
Each testcase, contains a single line of input, of 3 integers, N, K, and X.
Output:
For each testcase, output in a single line, an array A of N integers, where each element of the array is between 0 to 1018 (both inclusive), satisfying the conditions of the problem, given by Raavan to his son.

Sample Input:
3
5 1 4
5 2 4
5 3 4
Sample Output:
4 4 4 4 4
3 7 3 7 3
11 6 9 11 6

'''
# cook your dish here
t = int(input())
for i in range(t):
    n,k,x = map(int,input().split())
    s = str(x)+" "+"0 "*(k-1)
    s = s*(n//k)
    if(n%k != 0):
        s = s+str(x)+" "+"0 "*(n%k-1)
    print(s)
