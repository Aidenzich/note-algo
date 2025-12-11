# Leetcode 101. Symmetric Tree

https://leetcode.com/problems/symmetric-tree/submissions/1804071343/?envType=study-plan-v2&envId=top-interview-150



這題要特別注意，也是展示了可以改變放到queue中的資料結構



```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        
        dq = deque([(root.left, root.right)])

        
        
        while dq:                        
            left, right = dq.popleft()

            if not left and not right:
                continue

            if not left or not right or left.val != right.val:
                return False



            dq.append((left.left, right.right))
            dq.append((left.right, right.left))
                            
                

        return True                    
```