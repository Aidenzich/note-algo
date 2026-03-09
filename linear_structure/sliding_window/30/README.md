# LeetCode 30 - Substring with Concatenation of All Words

## UMPIRE Method

### U - Understand
- 題目給定一個主字串 `s` 和一個字串陣列 `words`。
- 任務是找出 `s` 中所有由 `words` 內所有單字「拼接」而成的子字串之起始索引 (`starting index`)。
- `words` 陣列中的**所有單字長度都相同**。
- 這些單字在子串中的組合順序不限，但每個單字必須**剛好出現一次**，且中間不能有其他字元。

### M - Match
- **Sliding Window (滑動窗口)**：這是一題標準的連續子串問題，需要維護一個固定長度的子字串範圍。
- **Hash Map (計數表)**：需要統計 `words` 陣列中單字出現的頻率，並與目前窗口內的單字頻率進行比較。
- 由於每一個單字長度固定（例如記為 `word_len`），我們可以把 `s` 拆成多個不相交的區塊。這意味著我們只需對固定的偏移量 `0` 到 `word_len - 1` 分別做一次滑動窗口，每一次的步長 (Step) 都是 `word_len`。

### P - Plan
1. **邊界條件檢查**：如果 `s` 或是 `words` 為空，或者目標組合的總長度大於 `s` 的長度，直接回傳空陣列。
2. 計算必要變數：單字數量 `num_words`、單個單字長度 `word_len`、以及目標總長度 `target_len`。
3. 建立一個 Hash Map `words_freq`，用來記錄預期需要的每個單詞出現次數。
4. **外層迴圈**：起點 `i` 從 `0` 到 `word_len - 1`，這代表不同的劃分偏移量。
5. **內層雙指標 (Sliding Window)**：對於每個起點 `i`，初始化左右指標 `l = i` 和 `r = i`，並建立當前視窗的計數器 `curr_freq` 和成功配對的單詞數 `count = 0`。
   - 每次從指標 `r` 取出一個長度為 `word_len` 的單詞。
   - 如果該單詞存在於 `words_freq`：
     - 將 `curr_freq` 中該單詞計數加一，`count` 增加。
     - 若 `curr_freq` 中該單詞的數量超過了 `words_freq` 中預期的數量，代表我們目前視窗內包含了太多該單字：
       - 移動左指標 `l`（每次向右移動 `word_len`），並把移出視窗的單字從 `curr_freq` 扣除、`count - 1`，直到該單詞的頻率重新符合預期。
     - 若 `count == num_words`，表示整個視窗完全匹配，記錄下左指標 `l`。
   - 如果該單詞**不在** `words_freq`：
     - 視窗已經不合法，將 `curr_freq` 清空，`count = 0`，並將左指標直接更新為 `r`（也就是這個無效單詞的下一個起始位置）。

### I - Implement
```python
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s and not words:
            return []

        res = []
        num_words = len(words)
        word_len = len(words[0])
        target_len = num_words * word_len

        if len(s) < target_len:
            return []

        words_freq = Counter(words)

        # 0, 3, 6, 9 ...
        # 1, 4, 7, 10 ...
        # 2, 5, 8, 11 ....
        for i in range(word_len):
            curr_freq = Counter()
            count = 0
            l, r = i, i

            while (r + word_len) <= len(s):
                word = s[r: r+ word_len]
                r = r + word_len

                if word in words_freq:
                    curr_freq[word] += 1
                    count += 1

                    while curr_freq[word] > words_freq[word]:
                        left_word = s[l:l+word_len]
                        curr_freq[left_word] -= 1
                        count -= 1
                        l += word_len

                    if count == num_words:
                        res.append(l)
                    
                else:
                    curr_freq.clear()
                    count  = 0
                    l = r

        return res
```

### R - Review
- 若輸入 `s="barfoothefoobarman"`, `words=["foo","bar"]`，`word_len=3`。外層迴圈遍歷 `i=0, 1, 2`。在 `i=0` 時：
  - 取 `bar` -> 匹配 -> 計數
  - 取 `foo` -> 匹配 -> 計數，`count==2`，加入起點 `l=0`。
  - ...邏輯上是穩健的。
- Hash map 清空的方式：如果是不相干單字，清空後直接把 `l` 追上 `r`，時間上不會有重複計算的浪費，非常有效率。

### E - Evaluate
- **Time Complexity**: $O(n)$。雖然看起來有兩層迴圈以及內部的 `while` 左指標移動，但實質上是：對於每一個步長 `word_len` 所劃分出的單詞序列，右指標和左指標最多各走過一次。總共有 `word_len` 種偏移量，因此總操作次數約為 $\text{word\_len} \times 2 \times \frac{n}{\text{word\_len}} = 2n$，簡化為時間複雜度 $O(n)$，其中 $n$ 為字串 `s` 的長度。
- **Space Complexity**: $O(m \cdot k)$。其中 $m$ 是 `words` 陣列中單詞的數量，$k$ 是單個單詞的長度。雜湊表 `words_freq` 和迴圈內的 `curr_freq` 儲存了不超過 $m$ 個字串元素。
