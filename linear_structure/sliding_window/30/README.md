# LeetCode 30 - Substring with Concatenation of All Words

## UMPIRE Method

### U - Understand
- 在給定的 s 字串中找到所有由 words 內所有單字「拼接」而成的子字串，並回傳它們的起點索引。


### M - Match
- HashMap: 為了要比對字串是否是由 words 內所有單字組成，我們可以建立兩個 hashmap, 一個用來記錄 words 內所有單字的頻率，另一個用來記錄當前子字串內的單字頻率。
- Sliding Window: 使用滑動窗口來解決這個問題，每次移動的是固定的單字長度。
- 起始點偏移：由於需要考慮所有可能的單字切分結果，所以我們必須要從 0 ~ L-1 來遍歷所有可能的起始位置。

### P - Plan
- 邊界與防呆： 
  - 當 s 或 words 為空時可以直接回傳空陣列 []
  - 當 s 比 words 拼接而成的字串長度短時也回傳空陣列 []
- Sliding Window 實作：
  - 初始化 l, r 指標。 
  - r 每次移動 L 的距離，直到 r + L 到達 s 的右邊界，去判斷 r : r+L 之間的單字是否在 HashMap 中.
  - 如果不在，代表我們要縮減邊界，l = r。
  - 如果在，代表我們要增加邊界，r = r + L，並且更新 HashMap 中的頻率。如果頻率超過目標頻率，代表我們要縮減左邊界，把最舊的合法單字從 HashMap 中移除，直到頻率符合目標頻率為止。
- 利用 match_count 來記錄目前的合法單字數量，當 match_count == num_words 時，代表我們找到一個合法的子字串，將 l 加入結果中。


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


#### Golang
```go
func findSubstring(s string, words []string) []int {
	if len(s) == 0 || len(words) == 0 {
		return []int{}
	}

	res := []int{}
	numWords := len(words)
	wordLen := len(words[0])
	targetLen := numWords * wordLen

	if len(s) < targetLen {
		return res
	}

	// 建立基準的 words 頻率 map
	wordsFreq := make(map[string]int)
	for _, word := range words {
		wordsFreq[word]++
	}

	// 起始點偏移：0 到 wordLen - 1
	for i := 0; i < wordLen; i++ {
		currFreq := make(map[string]int)
		count := 0
		l := i
		r := i

		for r+wordLen <= len(s) {
			word := s[r : r+wordLen]
			r += wordLen

			// 如果截取出來的單字在目標 map 中
			if _, exists := wordsFreq[word]; exists {
				currFreq[word]++
				count++

				// 若窗口內該單字頻率超過目標頻率，開始縮減左邊界
				for currFreq[word] > wordsFreq[word] {
					leftWord := s[l : l+wordLen]
					currFreq[leftWord]--
					count--
					l += wordLen
				}

				// 若有效單字總數達到目標數量，記錄起始位置
				if count == numWords {
					res = append(res, l)
				}
			} else {
				// 單字不在目標中，中斷累積，重置窗口與計數
				currFreq = make(map[string]int) 
				count = 0
				l = r
			}
		}
	}

	return res
}
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
