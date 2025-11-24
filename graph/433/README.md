# 433. Minimum Genetic Mutation

[link](https://leetcode.com/problems/minimum-genetic-mutation/)

## Classify
這題屬於 Graph BFS 最短路徑問題。我們可以把每一個合法的基因序列看作是 Graph 中的一個節點。如果兩個基因序列只差一個字元，則它們之間有一條邊。題目要求從 `startGene` 變異到 `endGene` 的最小次數，其實就是求這兩個節點在 Graph 中的最短路徑長度。

## Line of thought

我們不用比較 $G$ 與 bank 中所有的字串，我們可以從 Gene 去生成所有可能的下一步突變，然後檢查這些生成的突變是否在 bank 裡。字串長度 $L=8$每個位置有 4 種可能 ('A', 'C', 'G', 'T')對於當前字串 $G$，所有可能的單次突變（鄰居）數量為：$L \times 3 = 8 \times 3 = 24$ 種。這個生成和檢查的過程效率是：$O(L \cdot 4)$，比 $O(L \cdot N)$ 快得多（因為 $N$ 可能很大）。

1.  **BFS Initialization**:
    - 使用一個 Queue 來儲存當前遍歷到的基因序列以及到達該序列所需的變異次數 `(gene, mutations)`。初始時放入 `(startGene, 0)`。
    - 使用一個 Set `bankSet` 來儲存合法的基因庫，這樣查詢是否合法只需 O(1)。
    - 使用一個 Set `visited` 來記錄已經訪問過的基因序列，避免走回頭路造成無窮迴圈。

2.  **BFS Process**:
    - 當 Queue 不為空時，取出隊首元素 `(current_gene, mutations)`。
    - 如果 `current_gene` 等於 `endGene`，則回傳 `mutations`，這就是最短路徑。
    - 嘗試對 `current_gene` 的每一個位置 (共 8 個字元) 進行變異：
        - 每個位置都可以變成 'A', 'C', 'G', 'T' 中的任意一個。
        - 變異後的新基因 `next_gene` 必須滿足以下條件才能加入 Queue：
            1.  `next_gene` 必須在 `bankSet` 中 (題目要求變異後的基因必須合法)。
            2.  `next_gene` 沒有被訪問過 (`not in visited`)。
    - 如果滿足條件，將 `(next_gene, mutations + 1)` 加入 Queue，並將 `next_gene` 加入 `visited`。

3.  **Edge Cases**:
    - 如果 `endGene` 不在 `bank` 中，則永遠無法達成，直接回傳 -1。
    - 如果 Queue 空了還沒找到 `endGene`，回傳 -1。

## Solution

```python
from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bankSet = set(bank)
        if endGene not in bankSet:
            return -1
        
        queue = deque([(startGene, 0)])
        visited = {startGene}
        
        while queue:
            curr, mutations = queue.popleft()
            
            if curr == endGene:
                return mutations
            
            # generate all possible mutations (replace one char)
            for i in range(len(curr)):
                original_char = curr[i]
                for char in "ACGT":
                    if char == original_char:
                        continue
                    
                    next_gene = curr[:i] + char + curr[i+1:]
                    if next_gene in bankSet and next_gene not in visited:
                        visited.add(next_gene)
                        queue.append((next_gene, mutations + 1))
                        
        return -1
```

## Traps
- **End Gene Validity**: 題目特別提到 `endGene` 必須在 `bank` 中才算有效。如果 `endGene` 不在 `bank` 裡，應該直接回傳 -1。
- **Gene Length**: 題目說明基因長度固定為 8，這限制了變異的搜尋空間，不需要處理變長字串。
```