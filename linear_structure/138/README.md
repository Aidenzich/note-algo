# 138. Copy List with Random Pointer

## Line of thought
第一輪遍歷建立『舊轉新』的 Map 映射，第二輪遍歷查表連接 next 與 random 指標。

## Solution
```python
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        # 1. 建立 Hash Map: { 舊節點 : 新節點 }
        old_to_new = {}
        
        curr = head
        while curr:
            # 創建對應的新節點 (只複製值，指標先空著)
            old_to_new[curr] = Node(curr.val)
            curr = curr.next
            
        # 2. 再次遍歷，根據 Map 連接指標
        curr = head
        while curr:
            new_node = old_to_new[curr]
            
            # 處理 next 指標
            if curr.next:
                new_node.next = old_to_new[curr.next]
            
            # 處理 random 指標 (最關鍵的一步)
            # 因為我們有 Map，不管 random 指去哪，我們都能查到對應的新節點
            if curr.random:
                new_node.random = old_to_new[curr.random]
                
            curr = curr.next
            
        return old_to_new[head]
```