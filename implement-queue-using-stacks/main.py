# https://leetcode.com/problems/implement-queue-using-stacks/

class MyQueue:
    #       | Time   |
    # push  |  O(1)  |
    # pop   |  O(2n) |
    # peek  |  O(2n) |
    # empty |  O(1)  |

    def __init__(self):
        self.mainStack = []
        self.subStack = []

    def push(self, x: int) -> None: # O(1)
        self.mainStack.append(x)

    def pop(self) -> int: # O(2n)
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

class MyQueue:
    #       | Time   |
    # push  |  O(1)  |
    # pop   |  O(2n) |
    # peek  |  O(2n) |
    # empty |  O(1)  |

    def __init__(self):
        self.mainStack = []
        self.subStack = []
        self.isCurrentMainStack = True

    def push(self, x: int) -> None:
        if not self.isCurrentMainStack:
            for i in range(len(self.subStack)):
                self.mainStack.append(self.subStack.pop())
        self.mainStack.append(x)
        self.isCurrentMainStack = True

    def pop(self) -> int:
        if self.isCurrentMainStack:
            for i in range(len(self.mainStack)):
                self.subStack.append(self.mainStack.pop())
            self.isCurrentMainStack = False
        return self.subStack.pop()

    def peek(self) -> int:
        if self.isCurrentMainStack:
            for i in range(len(self.mainStack)):
                self.subStack.append(self.mainStack.pop())
            self.isCurrentMainStack = False
        return self.subStack[-1]

    def empty(self) -> bool:
        pointer = None
        if self.isCurrentMainStack:
            pointer = self.mainStack
        else:
            pointer = self.subStack 
        return True if len(pointer) == 0 else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
