from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        numMap = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        def solve(letter, n, maxN, result):
            if n > maxN: # Need 1 more letter
                result.append(letter)
            else:
                for i in numMap[digits[n]]:
                    solve(letter+i, n+1, maxN, result)

        n = 0
        maxN = len(digits) - 1
        result = []

        if maxN >= 0:
            solve('', n, maxN, result)
        
        return result

# s = Solution()
# print(s.letterCombinations("67"))
