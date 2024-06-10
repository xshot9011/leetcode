# https://leetcode.com/problems/excel-sheet-column-title/

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        offset = 1
        base = 26
        maxPossible = 0
        cummulative = 0
        ans = ""

        while maxPossible < columnNumber:
            maxPossible += base ** offset
            offset += 1 
        
        offset -= 1 # prevent issue from offset = 0
        print(f'offset: {offset}')
        print(f'maxPossible: {maxPossible}')
        
        for power in range(offset):
            factor = base**power
            char = int((columnNumber/(factor))%base)
            char = 26 if char == 0 else char
            ans = 'Z' + ans if char == 26 else chr(ord('A')+char-1) + ans
            columnNumber = columnNumber-(char*(factor))
            
        return ans
