# https://leetcode.com/problems/crawler-log-folder/description

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        locator = {
            '../': 1,
            './': 1
        }
        for action in logs:
            if action in locator:
                if action == '../' and len(stack) > 0:
                    stack.pop()
            else:
                stack.append(action) 

        # Time: O(n)
        # Space: O(n)
        return len(stack)
    
    def minOperations2(self, logs: List[str]) -> int:
        counter = 0
        locator = {
            '../': 1,
            './': 1
        }
        for action in logs:
            if action in locator:
                if action == '../' and counter > 0:
                    counter -= 1
            else:
                counter += 1

        # Time: O(n)
        # Space: O(1)
        return counter
