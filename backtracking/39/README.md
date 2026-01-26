# 39. Combination Sum

## Line of thought
1. Unbounded Knapsack (完全背包變體): 每個數字可以被無限制重複選取，直到總和爆掉。
2. Sorting for Pruning (排序以剪枝):
   - 將 candidates 由小排到大。 
   - 一旦當前數字導致 target < 0，因為後面的數字更大，一定也不合，可以直接 break (剪枝)，省下大量時間。
3. Index Control (索引控制):
   - 因為可以「重複選自己」，所以進入下一層遞迴時，index 傳入 i (停留在原地)。
   - 為了不走回頭路 (避免重複組合如 [2,3] 和 [3,2])，for 迴圈從 start 開始，而不是從 0 開始。

## Solution
```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # 排序是為了讓後面的 "break" 生效 (剪枝優化)
        # 如果不排序，遇到大數字只能 continue，效率較差
        candidates.sort()

        def backtrack(start, curr, remain):
            if remain == 0:
                res.append(curr)
                return 

            for i in range(start, len(candidates)):
                num = candidates[i]

                # 因為已經排序過，如果現在這個數字減下去會 < 0，
                # 那後面更大的數字肯定更不行，直接 break 放棄這條路
                if remain - num < 0:
                    break

                # 可以重複選多次，因此不需要 i+1, 而是使用 i 即可
                backtrack(i, curr + [num], remain - num) 
        
        backtrack(0, [], target)
        return res
```