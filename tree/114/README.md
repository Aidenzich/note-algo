# 114. Flatten Binary Tree to Linked List

## Solution
```python
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return
            
            # 如果有左子樹，才需要搬移
            if node.left:
                # 1. 先把原本的右子樹存起來
                old_right = node.right
                
                # 3. 找到現在又子樹(原本的左子樹)的「最右下角」
                tail = node.left.right
                while tail.right:
                    tail = tail.right

                # 3. 把原本的右子樹接上去
                tail.right = old_right

                # 4. 把左子樹搬到右邊
                node.right = node.left
                node.left = None # 記得把左邊清空
                                                                        
            # 5. 繼續往右遞迴 (因為左邊已經被移到右邊了，所以只要處理右邊)
            dfs(node.right)

        dfs(root)
```


```python
class Solution:
    def __init__(self):
        self.prev = None
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        # 1. 先遞迴處理右子樹 (因為 flatten 後右子樹會在最下面)
        self.flatten(root.right)
        
        # 2. 再遞迴處理左子樹
        self.flatten(root.left)
        
        # 3. 處理當前節點 (Root)
        # 把當前節點的右邊指向 prev (上一個處理完的節點)
        root.right = self.prev
        root.left = None # 左邊記得清空
        
        # 4. 更新 prev 為當前節點，給上一層用
        self.prev = root
```