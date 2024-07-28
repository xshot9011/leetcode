# https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        isCarry = False
        maxLenght = max(len(num1), len(num2))
        ans = ""
        pointer = 0
        numBase = ord('0')
        
        while pointer < maxLenght or isCarry:
            aIndex = len(num1) - pointer - 1
            bIndex = len(num2) - pointer - 1
            a = 0
            b = 0
            if aIndex >= 0 and aIndex < len(num1):
                a = ord(num1[aIndex]) - numBase
            if bIndex >= 0 and bIndex < len(num2):
                b = ord(num2[bIndex]) - numBase
            summation = a + b 
            if isCarry:
                summation += 1
                isCarry = False
            if summation // 10 == 1:
                isCarry = True
            
            ans = chr((summation%10) + numBase) + ans
            pointer += 1

        # Time: O(maxLength)
        # Space: O(1)
        return ans
