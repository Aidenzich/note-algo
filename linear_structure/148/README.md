# Leetcode 148. Sort List
## Solution 1.
```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        min_heap = []
        current = head
        
        # 1. 將所有值放入 min-heap
        while current:
            heapq.heappush(min_heap, current.val)
            current = current.next
            
        
        dummy_head = ListNode(-1)
        new_current = dummy_head
        
        # 3. 從 heap pop 出最小值，建立新 list
        while min_heap:
            val = heapq.heappop(min_heap)
            new_current.next = ListNode(val)
            new_current = new_current.next
            
        return dummy_head.next
```


## Solution 2. Space O(1)
```python
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:      
        if not head or not head.next:
            return head
        
        # 1. 分割 (Divide) - 使用快慢指針找到中點        
        slow = head
        fast = head.next
        
        # 當 fast 跑到終點 None 時，slow 會剛好停在 "中點"
        # (因為 fast 從 head.next 出發, slow 會停在 "前半段的最後一個節點")
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
                    
        mid = slow.next
        slow.next = None
        
        # 2. Conquer - 遞迴排序左右兩半
        left_sorted = self.sortList(head)
        right_sorted = self.sortList(mid)
        
        return self.merge(left_sorted, right_sorted)

    
    def merge(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:        
        dummy_head = ListNode(-1)
        tail = dummy_head
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
            
        tail.next = l1 if l1 else l2
        
        return dummy_head.next
```