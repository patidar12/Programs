'''
Fractional Knapsack

You want to paint your house. The total area of your house is D units. There are a total of N workers. The ith worker is available after time Ti,
has hiring cost Xi and speed Yi. This means he becomes available for hiring from time Ti and remains available after that. Once available,
you can hire him with cost Xi, after which he will start painting the house immediately, covering exactly Yi units of house with paint per time unit.
You may or may not hire a worker and can also hire or fire him at any later point of time. However, no more than 1 worker can be painting the house at a given time.
Since you want the work to be done as fast as possible, figure out a way to hire the workers, such that your house gets painted at the earliest possible time,
with minimum cost to spend for hiring workers.

Note: You can hire a previously hired worker without paying him again.

Input
The first line of input contains two integers "N D", the number of workers and the area of your house respectively. The ith of the next N lines denotes the ith worker, and contains three integers "Ti Xi Yi", described in the statement.

Output
Output one integer, the minimum cost that you can spend in order to get your house painted at the earliest.

Constraints
1 ≤ N, T, X, Y ≤ 10^5
1 ≤ D ≤ 10^11

Sample Input
3 3
1 1 1
2 2 2
3 1 5

Sample Output
3

'''
## Read input as specified in the question.
## Print output as specified in the question.
from functools import cmp_to_key

def compare(tup1, tup2):
    if(tup1[0] != tup2[0]):
        return tup1[0] < tup2[0]
    if(tup1[2] != tup2[2]):
        return tup1[2] > tup2[2]
    return tup1[1] < tup2[1]

def merge(arr,start,mid,end):
    i = start
    j = mid
    k = 0
    temp = [0]*(end-start+1)
    while(i < mid and j <= end):
        if(compare(arr[i], arr[j])):
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

def getMinimumCost(arr,n,d):
    #maxn = 1000005
    #arr.sort(key = lambda x:x[0]*maxn*maxn - x[2]*maxn + x[1])
    mergeSort(arr,0,n-1)
    area = 0
    bestSpeed = 0
    cost = 0
    lastTime = arr[0][0]
    for i in range(n):
        additional = bestSpeed*(arr[i][0] - lastTime)
        area += additional
        if(area >= d):
            break
        if(arr[i][2] > bestSpeed):
            bestSpeed = arr[i][2]
            cost += arr[i][1]
        lastTime = arr[i][0]
    return cost

n,d = [int(x) for x in input().split()]
arr = [0]*n
for i in range(0,n):
    ti,hc,sp = [int(x) for x in input().split()]
    arr[i] = (ti,hc,sp)

print(getMinimumCost(arr,n,d))

