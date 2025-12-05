```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        q = deque([root])

        while q:
            size = len(q)

            for i in range(size):
                node = q.popleft()
                
                if i < size - 1: 
                    # 判斷是否是該層的最後一個節點
                    # 如果不是，則將該節點的 next 指向 queue 的第一個節點
                    # 因為 queue 現在剩下的就是右邊的鄰居
                    node.next = q[0]
        
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

        return root

```