class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])

        min_cost = [[float("inf")] * n for _ in range(m)]
        min_cost[0][0] = 0

        deque = collections.deque([(0, 0)])

        while deque:
            row, col = deque.popleft()
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for val, (dx, dy) in enumerate(dirs):
                newR, newC = row + dx, col + dy
                cost = 0 if grid[row][col] == val + 1 else 1

                if 0 <= newR < m and 0 <= newC < n and min_cost[row][col] + cost < min_cost[newR][newC]:
                    min_cost[newR][newC] = min_cost[row][col] + cost

                    if cost == 1:
                        deque.append((newR, newC))
                    else:
                        deque.appendleft((newR, newC))

        return min_cost[m - 1][n - 1]
