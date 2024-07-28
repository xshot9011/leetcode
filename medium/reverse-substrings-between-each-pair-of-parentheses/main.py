# https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses

class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for char in s:
            if char == '(':
                stack.append(char)
            elif char == ')':
                reverseStack = []
                while True:
                    c = stack.pop()
                    if c == '(':
                        break
                    reverseStack.append(c)
                while len(reverseStack) > 0:
                    stack.append(reverseStack.pop(0))
            else:
                stack.append(char)
        
        return ''.join(stack)
