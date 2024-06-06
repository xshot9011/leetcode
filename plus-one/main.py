# https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        cursor = len(digits)-1
        digits[cursor] += 1
        while cursor >= 0:
            if digits[cursor] >= 10:
                digits[cursor] = 0
                if cursor-1 < 0:
                    digits.insert(0, 1)
                else:
                    digits[cursor-1] += 1

            cursor -= 1

        return digits
