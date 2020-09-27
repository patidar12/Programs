'''
Problem discussion
Send Feedback
Harshit gave Aahad an array of size N and asked to minimize the difference between the maximum value and minimum value by modifying the array under the
condition that each array element either increase or decrease by k(only once).
It seems difficult for Aahad so he asked for your help

Input Format
The First line contains two space-separated integers: N,K
Next lines contain N space-separated integers denoting elements of the array

Output Format
The output contains a single integer denoting the minimum difference between maximum value and the minimum value in the array

Constraints
1 =< N <= 10^5 
1 <= Ai,K <= 10^9

Sample Input1:
3 6
1 15 10

Sample Output1:
5

Explaination
We change from 1 to 6, 15 to  9 and 10 to 4. Maximum difference is 5 (between 4 and 9). We can't get a lower difference.

'''

def getMinimumDiff(arr,n,k):
    arr.sort()
    arr[0] = arr[0]+k
    arr[n-1] = arr[n-1] - k
    if arr[0] > arr[n-1] :
        arr[0],arr[n-1] = arr[n-1], arr[0]
    big = arr[n-1]
    small = arr[0]
    diff = big - small
    for i in range(1,n-1):
        sub = arr[i] - k
        add = arr[i] + k
        if sub >= small or add <= big :
            continue
        diff_sub = big - sub
        diff_add = add - small
        if diff_sub < diff_add :
            diff = diff_sub
            min = sub
        else :
            diff = diff_add
            max = add
    return diff

n,k = [int(x) for x in input().split()]
arr = [int(x) for x in input().split()]
print(getMinimumDiff(arr,n,k))
