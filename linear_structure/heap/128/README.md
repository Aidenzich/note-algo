# 128. Longest Consecutive Sequence

## Line of Thought
這題是 maxHeap 的練習題，透過 maxHeap 可以復現題目的規則，並將時間複雜度控制在 $O(n \log n)$



## Solution
```python
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-s for s in stones]

        heapq.heapify(max_heap)


        while len(max_heap) > 1:
            s1 = - heapq.heappop(max_heap)
            s2 = - heapq.heappop(max_heap)

            if s1 != s2:
                new = s1 - s2
                heapq.heappush(max_heap, -new)

        return -max_heap[0] if max_heap else 0
            
        
```