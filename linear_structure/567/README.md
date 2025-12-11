# Leetcode 567. Permutation in String


## Solution 1

解題思路： 手動維護 window size, 當 r - l + 1 > window_size 時，代表是 `l++` 的時機


```python
def checkInclusion(self, s1: str, s2: str) -> bool:
    window_size = len(s1)
    c1, c2 = {}, {}

    for i in range(len(s1)):
        c1[s1[i]] = c1.get(s1[i], 0) + 1


    l = 0    
    for r in range(len(s2)):            
        c2[s2[r]] = c2.get(s2[r], 0) + 1

        if r - l + 1 > window_size: # 3
            c2[s2[l]] = c2.get(s2[l], 0) - 1
            if c2[s2[l]] <= 0: 
                del c2[s2[l]]

            l+=1

        if c1 == c2:
            return True

    return False
```

### Solution 2

解題思路： 在 solution 1 中，我們利用的是 dictionary 的比對 c1 == c2 來判斷是否符合條件，這會帶來 $O(N*K)$ 的時間複雜度，但一個更好的寫法是不使用 dictionary 比對，而是透過一個名為 matches 的 state 來判斷是否符合條件，這樣我們能夠移除字典比對的時間複雜度


```python
def checkInclusion(self, s1: str, s2: str) -> bool:    
    c1, c2 = {}, {}
    matches = 0

    for i in range(len(s1)):
        c1[s1[i]] = c1.get(s1[i], 0) + 1

    l = 0        
    for r in range(len(s2)):            
        c2[s2[r]] = c2.get(s2[r], 0) + 1

        # 當 ++ 時，有可能會是 「剛好達標」或是「剛好超標」
        if c2[s2[r]] == c1.get(s2[r], 0):
            matches += 1
        elif c2[s2[r]] == c1.get(s2[r], 0) + 1:
            matches -= 1

        if r - l +1 > len(s1): # 3
            c2[s2[l]] = c2.get(s2[l], 0) - 1

            # 減了後，正好等同於 c1, 這樣 match ++
            if c2[s2[l]] == c1.get(s2[l], 0):
                matches += 1
            elif c2[s2[l]] == c1.get(s2[l], 0) - 1:
                matches -= 1

            l+=1

        if matches == len(c1):
            return True


    return False
```

`matches` 會有四種變化狀態：
| 動作 | 狀態轉變 (State Transition) | matches 變化 |
|-|-|-|
| 加入 char_in | "太少 -> 剛好 (e.g., c2 從 1 變 2)" | matches += 1|
| 加入 char_in | "剛好 -> 太多 (e.g., c2 從 2 變 3)" | matches -= 1|
| 移除 char_out | "太多 -> 剛好 (e.g., c2 從 3 變 2)" | matches += 1|
| 移除 char_out | "剛好 -> 太少 (e.g., c2 從 2 變 1)" | matches -= 1|