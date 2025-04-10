class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return

        m, n = len(board), len(board[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def border(i, j):
            if not (i >= 0 and i < m and j >= 0 and j < n) or board[i][j] != 'O':
                return

            board[i][j] = '$'
            for dx, dy in dirs:
                border(i + dx, j + dy)

        for i in range(m):
            border(i, 0)
            border(i, n - 1)

        for j in range(n):
            border(0, j)
            border(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '$':
                    board[i][j] = 'O'