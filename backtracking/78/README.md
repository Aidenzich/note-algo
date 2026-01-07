# Leetcode 78. Subsets

## Line of thought
- 基礎的 Backtracking 應用
- **Deep Copy**：`self.ans.append(list(curr))` 是關鍵，否則存入的是引用，最後會變空列表。

## Solution
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack([], nums)
        return self.ans

    def backtrack(self, curr, options):
        self.ans.append(list(curr))

        for i in range(len(options)):
            curr.append(options[i])

            self.backtrack(curr, options[i+1:])
            
            curr.pop()
```