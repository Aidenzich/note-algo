# 143. Reorder List

## Line of thought
這是一份幫你整理好的 `Line of thought`，設計成**面試時可以順暢講出來的邏輯**。它先點出問題的核心，然後由淺入深提出兩個解法。


## Line of thought

這題的目標是將 Linked List 重新排列成「頭接尾、尾接頭...」的交錯形式 (`L0 -> Ln -> L1 -> Ln-1 ...`)。
由於 Singly Linked List 無法直接存取前一個節點（無法從尾巴往回走），我們主要有兩個解題方向：

**解法一：線性表 (Linear Table) - 空間換取時間**
這是最直覺的解法。因為 Linked List 最大的限制是無法隨機存取 (Random Access)，我們可以：
1. 先遍歷一次，將所有節點存入一個 **陣列 (Array/List)** 中。
2. 使用 **雙指針 (Two Pointers)**，一個指頭、一個指尾，向中間移動並重新連接。
3. **注意：** 最後必須將新鏈結串列的尾部設為 `None` 以避免無窮迴圈。

**解法二：尋找中點 + 反轉 + 合併 - 空間最佳化**
如果要達到 O(1) 的空間複雜度，我們可以將問題拆解成三個經典的子問題：

1. **找中點**：使用快慢指針 (Fast & Slow Pointers) 將 List 切成兩半。
2. **反轉後半段**：將後半段的 List 反轉 (Reverse Linked List)，這樣我們就可以順向遍歷後半段了。
3. **合併**：像拉拉鍊一樣 (Merge/Zipper)，將「前半段」與「反轉後的後半段」交替連接。



## Solution
### Space O(N), Time O(N)
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        # 2. 設定左右指針
        left = 0
        right = len(nodes) - 1
                
        # 當左右相交時停止
        while left < right:            
            nodes[left].next = nodes[right]
            left += 1
                        
            if left == right:
                break
                
            nodes[right].next = nodes[left]
            right -= 1
            
        # 此時 left 和 right 重疊在最後一個節點，把它設為 None
        nodes[left].next = None
```

### Space O(1), Time O(N)
```python
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next: return
        
        # --- 步驟 1: 找中點 (快慢指針) ---
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 此時 slow 是中點，將 list 切斷
        second_half = slow.next
        slow.next = None  # 切斷前半段
        
        # --- 步驟 2: 反轉後半段 (標準 Reverse Linked List) ---
        prev = None
        curr = second_half
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # 反轉後，prev 就是後半段的新頭
        
        # --- 步驟 3: 合併兩個 List (拉拉鍊) ---
        first, second = head, prev
        while second: # 後半段通常比較短或一樣長，以它為主
            temp1, temp2 = first.next, second.next
            
            first.next = second
            second.next = temp1
            
            first, second = temp1, temp2
```