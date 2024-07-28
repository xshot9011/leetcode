# https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = len(s)//2
        pointerEnd = len(s) - 1
        for i in range(count):
            temp = s[i]
            s[i] = s[pointerEnd - i]
            s[pointerEnd - i] = temp

        # Time: O(n//2)
        # Space: O(1)
