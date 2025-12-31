# 739. Daily Temperatures


## Line of thought
透過一個 stack(list) 來儲存當前還沒有找到最高溫度的位置 index
透過一直取 stack 的最後一項來更新 Answer




## Solution
```python
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # store prev indices # 目前還沒找到更高溫度的那些日子的『第幾天』

        for day, curr_temp in enumerate(temperatures):
            
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = day - prev_day
            stack.append(day)
            
        return answer
```