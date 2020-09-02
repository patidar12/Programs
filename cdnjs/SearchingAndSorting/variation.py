'''
Available on codechef : https://www.codechef.com/ZCOPRAC/problems/ZCO15002

Zonal Computing Olympiad 2015, 29 Nov 2014

We say that two integers x and y have a variation of at least K, if |x − y| ≥ K (the absolute value of their difference is at least K). Given a sequence of N integers a1,a2,...,aN and K, the total variation count is the number of pairs of elements in the sequence with variation at least K, i.e. it is the size of the set of pairs


{(i,j)|1≤i<j≤N and|ai−aj|≥K}


For example if K = 1 and the sequence is 3,2,4 the answer is 3. If K = 1 and the sequence is 3, 1, 3 then the answer is 2.


Your task is to write a program that takes a sequence and the value K as input and computes the total variation count.


Input format
The first line contains two positive integers N and K, separated by a space.


This is followed by a line containing N integers separated by space giving the values of the sequence.


Output format
A single integer in a single line giving the total variation count.


Test data
You may assume that all integers in the input are in the range 0 to 10^8 inclusive.


Subtask 1 (40 marks) : 1 ≤ N ≤ 4000, 1 ≤ K ≤ 10^8

Subtask 2 (60 marks) : 1 ≤ N ≤ 65000, 1 ≤ K ≤ 10^8


Sample Input
3 1 
3 1 3

Sample Output
2

'''
def merge(arr,first,mid,last):
    i = first
    j = mid
    k = 0
    temp = [0]*(last-first+1)
    while(i < mid and j <= last):
        if(arr[i] < arr[j]):
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1
    while(i < mid):
        temp[k] = arr[i]
        k += 1
        i += 1
    while(j <= last):
        temp[k] = arr[j]
        k += 1
        j += 1
    k = 0
    for i in range(first,last+1):
        arr[i] = temp[k]
        k += 1

def mergeSort(arr,first,last):
    if(first >= last):
        return
    mid = first + (last-first)//2
    mergeSort(arr,first,mid)
    mergeSort(arr,mid+1,last)
    merge(arr,first,mid+1,last)
    
'''
def binarySearch(arr,target,end):
    start = 0
    ans = -1
    while(start <= end):
        mid = start + (end-start)//2
        if(arr[mid][0] <= target):
            start = mid+1
        else:
            ans = mid
            end = mid-1
    return ans
'''

N,K = map(int,input().split())
arr = [int(x) for x in input().split()]
mergeSort(arr,0,N-1)
ans = 0
i = 0
j = 1
while(i < N and j < N):
    if(arr[j]-arr[i] >= K):
        ans += (N-j)
        i += 1
    else:
        j += 1
print(ans)
