# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word = {}
        for i in range(len(t)):
            if t[i] in word:
                word[t[i]] += 1
            else:
                word[t[i]] = 1
        
        for i in range(len(s)):
            if s[i] in word:
                word[s[i]] -= 1
                if word[s[i]] == 0:
                    del word[s[i]]
            else:
                return False

        if word == {}:
            return True
        return False
