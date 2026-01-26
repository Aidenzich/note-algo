# Leetcode 78. Subsets

## Line of thought
- 基礎的 Backtracking 應用
- **Deep Copy**：`self.ans.append(list(curr))` 是關鍵，否則存入的是引用，最後會變空列表。

## Solution

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def backtrack(curr, options):
            ans.append(curr)


            for i in range(len(options)):
                # 顯示 backtrack
                # curr.append(options[i])
                # backtrack(list(curr), options[i+1:])
                # curr.pop()


                # 隱式 backtack
                backtrack(curr + [options[i]], options[i+1:])

        backtrack([], nums)

        return ans
```

