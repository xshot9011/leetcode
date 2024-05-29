class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = {}
        for i in range(len(nums)):
            if nums[i] in found:
                if abs(i - found[nums[i]]) <= k:
                    return True
            found[nums[i]] = i

        return False
