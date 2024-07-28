# https://leetcode.com/problems/find-the-maximum-achievable-number/description/
# The description is hard to understand, while reading in discussion is much more easier to understand this.

class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + (2 * t)
