# Leetcode 286. Walls and Gates

## Line of thought
1. 先找出寶箱
2. 定義方向
3. 判斷是否越界
4. 判斷是否是空位 (Inf) or 2147483647
5. 如果是，從前一個距離寶箱的位置+1



## Solution
### Time $O(M \cdot N)$ Space $O(M \cdot N)$
```python
from collections import deque

class Solution:
    def wallsAndGates(self, grid: List[List[int]]) -> None:        
        if not grid:
            return
        
        m, n = len(grid), len(grid[0])
        q = deque()
        
        # 儲存所有寶箱
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
            
                # if nr < 0 or nr >= m or nc < 0 or nc >= n:
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                                
                if grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr, nc)) 
```