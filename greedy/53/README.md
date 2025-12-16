# 53. Maximum Subarray

## Line of thought
這題只要基於 Kadane's Algorithm 的框架，並稍作修改即可。

**Kadane's Algorithm** 是一種只需要遍歷陣列一次（$O(n)$）的演算法，透過不斷判斷「要延續之前的累積」還是「從當前數字重新開始」，來找出最大連續子陣列和的高效演算法。




## Solution
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_max = 0
        global_max = -float('inf')
        
        for num in nums:
            # 計算當前可能的最大子陣列和
            curr_max = max(num, curr_max + num)
            # 更新全局最大子陣列和
            global_max = max(global_max, curr_max)
            
        return global_max
```