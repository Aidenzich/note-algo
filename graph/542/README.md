# Leetcode 542. 01 Matrix

## Line of thought

這題是一題 “多源 BFS”, 
1. 在一開始我們會需要先找出整張 Graph 中，哪些點是 0, 這樣確立了我們第一輪的起始點有哪些。 同時，為了要讓原先的grid 可以轉變為距離值，我們需要將 1 的值先變更為 -1
2. 透過定義 directions 決定上下左右的偏移差，這樣我們就可以用 for loop 輕鬆實踐 BFS
3. 在將 queue 中的座標取出來後，加上偏移量，得到新座標，我們必須要驗證這個新座標是否在 Graph 邊界內，這是一個邊界檢查問題
4. 透過檢查 `grid[nr][nc]` 是否是 -1, 來更新該點的數值，代表的是，距離最近的 0 的距離


## Solution
- **Time**: $O(M \cdot N)$ - 每個格子最多進出 Queue 一次。
- **Space**: $O(M \cdot N)$ - 雖然我們是原地修改 (In-place)，但在最壞情況下，BFS 的 Queue 需要存儲 $O(M \cdot N)$ 個座標。

```python
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()        


        # 找出所有0 作為多源 BFS 的起點
        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    q.append((r, c))
                elif mat[r][c] == 1:
                    mat[r][c] = -1


        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc 

                    if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] == -1:
                        mat[nr][nc] = mat[r][c] + 1
                        q.append((nr, nc))


        return mat
```