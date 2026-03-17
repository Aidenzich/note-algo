# 146. LRU Cache
[https://leetcode.com/problems/lru-cache/](https://leetcode.com/problems/lru-cache/)

## Classify
Doubly Linked List + Hash Map 結合應用。
需要達到 O(1) 的讀取與寫入，Hash Map 能提供 O(1) 的鍵值對查詢，而 Doubly Linked List 則能提供 O(1) 的節點移動與刪除。
「第一眼」看到 LRU (Least Recently Used) 特性，就意謂著我們要有「順序」概念，且能快速將某個節點「抽出來放到最前面」。能同時滿足「快速尋找」和「隨意拔插調整順序」的資料結構，就是 Hash Map 配 Doubly Linked List。

## Line of thought
*   **直觀邏輯**：
    *   想像我們有一個排隊的隊伍（Doubly Linked List）。最新的、剛被用過的放在隊伍**最右邊（Tail）**，最老、最久沒被用過的放在隊伍**最左邊（Head）**。
    *   **Get**：從 Hash Map 用 key 瞬間找到隊伍中的那個人（Node），把他從原本的位置拔出來，然後插到隊伍最右邊（代表最近剛被用過）。
    *   **Put**：
        1. 如果這個 key 已經在隊伍裡了，一樣把它拔出來更新 value，插到最右邊。
        2. 如果這是一個新的 key：
            * 先把它加到隊伍最右邊。
            * 如果隊伍太長（超過 capacity），我們就把隊伍最左邊（Head 的下一個）的那個人踢出隊伍，同時也從 Hash Map 中刪除他的資料。
    *   為了避免處理邊界條件（例如隊伍空了還要判斷是不是 head or tail），我們需要**兩個啞節點 (Dummy Nodes)**：`head` 與 `tail`。真實資料永遠夾在 `head` 與 `tail` 中間。

*   **具體追蹤**：
    ```text
    capacity = 2
    put(1, 1) -> head <-> (1,1) <-> tail
    put(2, 2) -> head <-> (1,1) <-> (2,2) <-> tail
    get(1)    -> head <-> (2,2) <-> (1,1) <-> tail  # 1被拿出來放到右邊
    put(3, 3) -> 滿了，拔掉最左邊(2,2)，並把(3,3)插到右邊
                 head <-> (1,1) <-> (3,3) <-> tail
    get(2)    -> return -1 (不存在)
    ```

*   **抽象封裝**：
    為了不讓主邏輯太亂，我們只需要實作兩個輔助函式：
    *   `insert(node)`：永遠把 node 插在隊尾（`tail` 之前）。
    *   `remove(node)`：把 node 從當前位置拔除。
    所有的 Get 與 Put 操作，本質上都是這兩個動作的組合！

## Solution
### Time O(1), Space O(N)
N 為 capacity。

```python
class Node:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        # Dummy nodes
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        """將節點從當前位置拔除"""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _insert(self, node: Node):
        """永遠插入到 tail 的前一個位置 (代表最近訪問)"""
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 拔出來放到最新位置
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 已經存在，更新值並移到最新
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert(node)
        else:
            # 新節點，直接加到最新
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._insert(new_node)
            
            # 如果超過容量，移除最舊的 (head.next)
            if len(self.cache) > self.capacity:
                lru = self.head.next
                self._remove(lru)
                del self.cache[lru.key]

```

## ⚠️ 常見陷阱 (Traps & Notes)
*   **刪除 Hash Map 的 Key 需要 Node 裡存有 Key**：在滿載要踢掉最舊節點時，我們是從 Linked List 拿到最左邊的 `lru_node`，這時我們必須從 Hash Map 中 `del cache[lru_node.key]`。這就是為什麼 `Node` 類別裡面一定要存 `key`，不能只存 `val`。
*   **指標更新順序**：在手刻 `_remove` 與 `_insert` 時，最好先拿變數存起來這兩端（如 `prev_node`），避免指錯方向導致斷鏈或無限迴圈。
