class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold = -(-len(nums) // 2)
        nums.sort()
        # Time: O(nlog(n))
        # Space: O(1)
        return nums[threshold]
