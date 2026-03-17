# 460. LFU Cache
[https://leetcode.com/problems/lfu-cache/](https://leetcode.com/problems/lfu-cache/)

## Classify
Two Hash Maps + Doubly Linked Lists 組合。

有了 LRU 的經驗，我們知道要在 O(1) 拔插節點需要 Hash Map (找位置) 配 Doubly Linked List (調順序)。
但 LFU (Least Frequently Used) 複雜度在於：除了考慮「誰最久沒被用 (LRU)」，還要優先考慮「誰的使用頻率最低 (Freq)」。
因此，我們需要對**每一種頻率都維護一個獨立的 LRU 隊伍**。這要求我們有兩個 HashMap 和一個全域指針。

## Line of thought
*   **直觀邏輯**：
    想像我們有好幾個「跑道 (LRU隊伍)」，跑道1給頻率=1的人、跑道2給頻率=2的人...。
    1.  `key_table`: 字典簿。用 key 瞬間找到這名選手 (Node) 屬於哪條跑道，在哪個位置。
    2.  `freq_table`: 各個跑道。知道頻率 freq，就能抓出該頻率的一整條隊伍 (Doubly Linked List)。
    3.  `min_freq`: 指路牌。隨時記錄當下「最低頻率」是多少。客滿踢人時，就順著這個指路牌去 `freq_table[min_freq]` 跑道，把最左邊 (最老) 的人踢掉。

    **機制運作**：
    *   **Get**：在字典簿 (`key_table`) 找到選手，幫他的 freq + 1。然後把他從原本的 freq 跑道拔出來，插進他 `freq+1` 新跑道的最右邊 (最新)。
        * *注意*：如果他原本所在的跑道空了，而且剛好又是 `min_freq` 跑道，記得把 `min_freq` 往上加一 (`min_freq += 1`)。
    *   **Put**：
        1. 如果已經有這位選手了，這跟 Get 幾乎一樣：幫他加頻率，換跑道，順便更新他的數值。
        2. 如果是一位新選手：
            * 如果客滿了，先去 `freq_table[min_freq]` 跑道揪出最老的那位拔掉，同步從字典簿刪了他。
            * 把新選手排進 `freq=1` 的跑道最右邊，更新字典簿。
            * 因為新來了一個人，`min_freq` 毫不猶豫地被降為 `1`。

*   **具體追蹤**：
    ```text
    capacity = 2
    put(1, 1) -> 新增，freq=1。 min_freq = 1
                 freq_table[1]: [ (1,1,f=1) ]
    put(2, 2) -> 新增，freq=1。 min_freq = 1
                 freq_table[1]: [ (1,1,f=1) <-> (2,2,f=1) ]
    get(1)    -> 找到 1，freq 變成 2。拔出並放入 freq=2 跑道。
                 (freq=1 跑道剩 2，min_freq 維持 1)
                 freq_table[1]: [ (2,2,f=1) ]
                 freq_table[2]: [ (1,1,f=2) ]
    put(3, 3) -> 滿載。找出 min_freq=1 跑道的最邊邊 (即 2) 踢掉。新增 3，freq=1。 min_freq = 1
                 freq_table[1]: [ (3,3,f=1) ]
                 freq_table[2]: [ (1,1,f=2) ]
    get(2)    -> return -1
    get(3)    -> 找到 3，freq 變成 2。拔出並放入 freq=2 跑道。
                 (此時 freq_table[1] 空了，且 1 == min_freq，所以 min_freq += 1 變成 2！)
                 freq_table[1]: []
                 freq_table[2]: [ (1,1,f=2) <-> (3,3,f=2) ]
                 min_freq = 2
    ```

## Solution
### Time O(1), Space O(N)
N 為 capacity。我們重複利用一個 `DoublyLinkedList` 類別來降低實作複雜度。

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        # 內建 head, tail 啞節點
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
        
    def add_node(self, node: Node):
        """永遠加在 tail 的前一個位置 (最新)"""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        self.size += 1
        
    def remove_node(self, node: Node):
        """拔掉這個節點"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        self.size -= 1
        
    def pop_front(self) -> Node:
        """拔除 head.next (最舊)"""
        if self.size > 0:
            node = self.head.next
            self.remove_node(node)
            return node
        return None

from collections import defaultdict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_table = {}  # key: Node
        self.freq_table = defaultdict(DoublyLinkedList)  # freq: DoublyLinkedList

    def _update_freq(self, node: Node):
        """處理使用頻率 +1 的流程，並移動這個 Node 到新的 Queue"""
        f = node.freq
        self.freq_table[f].remove_node(node)
        
        # 如果剛拔掉的那個 Queue 是 min_freq 而且空了，min_freq 要晉升
        if f == self.min_freq and self.freq_table[f].size == 0:
            self.min_freq += 1
            
        node.freq += 1
        self.freq_table[node.freq].add_node(node)

    def get(self, key: int) -> int:
        if key not in self.key_table:
            return -1
        
        node = self.key_table[key]
        self._update_freq(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_table:
            # 已經在 Cache 內，更新數值跟使用頻率
            node = self.key_table[key]
            node.val = value
            self._update_freq(node)
        else:
            # 客滿踢人
            if len(self.key_table) >= self.capacity:
                old_node = self.freq_table[self.min_freq].pop_front()
                del self.key_table[old_node.key]
            
            # 建立新 Node
            new_node = Node(key, value)
            self.key_table[key] = new_node
            self.freq_table[1].add_node(new_node)
            self.min_freq = 1 # 被新人拉低平均

### Alternative: Python `OrderedDict` 實戰黑魔法
在標準的 45 分鐘面試中，要從頭手刻出上述 100 行無 bug 的程式碼具有相當難度。如果是使用 Python，內建的 `collections.OrderedDict` 本身就是「Hash Map + Doubly Linked List」的結合體。
你可以用它把程式碼縮減到 30 行以內，藉此減輕實作的時間壓力。

**⚠️ 面試溝通話術 (非常重要)：**
在寫這行程式碼前，**強烈建議**先向面試官確認：
> *"Since realizing the doubly linked list involves a lot of boilerplate code, do you mind if I assume we have a well-tested `DoublyLinkedList` class, or specifically in Python, use `OrderedDict` (which is essentially a hash map implemented with a doubly linked list under the hood) to focus on the core LFU logic first?"*

如果面試官同意，你就可以使用以下濃縮版的解法：

```python
import collections

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        # freq -> OrderedDict(key -> value)
        self.freq_table = collections.defaultdict(collections.OrderedDict)
        self.key_freq = {} # key -> freq

    def get(self, key: int) -> int:
        if key not in self.key_freq:
            return -1
        freq = self.key_freq[key]
        val = self.freq_table[freq][key] # 取出數值
        
        # 從原本頻率的隊伍刪除，移駕到 freq + 1 的新隊伍
        del self.freq_table[freq][key]
        if not self.freq_table[freq] and freq == self.min_freq:
            self.min_freq += 1
            
        self.key_freq[key] = freq + 1
        self.freq_table[freq + 1][key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
            
        if key in self.key_freq:
            # 已經存在，更新值並觸發頻率增加 (利用 get)
            self.freq_table[self.key_freq[key]][key] = value
            self.get(key)
            return

        # 客滿踢人
        if len(self.key_freq) >= self.capacity:
            # OrderedDict 設定 last=False 代表 pop 最左邊(最早)的元素
            old_key, _ = self.freq_table[self.min_freq].popitem(last=False)
            del self.key_freq[old_key]
            
        # 新增
        self.key_freq[key] = 1
        self.freq_table[1][key] = value
        self.min_freq = 1

```
```

## ⚠️ 常見陷阱 (Traps & Notes)
*   **如果 Capacity = 0**：這是一個 LeetCode 愛考的賤 Edge Case。遇到請直接 `return` 忽略，不然它可能會讓你陷入 `del key_table[old_node.key]` 找不到東西的錯誤。
*   **維護 `min_freq` 非常關鍵**：拔掉 Node 後，如果那個 freq 的跑道被清空了，**而且**那個 freq 正好是目前的 `min_freq` 時，代表最低門檻被抬高了，所以要 `self.min_freq += 1`。如果是被剛進來的元素擠掉，則不需要擔心，因為我們會硬把 `min_freq` 設為 1。
