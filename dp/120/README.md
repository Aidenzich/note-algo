# 120. Triangle

## Line of thought
這題的概念是直接將 Triangle 當作 dp, 並從下往上遍歷，從而讓我們在`dp[0][0]` 時就可以得到一個最小的路徑和。

## Solution

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        # Range: (4 - 2) ~ 0
        # 2, 1, 0
        # -2 因為我們需要確保 index 越界
        for row in range(len(triangle) -2, -1, -1):        
            for col in range(len(triangle[row])):
                        

                triangle[row][col] += min(
                    triangle[row + 1][col], 
                    triangle[row + 1][col + 1]
                )
        
        return triangle[0][0]            
```