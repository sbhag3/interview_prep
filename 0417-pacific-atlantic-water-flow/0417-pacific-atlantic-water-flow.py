class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        m, n = len(heights), len(heights[0])

        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(m):
            pacific_queue.append((i, 0))
            atlantic_queue.append((i, n - 1))
        for i in range(n):
            pacific_queue.append((0, i))
            atlantic_queue.append((m - 1, i))

        def bfs(q):
            visited = set()
            while q:
                (x, y) = q.popleft()
                visited.add((x, y))
                dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
                for dx, dy in dirs:
                    newX, newY = x + dx, y + dy
                    if newX < 0 or newX >= m or newY < 0 or newY >= n or (newX, newY) in visited or heights[newX][newY] < heights[x][y]:
                        continue
                    q.append((newX, newY))

            return visited

        pacific = bfs(pacific_queue)
        atlantic = bfs(atlantic_queue)

        ans = pacific.intersection(atlantic)
        return list(ans)

        

        