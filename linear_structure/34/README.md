# 34. Find First and Last Position of Element in Sorted Array
## Solution

### 中心擴散
```python
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                start = mid
                while start > 0 and nums[start - 1] == target:
                    start -= 1
                
                end = mid
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1
                    
                return [start, end]
            
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
                
        return [-1, -1]
```

### 兩次二分搜尋
```python
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:        
        def binarySearch(nums, target, findLeft):
            l, r = 0, len(nums) - 1
            index = -1 
            
            while l <= r:
                mid = (l + r) // 2
                
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    index = mid 
                    # 雖然找到了但繼續望左找
                    if findLeft:
                        r = mid - 1
                    # 雖然找到了但繼續望右找
                    else:
                        l = mid + 1
            return index
        
        left_index = binarySearch(nums, target, True)        
        right_index = binarySearch(nums, target, False)
        
        return [left_index, right_index]
```