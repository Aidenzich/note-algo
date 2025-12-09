


## 如何選擇 left == right 和 left < right
簡單來說，選擇哪種寫法，取決於你的 **「搜尋區間定義」** 以及 **「當條件不滿足時，你是如何移動邊界 (`left` 和 `right`) 的」**。


### Golden Rule: 看 `right` 怎麼動

1.  **如果你寫 `right = mid - 1`**：代表 `mid` 已經被檢查過且排除了，那麼就用 **`while left <= right`**。
2.  **如果你寫 `right = mid`**：代表 `mid` 可能是答案，不能排除，那麼就必須用 **`while left < right`**。


#### 1\. 模式一：`while left <= right` (找特定值)

這是最傳統的寫法，通常用於 **「在陣列中尋找某個具體的 Target 值」**。

  * **思維模式**：搜尋區間是 **閉區間 `[left, right]`**。
  * **為什麼有 `=`**：因為當 `left == right` 時，那個元素 **還沒被檢查過**，我們必須進入迴圈檢查它是不是 Target。
  * **邊界更新**：
      * 既然我們會在迴圈內檢查 `if nums[mid] == target`，如果不相等，代表 `mid` 肯定不是答案。
      * 所以下次搜尋直接跳過 `mid`：
          * `left = mid + 1`
          * `right = mid - 1` **(關鍵在這裡)**
  * **結束條件**：找不到時，`left` 會超過 `right`，迴圈結束，回傳 `-1`。

**程式碼模板：**

```python
# 範例：LeetCode 704. Binary Search
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1  # mid 肯定不是，勇敢減 1
```


#### 2\. 模式二：`while left < right` (找邊界/極值)

這通常用於 **「尋找最小、最大、峰值」** 或 **「滿足某條件的第一個位置」**（例如我們剛剛解的旋轉陣列最小值）。

  * **思維模式**：搜尋區間是 **左閉右開 `[left, right)`** 的概念，或者是我們在 **「縮小範圍」** 直到剩下最後一個元素。
  * **為什麼沒有 `=`**：因為我們的目標是讓 `left` 和 `right` 收縮到同一個點，當 `left == right` 時，**剩下的那個就是答案**，不需要再進迴圈判斷。
  * **邊界更新**：
      * 當我們發現 `mid` 滿足某種條件（例如 `nums[mid] < nums[right]`），這意味著 `mid` **可能是答案**，我們不能把它剔除。
      * 所以：
          * `right = mid` **(關鍵：保留 mid，不能減 1)**
          * `left = mid + 1` (另一邊通常可以勇敢加 1)
  * **風險提示**：如果你在這裡用了 `<=` 且 `right = mid`，當只剩兩個元素時（例如 `[0, 1]`），`mid` 會算出 `0`，`right` 更新為 `0`，`left` 還是 `0`，就會陷入 **無窮迴圈**。

**程式碼模板：**

```python
# 範例：LeetCode 153. Find Minimum in Rotated Sorted Array
while left < right:
    mid = (left + right) // 2
    if nums[mid] > nums[right]:
        left = mid + 1   # mid 肯定不是最小值，勇敢加 1
    else:
        right = mid      # mid 可能是最小值，必須保留！
        
# 迴圈結束時 left == right，直接回傳 nums[left]
return nums[left]
```



### 快速對照表

| 特徵 | `while left <= right` | `while left < right` |
| :--- | :--- | :--- |
| **用途** | 找精確的 `target` 值 | 找模糊的邊界、極值、最小值 |
| **右邊界更新** | `right = mid - 1` | `right = mid` |
| **回傳時機** | 迴圈內 `return mid` | 迴圈外 `return nums[left]` |
| **最後狀態** | `left > right` (區間空了) | `left == right` (剩一個候選人) |
| **無窮迴圈風險** | 低 | 高 (如果寫了 `<=` 配 `right=mid`) |

