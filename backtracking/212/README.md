# 212. Word Search II

https://leetcode.com/problems/word-search-ii/description/



## Solution
### Time Complexity: $O(M * N * 4 * 3^{L - 1})$ & Space Complexity: $O(K)$

```python
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # 1. 建立 Trie (字典樹)
        WORD_KEY = '$'
        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node[WORD_KEY] = word

        row_num = len(board)
        col_num = len(board[0])
        matched_words = []

        # 2. 定義 Backtracking 函式
        def backtrack(row, col, parent_node):
            letter = board[row][col]
            curr_node = parent_node[letter]
            
            if WORD_KEY in curr_node:
                matched_words.append(curr_node[WORD_KEY])
                del curr_node[WORD_KEY]

            
            board[row][col] = '#'
            
            for r_offset, c_offset in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = row + r_offset, col + c_offset
                
                
                if 0 <= new_r < row_num and 0 <= new_c < col_num:
                    if board[new_r][new_c] in curr_node:
                        backtrack(new_r, new_c, curr_node)
        
            board[row][col] = letter

            if not curr_node:
                del parent_node[letter]


        for r in range(row_num):
            for c in range(col_num):
                if board[r][c] in trie:
                    backtrack(r, c, trie)

        return matched_words
```


