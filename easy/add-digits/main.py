# https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        ans = 0
        while True:
            while num > 0:
                ans += num%10
                num //= 10
            if ans >= 10:
                num = ans
                ans = 0
            else:
                return ans
