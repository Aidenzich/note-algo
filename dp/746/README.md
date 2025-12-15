# 746. Min Cost Climbing Stairs

## Line of thought
dp 用來存到達目標的最小成本，
一個位置的成本會有兩種可能性：
- `dp[i-1] + cost[i-1]`
- `dp[i-2] + cost[i-2]`

取最小值即可



## Solution
```python
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Everytime can move 1 or 2 step
        # You can start from index 0 or index 2
        n = len(cost)
        dp = [0] * (n+1)
        

        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
            
        return dp[-1]
```