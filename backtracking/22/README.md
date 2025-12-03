# 22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/

## Classify
DFS（深度優先搜尋） 配合 剪枝（Pruning） 的 Backtracking

## Solution

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current_str, open_n, closed_n):
            if open_n == n and closed_n == n:
                res.append(current_str)
                return 

            if open_n < n:
                backtrack(current_str + "(", open_n+1, closed_n)

            if closed_n < open_n:
                backtrack(current_str + ")", open_n, closed_n + 1)

        backtrack("", 0, 0)
        return res
            
```
