# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        # Time: O(nlog(n))
        # Space: O(1)
        return nums[(len(nums)//2)]
