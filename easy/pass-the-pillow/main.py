# https://leetcode.com/problems/pass-the-pillow/description

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        # 1 2 3 4 |
        #   1 2 3  (n-1) * 2 = origin
        # 6 5 4      origin % time = position
        
        #   1 2 3 position < n
        # 6 5 4   position >= 1
        fullRound = (n-1) * 2
        position = time % fullRound

        if position < n:
            return position + 1
        return (2 * n) - position - 1
        