# 289. Game of Life



## Solution
```python

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board: return
        
        rows = len(board)
        cols = len(board[0])
        
        # Deltas for 8 directions
        neighbors = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        
        # 第一階段：遍歷每個細胞，計算鄰居並標記狀態
        for r in range(rows):
            for c in range(cols):
                
                # 1. 統計活鄰居數量
                live_neighbors = 0
                for delta_r, delta_c in neighbors:
                    next_r, next_c = r + delta_r, c + delta_c
                    
                    # 邊界檢查 & 狀態檢查
                    # 注意：如果鄰居是 1 或 2，代表它原本是活的
                    if 0 <= next_r < rows and 0 <= next_c < cols:
                        if board[next_r][next_c] in (1, 2):
                            live_neighbors += 1
                
                # 規則 1 & 3: 活細胞死亡 (原本是 1，鄰居 < 2 或 > 3) -> 標記為 2
                if board[r][c] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[r][c] = 2
                
                # 規則 4: 死細胞復活 (原本是 0，鄰居 == 3) -> 標記為 3
                elif board[r][c] == 0:
                    if live_neighbors == 3:
                        board[r][c] = 3
                        
        # 第二階段：解碼，將 2 和 3 轉回 0 和 1
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
```