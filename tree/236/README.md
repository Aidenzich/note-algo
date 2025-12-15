# 236. Lowest Common Ancestor of a Binary Tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

## Classify

*   **遞迴 (Bottom-up DFS)**：這題要求的是節點之間的關係，而這個關係取決於它們子樹的結構。我們需要讓資訊從葉節點 (leaves) 一路「冒泡」(bubble up) 回根節點 (root)。

## Line of thought

*   **「搜救隊」直覺**：想像樹中的每個節點都是一支搜救隊的隊長。他們的工作是向長官回報：「在我的轄區內有沒有看到 `p` 或 `q`？」
*   **回報規則**：
    1.  **發現目標**：如果我是 `p` 或 `q`，回傳我自己
    2.  **死路**：如果我是 `null`，回傳 `null`
    3.  **整合報告（關鍵時刻！）**：去左邊和右邊搜查。
        *   如果**左邊和右邊**都回報說找到了目標，這代表 `p` 在一邊，`q` 在另一邊。那麼**我就是那個分岔點**。我就是「最近共同祖先」(LCA)。我將「我自己」作為結果向上回報
        *   如果 **只有一邊** 回報了目標，這代表兩個目標都在那一邊（其中一個是另一個的祖先），或者我們目前只找到了其中一個。我直接將那個結果向上傳遞
        *   如果兩邊都沒回報，我就回報無（`null`）

```text
追蹤範例 Trace Example (p=6, q=4)

Tree:
      3
     / \
    5   1
   / \
  6   2
       \
        4

1. Search(3) 搜尋 3
   > L: Search(5) 搜尋 5
     > L: Search(6) 搜尋 6
       -> 匹配 p! 回傳 Node(6)
     > R: Search(2) 搜尋 2
       > L: Search(null) -> 回傳 null
       > R: Search(4) 搜尋 4
         -> 匹配 q! 回傳 Node(4)
       > Reduce(2) 整合 2 的結果
         -> 左=null, 右=4。只有一邊找到。回傳 4
     > Reduce(5) 整合 5 的結果
       -> 左=6, 右=4。兩邊都找到！回傳 Node(5) (找到 LCA 了)
   > R: Search(1) -> ... -> 回傳 null
   > Reduce(3) 整合 3 的結果
     -> 左=5, 右=null。只有一邊找到。回傳 5 (結果向上冒泡)
```

## Solution

### Time O(N) | Space O(H)

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':    
        # 1. Base Case: 找到 p 或 q，或者是死路 (null)
        if not root or root == p or root == q:
            return root
                
        # 2. Divide: 往左右搜尋
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 3. Conquer (整合):
        # 如果左右都有回傳東西，表示 p 和 q 分別在兩邊，那我就是 LCA
        if left and right:
            return root
        
        # 否則，回傳那個有找到東西的一邊 (如果都沒找到就回傳 null)
        return left if left else right
```