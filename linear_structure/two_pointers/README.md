# Algorithm. Two Points



## Template
```python
n = len(nums)
l, r = 0, n-1
    
while l < r:    
    
    if (condition_for_left): # e.g., current_sum < target
        # 左指標向右移，讓「和」變大
        left += 1
        
    elif (condition_for_right): # e.g., current_sum > target
        # 右指標向左移，讓「和」變小
        right -= 1
        
    else: # (condition_is_met) # e.g., current_sum == target
        # 找到答案！
        # 可能是 return, 或是 left += 1, right -= 1 繼續找下一對
        pass
```



## 使用 Two Pointers 實現「反轉」
    
    
開始之前，先來定義「反轉」這個動作是如何用雙指標實現的。想像一下，我們在要反轉的區段：

1.  **最左邊**放一個 `left` 指標。
2.  **最右邊**放一個 `right` 指標。
3.  只要 `left` 在 `right` 的左邊，就不斷：
      * **交換** `nums[left]` 和 `nums[right]` 的值。
      * 將 `left` 指標向右移動一步 (`left += 1`)。
      * 將 `right` 指標向左移動一步 (`right -= 1`)。

這個過程就像兩隻手從數列的兩端開始，不斷交換物品，直到在中間相遇。

```python
def reverse(nums, start, end):
    left, right = start, end
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
```

#### 反轉整個陣列的步驟拆解
反轉整個陣列 (Reverse the whole array)，這個操作等同於呼叫 `reverse(nums, 0, 6)`。

- **初始狀態**:
    `left = 0 (值=1)`，`right = 6 (值=7)`。
    
    ```text
    [1, 2, 3, 4, 5, 6, 7]
    ↑                  ↑
    left               right
    ```

- **運作步驟**
    1.  交換 `nums[0]` 和 `nums[6]` → `[7, 2, 3, 4, 5, 6, 1]`
    2.  `left` 右移, `right` 左移。`left = 1`，`right = 5`。
    3.  交換 `nums[1]` 和 `nums[5]` → `[7, 6, 3, 4, 5, 2, 1]`
    4.  `left` 右移, `right` 左移。`left = 2`，`right = 4`。
    5.  交換 `nums[2]` 和 `nums[4]` → `[7, 6, 5, 4, 3, 2, 1]`
    6.  `left` 右移, `right` 左移。`left` 在 `3`，`right` 在 `3`。`left < right` 條件不成立，迴圈結束。
- **操作後結果**: `[7, 6, 5, 4, 3, 2, 1]`


#### 結論

所以， `nums.reverse()` 或 `reversed(nums[:k])` 這些簡潔的 Python 語法，它們背後的**運作原理**就是我們剛剛用 `left` 和 `right` **兩個指標 (Two Pointers)** 從兩端向內移動並交換元素的過程。
