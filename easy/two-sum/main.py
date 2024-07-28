# https://leetcode.com/problems/two-sum/description/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(list(enumerate(nums)), key=lambda x: x[1])
        array_size = len(nums)
        first_pointer = 0
        last_pointer = len(nums)-1
        NUMBER_INDEX = 1
        INDEX = 0
        for i in range(0, array_size, 1):
            summation = nums[first_pointer][NUMBER_INDEX] + nums[last_pointer][NUMBER_INDEX]
            if summation == target:
                return [nums[first_pointer][INDEX], nums[last_pointer][INDEX]]
            elif summation > target:
                last_pointer -= 1
            else:
                first_pointer += 1
