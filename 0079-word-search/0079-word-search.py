class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        
        def backtrack(row, col, suffix):
            if len(suffix) == 0:
                return True

            if (
                row < 0
                or row == m
                or col < 0
                or col == n
                or board[row][col] != suffix[0]
            ):
                return False

            board[row][col] = "#" # used
            for dx, dy in [(0, 1), (-1, 0), (0, -1), (1, 0)]:
                if backtrack(row + dx, col + dy, suffix[1:]):
                    return True

            board[row][col] = suffix[0]
            return False

        for row in range(m):
            for col in range(n):
                if backtrack(row, col, word):
                    return True

        return False
        