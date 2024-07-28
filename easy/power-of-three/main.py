# https://leetcode.com/problems/power-of-three/

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        # return math.log(n, 3).is_integer() -> The same n (odd) -> .9999x
        if n <= 0:
            return False

        while n > 1:
            n /= 3
        
        # Time: O(log3(n))
        # Space: O(1)
        return n%3 == 1
