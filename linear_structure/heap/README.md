# LeetCode Heap (Priority Queue) 實戰複習筆記

## 1. 核心觀念 (Core Concepts)
* **定義**: Heap 是一種完全二元樹 (Complete Binary Tree)。
* **性質**: 
    * **Min-Heap (小頂堆)**: 父節點的值 <= 子節點的值。根節點 (Root) 是全域**最小值**。
    * **Max-Heap (大頂堆)**: 父節點的值 >= 子節點的值。根節點 (Root) 是全域**最大值**。
* **Python 實作**: Python 的標準庫 `heapq` 預設是 **Min-Heap**。

## 2. 時間複雜度 (Time Complexity)
| 操作 | 函數 (Python) | 時間複雜度 | 說明 |
| :--- | :--- | :--- | :--- |
| **Push** | `heapq.heappush(h, val)` | $O(\log N)$ | 插入元素並維持堆性質 |
| **Pop** | `heapq.heappop(h)` | $O(\log N)$ | 移除並回傳堆頂元素 (min/max) |
| **Peek** | `h[0]` | $O(1)$ | 查看堆頂元素 (不移除) |
| **Heapify** | `heapq.heapify(list)` | **$O(N)$** | 將無序陣列轉換為堆 (線性時間，很重要！) |
| **nlargest** | `heapq.nlargest(k, list)` | $O(N \log K)$ | 取最大的 K 個 |
| **nsmallest** | `heapq.nsmallest(k, list)` | $O(N \log K)$ | 取最小的 K 個 |

> **注意**: 很多人誤以為 `heapify` 是 $O(N \log N)$，但實際上是 $O(N)$。如果題目給定一個陣列要建堆，直接 `heapify` 比一個個 `heappush` 快。

## 3. Python `heapq` 實戰技巧

### A. 實作 Max-Heap (大頂堆)
Python 沒有內建 Max-Heap，標準做法是 **「將值取負號」** 存入，取出時再 **「加回負號」**。

```python
import heapq

# 模擬 Max-Heap
nums = [1, 5, 3]
max_heap = [-n for n in nums]  # [-1, -5, -3]
heapq.heapify(max_heap)        # [-5, -1, -3] (Root is -5, real val 5)

# 取得最大值
max_val = -heapq.heappop(max_heap) # 5
```

### B. 存儲複雜物件 (Tuples)
Heap 內的元素如果是 Tuple，Python 會依序比較 Tuple 內的元素 (`item[0]`, `item[1]`, ...)。
常用於存儲 `(priority, task_name)` 或 `(distance, node)`。

```python
h = []
heapq.heappush(h, (5, "write code"))
heapq.heappush(h, (1, "fix bug"))

# 會先彈出 (1, "fix bug") 因為 1 < 5
```

## 4. 常見題型模式 (Common Patterns)

### 模式 1: Top K Elements (前 K 大/小)
這是 Heap 最經典的應用。

* **求「第 K 大」或「前 K 大」**:
    * **解法**: 維護一個大小為 `K` 的 **Min-Heap**。
    * **邏輯**: 遍歷數組，將元素 push 進堆；如果堆的大小超過 K，就 pop 掉最小的（因為我們要留大的）。最後堆裡剩下的就是前 K 大，堆頂是第 K 大。
* **求「第 K 小」或「前 K 小」**:
    * **解法**: 維護一個大小為 `K` 的 **Max-Heap**。
    * **邏輯**: 同理，pop 掉最大的，留下就是最小的。

### 模式 2: Merge K Sorted Lists (合併 K 個排序鏈結串列)
* **核心**: 多路歸併 (Multi-way Merge)。
* **做法**: 將 K 個鏈結串列的「頭節點」放入 Min-Heap。每次 Pop 出最小的節點接到結果鏈表上，然後將該節點的 `next` (如果有的話) Push 回 Heap。
* **複雜度**: $O(N \log K)$，其中 N 是總節點數，K 是鏈表個數。

### 模式 3: Two Heaps (雙堆模式 - 中位數)
用於處理動態數據流的中位數問題。
* **結構**: 
    * `small`: Max-Heap，存儲較小的一半數據。
    * `large`: Min-Heap，存儲較大的一半數據。
* **平衡**: 保持 `len(small) == len(large)` 或 `len(small) == len(large) + 1`。
* **中位數**: 
    * 如果是奇數個：`small` 的堆頂。
    * 如果是偶數個：(`small`堆頂 + `large`堆頂) / 2。

### 模式 4: Dijkstra's Algorithm (最短路徑)
* 雖然是 Graph 演算法，但核心是 Heap。
* **BFS + Priority Queue**: 總是優先處理當前路徑成本最小的節點。
* **存儲**: `(current_dist, node_index)`。

## 5. 經典題目清單 (LeetCode Must Do)

* **基礎操作**: 
    * [215] Kth Largest Element in an Array (必做，Top K 模板)
    * [347] Top K Frequent Elements (頻率統計 + Heap)
* **合併與排序**:
    * [23] Merge k Sorted Lists (Hard 但非常經典)
    * [373] Find K Pairs with Smallest Sums
* **雙堆應用**:
    * [295] Find Median from Data Stream (Two Heaps 經典)
    * [480] Sliding Window Median
* **貪婪策略 (Greedy + Heap)**:
    * [621] Task Scheduler
    * [767] Reorganize String (頻率最高的先排，冷卻處理)

## 6. 應試小提醒 (Tips)
1.  **Lazy Removal (延遲刪除)**: 
    * 有些題目需要從堆中刪除特定非堆頂元素。標準 `heapq` 不支援 $O(\log N)$ 刪除任意元素。
    * **技巧**: 標記該元素為「已刪除」（例如用 Hash Map 記錄刪除次數或 ID），當它浮到堆頂時再真正 Pop 掉。
2.  **複雜度陷阱**: 
    * 不要在迴圈中隨意使用 `list.remove()` 或 `list.index()`，這會把複雜度退化成 $O(N)$。
3.  **如果數據範圍很小**: 
    * 如果元素值範圍有限（如 0-100），有時 Bucket Sort 比 Heap 更快。