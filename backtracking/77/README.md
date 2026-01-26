# Leetcode 77. Combinations

## Solution
```python
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start, curr):
            if len(curr) == k:
                res.append(curr.copy())
                return

            for i in range(start, n+1):
                # 顯性
                # curr.append(i)
                # backtrack(i+1, curr)
                # curr.pop()

                # 隱性
                backtrack(i+1, curr + [i])



        backtrack(1, [])

        return res
```