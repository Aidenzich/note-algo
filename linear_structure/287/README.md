# 287: Find the Duplicate Number (尋找重複數)
給定一個包含 $n + 1$ 個整數的陣列 `nums`，其數字都在 $[1, n]$ 範圍內（包括 1 和 $n$），可知至少存在一個重複的整數。假設 `nums` 中 **只有一個重複的整數**，請找出這個重複數。

**範例 1:**
> **Input:** `nums = [1,3,4,2,2]`
> **Output:** `2`

**範例 2:**

> **Input:** `nums = [3,1,3,4,2]`
> **Output:** `3`

### 關鍵限制 (Constraints)

這題的難點在於題目附加的限制條件（通常在面試中會追加）：

1. **不可修改陣列** (Read-only)：不能先 sort，也不能用交換位置的方法。

2. **空間複雜度** $O(1)$：不能使用 Hash Set 或額外的陣列來計數。

3. **時間複雜度優於** $O(n^2)$：不能使用暴力雙迴圈。

## Line of thought

根據鴿籠原理 (Pigeonhole Principle)，有 $n+1$ 個位置，卻只有[$1$ 到 $n$] 這 $n$ 個不同的值，因此一定至少有一個數字是重複的。常見但不符合所有限制的解法：
* **排序法 (Sorting)**: 排序後檢查相鄰元素。 -> **違反限制 1** (修改了陣列) 或 時間 $O(n \\log n)$。
* **雜湊表 (Hash Set)**: 遍歷並存入 Set，若已存在則回傳。 -> **違反限制 2** (空間 $O(n)$)。
* **負數標記法 (Negative Marking)**: 把走過的 index 對應的值變為負數。 -> **違反限制 1** (修改了陣列)。

因此，我們主要探討符合限制的兩種解法：**二分搜尋法** 與 **快慢指針法**。


## Solution

### 解法一：二分搜尋法 (Binary Search)

#### 核心概念

一般的二分搜尋是對「索引 (Index)」進行搜尋，但這裡是對 **「數值範圍** $[1, n]$**」** 進行搜尋。

我們猜測一個數 `mid`，然後計算陣列中有多少個數字 **小於等於** `mid`（設為 `count`）。

* 若 `count > mid`：根據鴿籠原理，重複的數字一定落在 $[1, mid]$ 區間內。

* 若 `count <= mid`：重複的數字一定落在 $[mid+1, n]$ 區間內。

### 步驟圖解

假設 `nums = [1, 3, 4, 2, 2]`，範圍 $[1, 4]$。

1. **範圍** `[1, 4]`，`mid = 2`。

   * 計算 `nums` 中 $\\le 2$ 的個數：有 `1, 2, 2` 共 **3** 個。

   * $3 > 2$ (count > mid)，表示前半段太擠了，重複數在 `[1, 2]`。

2. **範圍** `[1, 2]`，`mid = 1`。

   * 計算 `nums` 中 $\\le 1$ 的個數：只有 `1` 共 **1** 個。

   * $1 \\le 1$ (count <= mid)，表示前半段正常，重複數在 `[2, 2]`。

3. **範圍** `[2, 2]`，找到答案 **2**。

### Python 實作

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 1, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # 計算陣列中有多少數小於等於 mid
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # 鴿籠原理判斷
            if count > mid:
                # 如果小於等於 mid 的數量多於 mid 本身
                # 代表重複數一定在 [left, mid] 區間
                right = mid
            else:
                # 否則在 [mid + 1, right]
                left = mid + 1
                
        return left
