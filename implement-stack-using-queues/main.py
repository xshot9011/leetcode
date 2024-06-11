# https://leetcode.com/problems/implement-stack-using-queues/
class MyStack:
    def __init__(self):
        self.queue = []
        # out <- [1 - 2 - 3 - 4] <- in

    def push(self, x: int) -> None:
        self.queue.append(x)        

    def pop(self) -> int:
        if not self.empty():
            for i in range(len(self.queue)-1):
                self.queue.append(self.queue.pop(0))
            return self.queue.pop(0)
        return 0

    def top(self) -> int:
        return self.queue[-1] if not self.empty() else None

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
