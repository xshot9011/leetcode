# https://leetcode.com/problems/reverse-bits/
class Solution:
    def reverseBits(self, n: int) -> int:
        number = 0

        for i in range(32):
            lastBit = n & 1 # get last bit
            n = n >> 1 # Shif it
            number = number << 1 # insert new last bit
            number = number | lastBit

        return number
