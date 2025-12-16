# 703. Kth Largest Element in an Array

## Line of thought
基本的heap 應用題，透過只保留k 個元素在heap中，我們就可以確保`heap[0]` 值是第 k 大的元素。


## Solution
```python
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        # Heap 只保證 heap[0] 是最小的
        return self.heap[0]
```