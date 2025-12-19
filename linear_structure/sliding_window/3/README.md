# Leetcode 3. Longest Substring Without Repeating Characters


## Line of Thought
題目要求我們找到一個最長的子字串，其中所有字符都是唯一的. 

## Solution.
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding Window
        window_data = set()
        l = 0
        max_len = 0

        # dvdf
        for idx, c in enumerate(s):
            while s[idx] in window_data:
                window_data.remove(s[l])
                l += 1
            
            window_data.add(c)

            max_len = max(idx - l + 1, max_len)

        return max_len
```

