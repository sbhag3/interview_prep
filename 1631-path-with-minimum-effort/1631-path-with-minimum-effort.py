class Solution(object):
    def minimumEffortPath(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: int
        """
        m, n = len(heights), len(heights[0])

        def in_bounds(x, y):
            return 0 <= x < m and 0 <= y < n

        def bfs(effort):
            visited = [[False] * n for _ in range(m)]
            q = deque([(0, 0)])
            while q:
                x, y = q.popleft()
                if x == m - 1 and y == n - 1:
                    return True
                visited[x][y] = True
                dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for dx, dy in dirs:
                    newX, newY = x + dx, y + dy
                    if in_bounds(newX, newY) and not visited[newX][newY]:
                        diff = abs(heights[newX][newY] - heights[x][y])
                        if diff <= effort:
                            visited[newX][newY] = True
                            q.append((newX, newY))

        left, right = 0, 1000000

        while left < right:
            mid = (left + right) // 2
            if bfs(mid):
                right = mid
            else:
                left = mid + 1

        return left

        
        