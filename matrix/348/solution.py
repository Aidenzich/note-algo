class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        # 初始化二維陣列
        self.board = [[0] * n for _ in range(n)]      

    def move(self, row: int, col: int, player: int) -> int:
        # 下棋
        self.board[row][col] = player
        
        # 1. 檢查 Row (橫向)
        status = 1 # 假設贏了
        for j in range(self.n):
            if self.board[row][j] != player:
                status = 0
                break
        if status: return player
        
        status = 1
        for j in range(self.n):
            if self.board[j][col] != player:
                status = 0
                break
        if status: return player
        
        if row == col:  # 修正: rol -> row
            status = 1
            for j in range(self.n):
                if self.board[j][j] != player:
                    status = 0
                    break            
            if status: return player
        
        if row == self.n - col - 1:  # 修正: rol -> row
            status = 1
            for j in range(self.n):
                # 修正: n -> self.n
                if self.board[self.n - 1 - j][j] != player:
                    status = 0
                    break            
            if status: return player
        
        return 0