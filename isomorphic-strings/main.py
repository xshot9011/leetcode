# https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stMap = {} # {'original': 'replace_to'}
        tsMap = {} # {'replaced_to': 'original'}
        
        for i in range(len(s)):
            if s[i] in stMap:
                if stMap[s[i]] != t[i]:
                    return False
            elif t[i] in tsMap:
                if tsMap[t[i]] != s[i]:
                    return False
            else:
                stMap[s[i]] = t[i]
                tsMap[t[i]] = s[i]

        # Time: O(n)
        # Space: O(2n)
        return True 
