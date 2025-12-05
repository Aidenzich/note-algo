# 61. Rotate List

## Solution
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        old_tail = head
        length = 1
        while old_tail and old_tail.next:
            old_tail = old_tail.next
            length += 1

        k = k % length
        if k == 0:
            return head

        old_tail.next = head
        new_tail = head
        for _ in range(length - 1 -k):
            new_tail = new_tail.next

        new_head = new_tail.next # 該node 的next會被移動到變成 new head
        new_tail.next = None

        return new_head
```