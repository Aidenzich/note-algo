# Leetcode 106. Construct Binary Tree from Inorder and Postorder Traversal

## Classify
![alt text](../105/imgs/algorithm-Tree.png)
這題是一個樹問題，並且目標是建構一棵樹，因此可以快速的定義到建構樹的執行步驟，並且，我們知道要建構一個 binary tree, 必須要有一個 inorder 決定放置的位置(左右) 並透過 preorder/postorder 來決定哪個點是 root. 因此可能涉及的是樹常見的3種遍歷方式： `Inorder`, `PreOrder`, `PostOrder`.

## Line of thought

這題是使用 **inorder** 與 **postorder** 陣列來建立 binary tree 的基本題型，要記住的概念主要有兩點：

1.  **Postorder** 是用來看「root」在哪裡的，根據 postorder 的順序： **左節點 -> 右節點 -> 父節點**，我們可以知道，在 postorder 陣列中，**最後一個**元素就是我們要找的 Tree 的 root。
2.  **Inorder** 是用來決定「放哪邊」的，我們透過在 postorder 找到的 root, 透過遞迴的順序決定會是放在左邊或右邊。

因此我們透過建立一個 inorder 的 map, 讓我們可以直接透過 root 的 val 定義到它在 inorder 中的位置，從而可以決定下一個 build 的區間範圍。 並且我們使用一個變數 `root_index`，來記錄在 postorder 順序時，root 移動到哪個位置（**注意：Postorder 會從陣列的尾端開始往前移動**）。

而我們 build 的函式則可以定義為輸入是 `l` 與 `r`, 代表從該區間 `[l, r]` 中，建立一個新的 root 節點，並決定好其 left 與 right 節點。 在 `build` 函式中，必須**先遞迴建立右子樹** (`root.right`)，**再建立左子樹** (`root.left`)。

這是因為 `root_index` 是依賴 `Postorder` 的 **[ (左子樹), (右子樹), 根 ]** 順序來「**逆序**」消耗節點的（從 `postorder` 陣列的末尾開始）。`root.right` 的呼叫會負責消耗掉所有 `postorder` 陣列中屬於右子樹的節點，之後 `root_index` 才會剛好指向左子樹的「**結尾**」(即左子樹的根)。



## Solution
### Time $O(N)$, Space $O(N)$
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}

        self.root_idx = len(postorder) - 1

        def build(l, r):
            if l > r:
                return None


            root_val = postorder[self.root_idx]
            root = TreeNode(val=root_val)
            
            
            mid = inorder_map[root_val]
            
            
            self.root_idx -= 1
            # 右 -> 左
            root.right = build(mid+1, r)
            root.left = build(l, mid-1)

            return root

        return build(0, len(inorder)-1)
```