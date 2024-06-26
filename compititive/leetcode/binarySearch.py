'''
leetcode:
    https://leetcode.com/explore/challenge/card/october-leetcoding-challenge/560/week-2-october-8th-october-14th/3488/


Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums.
If target exists, then return its index, otherwise return -1.

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4

Explanation: 9 exists in nums and its index is 4

Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1

Explanation: 2 does not exist in nums so return -1
 

Note:

You may assume that all elements in nums are unique.
n will be in the range [1, 10000].
The value of each element in nums will be in the range [-9999, 9999]

'''

class Solution:
    @staticmethod
    def binarySearch(arr,start,end,target):
        if(start > end):
            return -1

        mid = start + ((end - start) >> 1)
        if(arr[mid] == target):
            return mid
        if(arr[mid] > target):
            return Solution.binarySearch(arr,start,mid-1,target)

        return Solution.binarySearch(arr,mid+1,end,target)


    def search(self, nums: List[int], target: int) -> int:
        return Solution.binarySearch(nums,0,len(nums)-1,target)
