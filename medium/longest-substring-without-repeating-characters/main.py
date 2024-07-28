# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# To be honest, this one too complicate
# TODO optimize it later

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cached = {}
        ans = 0
        ignoreBefore = 0
        counter = 0

        for index, char in enumerate(s):
            if char in cached:
                if ignoreBefore <= cached[char]:
                    if index - cached[char] == 1:
                        cached = {}
                        ans = max(ans, counter)
                        counter = 1
                    else:
                        ignoreBefore = cached[char]
                        ans = max(ans, counter, cached[char] - index)
                        counter = index - cached[char]
                else:
                    counter += 1
            else:
                counter += 1
            cached[char] = index

        return max(ans, counter)
