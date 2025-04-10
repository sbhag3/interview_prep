class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        seen = {(0, 0)}
        pq = [(grid[0][0], 0, 0)]

        ans = 0

        while pq:
            elevation, row, col = heapq.heappop(pq)
            ans = max(ans, elevation)
            if row == col == n - 1:
                return ans
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in dirs:
                newX, newY = row + dx, col + dy
                if newX >= 0 and newX < n and newY >= 0 and newY < n and (newX, newY) not in seen:
                    heapq.heappush(pq, (grid[newX][newY], newX, newY))
                    seen.add((newX, newY))

