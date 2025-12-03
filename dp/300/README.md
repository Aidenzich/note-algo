# 300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence/

## Classify

**Dynamic Programming**
我們想要找一個最長的子序列，這通常意味著我們需要基於較小的子問題（較短的序列）來構建答案。
直觀上，對於每個元素，我們想知道「如果我接在某個比我小的元素後面，能形成多長的序列？」

## Line of thought

### 直觀邏輯 (Intuitive Logic)

想像我們在排隊。每個人（數字）都想加入一個隊伍，但規則是：你只能排在比你矮（小）的人後面。

為了讓隊伍最長，當輪到我（`nums[i]`）時，我會回頭看所有排在我前面的人（`nums[j]` where `j < i`）。
在所有比我小的人當中，誰身後的隊伍目前最長？我就排在他後面，這樣我的隊伍長度就是他的長度 + 1。

如果前面沒有人比我小，那我就是一個新的隊伍的開始，長度為 1。

### 具體追蹤 (Concrete Trace)

`nums = [10, 9, 2, 5, 3, 7, 101, 18]`
`dp[i]` 代表以 `nums[i]` **結尾**的最長遞增子序列長度。
初始化 `dp = [1, 1, 1, 1, 1, 1, 1, 1]` (每個人自己都是長度 1)

```text
# i: 0, nums[0]=10
  - 前面沒人。
  dp[0] = 1

# i: 1, nums[1]=9
  - j:0 (10) >= 9 (不能接)
  dp[1] = 1

# i: 2, nums[2]=2
  - j:0 (10) >= 2
  - j:1 (9) >= 2
  dp[2] = 1

# i: 3, nums[3]=5
  - j:0 (10) >= 5
  - j:1 (9) >= 5
  - j:2 (2) < 5 -> 接在 2 後面 (dp[2]+1 = 2)
  dp[3] = 2

# i: 4, nums[4]=3
  - j:0..1 >= 3
  - j:2 (2) < 3 -> 接在 2 後面 (dp[2]+1 = 2)
  - j:3 (5) >= 3
  dp[4] = 2

# i: 5, nums[5]=7
  - j:2 (2) < 7 -> len 2
  - j:3 (5) < 7 -> 接在 5 後面 (dp[3]+1 = 3)
  - j:4 (3) < 7 -> 接在 3 後面 (dp[4]+1 = 3)
  Max is 3.
  dp[5] = 3
```

最終 `dp` 陣列會是 `[1, 1, 1, 2, 2, 3, 4, 4]`。
最大值為 4。

## Solution

### Time O(N^2), Space O(N)

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # dp[i] 代表以 nums[i] "結尾" 的 LIS 長度
        # 初始化為 1，因為每個元素自己本身就是一個長度為 1 的 LIS
        dp = [1] * len(nums)
        
        # 外層迴圈 i：我們現在要決定 nums[i] 能接在誰後面
        for i in range(len(nums)):
            # 內層迴圈 j：回頭看所有在 i 之前的人
            for j in range(i):
                # 如果 nums[i] 比 nums[j] 大，代表可以接在 j 後面
                if nums[i] > nums[j]:
                    # 我們想要找 "能接的人當中，原本隊伍最長的"
                    # dp[i] 更新為 max(自己原本的長度, 接在 j 後面的長度)
                    dp[i] = max(dp[i], dp[j] + 1)
        
        # 答案是 dp 陣列中的最大值（不一定是以最後一個元素結尾）
        return max(dp)
```

## ⚠️ 常見陷阱 (Trap)

1.  **回傳值不是 `dp[-1]`**：最長遞增子序列不一定以最後一個元素結尾（例如 `[1, 3, 6, 7, 9, 4, 10, 5, 6]`，最後一個元素可能很小），所以要回傳 `max(dp)`。
2.  **初始值**：每個元素至少可以自成一個長度為 1 的子序列，所以 `dp` 陣列初始化為 1。
