'''
leetcode:
    https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/559/week-1-october-1st-october-7th/3481/

Combination Sum

Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates 
where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3],[7]]

Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8

Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:

Input: candidates = [2], target = 1
Output: []

Example 4:

Input: candidates = [1], target = 1
Output: [[1]]

Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]
 

Constraints:

1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500


'''
# All solution are accepted
class Solution:
    '''
    @staticmethod
    def storeComb(arr, start, target, sum, curr, result):
        if(sum > target):
            return
        if(target == sum):
            temp = [x for x in curr]
            result.append(temp)
            return
        for i in range(start, len(arr)):
            curr.append(arr[i])
            Solution.storeComb(arr, i, target, sum + arr[i], curr, result)
            curr.pop(-1)

    '''
    '''
    @staticmethod
    def storeComb(arr, target, n, curr, result):
        if(target == 0):
            temp = [x for x in curr]
            result.append(temp)
            return
        if(n <= 0):
            return
        if(arr[0] > target):
            Solution.storeComb(arr[1:], target, n-1, curr, result)
            return
        Solution.storeComb(arr[1:], target, n-1, curr, result)
        curr.append(arr[0])
        Solution.storeComb(arr, target - arr[0], n, curr, result)
        curr.pop(-1)
    '''
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        result = []
        curr = []
        n = len(candidates)
        #Solution.storeComb(candidates, 0, target, 0, curr, result)
        Solution.storeComb(candidates, target, n, curr, result)
        return result
        '''
        dp = [[] for _ in range(target+1)]
        dp[0].append([])
        for cand in candidates:
            for j in range(cand,target+1):
                for item in dp[j-cand]:
                    dp[j].append(item+[cand])
        return dp[target]

