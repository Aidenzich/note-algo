# 73. Set Matrix Zeroes

https://leetcode.com/problems/set-matrix-zeroes/description/


## Solution
```python
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        # 1. 檢查第一列 (Row 0) 和第一行 (Col 0) 本身是否包含 0
        first_row_has_zero = False
        first_col_has_zero = False
        
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_has_zero = True
                break
                
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_has_zero = True
                break
                
        # 2. 遍歷內部矩陣，將 0 的訊息投影到「第一行」與「第一列」
        # 從 1 開始，避開邊界以免混淆
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0  # 標記該行 (Row Header)
                    matrix[0][c] = 0  # 標記該列 (Col Header)
        
        # 3. 根據邊界的標記，將內部的格子設為 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
                    
        # 4. 最後處理第一行與第一列
        if first_row_has_zero:
            for c in range(cols):
                matrix[0][c] = 0
                
        if first_col_has_zero:
            for r in range(rows):
                matrix[r][0] = 0
```