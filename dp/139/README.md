# 139. Word Break
https://leetcode.com/problems/word-break/

## Classify

這題是一個經典的動態規劃問題，因為要判斷一個字串是否可以被切分成字典中的單字，我們需要判斷 $i$ 位置前的字串是否可以由 $\text{wordDict}$ 中的單字組成。

## Line of thought

我們可以使用 `dp[i]` 來記錄 `s[0:i]` 是否為合法(可以由 $\text{wordDict}$ 中的單字組成)。
我們可以先把 $\text{wordDict}$ 放到一個 set 中，這樣可以快速判斷一個字串是否在 $\text{wordDict}$ 中。

然後我們建立一個 dp array，其中 `dp[i]` 代表 `s[0:i]` 是否為合法。初始值都設為 False
針對dp[0] 的狀況，由於在 s[0:0] 的情況下，我們可以說是合法的，因此 `dp[0] = True`

進行兩層回圈：
- 外層迴圈 i 代表的是 s[0:i] 的情況
- 內層迴圈 j 代表的是上一個合法的 s[0:j] 的情況
- s[j:i] 即代表，目前位置與上一個合法的 s[0:j] 之間的字串，透過將這段字串與 word_set 做比對，即可判斷是否合法


## Solution
### Top-Down DP, Time $O(n^2)$, Space $O(n)$
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)

        dp = [False] * (n+1)
        dp[0] = True



        # i: 1, j:0 s[0:1]
        # i: 2, j:0 s[0:2], j:1 s[1:2]
        # i: 3, j:0 s[0:3], j:1 s[1:3], j:2 s[2:3]
        # i: 4, j:0 s[0:4], j:1 s[1:4], j:2 s[2:4], j:3 s[3:4]
        

        for i in range(1, n+1): # 用 range(n+1) 也行
            for j in range(i):
                if dp[j]:
                    substr = s[j:i]

                    if substr in word_set:
                        dp[i] = True
                        break
        return dp[n]
```

### Bottom-Up DP, Time $O(n \cdot L \cdot m)$, Space $O(n)$
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
      dp = [False] * (len(s) + 1)
      dp[len(s)] = True

      for i in range(len(s) - 1, -1, -1):
        for word in wordDict:
          if i + len(word) <= len(s) and s[i:i + len(word)] == word:
            dp[i] = dp[i + len(word)]
            if dp[i]:
              break

      return dp[0]
```