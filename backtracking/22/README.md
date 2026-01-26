# 22. Generate Parentheses

https://leetcode.com/problems/generate-parentheses/

## Classify
DFS（深度優先搜尋） 配合 剪枝（Pruning） 的 Backtracking

## Line of Thought
當我們看到題目要求「合法的括號組合」時，我們試著列出它的 **數學定義 (Properties)**：
1.  **總數量固定**：一定要有 $n$ 個左括號，$n$ 個右括號。
2.  **順序規則**：不管你讀到字串的哪裡，**右括號的數量永遠不能超過左括號**（否則前面一定有一個沒閉合的右括號，例如 `)(` ）。

一旦列出了這兩條規則，解法就自然浮現了：
* **規則 1 翻譯成代碼** $\rightarrow$ 我們需要兩個變數 `open` 和 `closed` 來記錄用了多少，上限是 $n$。
* **規則 2 翻譯成代碼** $\rightarrow$ `if closed < open` 才能加右括號。

這即是將 **「合法性檢查 (Validity Check)」** 拆解後，直接放進遞迴的條件裡。


### 思維模式：限制滿足 (Constraint Satisfaction)

這類 Backtracking（回溯法）題目通常都有一個通用的思考模板，通常不建議去背 `open` 和 `close`，而是建議你記住這個思考模式：

**模板：**
> 「我有什麼資源？」(State) $\rightarrow$ 「我現在能做什麼選擇？」(Choices) $\rightarrow$ 「哪些選擇是合法的？」(Constraints)

套用到這題：
1.  **資源 (State)**：有 $n$ 個左括號額度，$n$ 個右括號額度。
2.  **選擇 (Choices)**：放 `(` 或放 `)`。
3.  **限制 (Constraints)**：
    * 左括號沒用完才能放 `(`。
    * 右括號用得比左括號少，才能放 `)`。

#### Appendix
這種「維護當前狀態」的技巧在很多題目都通用。

* **題目：組合總和 (Combination Sum)**
    * **直觀**：湊數字。
    * **狀態轉化**：設定一個 `remaining_target`。
    * **限制**：只有當 `remaining_target >= num` 時，我才能選這個數字 `num`。
* **題目：全排列 (Permutations)**
    * **直觀**：把數字排排看。
    * **狀態轉化**：設定一個 `used` 布林陣列或是 `Set`。
    * **限制**：只有當這個數字 `not in used` 時，我才能選它。

## Solution

```python
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(current_str, open_n, closed_n):
            if open_n == n and closed_n == n:
                res.append(current_str)
                return 

            if open_n < n:
                backtrack(current_str + "(", open_n+1, closed_n)

            if closed_n < open_n:
                backtrack(current_str + ")", open_n, closed_n + 1)

        backtrack("", 0, 0)
        return res
```
