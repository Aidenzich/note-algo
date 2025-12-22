# 121. Best Time to Buy and Sell Stock

## Line of thought
這題的目標是找出最大獲利，也就是要找到一個「買入點」和一個「賣出點」，使得價差最大。限制是只能交易一次，且必須「先買後賣」。

雖然直覺上是貪婪算法（紀錄最低價），但我將其視為 **Sliding Window** 的模型來處理，這樣更能統一解題邏輯：

1. **定義指標與狀態**：`left` 代表當前視窗內的「最佳買入點」，`max_profit` 紀錄最大差值。
2. **擴展右邊界**：利用 `for loop` 控制 `right` 指標（代表當前的賣出時機），遍歷每一天的價格。
3. **收縮/重置左邊界**：利用 `if` 判斷 `prices[right] < prices[left]`。如果當前價格比買入價還低，說明找到更低的成本，直接將 `left` 移動到 `right`（重置視窗起點），否則就計算並更新利潤。
    - 補充，在更進階的 Sliding Window 圖例中，我們會使用 while loop 來控制 left 指標的移動




## Solution
### With minPrice
```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minPrice = float("inf")
        maxProfit = 0
        for p in prices:
            if minPrice > p:
                minPrice = p
            
            maxProfit = max(maxProfit, p - minPrice) 

        
        return maxProfit

```

### With Sliding Window

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, left = 0, 0        

        for right in range(1, len(prices)):
            p = prices[right]
            if prices[left] > p:
                left = right
            
            max_profit = max(p - prices[left], max_profit)

        return max_profit
```
        