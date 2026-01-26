# 90. Subsets II

## Line of thought

1. **排序 (Sort)**：必須先對輸入陣列排序，讓重複的值相鄰，這是後續去重的關鍵。
2. **Deep Copy**：在 `ans.append()` 時使用 `list(curr)`，避免回溯過程影響到已存入的結果。 (如果使用隱性回溯，就不需要深拷貝)
3. **去重邏輯 (Pruning)**：使用 `if i > start and nums[i] == nums[i-1]`。
* `i == start`：代表這是當前層級的第一個選擇，必須執行（才能產生如 `[2, 2]` 的結果）。
* `i > start`：代表在同一層中嘗試其他分支出現重複數字，此時跳過 (skip) 才能避免重複子集。



## Solution
```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtrack(start, curr):
            ans.append(curr)        
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                backtrack(i+1, curr + [nums[i]])

        backtrack(0, [])
        return ans
```