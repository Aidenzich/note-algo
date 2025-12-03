# 909. Snakes and Ladders

https://leetcode.com/problems/snakes-and-ladders/description/


## Solution
```python
from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n * n
                
        # 將 1 ~ n^2 的數字轉換為 board 的 (row, col)
        def get_coord(num):
            # 因為 num 是從 1 開始，轉成 0-indexed 方便計算
            idx = num - 1
            
            # 計算這是從底部數上來的第幾行 (0, 1, 2...)
            r_from_bottom = idx // n

            # 實際的 row 索引 (矩陣是從上往下 index)
            r = n - 1 - r_from_bottom
            
            # 計算 col 索引
            # 如果是偶數行 (0, 2, 4...)：方向是左 -> 右
            # 如果是奇數行 (1, 3, 5...)：方向是右 -> 左
            c = idx % n
            if r_from_bottom % 2 == 1:
                c = n - 1 - c
            
            return r, c
        
        # Queue : (當前數字, 累積步數)
        queue = deque([(1, 0)])
        visited = {1}
        
        while queue:
            curr, step = queue.popleft()
            
            # 嘗試擲骰子 1 到 6
            for i in range(1, 7):
                next_val = curr + i
                
                # 超出邊界
                if next_val > target:
                    break
                
                # 取得該數字在棋盤上的實際位置
                r, c = get_coord(next_val)
                
                # 檢查是否有蛇或梯子
                destination = next_val
                if board[r][c] != -1:
                    destination = board[r][c]
                
                # 到達終點
                if destination == target:
                    return step + 1
                
                # 若沒走過，加入 Queue
                if destination not in visited:
                    visited.add(destination)
                    queue.append((destination, step + 1))
                
        return -1
```