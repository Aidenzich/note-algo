# 82. Remove Duplicates from Sorted List II

https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

## Classify

Linked List, Sentinel Node (Dummy Node), Two Pointers

## Line of thought

這題的關鍵在於我們要刪除「所有」重複的節點，而不僅僅是留下一份。這意味著如果有一連串的 `3->3`，這兩個 `3` 都要消失。

我們一樣使用一個 **Dummy Node (Sentinel)** 指向 `head`，這樣我們才能優雅地處理「頭部消失」的情況。

我們需要兩個指標：
1.  `pre`: 指向「確定不重複」的最後一個節點。一開始是 `dummy`。
2.  `head` (或 `cur`): 用來掃描當前的節點，尋找重複區段。

當我們站在 `pre` 看著後面的 `head` 時，我們要檢查 `head` 和 `head.next` 是否值相同：

*   **如果發現重複 (`head.val == head.next.val`)**：
    *   我們要一路往後跳，直到跨過所有值相同的節點。
    *   找到重複的邊界後，我們直接把 `pre.next` 接到 `head.next`。
    *   **注意**：這時候 `pre` **不能動**！因為我們剛接過來的新鄰居（`head.next`）可能又是另一個重複區的開始（例如 `3->3->4->4`，刪掉 `3` 後變成 `...->4->4`，`4` 也是要刪的）。
*   **如果沒有重複 (`head.val != head.next.val`)**：
    *   表示 `head` 是安全的（它是單獨存在的）。
    *   這時候 `pre` 就可以放心地往前移動一步，變成 `head`。
    *   `head` 繼續往下走。

```text
Example: 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5

Init: dummy -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
      pre      head

1. head(1) != next(2): Safe.
   pre -> 1
   head -> 2

2. head(2) != next(3): Safe.
   pre -> 2
   head -> 3

3. head(3) == next(3): Duplicate detected!
   Loop head until last 3.
   pre(2) points to head.next(4).
   List: 1 -> 2 -> 4 -> 4 -> 5
   pre is still 2. head becomes 4.

4. head(4) == next(4): Duplicate detected!
   Loop head until last 4.
   pre(2) points to head.next(5).
   List: 1 -> 2 -> 5
   pre is still 2. head becomes 5.

5. head(5) next is None. Finish.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        pre = dummy
        
        while head and head.next:
            if head.val == head.next.val:
                # 發現重複，開始跳過所有相同值的節點
                while head.next and head.val == head.next.val:
                    head = head.next
                # 此時 head 指向該重複值的最後一個節點
                # 我們要將 pre 接到 head 的下一個 (跳過整個重複區段)
                pre.next = head.next
                # head 往下移動，準備檢查下一輪
                # 注意：pre 這裡不動，因為新的 head.next 可能還是重複的
                head = head.next
            else:
                # 沒有重複，pre 和 head 都安全前進
                pre = pre.next
                head = head.next
                
        return dummy.next
```
