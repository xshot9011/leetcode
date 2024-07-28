# https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        nowNum = n
        foundNum = {}
        while True:
            summation = 0
            for i in str(nowNum):
                summation += int(i)**2
            print(f'summation: {summation}')
            if summation == 1:
                return True
            if summation in foundNum:
                return False
            foundNum[summation] = 1
            nowNum = summation
