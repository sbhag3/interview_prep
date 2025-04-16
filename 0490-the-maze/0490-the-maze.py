class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m, n = len(maze), len(maze[0])
        visited = [[False] * n for _ in range(m)]

        def in_bounds(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        def dfs(x, y):
            if visited[x][y]:
                return False
            if x == destination[0] and y == destination[1]:
                return True

            visited[x][y] = True
            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in dirs:
                currX = x
                currY = y
                while in_bounds(currX, currY) and maze[currX][currY] == 0:
                    currX += dx
                    currY += dy

                if dfs(currX - dx, currY - dy):
                    return True
            return False

        return dfs(start[0], start[1])
        