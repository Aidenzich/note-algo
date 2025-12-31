# 981. Time Based Key-Value Store


## Line of thought
用 hashmap -> key -> List

在 `get` 的時候用 `Binary Search` 加速

## Solution
```python
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.map.get(key)

        if not values:
            return ""

        l, r = 0, len(values) - 1
        res = ""

        while l <= r: 
            mid = (l + r) // 2
            curr_time = values[mid][0]
            curr_val = values[mid][1]
            
            if curr_time <= timestamp:
                res = curr_val
                l = mid + 1
            else:
                r = mid - 1

        return res
```