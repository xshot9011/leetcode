# https://leetcode.com/problems/number-of-atoms/

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        minNumberAscii = ord('0')
        maxNumberAscii = ord('9')
        minLowerCharAscii = ord('a')
        maxLowerCharAscii = ord('z')
        minUpperCharAscii = ord('A')
        maxUpperCharAscii = ord('Z')

        formatFormulas = []
        for char in formula:
            charAscii = ord(char)
            if minNumberAscii <= charAscii and charAscii <= maxNumberAscii:
                # Before Number: {X9, x9, )9, 99} = { char9, )9, 989 }
                prevObject = formatFormulas.pop()
                if type(prevObject) == str:
                    if not (prevObject == '(' or prevObject == ')'):
                        prevObject = prevObject + char
                        formatFormulas.append(prevObject)
                    else:
                        formatFormulas.append(prevObject)
                        formatFormulas.append(char)
                else:
                    formatFormulas.append(prevObject)
                    formatFormulas.append(char)
                    
            elif minUpperCharAscii <= charAscii and charAscii <= maxUpperCharAscii:
                formatFormulas.append([char, 1])
            elif minLowerCharAscii <= charAscii and charAscii <= maxLowerCharAscii:
                tempElement = formatFormulas.pop()
                tempElement[0] = tempElement[0] + char
                formatFormulas.append(tempElement)
            elif char == '(' or char == ')':
                formatFormulas.append(char)

        print(f'formatFormulas: {formatFormulas}')
        elements = []
        _elements = []
        for i in formatFormulas:
            if type(i) != list:
                if i == '(' or i == ')':
                    elements.append(i)
                else:
                    amount = int(i)
                    lastObject = elements.pop()
                    if lastObject == ')':
                        while lastObject != '(' and len(elements) > 0:
                            if type(lastObject) == list:
                                lastObject[1] = lastObject[1] * amount
                                _elements.append(lastObject)
                            lastObject = elements.pop()
                        while len(_elements) > 0:
                            elements.append(_elements.pop())
                    else:
                        lastObject[1] = lastObject[1] * amount
                        elements.append(lastObject)
            else:
                elements.append(i)
        
        print(f'element: {elements}')
        ans = {}
        for i in elements:
            if type(i) == list:
                element = i[0]
                amount = i[1]
                if element in ans:
                    ans[element] += amount
                else:
                    ans[element] = amount
                
        # Time: O(nlog(n))
        # Space: O(n)
        return ''.join([f'{element}{quantity}' if quantity != 1 else f'{element}' for element, quantity in dict(sorted(ans.items())).items()])
            

solution = Solution()
print(solution.countOfAtoms("K4(ON(SO3)2)10(H20)20Mg90"))
# print(solution.countOfAtoms("H2OH3"))
# print(solution.countOfAtoms("Mg(OH)2"))
# print(solution.countOfAtoms("K4(ON(SO3)2)H2"))