```

### 複雜度分析

* **時間複雜度**: $O(n \log n)$。二分搜尋範圍是 $O(\\log n)$，每次都要遍歷陣列 $O(n)$ 來計算 count。

* **空間複雜度**: $O(1)$。

### 解法二：快慢指針法 (Floyd's Cycle Detection) - 最優解

#### 核心概念

這是本題最精妙的解法。我們可以將陣列視為一個 **Linked List**：

* **Index** 代表節點位置。

* **Value** (`nums[i]`) 代表 `next` 指標指向的下一個節點 index。

因為陣列中有重複的數字，這意味著有多個 index 指向同一個 value，這在圖論上會形成一個 **環 (Cycle)**。題目就變成了 **「尋找 Linked List 環的入口點」** (也就是 LeetCode 142 題)。

### 為什麼會有環？

舉例 `nums = [1, 3, 4, 2, 2]`：

* Index 0 -> Value 1 (跳到 Index 1)

* Index 1 -> Value 3 (跳到 Index 3)

* Index 3 -> Value 2 (跳到 Index 2)

* Index 2 -> Value 4 (跳到 Index 4)

* Index 4 -> Value 2 (跳到 **Index 2**)  <-- **回到 Index 2，形成環！**

* 環的入口就是重複數 **2**。

### 演算法步驟

1. **第一階段（相遇）**：

   * 定義 `slow` 和 `fast` 指針，從起點 `0` 出發。

   * `slow` 每次走一步 (`nums[slow]`)。

   * `fast` 每次走兩步 (`nums[nums[fast]]`)。

   * 由於存在環，兩者最終一定會在環內某點相遇。

2. **第二階段（找入口）**：

   * 相遇後，將 `slow` 重置回起點 `0`，`fast` 停在相遇點。

   * 讓 `slow` 和 `fast` 每次都 **各走一步**。

   * 當它們再次相遇時，相遇點即為 **環的入口（重複數）**。

### 數學證明
```graph
起點 (Start)
        |
        | (距離 X)
        |
      入口 (Entry) <-------+
        /                  \
       / (距離 Y)           \ (距離 Z)
      /                      \
    相遇點 (Meeting Point) ---+
```

我們假設：
* 起點到環入口距離為 $X$。
* 環入口到相遇點距離為 $Y$。
* 環的剩餘長度為 $Z$。

當Slow 與 Fast 相遇時：
* Slow 走了 $X + Y$。
* Fast 走了 $X + Y + n(Y + Z)$ (因為一定比較快，要再次相遇必然多繞了 n 圈)。
* 因為 Fast 速度是 Slow 的兩倍：$2(X + Y) = X + Y + n(Y + Z)$
* 化簡得：$X + Y = n(Y + Z) \implies X = (n-1)(Y + Z) + Z$
* 當 $n=1$ 時，$X = Z$。這意味著**從起點走 $X$ 步** 與 **從相遇點繼續走 $Z$ 步** 會剛好在環入口相遇。 

### Python 實作

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 1. 初始化快慢指針
        slow, fast = 0, 0
        
        # 2. 第一階段：尋找相遇點
        while True:
            slow = nums[slow]           # 走一步
            fast = nums[nums[fast]]     # 走兩步
            if slow == fast:
                break
        
        # 3. 第二階段：尋找環入口
        slow = 0                        # slow 回到起點
        while slow != fast:
            slow = nums[slow]           # 兩個都走一步
            fast = nums[fast]
            
        return slow
```

### 複雜度分析

* **時間複雜度**: $O(n)$。第一階段快慢指針追逐是線性的，第二階段找入口也是線性的。

* **空間複雜度**: $O(1)$。只使用了兩個指針變數。

## 5. 總結比較

| **方法** | **時間複雜度** | **空間複雜度** | **修改陣列?** | **備註** | 
| :--- | :---: | :---: | :---: | :--- |
| **排序法** | $O(n \\log n)$ | $O(1)$ 或 $O(\\log n)$ | **是** | 面試中可能被拒絕 | 
| **雜湊表** | $O(n)$ | $O(n)$ | 否 | 空間不符限制 | 
| **二分搜尋** | $O(n \\log n)$ | $O(1)$ | **否** | 符合所有限制，容易想到 | 
| **快慢指針** | $O(n)$ | $O(1)$ | **否** | **最優解**，需要抽象轉化思維 | 

**建議策略：**
面試時，如果一時想不出 $O(n)$ 的快慢指針解法，可以先提出 **二分搜尋法**，這也是一個非常棒的解答。若面試官要求線性時間，再引入 **Linked List Cycle** 的概念。