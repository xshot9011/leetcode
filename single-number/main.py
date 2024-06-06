# https://leetcode.com/problems/single-number/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        foundNum = {}

        for num in nums: # O(n)
            if num not in foundNum: # O(1)
                foundNum[num] = 1
            else:
                del foundNum[num]
    
        for key, value in foundNum.items():
            return key
