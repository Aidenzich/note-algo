# 221. Maximal Square

## Line of thought
新增一個 dp 矩陣，用來儲存該位置為右下角時，可構成的最大正方形(內容全為1)的邊長。

## Solution
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        
        # dp[i][j] store 全為1正方形的邊長
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i-1][j-1] == '1':
                    
                    dp[i][j] = min(
                        dp[i-1][j], # 左
                        dp[i][j-1], # 上
                        dp[i-1][j-1], # 左上
                    ) + 1
                    max_side = max(max_side, dp[i][j])
        
        return max_side * max_side
```