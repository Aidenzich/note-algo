# Leetcode 134. Gas Station
> 這題是 Greedy 的，因為時間複雜度需要在 O(N) 才能通過測資，需要記住兩個前提：如果sum(gas) < sum(cost) 代表走不完, 如果一個起點可以走完所有點，那他必定可以走完 start~n 

```python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:        
        n, start, tank = len(gas), 0, 0

        # 前提1： 如果sum(gas) < sum(cost) 代表走不完
        if sum(gas) < sum(cost):
            return -1


        # -2, -2, -2, 3, 3
        # -2, -2, 3, 3
        # -2, 3, 3
        # 3, 3

        # 前提2： 如果一個起點可以走完所有點，那他必定可以走完 start~n

        for i in range(n):
            tank += gas[i] - cost[i] 

            if tank < 0:
                start = i + 1                
                tank = 0

        return start
```

