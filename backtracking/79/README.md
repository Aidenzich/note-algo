# 79. Word Search

## Link
https://leetcode.com/problems/word-search/

## Classify
Backtracking (Matrix DFS)
這是一道典型的矩陣搜尋題目，需要在二維網格中尋找是否存在連續的路徑構成目標字串。因為需要嘗試所有可能的路徑且不能重複走回頭路，直覺對應 Backtracking (DFS)。

## Line of thought
整體的策略非常直觀：
1.  **遍歷**：掃描整個棋盤 (Board)，尋找每一個可能的「起點」（即與 `word[0]` 相同的格子）。
2.  **擴散**：一旦找到起點，就啟動 DFS 向四個方向（上、下、左、右）探索，看能否依序匹配 `word` 的剩餘字符。
3.  **標記與回溯**：
    *   為了避免走回頭路（例如 A->B->A），我們在進入某個格子時，先將其標記為已訪問（例如改成 '#'）。
    *   當該路徑探索失敗或成功返回後，必須將格子**還原**回原本的字符（Backtracking 的精髓），這樣其他路徑嘗試時才能再次使用該格子。

可以把這過程想像成在走迷宮，但只有腳下的磚塊字符符合 `word` 的順序時才能踩上去。我們沿途撒下麵包屑（`#`）標示走過的路，如果走進死胡同就沿著原路退回，並把麵包屑撿起來。

### Concrete Trace
假設 Board 與 Word 如下：
```text
Board:
[
  ['A', 'B', 'C', 'E'],
  ['S', 'F', 'C', 'S'],
  ['A', 'D', 'E', 'E']
]

Word: "ABCCED"
```

我們從 (0,0) 的 'A' 開始：

```text
1. Start at (0,0) 'A'. Match word[0]. 
   Board[0][0] from 'A' -> '#'.
   Looking for word[1] 'B'. Matches neighbor (0,1).

2. Move to (0,1) 'B'. Match word[1].
   Board[0][1] from 'B' -> '#'.
   Looking for word[2] 'C'. Matches neighbor (0,2).

3. Move to (0,2) 'C'. Match word[2].
   Board[0][2] from 'C' -> '#'.
   Looking for word[3] 'C'. Neighbors: (0,1) is '#', (0,3) is 'E', (1,2) is 'C'.
   Matches neighbor (1,2).

4. Move to (1,2) 'C'. Match word[3].
   Board[1,2] from 'C' -> '#'.
   Looking for word[4] 'E'. Matches neighbor (2,2).

5. Move to (2,2) 'E'. Match word[4].
   ... 繼續直到匹配 word 最後一個字符 'D'。
```

如果在某一步（例如步驟 3）選擇了錯誤的方向（比如假設 (0,3) 是 'C' 但後面走不通），DFS 會回傳 False，這時我們會退回到步驟 3，將 (0,3) 變回原本的字符，然後嘗試下一個可能的鄰居 (1,2)。

## Solution
### Time O(M*N * 3^L), Space O(L)
- M, N 為 Board 長寬，L 為 Word 長度。
- 每個格子都可能是起點。
- DFS 深度最大為 L。除了起點外，每一步最多有 3 個方向可選（不走回頭路）。

```python
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        word_len = len(word)
    
        def dfs(r: int, c: int, k: int) -> bool:            
            # Base Case 1: 整個 word 都匹配成功
            if k == word_len:
                return True
            
            # Base Case 2: 越界
            if r < 0 or r >= M or c < 0 or c >= N:
                return False
            
            # Base Case 3: 字符不匹配或是已經走過的路 ('#')
            if board[r][c] != word[k]:
                return False
            
            # [Mark]: 標記當前格子，避免走回頭路
            original_char = board[r][c]
            board[r][c] = '#'
            
            # [Branch]: 嘗試四個方向
            found = (
                dfs(r + 1, c, k + 1) or  # 下
                dfs(r - 1, c, k + 1) or  # 上
                dfs(r, c + 1, k + 1) or  # 右
                dfs(r, c - 1, k + 1)     # 左
            )
            
            # [Backtrack]: 恢復現場，讓其他路徑也可以使用這個格子
            board[r][c] = original_char

            return found

        for r in range(M):
            for c in range(N):
                # Optimization: 只有當第一個字符匹配時才啟動 DFS
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                
        return False
```