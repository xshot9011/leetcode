class Solution:
    def reverse(self, x: int) -> int:
        res = 0
        if x < 0:
            res = int(str(x)[1:][::-1]) * -1
        else:
            res = int(str(x)[::-1])

        preCal = 2**31 
        if res > preCal - 1 or res < -(preCal):
            return 0

        return res
