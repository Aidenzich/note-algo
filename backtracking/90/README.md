# 90. Subsets II

## Line of thought

1. **排序 (Sort)**：必須先對輸入陣列排序，讓重複的值相鄰，這是後續去重的關鍵。
2. **Deep Copy**：在 `ans.append()` 時使用 `list(curr)`，避免回溯過程影響到已存入的結果。
3. **去重邏輯 (Pruning)**：使用 `if i > start and nums[i] == nums[i-1]`。
* `i == start`：代表這是當前層級的第一個選擇，必須執行（才能產生如 `[2, 2]` 的結果）。
* `i > start`：代表在同一層中嘗試其他分支出現重複數字，此時跳過 (skip) 才能避免重複子集。



## Solution

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        # 1. 排序是去重的必要前提
        nums.sort()
        # 2. 使用 start 指標從 0 開始
        self.backtrack(0, [], nums)
        return self.ans

    def backtrack(self, start, curr, nums):
        # 進入遞迴即代表找到一個子集，存入副本
        self.ans.append(list(curr))

        for i in range(start, len(nums)):
            # 3. 核心去重邏輯
            # 如果目前不是這一層的第一個選項，且跟前一個數字相同，則跳過
            if i > start and nums[i] == nums[i-1]:
                continue

            # 選擇當前元素
            curr.append(nums[i])
            
            # 遞迴：傳入 i + 1 作為下一層的起點
            self.backtrack(i + 1, curr, nums)
            
            # 回溯：撤銷選擇
            curr.pop()

```