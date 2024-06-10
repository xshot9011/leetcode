# https://leetcode.com/problems/excel-sheet-column-number/

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        base = 26
        power = 0
        beforeA = 64
        summation = 0

        for i in range(len(columnTitle)-1, -1, -1):
            summation += (ord(columnTitle[i]) - beforeA)*(base**power)
            power += 1
        # Time: O(n)
        # Space: O(1)
        return summation
