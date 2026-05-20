class MinStack:

    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minList:
            self.minList.append(min(self.minList[-1], val))
        else:
            self.minList.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.minList.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minList[-1]
        
