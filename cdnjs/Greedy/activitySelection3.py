'''

Activity Selection

You are given n activities with their start and finish times. Select the maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.

Input
The first line of input contains one integer denoting N.
Next N lines contains two space separated integers denoting the start time and finish time for the ith activity.

Output
Output one integer, the maximum number of activities that can be performed

Constraints
1 ≤ N ≤ 10^6
1 ≤ ai, di ≤ 10^9

Sample Input
6
1 2
3 4
0 6
5 7
8 9
5 9

Sample Output
4

'''

## Read input as specified in the question.
## Print output as specified in the question.
def getMaxActivity(arr,n):

    arr.sort(key = lambda x: x[1])
    act_count = 1
    prev_act = 0
    for i in range(1,n):
        if(arr[i][0] >= arr[prev_act][1]):
            act_count += 1
            prev_act = i
    return act_count

n = int(input())
arr = [None]*n
for i in range(0,n):
    first,second = map(int,input().split())
    arr[i] = (first, second)
print(getMaxActivity(arr,n))
