# https://leetcode.com/problems/slowest-key/

class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0] + releaseTimes
        keysPressed = '0' + keysPressed
        maxTime = 0
        maxKey = chr(0)

        for i in range(1, len(releaseTimes)):
            releaseTime = releaseTimes[i] - releaseTimes[i-1]
            if releaseTime >= maxTime:
                if releaseTime == maxTime:
                    maxKey = chr(max(ord(keysPressed[i]), ord(maxKey)))
                else:
                    maxKey = keysPressed[i]
                maxTime = releaseTime
        # Time: O(n)
        # Space: O(1)
        return maxKey
