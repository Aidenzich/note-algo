# 92. Reverse Linked List II

[https://leetcode.com/problems/reverse-linked-list-ii/](https://leetcode.com/problems/reverse-linked-list-ii/)

## Classify

*   **Linked List**
*   **In-Place Reversal**

這題是經典的 Linked List 操作題。第一眼看到 "Reverse" 和 "Linked List"，直覺想到需要調整指標方向。因為是 "Reverse II" (局部反轉)，所以需要定位反轉區間的起點和終點。

## Line of thought

核心哲學是 **「抽牌插入」(Extract and Insert)**。

我們不需要真的把 list 切斷再接回去，而是可以想像成：
固定住反轉區間的前一個節點 (`pre`)，然後不斷把 `curr` (反轉區間的第一個節點) 後面的那張牌 (`next`) 抽出來，插到 `pre` 的後面。

*   **Dummy Node**: 因為 `left` 可能為 1 (從頭開始反轉)，為了統一邏輯，我們需要一個 `dummy` node 指向 `head`。
*   **變數定義**:
    *   `pre`: 永遠指向反轉區間的**前一個**節點。它是不動的錨點。
    *   `curr`: 剛開始是反轉區間的**第一個**節點。在反轉過程中，它會不斷被往後推，直到變成區間的最後一個節點。
    *   `next`: 這是我們要「移動」的節點。每次迴圈都把 `curr` 後面的這個 `next` 搬到 `pre` 後面。

### Concrete Trace

Input: `1 -> 2 -> 3 -> 4 -> 5`, `left = 2`, `right = 4`
Dummy -> 1 -> 2 -> 3 -> 4 -> 5

初始化:
1.  走到 `left - 1` 的位置設為 `pre`。這裡是 `1`。
2.  `pre` 的下一個是 `curr`。這裡是 `2`。

我們需要執行 `right - left = 2` 次搬運操作。

**Round 1:**
目標：把 `3` (`next`) 搬到 `1` (`pre`) 後面。
目前的鏈: `1(pre) -> 2(curr) -> 3(next) -> 4 -> 5`

1.  `curr.next = next.next` (把 2 接到 4)
2.  `next.next = pre.next` (把 3 接到 2)
3.  `pre.next = next` (把 1 接到 3)

結果: `1 -> 3 -> 2(curr) -> 4 -> 5`
(注意 `curr` 還是指向 2，但 2 已經往後移了)

**Round 2:**
目標：把 `4` (`next`) 搬到 `1` (`pre`) 後面。
目前的鏈: `1(pre) -> 3 -> 2(curr) -> 4(next) -> 5`

1.  `curr.next = next.next` (把 2 接到 5)
2.  `next.next = pre.next` (把 4 接到 3)
3.  `pre.next = next` (把 1 接到 4)

結果: `1 -> 4 -> 3 -> 2(curr) -> 5`

迴圈結束，回傳 `dummy.next`。

```text
Initial:
D -> 1(pre) -> 2(curr) -> 3(next) -> 4 -> 5

Step 1 (Move 3):
D -> 1(pre) -> 3 -> 2(curr) -> 4(next) -> 5

Step 2 (Move 4):
D -> 1(pre) -> 4 -> 3 -> 2(curr) -> 5
```

## Solution

### Time O(N), Space O(1)

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        # 1. 走到反轉區間的前一個位置 (pre)
        pre = dummy
        for _ in range(left - 1):
            pre = pre.next
            
        # 2. 設定 curr (反轉區間的第一個節點)
        curr = pre.next
        
        # 3. 開始執行 "抽牌插入"
        # 我們需要搬動 right - left 個節點
        for _ in range(right - left):
            next_node = curr.next       # 抓住要移動的節點 (next)
            
            # left, 2, 3, 4
            #          ^
            #         curr
            # left, [3], 2, 4
            #               ^
            #              curr
            # left, [4], 3, 2
            curr.next = next_node.next
            next_node.next = pre.next   
            pre.next = next_node
            
            # 物理意義：
            # curr 就像是輸送帶上的貨物，一直往後送
            # next 是被抓出來放到最前面的貨物
            # pre 是輸送帶的起點，永遠指向目前排好的隊伍頭
            
        return dummy.next
```

⚠️ 常見陷阱 (Trap):
*   **`left == 1`**: 如果沒有 `dummy` node，處理 `head` 變動會很麻煩。
*   **指標順序**: 在「抽牌插入」的三個步驟中，順序不能錯，否則會斷鏈。建議畫圖輔助記憶：先接尾巴 (`curr.next`)，再接頭 (`next.next`)，最後接 `pre` (`pre.next`)。
