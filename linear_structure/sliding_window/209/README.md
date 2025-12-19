# 209. Minimum Size Subarray Sum


## Line of Thought
題目要求我們找到一個最短的子字串，其中所有字符的和大於等於 `target`.
- `Window Sum` 指的是當前窗口中所有字符的和.
- 使用 `min_len` 來記錄最短的子字串的長度.
- 使用 `l` 來表示當前窗口的左邊界.
- 使用 `r` 來表示當前窗口的右邊界.


## Solution
```python
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        window_sum = 0
        min_len = float("inf")
        
        # 2,3,1,2,4,3
        # ^             window_sum = 2
        #   ^           window_sum = 5
        #     ^         window_sum = 6
        #       ^       window_sum = 8 > 7
        #       ^       window_sum = 8 - 2 = 6 < 7, min_len = 4
        #         ^     window_sum = 6 + 4 = 10 > 7
        #         ^     window_sum = 6 + 4 - 3 = 7 == 7

        for r, v in enumerate(nums):
            window_sum += v

            while window_sum >= target:
                window_sum -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1
            
        if min_len == float("inf"):
            return 0

        return min_len
```