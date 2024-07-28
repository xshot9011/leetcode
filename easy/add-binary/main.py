class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ''
        maxLenght = max(len(a), len(b))
        isCarry = False
        
        counter = 0
        while counter < maxLenght or isCarry:
            aIndex = len(a) - counter - 1
            bIndex = len(b) - counter - 1
            operand1 = 0
            operand2 = 0
            if counter < len(a):
                operand1 = int(a[aIndex])
            if counter < len(b):
                operand2 = int(b[bIndex])
            summation = operand1 + operand2
            if isCarry:
                summation += 1
                isCarry = False
            if summation // 2 == 1:
                isCarry = True            

            ans = str(summation%2) + ans
            counter += 1
        
        return ans
    
    def addBinary2(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        ans = bin(a+b)[2:]
        
        return ans
