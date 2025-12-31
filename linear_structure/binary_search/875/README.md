# 875. Koko Eating Bananas

## Line of thought
這題我們就是把要尋找的速度 k 用二分法來尋找，把 l 設為 1, r 設為 max(piles)。
透過二分搜尋法，我們可以找到最小的速度 k，使得 koko 可以在 h 小時吃完所有香蕉。
在 while 的一次迴圈中，我們必須看當前的吃香蕉速度 mid 是否可以在 h 小時內吃完所有香蕉，如果可以，代表 mid 太大了，我們可以縮小 r，如果不能，代表 mid 太小了，我們可以放大 l。


## Solution
```python
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # k = 3
        # t = 8
        l, r = 1, max(piles)

        while l < r: 
            mid = (l + r) // 2

            hours_spent = 0
            for p in piles:
                hours_spent += math.ceil(
                    p / mid
                )

            if hours_spent <= h:
                r = mid
            else:
                l = mid + 1

        print(l, mid)
        return l
```