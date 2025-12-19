# Leetcode 76. Minimum Window Substring

## Classify
Sliding Window, Hash Table, String
思路：這題要求我們在字串 `s` 中找到包含字串 `t` 所有字符的最小子字串。因為我們需要尋找一個連續的區間（子字串），且這個區間的大小是動態變化的（我們希望它盡可能小），這非常適合使用滑動窗口（Sliding Window）的方法。

## Line of thought
題目要求我們在 `s` 中找到一個最小的窗口，該窗口包含 `t` 中所有的字符。

我們可以使用滑動窗口策略，維護兩個指針 `l` (左邊界) 和 `r` (右邊界)：
1.  **擴展窗口**：移動 `r` 指針，將字符加入窗口，直到窗口包含了 `t` 中所有的字符。
2.  **收縮窗口**：一旦窗口滿足條件（包含所有 `t` 的字符），我們嘗試移動 `l` 指針來縮小窗口，同時更新最小長度 `minLen`。我們持續收縮，直到窗口不再滿足條件為止。
3.  **重複**：繼續移動 `r`，重複上述過程。

**優化判斷條件**：
為了避免每次移動指針都遍歷整個 Hash Map 來檢查是否滿足條件，我們可以使用一個變量 `matches`：
-   當某個字符加入窗口後，其數量**剛好達到** `t` 中該字符的需求數量時，`matches` 加 1。
-   當某個字符移出窗口後，其數量**變得小於** `t` 中該字符的需求數量時，`matches` 減 1。
-   當 `matches` 等於 `t` 中不同字符的總數時，表示窗口滿足條件。

這樣我們就可以在 O(1) 時間內判斷窗口是否有效。

## Solution
### Time O(n) Space O(n)
```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:        
        l = 0
        sCount, tCount = {}, {}
        matches = 0
        minLen = float("inf")
        res = ""

        for i in range(len(t)):
            tCount[t[i]] = tCount.get(t[i], 0) + 1
                        
        for r, c in enumerate(s):
            sCount[c] = sCount.get(c, 0) + 1
            
            if c in tCount and sCount[c] == tCount[c]:
                matches += 1

            while matches == len(tCount):                        
                                        
                if (r-l+1) < minLen:
                    minLen = r-l+1
                    res = s[l:r+1]


                sCount[s[l]] -= 1
                if s[l] in tCount and sCount[s[l]] < tCount[s[l]]:
                    matches -= 1

                l+=1


        return res
```

這題本身只在乎子字段是否滿足條件，而不用在乎當一個char 數量超出條件時的狀況，因此我們不用在 char 的 Counter 超出條件時就將 matches--.

### Time O(n) Space O(1)
這裡的 Space O(1) 是指如果我們假設字符集的大小是固定的（例如 ASCII 只有 128 個字符），那麼 Hash Map 或 Array 的大小就是常數，不會隨著輸入字串 `s` 的長度 `n` 而增長。

此外，為了確保嚴格的 Time O(n)，我們應該避免在迴圈中進行字串切片（Slicing），因為切片操作本身需要 O(k) 的時間。我們可以改為記錄最佳窗口的「起始位置」和「長度」，最後再切片。

```python
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        # 使用字典記錄 t 的字符需求
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
            
        window_count = {}
        
        have, need = 0, len(t_count)
        l = 0
        res = [-1, -1] # 記錄起始和結束位置
        res_len = float("inf")
        
        for r in range(len(s)):
            c = s[r]
            window_count[c] = window_count.get(c, 0) + 1
            
            if c in t_count and window_count[c] == t_count[c]:
                have += 1
                
            while have == need:
                # 更新結果 (只記錄長度和位置，不切片)
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = (r - l + 1)
                
                # 收縮窗口
                window_count[s[l]] -= 1
                if s[l] in t_count and window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if res_len != float("inf") else ""
``` 