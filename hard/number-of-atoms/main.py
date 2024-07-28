# https://leetcode.com/problems/number-of-atoms/

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        ans = ''
        currentElement = ''
        mayLowercaseFollowedByUppercase = False
        wasPrevCharUppercase = False
        formula = formula + '\n'
        minNumberAscii = ord('0')
        maxNumberAscii = ord('9')
        minLowerCharAscii = ord('a')
        maxLowerCharAscii = ord('z')
        minUpperCharAscii = ord('A')
        maxUpperCharAscii = ord('Z')

        elements = []
        _elements = []
        for index, char in enumerate(formula):
            charAscii = ord(char)
            print(f'charAscii: {char}({charAscii})')
            if char == '\n':
                print('if char == "\\n":')
            elif minNumberAscii <= charAscii and charAscii <= maxNumberAscii:
                print('Case::: Number')
                mayLowercaseFollowedByUppercase = False
                wasPrevCharUppercase = False
                currentElement = ''
                # prevObject = elements.pop()
                # print('prevObject: {prevObject}')
                # if prevObject == ')':
                #     pass
                # else: # Number
                #     pass
            elif minUpperCharAscii <= charAscii and charAscii <= maxUpperCharAscii:
                if wasPrevCharUppercase:
                    print('Case::: PreUpper, UpperCase')
                    mayLowercaseFollowedByUppercase = True
                    print(f'======== currentElement: {currentElement}')
                    currentElement = char
                    print(f'======== currentElement: {currentElement}')
                elif not wasPrevCharUppercase:
                    print('Case::: preLower, UpperCase')
                    mayLowercaseFollowedByUppercase = True
                    wasPrevCharUppercase = True
                    currentElement = char
                elif not mayLowercaseFollowedByUppercase:
                    print('Case::: UpperCase')
                    mayLowercaseFollowedByUppercase = True
                    wasPrevCharUppercase = True
                    currentElement = char
                    print(f'======== currentElement: {currentElement}')
            elif mayLowercaseFollowedByUppercase and minLowerCharAscii <= charAscii and charAscii <= maxLowerCharAscii:
                print('Case::: LowerCase')
                mayLowercaseFollowedByUppercase = False
                wasPrevCharUppercase = False
                currentElement = currentElement + char
                print(f'======== currentElement: {currentElement}')
            elif char == '(' or char == ')':
                print('Case::: Paren Detected')
                mayLowercaseFollowedByUppercase = False
                wasPrevCharUppercase = False
                currentElement = ''
                elements.append((char, None))
            print('========'*3)

        return ans
