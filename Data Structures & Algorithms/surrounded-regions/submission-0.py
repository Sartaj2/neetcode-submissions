class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        def dfs(r, c):
            if (
                (r, c) in visit or
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] != 'O'
            ):
                return
            visit.add((r, c))
            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)

        # Only mark safe 'O's (connected to border)
        for r in range(ROWS):
            for c in range(COLS):
                if (r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == 'O':
                    dfs(r, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O' and (r, c) not in visit:
                    board[r][c] = 'X'  # Flip surrounded 'O' to 'X'
