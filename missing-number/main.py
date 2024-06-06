# https://leetcode.com/problems/missing-number/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)+1):
            if i == len(nums):
                return i
            if nums[i] != i:
                return i
        return 0
