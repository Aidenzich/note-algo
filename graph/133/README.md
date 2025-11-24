# 133. Clone Graph

[link](https://leetcode.com/problems/clone-graph/)

## Classify
![alt text](<imgs/133.png>)
這題屬於 Graph 遍歷的問題，需要 Deep Copy 一個無向圖。因為圖中可能存在環 (Cycle)，所以必須使用 Hash Table (Dictionary) 來記錄已經複製過的節點，避免無窮迴圈。可以使用 DFS 或 BFS 來實作。

## Line of thought
這題的核心在於如何 "Deep Copy" 一個圖。Deep Copy 意味著我們不僅要複製節點的值，還要複製節點之間的連接關係 (Neighbors)，而且這些 Neighbors 也必須是新的節點。

1.  **Mapping (Visited Record)**:
    - 我們需要一個機制來對應 "原圖節點" 和 "新圖節點"。
    - 使用一個 Hash Map `visited`，key 是原節點 (或是原節點的 val，因為題目說 val 唯一)，value 是新建立的對應節點。
    - 如果一個節點已經在 `visited` 中，代表它已經被複製過 (或是正在被複製中)，我們直接回傳 `visited` 中的那個新節點即可，這樣可以處理環的問題。

2.  **DFS Approach**:
    - 定義一個遞迴函數 `dfs(node)`，它的功能是 "回傳 node 的 Deep Copy"。
    - **Base Case**: 如果 `node` 是 None，回傳 None。
    - **Check Visited**: 如果 `node.val` 已經在 `visited` 中，直接回傳 `visited[node.val]`。
    - **Create Node**: 建立一個新節點 `new_node`，值為 `node.val`。
    - **Register**: **立刻**將 `new_node` 放入 `visited` 中 (`visited[node.val] = new_node`)。這步非常重要，必須在處理 neighbors 之前做，否則遇到環的時候會再次進入遞迴導致 Stack Overflow。
    - **Copy Neighbors**: 遍歷 `node.neighbors`，對每個 neighbor 呼叫 `dfs(neighbor)`，並將回傳的結果 append 到 `new_node.neighbors` 中。
    - **Return**: 回傳 `new_node`。

## Solution

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        visited = {}

        def dfs(node):
            if not node:
                return None
            if node.val in visited:
                return visited[node.val]

            
            new = Node(val=node.val)
            visited[node.val] = new

            for n in node.neighbors:
                new_n = dfs(n)
                if new_n:
                    new.neighbors.append(new_n)

            return new

        return dfs(node)
```

## Traps
- **Infinite Loop (Cycle)**: 如果沒有使用 `visited` 記錄已經訪問過的節點，當圖中有環時，DFS 會陷入無窮迴圈。
- **Register Timing**: 必須在遞迴複製 neighbors **之前**就把新節點加入 `visited`。如果等到 neighbors 都複製完才加入，遇到環時 `visited` 裡還沒有這個節點，就會再次遞迴。