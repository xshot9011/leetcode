# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def getNumber(nums: List[int]) -> List[int]:
            """
            Args:
                nums List[int]: List of number that used to generated

            Returns:
                List[int]: New generated list
            """
            newList = []
            if len(nums) == 0:
                return [1]
            if len(nums) == 1:
                return [1, 1]
            x = 0
            y = 1
            for i in range(1, len(nums)):
                newList.append(nums[x]+nums[y])
                x += 1
                y += 1
            return [1] + newList + [1]
        
        ans = [[1]]
        for i in range(1, numRows):
            newList = getNumber(ans[i-1])
            ans.append(newList)
        
        return ans
