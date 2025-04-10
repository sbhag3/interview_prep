class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = 9
        rows = [0] * n
        cols = [0] * n
        boxes = [0] * n

        for r in range(n):
            for c in range(n):
                if board[r][c] == ".":
                    continue

                p = int(board[r][c]) - 1

                if rows[r] & (1 << p):
                    return False
                rows[r] |= (1 << p)

                if cols[c] & (1 << p):
                    return False
                cols[c] |= (1 << p)

                idx = (r // 3) * 3 + (c // 3)
                if boxes[idx] & (1 << p):
                    return False
                boxes[idx] |= (1 << p)

        return True