# https://leetcode.com/problems/valid-palindrome/description/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isChar(number):
            if number >= 97 and number <= 122:
                return True
            elif number >= 48 and number <= 57:
                return True
            return False

        firstPointer = 0
        lastPointer = len(s) - 1
        if lastPointer == 0:
            return True

        while firstPointer <= lastPointer:
            if not isChar(ord(s[firstPointer].lower())):
                firstPointer += 1
            elif not isChar(ord(s[lastPointer].lower())):
                lastPointer -= 1
            else:
                if s[firstPointer].lower() != s[lastPointer].lower():
                    return False
                firstPointer += 1
                lastPointer -= 1

        return True
            
