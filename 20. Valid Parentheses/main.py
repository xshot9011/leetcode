class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        openParen = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        closeParen = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for i in range(len(s)):
            if s[i] in openParen:
                stack.append(s[i])
            elif s[i] in closeParen:
                if len(stack) > 0:
                    lastChat = stack.pop()
                    if closeParen[s[i]] != lastChat:
                        return False
                else:
                    return False
        
        return True if len(stack) == 0 else False
