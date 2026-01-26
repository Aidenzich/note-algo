# 131. Palindrome Partitioning

https://leetcode.com/problems/palindrome-partitioning/

## Classify

> Backtracking

因為題目要求列出**所有**可能的分割結果，這種「窮舉所有組合」的特性通常直覺對應到 **Backtracking** (DFS)。
我們可以想像手裡拿著一把刀，試著在字串的每一個可能位置切下去。如果切下來的左半邊是迴文 (Palindrome)，我們就保留這一塊，然後對剩下的右半邊繼續重複同樣的動作。

## Line of Thought

核心邏輯是 **試探性切割(Trial Division)**。

1.  **直觀邏輯**:
    *   我們站在字串的起點 `start`。
    *   嘗試在 `start` 到 `len(s)` 之間的每一個位置 `i` 切一刀。
    *   這一刀切出來的片段是 `s[start : i+1]`。
    *   **檢查**: 這個片段是迴文嗎？
        *   **是**: 把這個片段加入目前的暫存列表 `curr`，然後**遞迴**處理剩下的字串 (從 `i+1` 開始)。
        *   **否**: 這刀切得不好，放棄，嘗試在下一個位置 `i+1` 切。
    *   **終止條件**: 當 `start` 已經超過字串長度，代表整串都切完了，這時候 `curr` 裡面就是一組成功的分割，將其加入結果 `res`。

2.  **具體追蹤 (Concrete Trace)**:
    `s = "aab"`

    ```text
    backtrack(start=0, curr=[])
    |-- i=0, sub="a" (是迴文) -> recurse(1, ["a"])
    |   |-- i=1, sub="a" (是迴文) -> recurse(2, ["a", "a"])
    |   |   |-- i=2, sub="b" (是迴文) -> recurse(3, ["a", "a", "b"])
    |   |       |-- start=3 == len(s) -> res.append(["a", "a", "b"])
    |   |
    |   |-- i=2, sub="ab" (非迴文) -> skip
    |
    |-- i=1, sub="aa" (是迴文) -> recurse(2, ["aa"])
    |   |
    |   |-- i=2, sub="b" (是迴文) -> recurse(3, ["aa", "b"])
    |       |-- start=3 == len(s) -> res.append(["aa", "b"])
    |
    |-- i=2, sub="aab" (非迴文) -> skip
    ```

## Solution

### Time $O(N \cdot 2^N)$, Space $O(N)$
```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(start, curr):
            # 如果起始點已經到了字串末尾，代表一種分割完成
            if start >= len(s):
                res.append(curr)
                return

            # 嘗試在每一個可能的位置切一刀
            for i in range(start, len(s)):
                sub = s[start: i + 1]

                # 判斷是否翻轉過來相同 (Ex: "abba" == "abba")
                if sub == sub[::-1]:
                    # curr 是目前累積的結果，一開始是 []，會越加越多
                    # 使用 curr + [sub] 創造一個新的 list 傳入下一層，避免副作用
                    backtrack(i+1, curr + [sub])

        backtrack(0, [])
        return res
```
*   **Time**: 最壞情況下 (例如 "aaaa")，每一個字元之間都可能是切割點，共有 $2^{N-1}$ 種分割方式。對於每一種分割，我們需要 $O(N)$ 的時間來構建子字串與檢查迴文。
*   **Space**: $O(N)$ 是遞迴深度 (Stack depth) 以及暫存路徑 `curr` 的空間 (不包含 output result)。



## Traps & Notes
*   **⚠️ 常見陷阱 (Trap)**: Python 的 list 是 Mutable 的。
    *   如果你在遞迴時使用 `curr.append(sub)` 然後 `backtrack(...)` 再 `curr.pop()` (Backtracking 的標準寫法)，記得在加入 `res` 時要 copy 一份 (`res.append(curr[:])`)。
    *   本解法使用 `curr + [sub]`，這會直接產生一個新的 list，雖然空間稍微多一點點，但寫法更簡潔且不易出錯 (不用手動 pop)。