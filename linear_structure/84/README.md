# Leetcode 84. Largest Rectangle in Histogram

使用一個單調遞增棧 (monotonic increasing stack) 儲存柱子的索引，當遇到比棧頂更矮的柱子時，就依次彈出stack，並以被彈出的柱子為高、當前柱子為「右邊界」、棧中新頂部為「左邊界」，來計算並更新最大矩形面積。

```python
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0


        for i, h in enumerate(heights + [0]):
            
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
```


p.s. Python List 就是 Stack. 