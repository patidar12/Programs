'''
Largest Bitonic Subarray
Send Feedback
You are given an array of positive integers as input. Write a code to return the length of the largest 
such subsequence in which the values are arranged first in strictly ascending order and then in strictly descending order.
Such a subsequence is known as bitonic subsequence. A purely increasing or purely decreasing subsequence will
also be considered as a bitonic sequence with the other part empty.
Note that the elements in bitonic subsequence need not be consecutive in the given array but the order should remain same.

Input Format:
Line 1 : A positive Integer N, i.e., the size of array
Line 2 : N space-separated integers as elements of the array 

Output Format:
Length of Largest Bitonic subsequence

Input Constraints:
1<= N <= 100000

Sample Input 1:
6
15 20 20 6 4 2

Sample Output 1:
5

Sample Output 1 Explanation:
Here, longest Bitonic subsequence is {15, 20, 6, 4, 2} which has length = 5.

Sample Input 2:
2
1 5

Sample Output 2:
2

Sample Input 3:
2
5 1

Sample Output 3:
2

'''

## Read input as specified in the question.
## Print output as specified in the question.

def longBit(arr,n):
    lis = [1]*n
    lds = [1]*n
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            if(arr[i] > arr[j] and lis[j]+1 > lis[i]):
                lis[i] = lis[j]+1
    for i in range(n-2,-1,-1):
        for j in range(i+1,n):
            if(arr[j] < arr[i] and lds[j] + 1 > lds[i]):
                lds[i] = lds[j] + 1
    best = 0
    for i in range(n):
        curr = lis[i]+lds[i]-1
        if(curr > best):
            best = curr
    return best

arr = [int(x) for x in input().split()]
n = arr[0]
print(longBit(arr[1:],n))
