# 53. Maximum Subarray

## Line of thought
Use Kaden's algorithm:
- find max_sum
- find min_sum
- find max of max_sum and total_sum - (-min_sum)

解決環狀問題有一個非常巧妙的數學轉化方法，不需要真的去模擬「環狀」連接。我們將情況分為兩種：

1. 最大子陣列沒有跨越邊界： 這就是標準的 Kadane's Algorithm（你已經會寫的部分）。
2. 最大子陣列跨越了邊界： 這意味著原本陣列中間的某一段是「負擔」（總和最小），我們把中間這段「最小子陣列」挖掉，剩下的頭尾兩段加起來就是最大值。



$$
\text{跨越邊界的最大和} = \text{陣列總和 (Total Sum)} - \text{最小子陣列和 (Min Subarray Sum)}
$$

## Solution
```python
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 初始化
        curr_max = 0
        curr_min = 0
        global_max = -float('inf')  # 設為無限小，確保能抓到任何數
        global_min = float('inf')   # 設為無限大
        total_sum = 0
        
        for num in nums:
            # 1. 計算總和
            total_sum += num
            
            # 2. 標準 Kadane 找最大子陣列 (不跨界情況)
            curr_max = max(num, curr_max + num)
            global_max = max(global_max, curr_max)
            
            # 3. 反向 Kadane 找最小子陣列 (為了跨界情況)
            curr_min = min(num, curr_min + num)
            global_min = min(global_min, curr_min)
            
        # 特殊情況處理：
        # 如果整個陣列都是負數 (例如 [-3, -2, -1])
        # 此時 global_max 會是 -1 (最大的單一元素)
        # 但 total_sum - global_min 會是 0 (因為 total_sum 等於 global_min)
        # 我們不能回傳 0 (題目通常要求子陣列不能為空)，所以要直接回傳 global_max
        if global_max < 0:
            return global_max
            
        # 比較：不跨界的最大值 vs (總和 - 跨界的中間最小值)
        return max(global_max, total_sum - global_min)
```