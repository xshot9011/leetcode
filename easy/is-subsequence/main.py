# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sIndex = 0
        tIndex = 0
        sLen = len(s)
        tLen = len(t)

        while tIndex < tLen and sIndex < sLen:
            if s[sIndex] == t[tIndex]:
                sIndex += 1

            tIndex += 1

        # Time: O(max(t, s))
        # Space: O(1)
        return sIndex == len(s) # Last match get +1 == len(s)
