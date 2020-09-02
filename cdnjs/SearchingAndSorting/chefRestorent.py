'''
Available on codchef

Chef is a cook and he has recently opened a restaurant.

The restaurant is open during N time intervals [L1,R1),[L2,R2),…,[LN,RN). No two of these intervals overlap — formally, for each valid i, j such that i≠j, either Ri<Lj or Rj<Li.

M people (numbered 1 through M) are planning to eat at the restaurant; let's denote the time when the i-th person arrives by Pi. If the restaurant is open at that time, this person does not have to wait, but if it is closed, this person will wait until it is open. Note that if this person arrives at an exact time when the restaurant is closing, they have to wait for the next opening time.

For each person, calculate how long they have to wait (possibly 0 time), or determine that they will wait forever for the restaurant to open.

Input
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first line of the input contains two space-separated integers N and M.
N lines follow. For each valid i, the i-th of these lines contains two space-separated integers Li and Ri.
M lines follow. For each valid i, the i-th of these lines contains a single integer Pi.
Output
For each test case, print M lines. For each valid i, the i-th of these lines should contain a single integer — the time person i has to wait, or −1 if person i has to wait forever.

Constraints
1≤T≤100
1≤N,M≤105
1≤Li<Ri≤109 for each valid i
1≤Pi≤109 for each valid i
the intervals are pairwise disjoint
the sum of N for all test cases does not exceed 3⋅105
the sum of M for all test cases does not exceed 3⋅105
Subtasks
Subtask #1 (30 points):

the sum of N for all test cases does not exceed 1,000
the sum of M for all test cases does not exceed 1,000
Subtask #2 (70 points): original constraints

Example Input
1
4 5
5 7
9 10
2 3
20 30
5
6
7
35
1
Example Output
0
0
2
-1
1

'''
def merge(arr,first,mid,last):
    i = first
    j = mid
    k = 0
    temp = [None]*(last-first+1)
    while(i < mid and j <= last):
        if(arr[i][0] < arr[j][0]):
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

def binarySearch(arr,target,end):
    start = 0
    ans = end+1
    while(start <= end):
        mid = start + (end-start)//2
        if(arr[mid][0] < target):
            start = mid+1
        else:
            ans = mid
            end = mid-1
    return ans

tcs = int(input())
for tc in range(tcs):
    N,M = map(int,input().split())
    arr = []
    for i in range(N):
        sTime,eTime = map(int,input().split())
        arr.append((sTime,eTime))
    mergeSort(arr,0,N-1)
    for i in range(M):
        pi = int(input())
        index = binarySearch(arr,pi,N-1)
        ans = -1
        if(index == 0):
            ans = arr[index][0] - pi
        else:
            if((arr[index-1][1] > pi)):
                ans = 0
            elif(index < N):
                ans = arr[index][0] - pi

        print(ans)
