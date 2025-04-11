class Solution(object):
    def maximumSafenessFactor(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)

        def in_bounds(x, y):
            return min(x, y) >= 0 and max(x, y) < n

        def precompute():
            q = deque()
            min_dist = {}
            for i in range(n):
                for j in range(n):
                    if grid[i][j]:
                        q.append([i, j, 0])
                        min_dist[(i, j)] = 0


            while q:
                x, y, dist = q.popleft()
                dirs = [(0,1), (0,-1), (1,0), (-1,0)]
                for dx, dy in dirs:
                    newX, newY = x + dx, y + dy
                    if in_bounds(newX, newY) and (newX, newY) not in min_dist:
                        min_dist[(newX, newY)] = dist + 1
                        q.append([newX, newY, dist + 1])

            return min_dist

        min_dist = precompute()

        heap = [(-min_dist[(0, 0)], 0, 0)]
        visited = set()

        visited.add((0, 0))

        while heap:
            dist, x, y = heapq.heappop(heap)
            dist = -dist
            if (x, y) == (n - 1, n - 1):
                return dist

            dirs = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in dirs:
                newX, newY = x + dx, y + dy
                if in_bounds(newX, newY) and (newX, newY) not in visited:
                    visited.add((newX, newY))
                    dist2 = min(dist, min_dist[(newX, newY)])
                    heapq.heappush(heap, (-dist2, newX, newY))


        