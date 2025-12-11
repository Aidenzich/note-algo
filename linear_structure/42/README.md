# 42. Trapping Rain Water


## Solution
```python
class Solution:
    def trap(self, height: List[int]) -> int:
        
        n = len(height)

        if n < 3:
            return 0

        # 0,1,0,2,1,0,1,3,2,1,2,1
        
        #    ---------------------->
        # 0,[1,0,2,1,0,1,3,2,1,2,1]
        # ^

        #   <----------------------
        #   [0,1,0,2,1,0,1,3,2,1,2],1
        # ^

        # Find the heighest wall in the left
        left_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
            
        right_max = [0] * n
        right_max[-1] = height[-1]


        for i in range(n-2,-1,-1):
            right_max[i] = max(right_max[i+1], height[i])
            

        # Merge
        total = 0
        for i in range(n):
            level = min(left_max[i], right_max[i])
            water = level - height[i]
            total += max(0, water)

        return total


```