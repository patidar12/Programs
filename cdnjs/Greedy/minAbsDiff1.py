'''
Min. Absolute Difference In Array

Given an integer array A of size N, find and return the minimum absolute difference between any two elements in the array.
We define the absolute difference between two elements ai, and aj (where i != j ) is |ai - aj|.

Input format :

Line 1 : Integer N, Array Size
Line 2 : Array elements (separated by space)

Output Format :

Minimum difference

Constraints :
1 <= N <= 10^6

Sample Input :
5
2 9 0 4 5

Sample Input :
1


'''

## Read input as specified in the question.
## Print output as specified in the question.
def merge(arr,start,mid,end):
    i = start
    j = mid
    k = 0
    temp = [0]*(end-start+1)
    while(i < mid and j <= end):
        if(arr[i] < arr[j]):
            temp[k] = arr[i]
            i += 1
            k += 1
        else:
            temp[k] = arr[j]
            j += 1
            k += 1
    while(i < mid):
        temp[k] = arr[i]
        k += 1
        i += 1
    while(j <= end):
        temp[k] = arr[j]
        k += 1
        j += 1
    k = 0
    for i in range(start,end+1):
        arr[i] = temp[k]
        k += 1


def mergeSort(arr, start, end):
    if(start < end):
        mid = start + (end - start)//2
        mergeSort(arr,start,mid)
        mergeSort(arr,mid+1,end)
        merge(arr,start,mid+1,end)

def getMinDiff(arr,n):
    min = float('inf')
    #arr.sort()
    mergeSort(arr,0,n-1)
    for i in range(1,len(arr)):
        diff = abs(arr[i]-arr[i-1])
        if diff < min :
            min = diff
    if min == float('inf'):
        min = -arr[0]
    return min
n = int(input())
arr = [int(x) for x in input().split()]
print(getMinDiff(arr,n))

