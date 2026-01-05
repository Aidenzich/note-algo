# 173. Binary Search Tree Iterator

## Link
https://leetcode.com/problems/binary-search-tree-iterator/

## Classify
*   **Simulation of Inorder Traversal**
*   **Controlled Recursion (Stack)**

## Line of thought

*   **U (Understand)**: 題目要求實作一個 Iterator，能按「升序」回傳 BST 的節點值。關鍵限制是記憶體只能使用 O(h)，其中 h 是樹的高度。這意味著我們不能先跑一個完整的遞迴把所有節點存成 List (O(N) memory)，我們必須「模擬」遞迴的過程，並在需要時「暫停」。
*   **M (Match)**: BST 的升序排列正是 **Inorder Traversal (Left -> Root -> Right)**。
*   **P (Plan)**:
    1.  如果用一般的遞迴 Inorder，我們會一路走到最左下的節點，印出，然後退回上一層（Root），再往右走。
    2.  為了模擬這個「暫停」與「繼續」，我們使用 **Stack**。 題目的 Pointer 即 Stack 的頂端節點(stack.pop())
    3.  初始化時：一路往左走到底，沿途將節點壓入 Stack。此時 Stack 頂部就是所有當前未拜訪的節點中「最小」的那個。
    4.  `next()` 被呼叫時：
        *   彈出 Stack 頂部節點（這是當前的 "Left" 或 "Root"）。
        *   因為 Inorder 是 Left -> Root -> Right，處理完這個節點後，如果有 **Right Child**，我們必須轉向右邊。
        *   但是在把右小孩加入前，記得這個右小孩本身也是一個子樹的根，所以要對它執行一樣的「一路往左走到底」操作。

### Concrete Trace
假定樹結構： `[7, 3, 15, null, null, 9, 20]`
```text
       7
      / \
     3   15
        /  \
       9    20
```

1.  **Init(7)**:
    *   Push 7 -> Stack: `[7]`
    *   7.left = 3, Push 3 -> Stack: `[7, 3]`
    *   3.left = null, 停。
    *   **Stack**: `[7, 3]` (Top 是 3)

2.  **next()**:
    *   Pop **3** (回傳值)。
    *   3.right = null (沒有右子樹，無需處理)。
    *   **Stack**: `[7]`

3.  **next()**:
    *   Pop **7** (回傳值)。
    *   7.right = 15。處理 15。
    *   Push 15 -> Stack: `[15]`
    *   15.left = 9, Push 9 -> Stack: `[15, 9]`
    *   9.left = null, 停。
    *   **Stack**: `[15, 9]`

4.  **next()**:
    *   Pop **9**。
    *   9.right = null。
    *   **Stack**: `[15]`

5.  **next()**:
    *   Pop **15**。
    *   15.right = 20。處理 20。
    *   Push 20 -> Stack: `[20]`
    *   20.left = null, 停。
    *   **Stack**: `[20]`

...以此類推。

## Solution

### Time O(1) amortized, Space O(h)

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        # Stack 用來模擬遞迴的 Call Stack
        self.stack = []
        # 初始化：把「最左側路徑」的所有節點都加入 Stack
        self._push_left(root)

    def next(self) -> int:
        # Stack 的頂端永遠是當前的「最小值」（Inorder 的下一個順序）
        node = self.stack.pop()
        
        # Inorder: Left -> Root -> Right
        # 當我們取出 node (Root角色) 後，如果有右子樹，
        # 下一個要被訪問的會是「右子樹中最左邊的節點」
        if node.right:
            self._push_left(node.right)
        
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0

    def _push_left(self, node):
        # 輔助函式：將一個節點及其所有左後代推入 Stack
        # 就像是用刀子一路切到最左邊
        while node:
            self.stack.append(node)
            node = node.left
```

## Traps & Notes
*   ⚠️ **常見陷阱 (Trap)**: 面試時最直覺的作法是先跑一次 DFS 把所有節點存到 `Array` 中。雖然 Time 也是 O(N)，但 Space 會是 O(N) 而非 O(h)。題目若強調記憶體限制，Array 解法會不合格。
*   **Amortized Analysis**: 雖然 `next()` 裡的 `_push_left` 包含一個 while loop，但在整個遍歷過程中，每個節點只會被 push 若且唯若一次，所以平均時間複雜度是 O(1)。