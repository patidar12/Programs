'''
The Longest Increasing Subsequence (LIS) problem is to find the length of 
the longest subsequence of a given sequence such that all elements of the subsequence
are sorted in increasing order. For example, the length of LIS for
{10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
Input: arr[] = {3, 10, 2, 1, 20}
Output: Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input: arr[] = {3, 2}
Output: Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input: arr[] = {50, 3, 10, 7, 40, 80}
Output: Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}

'''

# Python

#code
def lis(arr,n):
    output = [1]*n
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if(arr[i] >= arr[j] and output[j]+1 > output[i]):
                output[i] = output[j]+1
    tlen = 0
    for i in range(n):
        if(tlen < output[i]):
            tlen = output[i]
    return tlen

n = int(input())
arr = [int(x) for x in input().split()]
ans = lis(arr,n)
print(ans)
