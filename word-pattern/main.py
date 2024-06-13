# https://leetcode.com/problems/word-pattern/

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapToWord = {}
        mapVerified = {}
        s = s.split()
        if len(s) != len(pattern):
            return False

        for index, word in enumerate(s):
            if pattern[index] in mapToWord:
                if mapToWord[pattern[index]] != word:
                    return False
            elif word in mapVerified:
                if mapVerified[word] != pattern[index]:
                    return False
            else:
                mapToWord[pattern[index]] = word
                mapVerified[word] = pattern[index]

        return True
