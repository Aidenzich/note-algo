# 424. Longest Repeating Character Replacement

## Line of Thought
題目可以簡化成要求我們找到一個最長的子字串，其中最多可以有 `k` 個不同的字符。 

這題需要使用 Sliding window 的策略，判斷當前位置前的子字串最長可以到多少
因此我們會需要維護幾個狀態：
- left: 當前子字串的左邊界
- right: 當前子字串的右邊界
- counter: 當前子字串中每個字符的出現次數
- window_size: 當前子字串的長度
- max_count: 當前子字串中最多出現的字符次數
- max_len: 記錄所有結果中最長的子字串的長度

max_count + k 表示我們可以將最多 k 個字符替換成其他字符，使得所有字符都相同。這也代表著在當前位置，我們最多可以得到最長的 max_count + k 的子字串。
因此如果 window_size > max_count + k, 表示這個 window 不合法，我們需要收縮窗口，直到 window_size <= max_count + k, 滿足了這個條件後我們才可以更新 max_len


## Solution
```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left = 0
        max_count = 0
        n = len(s)
        max_len = 0

        # left  right
        # 0, 1, 2
        for right in range(n):
            char = s[right]
            counter[char] = counter.get(char, 0) + 1

            # 現階段最大長度
            max_count = max(counter[char], max_count)

            window_size = right - left  + 1

            if window_size > max_count + k:
                left_char = s[left]
                counter[left_char] -= 1
                left += 1 


            max_len = max(max_len, right - left + 1)

        return max_len

```