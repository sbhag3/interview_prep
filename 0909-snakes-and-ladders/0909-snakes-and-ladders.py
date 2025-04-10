class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)
        cells = [None] * (n**2 + 1)
        idx = 1
        cols = list(range(0, n))
        for row in range(n - 1, -1, -1):
            for col in cols:
                cells[idx] = (row, col)
                idx += 1
            cols.reverse()
        dist = [-1] * (n**2 + 1)
        q = deque([1])
        dist[1] = 0
        while q:
            curr = q.popleft()
            for step in range(curr + 1, min(curr + 6, n**2) + 1):
                row, col = cells[step]
                dst = board[row][col] if board[row][col] != -1 else step
                if dist[dst] == -1:
                    dist[dst] = dist[curr] + 1
                    q.append(dst)
        return dist[n**2]
        