class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def in_bounds(x, y):
            return x >= 0 and x < m and y >= 0 and y < n

        m, n = len(image), len(image[0])

        q = deque()
        visited = [[False] * n for _ in range(m)]
        visited[sr][sc] = True
        q.append((sr, sc))

        while q:
            x, y = q.popleft()
            if image[x][y] == color:
                continue

            dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for dx, dy in dirs:
                newX, newY = x + dx, y + dy
                if in_bounds(newX, newY) and image[x][y] == image[newX][newY] and not visited[newX][newY]:
                    visited[newX][newY] = True
                    q.append((newX, newY))

            image[x][y] = color

        return image
        