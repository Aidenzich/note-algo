# Leetcode 79. Word Search


## Line of thought


## Solution
```python
class Solution:    
    def exist(self, board: list[list[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        word_len = len(word)
    
        def dfs(r: int, c: int, k: int) -> bool:            
            if k == word_len:                
                return True
            
            if r < 0 or r >= M or c < 0 or c >= N:
                return False
                        
            if board[r][c] != word[k]:
                return False
            
            original_char = board[r][c]
            board[r][c] = '#'
            
            found = (
                dfs(r + 1, c, k + 1) or  # 下
                dfs(r - 1, c, k + 1) or  # 上
                dfs(r, c + 1, k + 1) or  # 右
                dfs(r, c - 1, k + 1)     # 左
            )
            
            board[r][c] = original_char

            return found

        for r in range(M):
            for c in range(N):
                # 只有當第一個字符匹配時才啟動 DFS
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
                
        return False
```