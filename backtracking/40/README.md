# 40. Combination Sum II

https://leetcode.com/problems/combination-sum-ii/description/

## Classify
**Backtracking (回溯法)**
題目要求找出所有總和為目標值的*唯一組合*。

限制條件（`candidates` 長度 <= 100, `target` <= 30）以及「選擇或不選擇」元素的特性暗示了帶有剪枝的窮舉搜索，這符合回溯法 (Backtracking) 的模式。與 Combination Sum I 最大的不同在於每個數字只能使用一次，且輸入包含重複的數字。

## Line of thought
- Step 1: 先排序，讓重複的數字聚集在一起
- Step 2: 跳過重複的數字
- Step 3: 剪枝來優化速度


## Solution
### Time O(2^N), Space O(N)
*   Time: 在最壞情況下，我們可能會探索 $2^N$ 種組合。加上排序 $O(N \log N)$ 與指數級相比可以忽略不計。
*   Space: $O(N)$ 用於遞迴堆疊和暫存列表儲存。

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() # 關鍵步驟 1: 排序以處理重複項

        def backtrack(start, curr, remain):
            if remain == 0:
                res.append(curr[:])
                return 
            
            for i in range(start, len(candidates)):
                # 關鍵步驟 2: 跳過重複項
                # 如果這不是我們在這個迴圈/層級中選擇的第一個數字 (i > start)，
                # 並且它與前一個數字相同，則這是一個重複的路徑。
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                
                num = candidates[i]
                
                # 優化：剪枝
                # 如果當前數字已經大於剩餘值，
                # 則無需進一步檢查，因為數字已排序。
                if remain - num < 0:
                    break

                # 遞迴：i+1 因為我們不能重複使用相同的元素索引
                backtrack(i + 1, curr + [num], remain - num)
            
        backtrack(0, [], target)
        return res
```

### ⚠️ 常見陷阱 (Trap)
*   **重複邏輯 (Duplicate Logic)**：很容易將 `i > start` 與 `i > 0` 混淆。`i > 0` 會跳過全域的*所有*重複項（阻止 `[1, 1]`），而 `i > start` 僅跳過*當前決策層級*的重複項（允許 `[1, 1]` 但阻止以 `1` 開頭的兩個獨立分支）。
*   **索引傳遞 (Index passing)**：記住傳遞 `i + 1` 到下一次遞迴，而不是 `start + 1`。你要從*當前*選擇的元素之後繼續前進。