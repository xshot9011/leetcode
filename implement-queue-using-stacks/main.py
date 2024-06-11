# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:

    def __init__(self):
        self.mainStack = []
        self.subStack = []

    def push(self, x: int) -> None:
        self.mainStack.append(x)

    def pop(self) -> int:
        for i in range(len(self.mainStack)):
            self.subStack.append(self.mainStack.pop())
        lastElement = self.subStack.pop()
        for i in range(len(self.subStack)):
            self.mainStack.append(self.subStack.pop())
        return lastElement

    def peek(self) -> int:
        for i in range(len(self.mainStack)):
            self.subStack.append(self.mainStack.pop())
        lastElement = None
        if len(self.subStack):
            lastElement = self.subStack[-1]
        for i in range(len(self.subStack)):
            self.mainStack.append(self.subStack.pop())
        return lastElement
        

    def empty(self) -> bool:
        return True if len(self.mainStack) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
