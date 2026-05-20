class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        self.arr.sort()
        

    def findMedian(self) -> float:
        n = len(self.arr)
        if n % 2 == 0:
            one = n//2
            two = one - 1
            return (self.arr[one] + self.arr[two])/2
        else:
            return self.arr[(n//2)]
        
        