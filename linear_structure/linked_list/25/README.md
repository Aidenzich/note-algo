# 25. Reverse Nodes in k-Group

## Line of thought

這題透過 k 找出當前的 group 後進行翻轉即可，這題的難點在於變數控制：
* 視野切換：你同時在看「宏觀結構」（整串 List 的連接）和「微觀結構」（內部 k 個節點的翻轉）。
* 記憶體斷裂風險：只要賦值順序錯一行（例如先改了 `curr.next` 卻沒存 `next`），整條鍊子就斷了，這就是為什麼這題需要這麼多暫存變數 (temp_next, group_end 等)。
* 錨點（Anchors）：最後成功的關鍵，在於用 `group_prev` 和 `group_next` 當作「樁」。先把這一段的前後夾住，中間不管怎麼翻天覆地，只要最後頭尾能對上這兩個樁，就不會出錯。

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:
            # 找當前 group 的終點
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next


            # [1,2,3,4,5]
            #      ^
            group_next = kth.next

            # 開始翻轉
            curr = group_prev.next      # 1
            prev = group_next           # 3            
            temp_curr = curr            
            while temp_curr != group_next:
                temp_next = temp_curr.next  # 1st. 2                2nd. 3
                temp_curr.next = prev       # 1st. 2 -> 3. [1, 3]   2nd. 3 -> 1. [2, 1, 3]
                prev = temp_curr            # 1st. 3 -> 1.          2nd. 1 -> 2
                temp_curr = temp_next       # 1st. 1 -> 2           2nd. 2 -> 3

            group_end = group_prev.next # group_prev.next 其實就是反轉過後的尾巴，先儲存起來讓下一輪使用
            group_prev.next = prev      # 把 prev 接上去, 即把 2 接到 dummy 上

            # 給下一輪
            group_prev = group_end
        
        return dummy.next
```