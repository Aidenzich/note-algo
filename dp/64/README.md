# 64. Minimum Path Sum

## Line of thought
這題同樣是直接將 grid 當作 dp, 並從左上角遍歷到右下角，從而讓我們在`grid[m-1][n-1]` 時就可以得到一個最小的路徑和。
有四種情況需要考慮：
1. `i == 0 and j == 0`: 這表示我們在左上角，不需要做任何操作。
2. `i == 0`: 這表示我們在第一行，只能從左邊來。
3. `j == 0`: 這表示我們在第一列，只能從上邊來。
4. `else`: 這表示我們在其他位置，可以從左邊或上邊來。


## Solution
```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i==0:
                    grid[i][j] += grid[i][j - 1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                    


        return grid[-1][-1]
```