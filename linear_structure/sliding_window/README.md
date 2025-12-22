# Sliding Window 的標準模板

絕大多數「變動長度」的 Sliding Window 題目，結構都是長這樣：

```python
# 黃金模板
l = 0
for r in range(len(nums)):
    # 1. 進：讓 nums[r] 進入視窗，更新狀態
    current_state += nums[r]
    
    # 2. 出：當視窗狀態「不符合條件」時，縮減左邊界 (While loop)
    while (condition_is_invalid):
        # 移除 nums[l] 的影響
        current_state -= nums[l]
        l += 1  # 慢慢縮小視窗
    
    # 3. 算：更新答案 (這時候視窗是合法的)
    ans = max(ans, r - l + 1)

```


### 比較表

| 特性 | 標準 Sliding Window (大多數題目) | LeetCode 121 (股票買賣) |
| --- | --- | --- |
| **右指標 (Right)** | `for r in range(...)` | `for r in range(...)` |
| **左指標 (Left) 移動方式** | **While 迴圈** (`while condition: l += 1`) | **If 判斷** (`if lower: l = r`) |
| **移動邏輯** | 視窗太大或不合規，**慢慢吐出**左邊元素 | 發現更好的起點，**直接拋棄**舊起點 |
| **代表題目** | LeetCode 3 (無重複最長子串)<br>LeetCode 209 (最小長度子陣列) | LeetCode 121 (買賣股票) |
