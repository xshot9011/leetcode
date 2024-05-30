class Solution:
    def isPalindrome(self, s: str) -> bool:
        def isChar(number):
            return True if (number >= 97 and number <= 122) or (number >= 48 and number <= 57) else False

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
