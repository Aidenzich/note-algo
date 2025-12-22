# 239. Sliding Window Maximum
## Line of Thought
這如果直接使用標準的 Sliding Window 模板，時間複雜度會是 $O(N \times k)$，因為每次都要花 O(k) 的時間去掃描整個視窗找最大值而導致超時。

因此這題需要直接維護一個 Double Ended Queue (Deque) 來儲存**Window 內，可能成為最大值的 index**，並且確保 `dq[0]` 永遠是當前的最大值 index，這樣可以快速找到最大值。
一樣，我們使用 `for r in range(len(nums))` 來控制右指標，並使用 `l = r - k + 1` 來控制左指標(由於視窗大小為 k)。
如果新來的 `nums[r]` 比隊列尾巴大，那尾巴永遠不可能成為最大值了，因此我們可以從尾巴開始 pop



## Solution
### Time  $O(N \times k)$
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        n = len(nums)

        # left 從 0 開始，直到剩下的元素不足 k 個為止
        for left in range(n - k + 1):
            # 定義視窗範圍：從 left 到 left + k
            window = nums[left : left + k] 
            
            # 這裡就是效能殺手
            # 每次都要花 O(k) 的時間去掃描整個視窗找最大值
            max_val = max(window)
            
            result.append(max_val)
            
        return result
```


### Time  $O(N)$
```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        res = []
        

        for r in range(len(nums)):
            l = r - k + 1
            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if dq[0] < l:
                dq.popleft()

            if l >= 0:
                res.append(nums[dq[0]])


        return res
```