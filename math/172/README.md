# 172. Factorial Trailing Zeroes

## Line of thought
這道題要求計算 **$n!$ 結尾零的個數**。這個問題的答案並不是簡單地計算 $n!$ 本身，因為 $n$ 很大時 $n!$ 會迅速變得非常龐大。
1. **結尾零**的產生是因為因數 **10** 的存在。而 10 是由 **$2 \times 5$** 組成的。
2. 因此，計算 $n!$ 中結尾零的個數，等價於計算 $n!$ 的**質因數分解中，因數 5 和因數 2 兩者配對的次數**。

    $$
    n! = 2^a \cdot 5^b \cdot \text{other primes}
    $$

3. 結尾零的個數為 $\min(a, b)$, 因為最大的配對數取決於因數 5 跟 因數 2 之中的最小數量
4. 我們只需要考慮因數 5，因為在 $n! = 1 \times 2 \times 3 \times \dots \times n$ 的乘積中，因數 2 出現的頻率遠高於因數 5。對於任何 $n \ge 5$，因數 2 的總數 ($a$) 總是**大於或等於**因數 5 的總數 ($b$)。
    * **因數 2** 每隔 2 個數字出現一次 ($2, 4, 6, 8, \dots$)。
    * **因數 5** 每隔 5 個數字出現一次 ($5, 10, 15, 20, \dots$)。



因此，我們只需要計算 **$n!$ 的質因數分解中因數 5 的總個數 $b$** 即可，即 $b = \text{number of trailing zeros}$。

### 如何計算因數 5 的個數？

因數 5 來自於 $n!$ 中所有 5 的倍數：

1.  **來自 5 的倍數**：每個 $5, 10, 15, \dots$ 等數字都至少貢獻一個因數 5。這些數字的個數是 $\lfloor n/5 \rfloor$。
2.  **來自 25 的倍數**：$25, 50, 75, \dots$ 這些數字除了第一個因數 5 之外，還額外貢獻一個因數 5（因為 $25 = 5 \times 5$）。這些數字的個數是 $\lfloor n/25 \rfloor$。
3.  **來自 125 的倍數**：$125, 250, \dots$ 這些數字又額外貢獻一個因數 5（因為 $125 = 5^3$）。這些數字的個數是 $\lfloor n/125 \rfloor$。

以此類推，直到 $5^k > n$ 為止。

因此，結尾零的總個數 $Z$ 為：

$$
Z = \left\lfloor \frac{n}{5} \right\rfloor + \left\lfloor \frac{n}{25} \right\rfloor + \left\lfloor \frac{n}{125} \right\rfloor + \dots
$$

> 這就是著名的 **Legendre's Formula**。

## Solution
### Time Complexity: $O(\log_5 n)$ Space Complexity: $O(1)$
```python
class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        計算 n! 結尾零的個數，相當於計算 n! 中因數 5 的總個數。
        """
        if n < 0:
            return 0
        
        count = 0
        divisor = 5
        
        # 根據 Legendre's Formula 迭代計算：
        # count = floor(n/5) + floor(n/25) + floor(n/125) + ...
        while n >= divisor:
            # 加上 n 中 5 的當前冪次（如 5, 25, 125）的倍數的個數
            count += n // divisor
            
            # 將除數更新為 5 的下一個冪次
            divisor *= 5
            
        return count
```

* **時間複雜度：** $O(\log_5 n)$。迴圈執行的次數取決於 $n$ 能被 5 連續除以多少次，這個次數非常小。
* **空間複雜度：** $O(1)$。只使用了常數額外的空間。