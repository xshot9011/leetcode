# https://leetcode.com/problems/score-of-a-string/

class Solution:
    def scoreOfString(self, s: str) -> int:
        summation = 0

        for i in range(1, len(s)):
            summation += abs(ord(s[i])-ord(s[i-1]))
        
        return summation
