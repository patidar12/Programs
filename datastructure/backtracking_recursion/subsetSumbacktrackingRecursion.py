'''
GFG: Practice(Backtracking)
    https://www.geeksforgeeks.org/subset-sum-backtracking-4/

Given a set of numbers, check whether it can be partitioned into two subsets such that the sum of elements in both subsets is same or not.

Input:
The first line contains an integer 'T' denoting the total number of test cases. Each test case constitutes of two lines. First line contains 'N', representing the number of elements in the set and the second line contains the elements of the set.

Output:
Print YES if the given set can be partioned into two subsets such that the sum of elements in both subsets is equal, else print NO.

Constraints:
1 <= T <= 100
1 <= N <= 100
0 <= arr[i] <= 1000

Example:
Input:
2
4
1 5 11 5
3
1 3 5

Output:
YES
NO

Explanation:
Testcase 1: There exists two subsets such that {1, 5, 5} and {11}.

#pytohn

for _ in range(int(input().strip())):
    n = int(input().strip())
    nums = [ int(num) for num in input().split() if num ]
    s = sum(nums)
    if(s%2): print('NO')
    else:
        s //= 2
        @lru_cache(maxsize=1000001)
        def do(s, i):
            if(s == 0): return True
            elif(s < 0): return False
            flag = False
            for j in range(i, n):
                flag = flag or do(s-nums[j], j+1)
            return flag
        if(do(s, 0)):print('YES')
        else: print('NO')

'''
# Python

def subsetSum(arr,tsum,n):
    if(tsum == 0):
        return True
    if(n == 0):
        return False
    if(arr[n-1] > tsum):
        return subsetSum(arr,tsum,n-1)
    return subsetSum(arr,tsum-arr[n-1],n-1) or subsetSum(arr,tsum,n-1)

def isPartitioned(arr,n):
    tSum = sum(arr)
    if(tSum%2 != 0):
        return False
    k = tSum//2
    return subsetSum(arr,k,n)


tcs = int(input())
for tc in range(tcs):
    n = int(input())
    arr = [int(x) for x in input().split()]
    if(isPartitioned(arr,n)):
        print("YES")
    else:
        print("NO")

