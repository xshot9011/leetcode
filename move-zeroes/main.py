# https://leetcode.com/problems/move-zeroes/
# I saw other use more simple method, this one is too complex hahah

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pointerA = 0
        pointerB = 1
        
        # [0. 1.. 1 0 1 1 1 0 1] found zero
        # [1. 0.. 1 0 1 1 1 0 1] swap zero check non zero
        # [1 0. 1.. 0 1 1 1 0 1] inc
        # [1 1. 0.. 0 1 1 1 0 1] no found zero, inc
        # [1 1 0. 0.. 1 1 1 0 1] swap zero check non zero
        # [1 1 0. 0 1.. 1 1 0 1] inc
        # [1 1 1. 0 0.. 1 1 0 1] no found zero, inc
        # [1 1 1 0. 0 1.. 1 0 1] swap zero check non zero
        # [1 1 1 1. 0 0.. 1 0 1] ...
        # [1 1 1 1 0. 0 1.. 0 1] ...
        # [1 1 1 1 1. 0 0.. 0 1] ...
        # [1 1 1 1 1 0. 0 0.. 1]
        # [1 1 1 1 1 0. 0 0 1..]
        # [1 1 1 1 1 1. 0 0 0..]
        
        for i in range(len(nums)-1):
            if nums[pointerA] == 0:
                while nums[pointerB] == 0 and pointerB < len(nums) - 1:
                    pointerB += 1
                nums[pointerA] = nums[pointerB]
                nums[pointerB] = 0
            if pointerB >= len(nums) - 1:
                break

            pointerA += 1
            pointerB += 1
