class DynamicArray:
    
    def __init__(self, capacity: int):
        self.darry = []
        self.size = 0
        self.cap = capacity

    def get(self, i: int) -> int:
        return self.darry[i]


    def set(self, i: int, n: int) -> None:
        self.darry[i] = n


    def pushback(self, n: int) -> None:
        
        self.size += 1
        if self.size > self.cap:
            self.resize()
        self.darry.append(n)


    def popback(self) -> int:
        self.size -= 1
        return self.darry.pop()
 

    def resize(self) -> None:
        while self.size >  self.cap:
            self.cap *= 2
            


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.cap

