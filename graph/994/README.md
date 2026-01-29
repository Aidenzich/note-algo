# Leetcode 994. Rotting Oranges

## Line of thought

這題是一題 “多源 BFS”, 
1. 在一開始我們會需要先找出整張 Graph 中，哪些點是 rotten orange, 這樣確立了我們第一輪的起始點有哪些。
2. 我們需要維護一個變數 `fresh` 來記錄目前還沒有腐爛的橘子的數量。這樣我們才能夠方便計算我們最終是否所有橘子都腐爛了。
3. 透過定義 directions 決定上下左右的偏移差，這樣我們就可以用 for loop 輕鬆實踐 BFS
4. 在將 queue 中的座標取出來後，加上偏移量，得到新座標，我們必須要驗證這個新座標是否在 Graph 邊界內，這是一個邊界檢查問題
5. 透過檢查 `grid[nr][nc]` 是否是 1 (fresh orange), 來更新 fresh 的數量，並把這個新腐爛的 orange 加到 queue 當中。


## Solution 
### Time $O(M \cdot N)$ Sapce: $O(M \cdot N)$

```python
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0


        # 找出 rotten orange 並放到 queue 中，才能進行多源BFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))

                elif grid[r][c] == 1:
                    fresh += 1

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        minute = 0
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    
                    
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))

            minute += 1
                        
        return minute if fresh == 0 else -1
```