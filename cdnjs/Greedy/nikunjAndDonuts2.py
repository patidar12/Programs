'''
Nikunj and Donuts

Nikunj loves donuts, but he also likes to stay fit. He eats n donuts in one sitting, and each donut has a calorie count, ci.
After eating a donut with k calories, he must walk at least 2^j x k(where j is the number donuts he has already eaten) miles to maintain his weight.
Given the individual calorie counts for each of the n donuts, find and print a long integer denoting the minimum number of miles Nikunj must walk to maintain his weight.
Note that he can eat the donuts in any order.

Input

The first line contains an integer, n, denoting the number of donuts. 
The second line contains n space-separated integers describing the respective calorie counts of each donut I, i.e ci.

Output

Print a long integer denoting the minimum number of miles Nikunj must walk to maintain his weight.

Constraints
1 ≤ n ≤ 40
1 ≤ ci ≤ 1000

Sample Input
3
1 3 2

Sample Output
11

'''

## Read input as specified in the question.
## Print output as specified in the question.
def storePow(power):
    power[0] = 1
    for i in range(1,40):
        #power[i] = (power[i-1]*2)
        power[i] = power[i-1] << 1
def quickSort(arr,start,end):
    if(start < end):
        pi = partition(arr,start,end)
        quickSort(arr,start,pi-1)
        quickSort(arr, pi+1,end)

def partition(arr, start,end):
    p = arr[end]
    k = start-1
    for i in range(start,end):
        if(arr[i] > p):
            k += 1
            arr[k],arr[i] = arr[i], arr[k]
    arr[k+1],arr[end] = p,arr[k+1]
    return k+1

def getMinMiles(arr,n):
    power = [0]*40
    storePow(power)
    #arr.sort(reverse = True)
    quickSort(arr,0,n-1)
    min_miles = 0
    for i in range(0,n):
        min_miles += (power[i]*arr[i])
    return min_miles

n = int(input())
arr  = [int(x) for x in input().split()]
print(getMinMiles(arr,n))
