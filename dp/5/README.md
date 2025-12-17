# 5. Longest Palindromic Substring

## Line of thought
透過宣告一個 N * N 的矩陣，我們可以儲存所有可能的回文子字串 `s[i:j]`，並在遍歷矩陣時更新最大回文子字串的起始位置和長度。






## Solution
### DP
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)] # N * N 矩陣

        max_len= 1
        start = 0

        # i 需要依賴 i+1, 因此要把 i + 1 先算好，所以要反者來
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    # 0, 1 個字代表不需判斷是否是回文
                    # (i+1), (j-1) 代表 i+1, ...., j-1 即 i, j 中間的內容是否為回文
                    if j - i < 2 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                    
                        current_len = j - i + 1
                        if current_len > max_len:
                            max_len = current_len
                            start = i

        return s[start: start+max_len]
```