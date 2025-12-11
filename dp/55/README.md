# LeetCode 55. Jump Game

## 三種解法
| Solution | Time Complexity|
|-|-|
| Bottom-UP DP | O(N^2) |
| Top-Down DP | O(N^2)|
| Greedy Max-Reach | O(N) |



### Bottom-UP DP

DP represents the reachability of each index.

```python
n = len(nums)
dp = [False] * n
dp[0] = True



for i in range(n):
    for j in range(0, i):
        if dp[j] == True and j + nums[j] >= i:
            dp[i] = True
            break


return dp[n-1]
```


### Greedy
只有在 idx<=max_reach 時，才代表該idx是可觸及的

```python
# Greedy
max_reach = 0

for idx, n in enumerate(nums[:-1]):
    if idx <= max_reach:
        max_reach = max(max_reach, idx + n)



return max_reach >= len(nums) -1

```