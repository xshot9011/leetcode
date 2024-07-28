# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        # 1001
        #  100
        #   10
        #    1 & 1 -> counter += 1
        startBit = 1
        counter = 0

        while n > 0:
            if n & 1 == 1:
                counter += 1
            n >>= 1

        return counter
