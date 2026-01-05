# 973. K Closest Points to Origin

## Line of Thought
Heap 結構的簡單應用


## Solution
```python
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        ans = []
        distances = []

        for idx, p in enumerate(points):
            heapq.heappush(distances, 
                (pow(p[0], 2) + pow(p[1], 2), idx), 
            )

        
        for _ in range(k):
            elem = heapq.heappop(distances)
            ans.append(points[elem[1]])


        return ans
```