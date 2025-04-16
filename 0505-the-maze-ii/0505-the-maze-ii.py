import heapq

class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        dst = tuple(destination)
        heap = [(0, tuple(start))]
        dist = {tuple(start): 0}

        def in_bounds(x, y):
            return 0 <= x < m and 0 <= y < n and maze[x][y] == 0

        while heap:
            curr_dist, curr = heapq.heappop(heap)
            if curr == dst:
                return curr_dist

            for dx, dy in dirs:
                x, y = curr
                steps = 0

                while in_bounds(x + dx, y + dy):
                    x += dx
                    y += dy
                    steps += 1

                new_pos = (x, y)
                new_dist = curr_dist + steps

                if new_pos not in dist or new_dist < dist[new_pos]:
                    dist[new_pos] = new_dist
                    heapq.heappush(heap, (new_dist, new_pos))

        return -1