import heapq

class SmallestInfiniteSet:
    def __init__(self):
        self.values = list(range(1, 1001))
        self.heap_queues = heapq.heapify(self.values)

    def popSmallest(self) -> int:
        popped_num = heapq.heappop(self.values)
        print(f"HeapPopped: {popped_num}")
        return popped_num

    def addBack(self, num: int) -> None:
        if num not in self.values:
            heapq.heappush(self.values, num)

    def __repr__(self):
        return f"Values: {self.values}\n"