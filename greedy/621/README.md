# 621. Task Scheduler
https://leetcode.com/problems/task-scheduler/



## Line of thought
這題的核心限制在於 **「出現頻率最高的任務」**。為了讓該任務滿足冷卻時間 `n`，我們被迫將它們隔開，這會形成一個「最小骨架」。

我們可以把這想像成一個**填空遊戲**：

1.  **找出瓶頸（頻率最高的任務）**：
    假設 `A` 是頻率最高的任務，出現了 `max_freq` 次。
    我們必須先把 `A` 排好，且每個 `A` 之間至少要有 `n` 個間隔。

2.  **建立骨架 (Skeleton)**：
    想像我們將 `A` 擺在每一列的開頭，每一列長度為 `n + 1` (1個任務 + n個冷卻/其他任務)。
    我們會形成 `max_freq - 1` 個完整的區塊。之所以是減 1，是因為**最後一個 A 不需要後面的冷卻時間**。
    
    ```text
    例如：A: 3次, n: 2
    區塊 1: A _ _  (長度 3)
    區塊 2: A _ _  (長度 3)
    最後:   A      (長度 1)
    ```

3.  **填入其他任務**：
    *   **Case 1: 空位夠多 (骨架限制了長度)**
        除了 `A` 以外的任務，我們優先拿去填那些 `_` (空位)。
        如果在填完所有任務後，還有剩下的 `_`，那些就是必須的 `idle` 時間。
        此時總長度就是骨架的長度。
        
        *修正：* 如果有與 `A` 並列最高頻率的任務 (例如 `B` 也出現 3 次)，那它會跟著 `A` 一起擴充骨架的「尾巴」。
        
        ```text
        A: 3, B: 3, n: 2
        A B _ 
        A B _ 
        A B    <-- 尾巴變長了
        ```
        公式長度：`(max_freq - 1) * (n + 1) + num_of_max_freq_tasks`

    *   **Case 2: 任務太多 (空位被填滿)**
        如果排完骨架後，我們手上的任務多到把所有 `_` 都填滿了還不夠放。
        這代表什麼？代表我們有足夠多的「雜魚任務」可以拿來穿插冷卻時間。
        只要任務種類夠多，我們一定找得到方法不違反冷卻規則地把它們塞進去 (Interleaving)。
        這時候就不會有任何 `idle`，總時間就是「任務總數」。

4.  **結論**：
    答案取 **max(骨架公式長度, 任務總長度)**。

### Concrete Trace example
```text
Tasks: ["A","A","A","B","B","B"], n = 2

1. Count Freqs: A:3, B:3. 
   max_freq = 3.
   tasks_with_max_freq = 2 (A, B).

2. Calculate Skeleton:
   (max_freq - 1) * (n + 1) + tasks_with_max_freq
   = (3 - 1) * (2 + 1) + 2
   = 2 * 3 + 2 
   = 8

   Visual:
   A B _ 
   A B _ 
   A B 
   (長度確實為 8)

3. Compare with len(tasks) = 6.
   max(8, 6) = 8.
```

## Solution
### Solution 1: Greedy (Math)
#### Time O(N), Space O(1)
*   N 是 tasks 的總數。我們只需要遍歷一次 tasks 建立 hash map (or array)，之後的操作只跟字母數量 (26) 有關，視為 O(1)。

```python
class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 1. 統計每個任務的頻率: counts 紀錄每個字母出現的次數
        counts = [0] * 26
        for t in tasks:
            counts[ord(t) - ord('A')] += 1
        
        # 2. 找出最高頻率 (max_freq)
        max_freq = max(counts)
        
        # 3. 找出有幾個任務並列最高頻率
        # 例如 A:3, B:3, C:1 -> 則 max_freq_count = 2 (A和B)
        max_freq_count = 0
        for c in counts:
            if c == max_freq:
                max_freq_count += 1
                
        # 4. 計算骨架長度
        # 公式：(最高頻率 - 1) * (冷卻長度 + 1) + 並列第一的任務數
        # 解釋：
        # (max_freq - 1): 有幾個「完整」的區塊
        # (n + 1): 每個完整區塊的長度 (任務本身 + 冷卻)
        # max_freq_count: 最後一個區塊的長度 (不需要冷卻，只需把並列第一的任務排完)
        part_1 = (max_freq - 1) * (n + 1)
        part_2 = max_freq_count
        
        calculated_len = part_1 + part_2
        
        # 5. 回傳 max(公式解, 原始長度)    
        return max(len(tasks), calculated_len)
```

### Solution 2: Simulation (Priority Queue)
這是一個比較直觀的模擬方法。我們每一輪嘗試安排 `n + 1` 個時間單位（一個週期）。在每個週期中，我們貪婪地選擇當前剩餘次數最多的任務來執行。

使用 **Max Heap** 來快速取得剩餘次數最多的任務。

#### Time O(N), Space O(1)
雖然使用了 Heap，但因為任務種類最多只有 26 種，所以 Heap 的操作可以視為常數時間 O(log 26) = O(1)。

```python
import heapq

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # 統計每個任務的次數
        counts = {}
        for t in tasks:
            counts[t] = counts.get(t, 0) + 1
        
        # 將次數放入 Max Heap (Python 的 heapq 是 Min Heap，所以存負數)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)
        
        time = 0
        
        # 模擬排程
        while max_heap:
            temp_list = []
            
            # 嘗試填滿一個週期 (n + 1 的長度)
            # 或者直到 heap 空了 (任務都暫時安排完了)
            # i 代表這一個週期目前過了多久
            i = 0
            while i <= n:
                if max_heap:
                    # 取出頻率最高的任務執行
                    count = heapq.heappop(max_heap)
                    
                    # 如果該任務還有剩餘次數 (count 是負數，加 1 代表做了一次)，先暫存在 temp_list
                    # 等這輪週期結束後再放回 heap (因為冷卻時間內不能再被選)
                    if count + 1 < 0:
                        temp_list.append(count + 1)
                
                time += 1
                
                # 如果 heap 空了且 temp_list 也空了，代表所有任務都做完了
                if not max_heap and not temp_list:
                    break
                
                i += 1
            
            # 將冷卻結束的任務放回 heap
            for count in temp_list:
                heapq.heappush(max_heap, count)
                
        return time
```
