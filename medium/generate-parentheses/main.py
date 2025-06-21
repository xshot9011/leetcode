from typing import List

# icp = is correct parenthesis = true if () false ((
# if n = 1 and char = ) : false
# if open > n or close > n : false 
# if clsoe > open : fasle

# loop n time -> recursion
# n = 1
# (
# ) - 

# max round = n * 2
# n = 1
# (
    # n = 2
    # (
        # n = 3
        # ( icp = false
        # )
            # n = 4
            # (.      (()( icp = false
            # ).      (()) /
    # )
        # n = 3
        # (
            # n = 4
            # (.      ()(( icp = false
            # ).      ()() /
        # ) icp = false
# ) -

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def isValidPair(open, close, maxN):
            if open > maxN/2 or close > maxN/2:
                return False
            elif close > open:
                return False
            return True

        def solve(char, open, close, n, maxN, result):
            if n == maxN:
                result.append(char)
            else:
                if isValidPair(open+1, close, maxN):
                    solve(char+'(', open+1, close, n+1, maxN, result)
                if isValidPair(open, close+1, maxN):
                    solve(char+')', open, close+1, n+1, maxN, result)

        result = []
        solve('(', 1, 0, 1, n*2, result)
        
        return result

s = Solution()
print(s.generateParenthesis(3))
