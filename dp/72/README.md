# 72. Edit Distance

## Line of thought
我們可以再次畫出一個網格`dp`。
- 橫軸：代表 word2 的字元。
- 縦軸：代表 word1 的字元。
- `dp[i][j]` 的意義：把 word1 的前 $i$ 個字，變成 word2 的前 $j$ 個字，最少需要幾步？

這樣子刪除、插入、替換的狀態可以表示為：
1. **`dp[i-1][j]` (Delete)**: 「`dp[i-1][j]` 已經拼完」，所以現在多出來的這個 `i` 是多餘的。
2. **`dp[i][j-1]` (Insert)**: 「只拼到 `j-1` 的狀態」，既然 `word1` (用掉 `i` 個) 已經用完了卻還差一個 `j`，所以必須**插入**。
3. **`dp[i-1][j-1]` (Replace)**: 「`i-1` 與 `j-1` 都比對完了」，現在是兩個新字元面對面。如果不一樣，就是**替換**。


## Solution
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        # 建立 DP 表格，大小為 (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # 1. 初始化邊界
        # 第一行：把 word1 變成空字串，需要一直刪除
        for i in range(m + 1):
            dp[i][0] = i
            
        # 第一列：把空字串變成 word2，需要一直插入
        for j in range(n + 1):
            dp[0][j] = j
            
        # 2. 開始填表
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # 注意：字串索引是從 0 開始，所以要用 i-1 和 j-1
                if word1[i-1] == word2[j-1]:
                    # 字元相同，不做操作，步數等於左上角
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 字元不同，取 (左、上、左上) 的最小值 + 1
                    dp[i][j] = 1 + min(
                        dp[i][j-1],    # 插入 (來自左邊)
                        dp[i-1][j],    # 刪除 (來自上面)
                        dp[i-1][j-1]   # 替換 (來自左上)
                    )
                    
        return dp[m][n]
```