class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
            
        

    def findMedian(self) -> float:
        self.arr.sort()
        mid = len(self.arr) // 2
        if len(self.arr) % 2 == 0:
            return (self.arr[mid] + self.arr[mid - 1]) / 2
        return float(self.arr[mid])
         
        