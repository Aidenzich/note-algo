# 173. Binary Search Tree Iterator

## Line of thought

`push_left` 確保了我們一定從左邊開始， 又因為stack LIFO 的特性，我們可以確保取出順序必定是： 左 -> 中
而 if node.right 透過把中的右節點加入的機制，確保 左 -> 中 下一個一定是最新放入的「右」


## Solution
```python
# Definition for a binary tree node.
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._push_left(root)

    def next(self) -> int:
        node = self.stack.pop()

        if node.right:
            self._push_left(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
```